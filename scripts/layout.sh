#! /bin/bash -x

#FONTSIZE=$((`wc -l | tr -d ' '`*6))
#FONTSIZE=60
MYLEN=$( cat $1 | wc -l | tr -d ' ')
FONTSIZE=$((566/$MYLEN))
#enscript -f 'Helvetica-Bold@'$FONTSIZE'/'$FONTSIZE -p 'bla.ps' --non-printable-format=questionmark -T 1 --mark-wrapped-lines=arrow
enscript -f 'Helvetica-Bold@'$FONTSIZE'/'$FONTSIZE -p 'bla.ps' --non-printable-format=questionmark -T 1 --mark-wrapped-lines=arrow $1