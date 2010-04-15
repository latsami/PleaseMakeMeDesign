#! /bin/zsh

SVG_DEBUT='<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg width="400mm" height="600mm">
    <sodipodi:namedview
         id="base"
         pagecolor="#ffffff"
         inkscape:document-units="px"
         inkscape:current-layer="layer1"
    />
    <g
        inkscape:label="Calque 1"
        inkscape:groupmode="layer"
        id="layer1">
        <flowRoot
        style="font-size:16px;font-family:Bitstream Vera Sans;">
        <flowRegion>
            <rect width="600" height="600" x="0" y="0" />
        </flowRegion>
        <flowPara>'

SVG_FIN="</flowPara>
    </flowRoot>
    </g>
</svg>
"

echo $SVG_DEBUT $1 $SVG_FIN >| bash.svg