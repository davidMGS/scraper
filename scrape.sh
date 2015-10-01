#!/bin/bash

echo "Deleting csv..."
rm -f pts_against.csv
echo "Scraping..."
scrapy crawl pts_against_bot -o pts_against.csv -t csv
