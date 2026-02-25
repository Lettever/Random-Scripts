#!/usr/bin/env bash
# Adds scripts from random places into a repo

repo=~/Programming/script-repo
original_dir=$(pwd)

source_file=$(realpath "$1")
mkdir -p "$repo" && cd "$repo"
ln -vf "$source_file" .

git add . && git commit -m "Add $(basename "$1")" && git push
cd "$original_dir"
