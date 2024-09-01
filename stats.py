from handler import Handler


class Stats:
    def __init__(self, handler:Handler):
        #ENERGY
        self.capEnergy = handler.handler.get("capEnergy/value")
        self.energyBars = handler.handler.get("energyBars/value")
        self.energyPower = handler.handler.get("energyPower/value")
        #MAGIC
        self.magicCap = handler.handler.get("magic/value/capMagic/value")
        self.magicPower = handler.handler.get("magic/value/magicPower/value")
        self.magicBar = handler.handler.get("magic/value/magicPerBar/value")
