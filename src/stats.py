from src.handler import Handler

from src.utils.perks_quirk_names import itopod_perk_name
from src.utils.perks_quirk_names import quirk_names

# TODO: left 1-61, 66, 67, 76, 77
sets = {
    'traning': [62, 63, 64, 65, 75],
    'sewers': [40, 41, 42, 43, 44, 45, 46],
    'forest': [47, 48, 49, 50, 51, 52, 53],
    'cave': [54, 55, 56, 57, 58, 59, 60, 61],
    'hsb': [68, 69, 70, 71, 72, 73, 74],
    'grb': [78, 79, 80, 81, 82, 83, 84],
    'clockwork': [85, 86, 87, 88, 89, 90, 91],
    '2d': [95, 96, 97, 98, 99, 100, 101],
    'spoopy': [103, 104, 105, 106, 107, 108, 109],
    'green_heart': [171],
    'pissed_off_key': [172],
    'blue_heart': [196],
    'red_liquid': [93],
    'ppp': [231, 232, 233, 234, 235, 236],
    'purple_heart': [212],
    'badly_drawn': [168, 164, 165, 166, 167],

}


class Stats:
    def __init__(self, handler: Handler):
        self.process_ratios_stats(handler)
        self.maxed_sets = self.process_sets(handler)
        self.is_evil = False
        # ITOPOD
        self.ictpod_perk_dict = dict(zip(itopod_perk_name,
                                         handler.handler.get("adventure/value/itopod/value/perkLevel/value")['_items'][
                                             'value']))
        self.ictpod_highest_level = handler.handler.get("adventure/value/highestItopodLevel/value")
        self.quirk_perk_dict = dict(
            zip(quirk_names, handler.handler.get("beastQuest/value/quirkLevel/value/_items/value")))

        self.ngu_magic_exp = handler.handler.get("NGU/value/magicSkills/value/_items")['value'][1]['level']['value']
        self.ngu_energy_pp = handler.handler.get("NGU/value/skills/value/_items")['value'][8]['level']['value']

        self.spooky_set_bonus = self.maxed_sets['spoopy']

    def process_sets(self, handler):
        get_items_maxed_tf = [bool(x) for x in
                              handler.handler.get('inventory/value/itemList/value/itemMaxxed/value/_items/value')]
        items_maxed = dict(zip(range(len(get_items_maxed_tf)), get_items_maxed_tf))
        sets_new = {}
        for key, value in sets.items():
            sets_new[key] = all(items_maxed[x] for x in value)
        return sets_new

    def process_ratios_stats(self, handler):
        # ENERGY

        self.energy_base_power = handler.handler.get("energyPower/value")
        self.energy_base_cap = handler.handler.get("capEnergy/value")
        self.energy_base_bar = handler.handler.get("energyBars/value")
        # MAGIC
        self.magicCap = handler.handler.get("magic/value/capMagic/value")
        self.magicPower = handler.handler.get("magic/value/magicPower/value")
        self.magicBar = handler.handler.get("magic/value/magicPerBar/value")
        # R3
        self.r3_base_power = handler.handler.get("res3/value/res3Power/value")
        self.r3_base_cap = handler.handler.get("res3/value/capRes3/value")
        self.r3_base_bar = handler.handler.get("res3/value/res3PerBar/value")
