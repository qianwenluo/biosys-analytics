#!/usr/bin/env bash

set -u

if [[ $# -eq 0 ]] || [[ $# -gt 2 ]]; then
    printf "Usage: %s GREETING [NAME]\n" "$(basename "$0")"
    exit 1
fi


ARG=$1
NAME=${2:-Human}
echo "$ARG, $NAME!"

