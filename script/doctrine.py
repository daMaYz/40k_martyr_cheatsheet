#!/usr/bin/python
from psalm import Psalm

class Doctrine:
	doctrineList = []
	
	def __init__(self, effect, children):
		self.effect = effect
		self.children = children
		self.doctrineList.append(self)
		self.level = len(children) - 2
		
	def getChildrenAsPsalm(self):
		children = []
		for child in self.children:
			children.append(Psalm.findByName(child))
		return children
		
	def getChildrenAsHtml(self):
		html = ""
		for child in self.children:
			html += Psalm.findByName(child).getImgTag(".")
		return html
		
	def getFullEffect(self):
		effect = "<h3>" + self.effect + "</h3>"
		effect += self.getChildrenEffects()
		return effect
		
	def getChildrenEffects(self):
		childrenEffects = ""
		for child in self.children:
			childrenEffects += Psalm.findByName(child).effect
			childrenEffects += "<br>"
		return childrenEffects
		
	def getAll(lvl = 0):
		list = []
		if lvl == 0:
			return Doctrine.doctrineList
		else:
			for doc in Doctrine.doctrineList:
				if doc.level == lvl:
					list.append(doc)
			return list



Doctrine("All Warp Damage becomes Armour Breaking", ["Terminus Psalm", "Iron Psalm", "Technomartyr Psalm"])
Doctrine("+50% Damage and +30 Dodge while in Surprise state", ["Hermeticon Psalm", "Galvanic Psalm", "Volkite Psalm"])
Doctrine("100% Physical Damage is converted to Warp DamageGain +20% Warp Damage", ["Hermeticon Psalm", "Galvanic Psalm", "Iron Psalm"])
Doctrine("Melee attacks against Energy Shield reflect 100% Damage to the attacker", ["Voltaic Psalm", "Voltaic Psalm", "Technomartyr Psalm"])
Doctrine("Bleed status on enemies causes 100% Damage while they are near the hero", ["Terminus Psalm", "Haemo-drain Psalm", "Volkite Psalm"])
Doctrine("Each kill halves the remaining Cooldown of skills", ["Galvanic Psalm", "Iron Psalm", "Terminus Psalm"])
Doctrine("10% of all DoT Damage caused is gained as Suppression", ["Volkite Psalm", "Terminus Psalm", "Phosphoenic Psalm"])
Doctrine("+50% Grenade and Mine Damage", ["Static-burst Psalm", "Galvanic Psalm", "Iron Psalm"])
Doctrine("+50% Minion HP", ["Emanatus Psalm", "Galvanic Psalm", "Volkite Psalm"])
Doctrine("Critical Hit Chance is reduced to zero but weapon base damage is increased by 30%", ["Terminus Psalm", "Technomartyr Psalm", "Uncreator Psalm"])
Doctrine("+50% Heat Damage", ["Phosphoenic Psalm", "Volkite Psalm", "Hypergheist Psalm"])
Doctrine("+50% Physical Damage", ["Emanatus Psalm", "Electro-haze Psalm", "Iron Psalm"])
Doctrine("+50% Warp Damage", ["Uncreator Psalm", "Binharic Psalm", "Static-burst Psalm"])
Doctrine("Killing a Shocked enemy creates an explosion causing Shock and dealing damage equal to Damage from the killing blow", ["Nova Psalm", "Volkite Psalm", "Transonic Psalm"])
Doctrine("+100% Heat Damage", ["Phosphoenic Psalm", "Binharic Psalm", "Volkite Psalm", "Terminus Psalm"])
Doctrine("+100% Physical Damage", ["Haemo-drain Psalm", "Animus Psalm", "Aegis Psalm", "Uncreator Psalm"])
Doctrine("+100% Warp Damage", ["Neuralis Psalm", "Transonic Psalm", "Hypergheist Psalm", "Phosphoenic Psalm"])
Doctrine("Reduces Damage Reflect from enemies by 80%", ["Aegis Psalm", "Voltaic Psalm", "Hypergheist Psalm", "Technomartyr Psalm"])
Doctrine("Energy Shield HP is doubled but Maximum HP is reduced to 10%", ["Aegis Psalm", "Hypergheist Psalm", "Shroud Psalm", "Nova Psalm"])
Doctrine("Creates a damaging aura around the hero dealing (Base DMG*10%/sec) Heat damage", ["Phosphoenic Psalm", "Technomartyr Psalm", "Neuralis Psalm", "Binharic Psalm"])
Doctrine("Combo attacks deal 300% increased Damage", ["Neuralis Psalm", "Transonic Psalm", "Terminus Psalm", "Shroud Psalm"])
Doctrine("200% bonus to class resource recharge rate", ["Galvanic Psalm", "Icarus Psalm", "Phosphoenic Psalm", "Hypergheist Psalm"])
Doctrine("All Fleshbane attacks also cause Bleed", ["Transonic Psalm", "Haemo-drain Psalm", "Neuralis Psalm", "Volkite Psalm"])
Doctrine("All Critical hits also Stun enemies", ["Iron Psalm", "Emanatus Psalm", "Ordinatus Psalm", "Binharic Psalm"])
Doctrine("All AoE attacks affect a 30% smaller area but gain +150% Damage", ["Aegis Psalm", "Neuralis Psalm", "Iron Psalm", "Uncreator Psalm"])
Doctrine("All Heat type attacks have a 10% chance to Ignite enemies as well", ["Neuralis Psalm", "Hypergheist Psalm", "Phosphoenic Psalm", "Galvanic Psalm"])
Doctrine("+50% Minion Damage", ["Ordinatus Psalm", "Transonic Psalm", "Phosphoenic Psalm", "Hermeticon Psalm"])
Doctrine("+100% Damage to all Rifle Skills", ["Hyper-rad Psalm", "Terminus Psalm", "Uncreator Psalm", "Aegis Psalm"])
Doctrine("+100% Damage to all Pistol Skills", ["Static-burst Psalm", "Phosphoenic Psalm", "Iron Psalm", "Hypergheist Psalm"])
Doctrine("+100% Damage to all Heavy Weapon Skills", ["Shroud Psalm", "Icarus Psalm", "Static-burst Psalm", "Hermeticon Psalm"])
Doctrine("+100% Damage to all One-Handed Melee Weapon Skills", ["Ordinatus Psalm", "Shroud Psalm", "Emanatus Psalm", "Voltaic Psalm"])
Doctrine("+100% Damage to all Two-Handed Melee Weapon Skills", ["Transonic Psalm", "Voltaic Psalm", "Hyper-rad Psalm", "Animus Psalm"])
Doctrine("+50% Heat Damage and Heat Resistance of enemies is halved", ["Uncreator Psalm", "Phosphoenic Psalm", "Icarus Psalm", "Ordinatus Psalm", "Binharic Psalm"])
Doctrine("+50% Physical Damage and Physical Resistance of enemies is halved", ["Hyper-rad Psalm", "Haemo-drain Psalm", "Ordinatus Psalm", "Technomartyr Psalm", "Shroud Psalm"])
Doctrine("+50% Warp Damage and Warp Resistance of enemies is halved", ["Animus Psalm", "Electro-haze Psalm", "Voltagheist Psalm", "Nova Psalm", "Shroud Psalm"])
Doctrine("200% DoT duration", ["Hyper-rad Psalm", "Haemo-drain Psalm", "Binharic Psalm", "Hermeticon Psalm", "Voltagheist Psalm"])
Doctrine("Each vulnerability stack has a 300% increased effect on DoT effects", ["Technomartyr Psalm", "Haemo-drain Psalm", "Icarus Psalm", "Static-burst Psalm", "Uncreator Psalm"])
Doctrine("All skills that have Spread have their spread reduced", ["Ordinatus Psalm", "Neuralis Psalm", "Animus Psalm", "Hermeticon Psalm", "Emanatus Psalm"])
Doctrine("+30 HP/hit and Energy Shield HP/hit", ["Voltaic Psalm", "Aegis Psalm", "Hermeticon Psalm", "Shroud Psalm", "Emanatus Psalm"])
Doctrine("Below 10% HP, the hero becomes ethereal and gains 50% Movement Speed for 3 seconds (can only activate once every 10 seconds)", ["Technomartyr Psalm", "Hypergheist Psalm", "Shroud Psalm", "Nova Psalm", "Galvanic Psalm"])
Doctrine("Inflicting a Burn DoT on an enemy also puts Burn DoT on nearby enemies", ["Terminus Psalm", "Phosphoenic Psalm", "Icarus Psalm", "Phosphoenic Psalm", "Volkite Psalm"])
Doctrine("Inflicting a Poison DoT on an enemy also puts Poison DoT on nearby enemies", ["Hyper-rad Psalm", "Hyper-rad Psalm", "Transonic Psalm", "Voltagheist Psalm", "Hermeticon Psalm"])
Doctrine("+200% Damage against Shocked, Slowed or Stunned enemies", ["Static-burst Psalm", "Static-burst Psalm", "Nova Psalm", "Transonic Psalm", "Emanatus Psalm", "Transonic Psalm"])
Doctrine("50% of all Damage is substracted from Suppression instead of HP", ["Hermeticon Psalm", "Voltagheist Psalm", "Galvanic Psalm", "Electro-haze Psalm", "Animus Psalm", "Shroud Psalm"])
Doctrine("Causing Shock on an enemy creates an explosion dealing halved Damage and Shock to nearby enemies", ["Transonic Psalm", "Nova Psalm", "Icarus Psalm", "Aegis Psalm", "Animus Psalm", "Technomartyr Psalm"])
Doctrine("+100% Suppression regeneration and +10% Damage Reduction per second while channeling skills (maximum +40% Damage Reduction)", ["Aegis Psalm", "Voltagheist Psalm", "Voltaic Psalm", "Technomartyr Psalm", "Shroud Psalm", "Transonic Psalm"])
Doctrine("+20% Damage bonus on Hit Taken for 3 seconds (maximum 300%)", ["Nova Psalm", "Haemo-drain Psalm", "Technomartyr Psalm", "Hypergheist Psalm", "Hermeticon Psalm", "Binharic Psalm"])
Doctrine("For each projectile with Physical Damage, two additional projectiles are created in a 10° cone but skill damage is halved", ["Ordinatus Psalm", "Neuralis Psalm", "Terminus Psalm", "Galvanic Psalm", "Terminus Psalm", "Icarus Psalm"])




















