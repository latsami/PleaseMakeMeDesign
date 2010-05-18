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
(options, args) = parser.parse_args()

# récupère dans la variable "mots" les mots entrés par l'utilisateur
requete = options.requete

url = "http://identi.ca/search/notice?q=%s" % (requete)
# print url
recherche = urllib.urlopen(url)
html = recherche.read()
recherche.close()

soup = BeautifulSoup(html)
resultats = soup('li', 'hentry notice')

tweets = ''

for resultat in resultats:
    tweet = ''
    date = resultat.find('abbr', 'published')
    date = date.findAll( text=True )
    date = " ".join(date).encode('utf-8')
    
    location = resultat.find('span', 'location')
    if location:
        location = location.findAll( text=True )
        location = " ".join(location).encode('utf-8')
    
    content = resultat.find('p', 'entry-content')
    for texte in content.findAll( text=True ):
        if texte:  tweet += texte
    tweet = tweet.strip('\n').encode('utf-8') #enlève les sauts de ligne et encode en utf-8
    if location:
        tweets += date + ' -- ' + location + ' -- ' + tweet + '\n'
    else:
        tweets += date + ' -- ' + tweet + '\n'
try:
    tweets = BeautifulStoneSoup(tweets, convertEntities="html", smartQuotesTo="html").contents[0].encode('utf-8')
    print tweets.replace('&apos;', "'")
except:
    print "Il n'y a aucun resultat."
