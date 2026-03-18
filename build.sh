#!/usr/bin/env bash
set -e
asciidoctor -r asciidoctor-diagram article.adoc
asciidoctor -r asciidoctor-diagram walkthrough.adoc
echo "rebuilt article.html and walkthrough.html"
