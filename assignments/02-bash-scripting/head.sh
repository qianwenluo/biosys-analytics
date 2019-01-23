#!/usr/bin/env bash

set -u 

if [[ $# -eq 0 ]]; then
    echo "Usage: head.sh FILE NUMBER[optional]"
    exit 1
fi

ARG=$1
NUM_ITERATIONS=${2:-3}

if [[ ! -f "$ARG" ]]; then
    echo "$ARG is not a file"
    exit 1
fi

i=0
while read -r LINE; do
    echo $LINE
    i=$((i+1))
    if [[ $i -eq $NUM_ITERATIONS ]];then
        break
    fi
done < "$ARG"
