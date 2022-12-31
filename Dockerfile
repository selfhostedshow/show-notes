FROM squidfunk/mkdocs-material:7.2.8

COPY requirements.txt /docs/requirements.txt
RUN pip install -U -r /docs/requirements.txt
