# Final project
# testing stuff script 1
# working with lxml, requests, webbrowser,

from lxml import html
import requests

##page = requests.get('https://www.reddit.com/') # requests.get to retrieve web page/parse it w/html
##data = html.fromstring(page.content)
##
##
####//*[@id="thing_t3_6pwrgu"]/div[2]/div[1]/p[1]/a
##stuff1 = data.xpath('//*[@id="thing_t3_6pwrgu"]/div[2]/div[1]/p[1]/a')
##print(stuff1)
##at this point, this just prints an empty list...more playing around necessary




# --------------------

# CONSULT AUTOMATE THE BORING STUFF >> CHAPTER 11
# webbrowser - webbrowser.open(URL HERE) simply opens a browser to the url passed as an argument
import webbrowser

webbrowser.open('http://www.google.com')
webbrowser.open('http://www.reddit.com')

import requests # requests.get() takes a string of a URL to download

# Need to use HTML parsing to sort through content of URL for keyword/phrase
# input by user

prompt = input('Enter keyword or phrase:  ')




