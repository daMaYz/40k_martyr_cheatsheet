#!/usr/bin/python
import os
from utils import loadTemplate, getDefaultBgColor, BG
from psalm import Psalm
from doctrine import Doctrine
PLACEHOLDER_BGCOLOR = "BGCOLOR_HERE"
PLACEHOLDER_PSALMS = "PSALMS_HERE"
PLACEHOLDER_EFFECTS = "EFFECTS_HERE"
PLACEHOLDER_CONTENT = "CONTENT_HERE"

TEMPLATE_ROW = loadTemplate("tr_template.html")
TEMPLATE_INDEX = loadTemplate("index_template.html")

def getBgColor(lvl):
	return str(BG[0] + 10 * lvl) + ", " + str(BG[1] + 10 * lvl) + ", " + str(BG[2] + 10 * lvl)

def generateRowForDoctrine(doc):
	row = TEMPLATE_ROW
	row = row.replace(PLACEHOLDER_BGCOLOR, getBgColor(doc.level))
	row = row.replace(PLACEHOLDER_PSALMS, doc.getChildrenAsHtml())
	row = row.replace(PLACEHOLDER_EFFECTS, doc.getFullEffect())
	return row

## generate subpages for psalms
for psalm in Psalm.psalmList:
	psalm.writePsalmHtml()
	
content = ""
for i in range(1, 5):
	for doc in Doctrine.getAll(i):
		content += generateRowForDoctrine(doc) + "\n"
		
index = TEMPLATE_INDEX
index = index.replace(PLACEHOLDER_CONTENT, content)
index = index.replace(PLACEHOLDER_BGCOLOR, getDefaultBgColor())

writer = open("index.html", "w+")
writer.write(index)
writer.close()