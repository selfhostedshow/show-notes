/*
Override the theme for specific shows.

Based on https://github.com/squidfunk/mkdocs-material/blob/master/src/partials/javascripts/palette.html

NOTE: Not compatible with `navigation.instant`.
*/

(function() {
  var SHOWS = JSON.parse(document.getElementById("__shows").textContent);
  var PATH_PREFIX = location.pathname.split("/")[1];

  for (var showSlug in SHOWS) {
    if (PATH_PREFIX == showSlug) {
      console.log("Setting custom theme for", showSlug);
      document.body.setAttribute("data-show", showSlug);
    }
  }
}())
