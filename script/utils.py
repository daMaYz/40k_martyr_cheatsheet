#!/usr/bin/python
import os

BG = [20, 20, 20]

def loadTemplate(templateName):
	reader = open("./script/templates/" + templateName, "r")
	temp = reader.read()
	reader.close()
	return temp
	

def getDefaultBgColor():
	return str(BG[0]) + ", " + str(BG[1]) + ", " + str(BG[2])