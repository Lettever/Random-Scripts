#!/usr/bin/env bash
# Adds scripts from random places into a repo

repo=~/Programming/script-repo
mkdir -p "$repo" && cd "$repo"
ln -f "$(realpath "$1")" .
git add . && git commit -m "Add $(basename "$1")" && git push
