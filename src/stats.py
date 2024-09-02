from src.handler import Handler


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
