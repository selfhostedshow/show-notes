#!/usr/bin/env bash

set -e

python3 scrape.py

for show_dir in output/**
do
    pushd $show_dir
    mkdocs build
    popd
done
