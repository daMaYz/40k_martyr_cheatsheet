#!/usr/bin/python

class Psalm:
	psalmList = []
	def __init__(self, name, effect, children):
		self.name = name
		self.effect = effect
		self.children = children
		self.psalmList.append(self)
		
	def setChildren(self, children):
		self.children = children
		
	def getChildrenAsPsalm(self):
		children = []
		for child in self.children:
			children.append(Psalm.findByName(child))
		return children

	def getImageFile(self):
		return "./res/" + self.name + ".png"

	def getHtmlFile(self, dir):
		return dir + "/psalmPages/" + self.name + ".html"

	def findByName(name):
		for psalm in Psalm.psalmList:
			if name == psalm.name:
				return psalm
				
	def getImgTag(self, dir):
		return "<a href=\"" + self.getHtmlFile(dir) + "\"><img src=\"" + dir + "/res/" + self.name + ".png\" title=\"" + self.name + "\"></a>"
		
	
	def writePsalmHtml(self):
		writer = open("./psalmPages/" + self.name + ".html", "w+")
		writer.write("<html><head><title>" + self.name + "</title></head><body>")
		writer.write("<a href=\"../index.html\">mainPage</a>")
		writer.write("<h1>" + self.name + "</h1>")
		writer.write(self.getImgTag("..") + "<br><br>")
		writer.write(self.effect + "<br><br><h3>Children</h3>")
		for child in self.children:
			writer.write(Psalm.findByName(child).getImgTag(".."))
		writer.write("</body></html>")
		writer.close()

Psalm("Hermeticon Psalm", "+3% DMG reduce upon kill", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Terminus Psalm", "+5% DMG upon kill", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Voltaic Psalm", "+50 Energy Shield Charge and +50 to Energy Shield upon kill", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Galvanic Psalm", "5% chance upon kill to reset all cooldowns", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Iron Psalm", "1% Crit Chance & +1 Crit Power for 2 seconds upon kill", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Volkite Psalm", "+1 sec DoT duration", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Static-burst Psalm", "+1 sec Slow / Shock duration", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Electro-haze Psalm", "+1 sec Blind / Hallucination duration", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Technomartyr Psalm", "When struck, gain +20% damage for 2 seconds. Does not stack.", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Hypergheist Psalm", "When struck, gain +20% movement speed for 2 seconds. Does not stack", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Emanatus Psalm", "+0.5 sec Stun duration", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Phosphoenic Psalm", "+10% DMG on Ignited enemies", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Hyper-rad Psalm", "+10% DMG on Poisoned enemies", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Haemo-drain Psalm", "+10% DMG on Bleeding enemies", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Uncreator Psalm", "Vulnerability bonus increased from 10 to 15%", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Transonic Psalm", "+15% DMG to Slowed, Stunned, or Shocked enemies", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Animus Psalm", "+15% DMG to Blinded and Hallucinating enemies", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Shroud Psalm", "When struck, gain +5% DMG reduce for 2 seconds. Does not stack.", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Binharic Psalm", "+1 sec duration to Psalm-Code effect durations", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Nova Psalm", "10% chance to Shock enemies within 3 m when struck", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Ordinatus Psalm", "Reduce the Target's armor by 5% per Hit", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Icarus Psalm", "10% chance on kill to Slow enemies within 3 m", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Neuralis Psalm", "Gain +1% damage for each hit for 2 sec", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Aegis Psalm", "+10 Energy Shield HP per hit", ["Voltaic Psalm", "Electro-haze Psalm"])
Psalm("Voltagheist Psalm", "Increases Damage Reduction soft cap by 1", ["Voltaic Psalm", "Electro-haze Psalm"])























