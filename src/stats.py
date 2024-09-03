from src.handler import Handler
from src.icopod.icopod import itopod_perk_name


class Stats:
    def __init__(self, handler:Handler):
        #ENERGY
        self.energy_base_power = handler.handler.get("energyPower/value")
        self.energy_base_cap = handler.handler.get("capEnergy/value")
        self.energy_base_bar = handler.handler.get("energyBars/value")
        #MAGIC
        self.magicCap = handler.handler.get("magic/value/capMagic/value")
        self.magicPower = handler.handler.get("magic/value/magicPower/value")
        self.magicBar = handler.handler.get("magic/value/magicPerBar/value")
        #R3
        self.r3_base_power = handler.handler.get("res3/value/res3Power/value")
        self.r3_base_cap = handler.handler.get("res3/value/capRes3/value")
        self.r3_base_bar = handler.handler.get("res3/value/res3PerBar/value")
        #ITOPOD
        self.ictpod_perk_dict = dict(zip(itopod_perk_name, handler.handler.get("adventure/value/itopod/value/perkLevel/value")['_items']['value']))
        self.power = handler.handler.get("adventure/value/attack/value")
        self.toughness = handler.handler.get("adventure/value/defence/value")
        self.regen = handler.handler.get("adventure/value/regen/value")
        self.hp = handler.handler.get("adventure/value/curHP/value")
        self.highest_level = handler.handler.get("adventure/value/highestItopodLevel/value")

        self.ngu_magic_exp = handler.handler.get("NGU/value/magicSkills/value/_items")['value'][1]
