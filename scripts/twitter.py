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

from optparse import OptionParser
import urllib
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup

# Permet à l'utilisateur d'entrer une option avant d'exécuter le script
parser = OptionParser()
parser.add_option("-r", "--requete", dest="requete", default="", help="recherche le(s) mot(s) sur Twitter")
parser.add_option("-l", "--langue", dest="langue", default="all", help="choix de la langue (code ISO)")
parser.add_option("-t", "--tag", dest="tag", default="", help="chercher par un tag/theme precis")
parser.add_option("-n", "--nombre", dest="nombre", default="10", help="nombre de resultats souhaite")
parser.add_option("-d", "--debut", dest="debut", default="", help="recherche depuis une date precise, format aaaa-mm-jj")
parser.add_option("-f", "--fin", dest="fin", default="", help="recherche jusqu'une date precise, format aaaa-mm-jj")
(options, args) = parser.parse_args()

# récupère dans la variable "mots" les mots entrés par l'utilisateur
requete = options.requete
langue = options.langue
tag = options.tag
nombre = options.nombre
debut = options.debut
fin = options.fin

url = "http://search.twitter.com/search?&tag=%s&ands=%s&nots=&ors=&phrase=&q=&ref=&rpp=%s&since=%s&until=%s&near=&within=15&units=km&from=&to=&lang=%s" % (tag, requete, nombre, debut, fin, langue)
# print url
recherche = urllib.urlopen(url)
html = recherche.read()
recherche.close()

soup = BeautifulSoup(html)
resultats = soup('li', 'result')

tweets = ''
                   
for resultat in resultats:
    texte = resultat.find('div', 'msg')
    infos = resultat.find('div', 'info')
    for a in infos('a'):
        infos.a.extract()
    for span in infos('span'):
        infos.span.extract()
    tweets += texte.text.encode('utf-8') + ' ' + infos.text.replace('&middot;', '').encode('utf-8') + '\n'

try:
    tweets = BeautifulStoneSoup(tweets, convertEntities="html", smartQuotesTo="html").contents[0].encode('utf-8')
    print tweets.replace('&apos;', "'")
except:
    print "Il n'y a aucun resultat."
