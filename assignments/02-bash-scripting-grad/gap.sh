#!/usr/bin/env bash

set -u

DIR="/rsgrps/bh_class/qianwenluo/biosys-analytics/data/gapminder"


if [[ $# -eq 0 ]]; then
    i=0
    for FILE in `ls $DIR/* | sort -V`; do
        ((i++))
        BASENAME=$(basename "$FILE")
        echo "${BASENAME%.cc.txt}"
    done
fi

ARG=$1
find $DIR -type f -iname '$ARG*' -exec basename {} .cc.txt \;|grep \/ || printf "There are no countries starting with %s\n" \"$ARG\" 




