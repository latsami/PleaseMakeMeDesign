#! /usr/bin/env bash

content=`cat`

page=793
# page=500
# # mylen=$( cat | wc -l | tr -d ' ')
mylen=$( printf "%s" "$content" | wc -l | tr -d ' ')
fontsize=$((($page-($page/$mylen))/$mylen))

printf "%s" "${content}" \
| enscript \
    -f 'Helvetica-Bold@'${fontsize}'/'${fontsize} \
    --non-printable-format=questionmark \
    -T 16 \
    -B \
    --mark-wrapped-lines=arrow \
    -p 'bla.ps'