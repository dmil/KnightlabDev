#Scraper Script 
# - Dhrumil Mehta
# - Learning to use lxml
# - Scrapes headlines from www.dailynorthwestern.com

import lxml.html
from lxml import etree
from lxml.html import parse
import pdb
from lxml.cssselect import CSSSelector


doc = parse("http://www.dailynorthwestern.com")

root = doc.getroot()

outputfile = open('log.txt', 'w')


# A recursive function that returns a list of elements
# that contain an attribute with the world "headline"
def printelements(rootnode):
	if (type(rootnode) == lxml.html.HtmlElement): #and (len(rootnode) > 0)""":
		outputfile.write(str(rootnode.tag) + '   ' + str(rootnode.attrib))
		for item in list(rootnode):
			printelements(item)

# Recurs through every element, finds those with "headline" in the class
# and returns those elements (the newspaper headlines)
def getHeadlineElement(rootnode):
	if (type(rootnode) == lxml.html.HtmlElement): #and (len(rootnode) > 0)""":
		if 'class' in rootnode.attrib:
			if 'headline' in rootnode.attrib['class']:
				outputfile.write(str(rootnode.text))
		for item in list(rootnode):
			getHeadlineElement(item)

# A more intelligent way to getHeadlineElements
def smartway(rootnode):
	headlineElements = doc.getroot().cssselect('a[class*="headline"]')
	for item in headlineElements:
		outputfile.write(item.text)

#printelements(root)
#getHeadlineElement(root)
#smartway(root)

outputfile.close()


# Joe's Comments ------------------------
# Ponder Text + Tail Prop 
# Look @ Beautiful Soup and Xpath
# Producing XML - other tools | template
# ---------------------------------------