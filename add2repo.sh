#!/usr/bin/env bash

add2repo() {
    repo=~/Programming/script-repo
    mkdir -p "$repo" && cd "$repo"
    [ ! -d .git ] && git init
    ln -sf "$(realpath "$1")" .
    git add . && git commit -m "Add $(basename "$1")" && git push
}
