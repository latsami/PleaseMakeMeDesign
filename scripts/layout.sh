#! /bin/bash -x

#FONTSIZE=$((`wc -l | tr -d ' '`*6))
#FONTSIZE=12
PAGE=793
MYLEN=$( cat $1 | wc -l | tr -d ' ')
FONTSIZE=$((($PAGE-($PAGE/$MYLEN))/$MYLEN))
#enscript -f 'Helvetica-Bold@'$FONTSIZE'/'$FONTSIZE -p 'bla.ps' --non-printable-format=questionmark -T 1 --mark-wrapped-lines=arrow
enscript -f 'Helvetica-Bold@'$FONTSIZE'/'$FONTSIZE -p 'bla.ps' --non-printable-format=questionmark -T 8 -B --mark-wrapped-lines=arrow $1