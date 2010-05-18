#!/usr/bin/env python

import sys
import os

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

id = 1
text = ""
filename = "mon_poster.svg"
for line in sys.stdin.readlines():
    text += """<flowPara
         id="flowPara%s"
         style="-inkscape-font-specification:FreeSans Bold;font-family:FreeSans;font-weight:bold;font-style:normal;font-stretch:normal;font-variant:normal;font-size:72;text-anchor:start;text-align:start;writing-mode:lr;line-height:105%%">%s</flowPara>""" % ( id , html_escape(line.expandtabs(10)) )
    id += 1

filecontents = """\
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
   sodipodi:docname="poster4.svg">
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
     inkscape:cx="355"
     inkscape:cy="542.85714"
     inkscape:document-units="px"
     inkscape:current-layer="layer1"
     showgrid="false"
     inkscape:window-width="1278"
     inkscape:window-height="1003"
     inkscape:window-x="0"
     inkscape:window-y="19"
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
    </rdf:RDF >
  </metadata>
  <g
     inkscape:label="Calque 1"
     inkscape:groupmode="layer"
     id="layer1">
    <flowRoot 
       xml:space="preserve"
       id="flowRoot6162"
       style="font-size:72px;font-style:normal;font-weight:bold;fill:#000000;fill-opacity:1;stroke:none;font-family:FreeSans"><flowRegion
         id="flowRegion6164"><rect
           id="rect6166"
           width="2745.71411"
           height="1051.4288"
           x="5.4495672e-07"
           y="0.93362427" /></flowRegion>%s<flowSpan
         style="-inkscape-font-specification:FreeSans Bold;font-family:FreeSans;font-weight:bold;font-style:normal;font-stretch:normal;font-variant:normal;font-size:72;text-anchor:start;text-align:start;writing-mode:lr;line-height:105%%"
         id="flowSpan2855">                                   </flowSpan></flowRoot>  </g>
</svg>""" % text

mysvg = open(filename, "w")
mysvg.write(filecontents)
mysvg.close()
