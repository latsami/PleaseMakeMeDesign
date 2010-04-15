#! /usr/bin/env python -u

import sys

SVG_DEBUT="""\
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- generated for Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="210mm"
   height="297mm"
   id="svg6152"
   version="1.1"
   inkscape:version="0.47 r22583"
   sodipodi:docname="Nouveau document 2">
  <defs
     id="defs6154">
    <inkscape:perspective
       sodipodi:type="inkscape:persp3d"
       inkscape:vp_x="0 : 526.18109 : 1"
       inkscape:vp_y="0 : 1000 : 0"
       inkscape:vp_z="744.09448 : 526.18109 : 1"
       inkscape:persp3d-origin="372.04724 : 350.78739 : 1"
       id="perspective6160" />
  </defs>
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.35"
     inkscape:cx="375"
     inkscape:cy="520"
     inkscape:document-units="px"
     inkscape:current-layer="layer1"
     showgrid="false"
     inkscape:window-width="680"
     inkscape:window-height="698"
     inkscape:window-x="502"
     inkscape:window-y="103"
     inkscape:window-maximized="0" />
  <metadata
     id="metadata6157">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Calque 1"
     inkscape:groupmode="layer"
     id="layer1">
    <flowRoot
       xml:space="preserve"
       id="flowRoot6162"
       style="font-size:40px;font-style:normal;font-weight:normal;fill:#000000;fill-opacity:1;stroke:none;font-family:Bitstream Vera Sans"><flowRegion
         id="flowRegion6164"><rect
           id="rect6166"
           width="568.57141"
           height="325.71429"
           x="42.857143"
           y="280.93362" /></flowRegion>\
"""
SVG_FIN="""\
    </flowRoot>
    </g>
</svg>
"""

print SVG_DEBUT

for line in sys.stdin.readlines():
	print "<flowPara id='flowPara$(uuidgen)'>"
	print line.expandtabs(16)
	print "</flowPara>"	

print SVG_FIN