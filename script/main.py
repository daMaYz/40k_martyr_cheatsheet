#!/usr/bin/python
import os
from psalm import Psalm

	
def replaceAll( line ):
	for psalm in Psalm.psalmList:
		if psalm.name in line:
			print("checking: " + psalm.name)
			line = line.replace(psalm.name, psalm.getImgTag("."))
	print("--------")
	return line
			
def buildNewLine(line):
	index = line.find(">")
	newLine = line[:index+1]	#open td and stuff
	content = line[index+1:-6]
	
	newLine += replaceAll(content)	# newContent
	newLine += "<br>" + content		# oldContent
	newLine += "</td>\r\n"
	
	return newLine
	
	


## read original file
reader = open("./40kPsalm_original.html", "r")
lines = reader.readlines() 
newLines = [None] * len(lines)
counter = 0

for line in lines: 
	newLine = line
	for psalm in Psalm.psalmList:
		if psalm.name in newLine:
			newLine = buildNewLine(line)
			break
	newLines[counter] = newLine
	counter += 1
			
del reader

## write file
writer = open("./index.html", "w+")
for newLine in newLines: 
	writer.write(newLine)	

writer.close()

## generate subpages
for psalm in Psalm.psalmList:
	psalm.writePsalmHtml()
	print(psalm.getImgTag("."))