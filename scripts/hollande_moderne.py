#!/usr/bin/env python

import sys
import os

#librsvg2-2 - SAX-based renderer library for SVG files (runtime)
#librsvg2-common - SAX-based renderer library for SVG files (extra runtime)
#librsvg2-dbg - SAX-based renderer library for SVG files (debug)
#librsvg2-dev - SAX-based renderer library for SVG files (development)

#http://www.agapow.net/programming/python/using-percent-in-a-string

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
filename = "mon_poster"
for line in sys.stdin.readlines():
    text += """<flowPara
         id="flowPara%s"
         style="font-size:72px;font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;text-align:start;line-height:104.99999523%%;writing-mode:lr-tb;text-anchor:start;font-family:FreeSans;-inkscape-font-specification:FreeSans Bold">%s</flowPara>
""" % ( id , html_escape(line.expandtabs(10)) )
    id += 1

filecontents = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- generated for Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   version="1.2"
   width="210mm"
   height="297mm"
   id="svg6152">
  <defs
     id="defs6154" />
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
     id="layer1">
    <flowRoot
       id="flowRoot6162"
       xml:space="preserve"
       style="font-size:72px;font-style:normal;font-weight:bold;fill:#000000;fill-opacity:1;stroke:none;font-family:FreeSans"><flowRegion
         id="flowRegion6164"><rect
           width="2745.7141"
           height="1051.4288"
           x="5.4495672e-07"
           y="0.93362427"
           id="rect6166" /></flowRegion>%s</flowRoot>  </g>
</svg>""" % text

mysvg = open(filename + ".svg", "w")
mysvg.write(filecontents)
mysvg.close()

#os.system("svg2pdf " + filename + ".svg " + filename + ".pdf")
#os.system("lpr " + filename + ".pdf")
