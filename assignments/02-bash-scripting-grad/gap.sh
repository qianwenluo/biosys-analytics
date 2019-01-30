#!/usr/bin/env bash

set -u

DIR="../../data/gapminder/"

if [[ $# -eq 0 ]]; then
    i=0
    for FILE in `ls $DIR/* | sort -V`; do
        let i++
        BASENAME=$(basename "$FILE")
        printf "%5d %s\n" "$((i))" "${BASENAME%.*.*}"
    done
    exit 0
fi

ARG=$1

FILES=$(mktemp)
find "$DIR" -type f -iname "$ARG*" |sort -V > "$FILES" 
NUM_FILES=$(wc -l "$FILES" | awk '{print $1}')

if [[ $NUM_FILES -lt 1 ]]; then
    printf "There are no countries starting with %s\n" \"$ARG\"
    exit 0
fi

i=0
while read -r FILENAME; do
    BASENAME=$(basename "$FILENAME")
    printf "%5d %s\n" "$((i+1))" "${BASENAME%.*.*}"
    i=$((i+1))
done < "$FILES"
