#!/usr/bin/env bash
# Adds scripts from random places into a repo

repo=~/Programming/script-repo
og_dir=$(pwd)

mkdir -p "$repo" && cd "$repo"
ln "$(realpath "$1")" .
git add . && git commit -m "Add $(basename "$1")" && git push

cd "$og_dir"
