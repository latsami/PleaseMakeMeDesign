#!/usr/bin/python
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


import urllib
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup


requete = urllib.urlopen("http://search.twitter.com/search?ands=&from=&lang=fr&nots=&ors=&phrase=&q=&ref=&rpp=15&since=&tag=design&to=&units=km&until=&within=50")
html = requete.read()
requete.close()

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

tweets = BeautifulStoneSoup(tweets, convertEntities="html", smartQuotesTo="html").contents[0].encode('utf-8')
print tweets.replace('&apos;', "'")
