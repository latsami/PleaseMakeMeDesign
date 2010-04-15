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






# Importation des librairies nécessaires
import sys

lexique = sys.stdin.read()     # pour prendre le standard input comme argument
lexique = lexique.split('\n')     # séparer le texte en lignes

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
def paragraphe(texte):
    svg_text = """
    <flowRoot
        style="font-size:16px;font-family:Bitstream Vera Sans;">
        <flowRegion>
            <rect width="600" height="600" x="0" y="0" />
        </flowRegion>
        <flowPara>%s</flowPara>
    </flowRoot>
    """ % (texte)
    return svg_text
    
# Création d'une variable de type texte qui va accueillir le contenu texte du paragraphe
svg_texte=''

#  Pour chaque ligne du lexique :
for ligne in lexique:
    try:        # Si c'est possible d'exécuter les lignes suivantes :
        occurence, mot = ligne.split()      # Fait correspondre une occurence à un mot
        svg_mot = '<flowSpan style="font-size:%dpx;">%s </flowSpan>' % (int(occurence)*5, mot)      # Crée le code svg du mot, sa taille est proportionnelle à son nombre d'occurrences
        svg_texte += svg_mot                # Rajoute le code svg du mot au paragraphe
    except:     # Si une erreur arrive alors on passe au mot suivant
        pass

# création du code svg du paragraphe
svg_debut += paragraphe(svg_texte)

# Ferme le code svg
svg = svg_debut + svg_fin

#  Enregistre le code svg dans un fichier
svg_fichier = open('frequence_mots_bloc.svg', 'w')
svg_fichier.write(svg)
svg_fichier.close()