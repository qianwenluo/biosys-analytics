#!/usr/bin/env bash
 
set -u 

if [[ $# -eq 0 ]]; then
    echo "Usage: cat-n.sh FILE"
    exit 1
fi

ARG=$1

if [[ ! -f "$ARG" ]]; then
    echo "$ARG is not a file"
    exit 1
fi


i=0
while read -r LINE; do
    echo $((i+1))" $LINE"
    i=$((i+1))
done < "$ARG"
