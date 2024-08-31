from handler import Handler


class Stats:
    def __init__(self, handler:Handler):
        self.capEnergy = handler.handler.get("capEnergy/value")
        self.energyBars = handler.handler.get("energyBars/value")
        self.energyPower = handler.handler.get("energyPower/value")