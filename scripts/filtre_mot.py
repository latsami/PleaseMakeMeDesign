#! /usr/bin/env python
# -*- coding: utf-8 -*-

# (c) Stéphanie Vilayphiou
# License: GNU-GPL 3
#
# This program is free software: you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as published 
# by the Free Software Foundation, either version 3 of the License, 
# or any later version.
#
# Please don't forget to mention the author's name along your new 
# project as specified in the license.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.






# Importation des librairies nécessaires au bon fonctionnement du script
from optparse import OptionParser
import sys

# Permet à l'utilisateur d'entrer une option avant d'exécuter le script
parser = OptionParser()
parser.add_option("-m", "--mots", dest="mots", default="hello", help="aligne les phrases sur un même mot (ou groupe de mots)")
(options, args) = parser.parse_args()
mots = options.mots       # récupère dans la variable "mots" les mots entrés par l'utilisateur
print "mots = " + mots

texte = sys.stdin.read()     # pour prendre le standard input comme argument
texte = texte.split('\n')    # séparer le texte en lignes

# Début basique d'un fichier svg
svg_debut = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
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
"""

# Fin basique d'un fichier svg
svg_fin = """
    </g>
</svg>
"""

# Fonction créant un code svg pour un bloc de texte
def paragraphe(largeur, gauche, haut, texte, alignement, couleur):    
    svg_text = """
    <flowRoot
        style="font-size:16px;line-height:18px;fill:%s;font-family:Bitstream Vera Sans;text-align:%s">
        <flowRegion>
            <rect width="%d" height="100" x="%d" y="%d" />
        </flowRegion>
        <flowPara>%s</flowPara>
    </flowRoot>
    """ % (couleur, alignement, largeur, gauche, haut, texte)
    return svg_text


i=0                         # Initialisation du compteur

# Pour chaque phrase du texte
for phrase in texte:
    indexMots = phrase.lower().find(mots)    # Trouve l'emplacement du MOT dans la phrase
    if indexMots != -1:                         # Si le MOT existe :
        
        # Sépare la partie antérieure et postérieure au MOT
        txt_gauche = phrase[:indexMots]
        txt_droite = phrase[indexMots+len(mots):]

        # Pour chaque partie de la phrase, crée un code svg pour écrire la phrase avec le MOT toujours au milieu
        txt_gauche = paragraphe(500, 0, i*100, txt_gauche, 'end', '#000000')
        txt_milieu = paragraphe(100, 510, i*100, mots, 'start', '#FF0000')
        txt_droite = paragraphe(500, 620, i*100, txt_droite, 'start', '#000000')
        
        # Rajoute les phrases (en svg) au code svg de base
        svg_debut += txt_gauche + txt_milieu + txt_droite
        
        # Incrémente le compteur
        i += 1
        
# Ferme le code svg
svg = svg_debut + svg_fin

#  Enregistre le code svg dans un fichier
svg_fichier = open('filtre_mot.svg', 'w')
svg_fichier.write(svg)
svg_fichier.close()