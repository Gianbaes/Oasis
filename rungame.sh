#!/bin/bash

export DISPLAY=:1
export XDG_RUNTIME_DIR="/tmp/runtime-$(id -u)"

mkdir -p "$XDG_RUNTIME_DIR"
chmod 700 "$XDG_RUNTIME_DIR"

exec /usr/local/python/3.14.2/bin/python \
    /workspaces/Oasis/main.py