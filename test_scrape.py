import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from unittest.mock import patch

import requests

from scrape import fetch, main


class FetchTests(unittest.TestCase):
    def setUp(self):
        self.statuses = []
        self.accept_headers = []
        test = self

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                test.accept_headers.append(self.headers.get("Accept"))
                self.send_response(test.statuses.pop(0))
                self.end_headers()
                self.wfile.write(b"episode")

            def log_message(self, *args):
                pass

        self.server = HTTPServer(("127.0.0.1", 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()
        self.url = f"http://127.0.0.1:{self.server.server_port}/episode"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()

    def test_recovers_from_transient_gateway_errors(self):
        self.statuses = [502, 503, 200]
        with patch("urllib3.util.retry.time.sleep"):
            response = fetch(self.url, headers={"Accept": "text/html"})
        self.assertEqual(response.content, b"episode")
        self.assertEqual(self.accept_headers, ["text/html"] * 3)

    def test_persistent_failure_stops_after_three_retries(self):
        self.statuses = [502] * 4
        with patch("urllib3.util.retry.time.sleep"):
            with self.assertRaises(requests.HTTPError) as error:
                fetch(self.url)
        self.assertEqual(error.exception.response.status_code, 502)
        self.assertEqual(len(self.accept_headers), 4)

    def test_not_found_is_not_retried(self):
        self.statuses = [404]
        with self.assertRaises(requests.HTTPError):
            fetch(self.url)
        self.assertEqual(len(self.accept_headers), 1)

    def test_requests_have_connection_and_read_timeouts(self):
        with patch("requests.Session.get") as get:
            fetch(self.url)
        self.assertEqual(get.call_args.kwargs["timeout"], (10, 30))


class MainTests(unittest.TestCase):
    def test_feed_failure_causes_nonzero_exit(self):
        with patch("scrape.fetch", side_effect=requests.HTTPError("503")), \
                patch("scrape.mkdir_safe"), \
                patch("scrape.traceback.print_exception"), \
                patch("builtins.print"):
            with self.assertRaises(SystemExit) as error:
                main()
        self.assertEqual(error.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
