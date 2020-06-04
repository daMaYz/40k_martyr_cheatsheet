#!/usr/bin/python
import os
from psalm import Psalm


## read original file
reader = open("./40kPsalm_original.html", "r")
lines = reader.readlines() 
psalms = []
effects = []
takeNext = False

for line in lines: 
	
	if takeNext:
		effects.append(line)
		takeNext = False
		
	for psalm in Psalm.psalmList:
		if psalm.name in line:
			psalms.append(line)
			takeNext = True
			break
		
del reader

p = []
e = []
for i in range(len(psalms)):
	psalmIndex = psalms[i].find(">")
	psalmContent = psalms[i][psalmIndex+1:-6].split(" + ")
	p.append(psalmContent)
	effectIndex = effects[i].find(">")
	effectContent = effects[i][effectIndex+1:].replace("</td>", "").replace("<br>", "").replace("\r", "").replace("\n", "")
	e.append(effectContent)
	
	
	
writer = open("./tmp.txt", "w+")
for i in range(len(p)):
	txt = "Doctrine(\"" + e[i] + "\", ["
	for psalm in p[i]:
		txt += "\"" + psalm + "\""
		if psalm != p[i][len(p[i]) - 1]:
			txt += ", "
	txt += "])"
	writer.write(txt + "\r")
	
writer.close()