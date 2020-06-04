#!/usr/bin/python
import os

IMG_TAG_PREFIX = "<img src=\"./res/"
IMG_TAG_SUFFIX = ".png\">"

def getImgTag( name ):
	return IMG_TAG_PREFIX + name + IMG_TAG_SUFFIX;
	
def replaceAll( line ):
	for name in names: 
		if name in line:
			line = line.replace(name, getImgTag(name))
	return line
			
def buildNewLine(line):
	index = line.find(">")
	newLine = line[:index+1]
	content = line[index+1:-6]
	
	newLine += replaceAll(content)
	newLine += "<br>" + content
	newLine += "</td>\r\n"
	
	
	return newLine
	
	
	
	
	
	
## read images	

files = os.listdir("./res")
names = [None] * len(files)
counter = 0

## extract names
for file in files:
	names[counter] = file.replace(".png", "")
	counter += 1
	
del counter
del files

## read original file
reader = open("40kPsalm.html", "r")
lines = reader.readlines() 
newLines = [None] * len(lines)
counter = 0

for line in lines: 
	newLine = line
	for name in names: 
		if name in newLine:
			newLine = buildNewLine(line)#newLine.replace(name, getImgTag(name))
			print(buildNewLine(line))
	newLines[counter] = newLine
	counter += 1
			
del reader

## write file
writer = open("new40kPsalm.html", "w+")
for newLine in newLines: 
	writer.write(newLine)	

writer.close()
