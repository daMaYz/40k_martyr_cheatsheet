#!/usr/bin/python
from utils import loadTemplate, getDefaultBgColor

PLACEHOLDER_DIR = "DIR_HERE"
PLACEHOLDER_NAME = "PSALMNAME_HERE"
PLACEHOLDER_EFFECT = "EFFECT_HERE"
PLACEHOLDER_CHILDREN = "CHILDREN_HERE"
PLACEHOLDER_PARENTS = "PARENTS_HERE"
PLACEHOLDER_BGCOLOR = "BGCOLOR_HERE"
TEMPLATE_ICON = loadTemplate("psalm_icon_template.html")
TEMPLATE_PAGE = loadTemplate("psalm_page_template.html")

class Psalm:
	psalmList = []
	
	def initAllParents():
		for psalm in Psalm.psalmList:
			psalm.initParents()
			



	
	def __init__(self, name, effect, children):
		self.name = name
		self.effect = effect
		self.children = children
		self.psalmList.append(self)
		self.parents = []
		
	def getChildrenAsPsalm(self):
		children = []
		for child in self.children:
			children.append(Psalm.findByName(child))
		return children

	def findByName(name):
		for psalm in Psalm.psalmList:
			if name == psalm.name:
				return psalm
				
	def getImgTag(self, dir):
		icon = TEMPLATE_ICON.replace(PLACEHOLDER_NAME, self.name)
		icon = icon.replace(PLACEHOLDER_NAME, self.name)
		icon = icon.replace(PLACEHOLDER_DIR, dir)
		return icon
		
	def addToParents(self, newParent):
		if newParent.name not in self.parents:
			self.parents.append(newParent.name)
		
	def initParents(self):
		for child in self.getChildrenAsPsalm():
			child.addToParents(self)
		
	def writePsalmHtml(self):
		children = ""
		for child in self.children:
			children += Psalm.findByName(child).getImgTag("..")
			
		parents = ""
		for parent in self.parents:
			parents += Psalm.findByName(parent).getImgTag("..")
		
		page = TEMPLATE_PAGE.replace(PLACEHOLDER_EFFECT, self.effect)
		page = page.replace(PLACEHOLDER_CHILDREN, children)
		page = page.replace(PLACEHOLDER_NAME, self.name)
		page = page.replace(PLACEHOLDER_BGCOLOR, getDefaultBgColor())
		page = page.replace(PLACEHOLDER_PARENTS, parents)
		
		writer = open("./psalmPages/" + self.name + ".html", "w+")
		writer.write(page)
		writer.close()

#lvl1
Psalm("Hermeticon Psalm", "+3% DMG reduce upon kill", [])
Psalm("Terminus Psalm", "+5% DMG upon kill", [])
Psalm("Voltaic Psalm", "+50 Energy Shield Charge and +50 to Energy Shield upon kill", [])
Psalm("Galvanic Psalm", "5% chance upon kill to reset all cooldowns", [])
Psalm("Iron Psalm", "1% Crit Chance & +1 Crit Power for 2 seconds upon kill", [])
#lvl2
Psalm("Volkite Psalm", "+1 sec DoT duration", ["Hermeticon Psalm", "Terminus Psalm"])
Psalm("Static-burst Psalm", "+1 sec Slow / Shock duration", ["Terminus Psalm", "Voltaic Psalm"])
Psalm("Electro-haze Psalm", "+1 sec Blind / Hallucination duration", ["Voltaic Psalm", "Galvanic Psalm"])
Psalm("Technomartyr Psalm", "When struck, gain +20% damage for 2 seconds. Does not stack.", ["Galvanic Psalm", "Iron Psalm"])
Psalm("Hypergheist Psalm", "When struck, gain +20% movement speed for 2 seconds. Does not stack", ["Hermeticon Psalm", "Iron Psalm"])
#lvl3
Psalm("Emanatus Psalm", "+0.5 sec Stun duration", ["Volkite Psalm", "Volkite Psalm", "Static-burst Psalm", "Static-burst Psalm"])
Psalm("Phosphoenic Psalm", "+10% DMG on Ignited enemies", ["Static-burst Psalm", "Static-burst Psalm", "Electro-haze Psalm", "Electro-haze Psalm"])
Psalm("Hyper-rad Psalm", "+10% DMG on Poisoned enemies", ["Electro-haze Psalm", "Electro-haze Psalm", "Technomartyr Psalm", "Technomartyr Psalm"])
Psalm("Haemo-drain Psalm", "+10% DMG on Bleeding enemies", ["Hypergheist Psalm", "Hypergheist Psalm", "Technomartyr Psalm", "Technomartyr Psalm"])
Psalm("Uncreator Psalm", "Vulnerability bonus increased from 10 to 15%", ["Hypergheist Psalm", "Hypergheist Psalm", "Volkite Psalm", "Volkite Psalm"])
#lvl4
Psalm("Transonic Psalm", "+15% DMG to Slowed, Stunned, or Shocked enemies", ["Emanatus Psalm", "Emanatus Psalm", "Emanatus Psalm", "Phosphoenic Psalm", "Phosphoenic Psalm", "Phosphoenic Psalm"])
Psalm("Animus Psalm", "+15% DMG to Blinded and Hallucinating enemies", ["Phosphoenic Psalm", "Phosphoenic Psalm", "Phosphoenic Psalm", "Hyper-rad Psalm", "Hyper-rad Psalm", "Hyper-rad Psalm"])
Psalm("Shroud Psalm", "When struck, gain +5% DMG reduce for 2 seconds. Does not stack.", ["Hyper-rad Psalm", "Hyper-rad Psalm", "Hyper-rad Psalm", "Haemo-drain Psalm", "Haemo-drain Psalm", "Haemo-drain Psalm"])
Psalm("Binharic Psalm", "+1 sec duration to Psalm-Code effect durations", ["Haemo-drain Psalm", "Haemo-drain Psalm", "Haemo-drain Psalm", "Uncreator Psalm", "Uncreator Psalm", "Uncreator Psalm"])
Psalm("Nova Psalm", "10% chance to Shock enemies within 3 m when struck", ["Emanatus Psalm", "Emanatus Psalm", "Emanatus Psalm", "Uncreator Psalm", "Uncreator Psalm", "Uncreator Psalm"])
#lvl5
Psalm("Ordinatus Psalm", "Reduce the Target's armor by 5% per Hit", ["Transonic Psalm", "Transonic Psalm","Transonic Psalm","Transonic Psalm", "Animus Psalm", "Animus Psalm", "Animus Psalm", "Animus Psalm"])
Psalm("Icarus Psalm", "10% chance on kill to Slow enemies within 3 m", ["Animus Psalm", "Animus Psalm", "Animus Psalm", "Animus Psalm", "Shroud Psalm", "Shroud Psalm", "Shroud Psalm", "Shroud Psalm"])
Psalm("Neuralis Psalm", "Gain +1% damage for each hit for 2 sec", ["Shroud Psalm", "Shroud Psalm", "Shroud Psalm", "Shroud Psalm", "Binharic Psalm", "Binharic Psalm", "Binharic Psalm", "Binharic Psalm"])
Psalm("Aegis Psalm", "+10 Energy Shield HP per hit", ["Binharic Psalm", "Binharic Psalm", "Binharic Psalm", "Binharic Psalm", "Nova Psalm", "Nova Psalm", "Nova Psalm", "Nova Psalm"])
Psalm("Voltagheist Psalm", "Increases Damage Reduction soft cap by 1", ["Transonic Psalm", "Transonic Psalm","Transonic Psalm","Transonic Psalm", "Nova Psalm", "Nova Psalm", "Nova Psalm", "Nova Psalm"])


Psalm.initAllParents()





















