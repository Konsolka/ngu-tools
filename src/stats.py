from src.handler import Handler

itopod_perk_name = ['The Newbie Energy Perk', 'The Newbie Magic Perk', 'The Newbie Adventure Perk', 'The Newbie Drop Chance Perk', 'The Newbie Stat Perk', 'Stat Boost For Rich Perks I', 'Generic Energy Power Perk I', 'Generic Energy Bar Perk I', 'Generic Energy Cap Perk I', 'Generic Magic Power Perk I', 'Generic Magic Bar Perk I', 'Generic Magic Cap Perk I', 'Boosted Boosts I', 'Faster NGU Energy', 'Faster NGU Magic', 'Double Basic Training', 'Quicker Fruit of Power ОІ Bonus Activation', 'Quicker Fruit of Numbers Bonus Activation', 'Instant Advanced Training Levels', '"Fruit of Knowledge sucks 1/5"', '"Fruit of Knowledge STILL sucks 1/5"', "Five O'Clock Shadow", 'Wandoos Lover', 'Golden Showers', 'I want your seeds ;)', "The Loot Goblin's Blessing", 'Improved Cube Boosting!', "Daycare Kitty's Blessing I", "Daycare Kitty's Blessing II", "You'll Really Want This", 'What a Crappy Perk', 'More Inventory Space I', 'More Inventory Space II', 'Boosted Boosts II', 'Bonus Titan EXP!', 'Bonus Boss EXP!', 'Adv. Training Level Bank I', 'Adv. Training Level Bank II', 'Adv. Training Level Bank III', 'Adv. Training Level Bank IV', 'Adv. Training Level Bank V', 'Time Machine Level Bank I', 'Time Machine Level Bank II', 'Time Machine Level Bank III', 'Time Machine Level Bank IV', 'Time Machine Level Bank V', 'Beard Temp Level Bank I', 'Beard Temp Level Bank II', 'Beard Temp Level Bank III', 'Beard Temp Level Bank IV', 'Beard Temp Level Bank V', "The First Harvest's The Best", 'A Digger Slot!', 'Ooh, Another Digger Slot!', 'Stat Boost For Rich Perks II', 'Adventure Boost For Rich Perks I', 'MacGuffin Daycare!', 'Generic Energy Power Perk II', 'Generic Energy Bar Perk II', 'Generic Energy Cap Perk II', 'Generic Magic Power Perk II', 'Generic Magic Bar Perk II', 'Generic Magic Cap Perk II', 'Faster NGU Energy II', 'Faster NGU Magic II', 'Improved MacGuffin Drops I', 'A MacGuffin Slot!', 'Another MacGuffin Slot!', 'MacGuffin ITOPOD Drops!', 'Improved MacGuffin ITOPOD Drops I', 'Improved MacGuffin ITOPOD Drops II', 'Improved MacGuffin ITOPOD Drops III', 'Blood MacGuffin О± Spell!', 'Blood MacGuffin ОІ Spell!', 'Generic Energy Power Perk III', 'Generic Energy Bar Perk III', 'Generic Energy Cap Perk III', 'Generic Magic Power Perk III', 'Generic Magic Bar Perk III', 'Generic Magic Cap Perk III', 'Faster NGU Energy III', 'Faster NGU Magic III', 'Stat Boost For Rich Perks III', 'Adventure Boost For Rich Perks II', 'Iron Pill Also Sucks 1/5', 'Iron Pill Still Sucks 1/5', 'Daycare Slot! c:', 'Not So Minor Anymore', 'Another MacGuffin Slot!', 'Better QP Rewards!', 'Improved Quest Looting', 'Advanced Gooder Idle Questing', 'Even More Advanced Gooder Idle Questing', 'Spawn Faster Damnit', 'The Fibonacci Perk', 'Generic Resource 3 Power Perk I', 'Generic Resource 3 Bar Perk I', 'Generic Resource 3 Cap Perk I', 'Generic Resource 3 Power Perk II', 'Generic Resource 3 Bar Perk II', 'Generic Resource 3 Cap Perk II', 'Generic Resource 3 Power Perk III', 'Generic Resource 3 Bar Perk III', 'Generic Resource 3 Cap Perk III', 'Truly Idle Questing', 'Gooder Idle Questing!', 'Another Gooder Idle Questing!', 'Boosted Boosts III', 'Faster wishes I', 'Minimum Wish Time Reduction I', 'Minimum Wish Time Reduction II', 'An Inventory Merge Slot', 'Another Inventory Merge Slot', 'Adventure Hack Milestone Reducer I', 'Blood Hack Milestone Reducer I', 'Daycare Hack Milestone Reducer I', 'Generic Energy Power Perk IV', 'Generic Energy Bar Perk IV', 'Generic Energy Cap Perk IV', 'Generic Magic Power Perk IV', 'Generic Magic Bar Perk IV', 'Generic Magic Cap Perk IV', 'Generic Resource 3 Power Perk IV', 'Generic Resource 3 Bar Perk IV', 'Generic Resource 3 Cap Perk IV']
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

}

class Stats:
    def __init__(self, handler:Handler):
        self.process_ratios_stats(handler)
        self.maxed_sets = self.process_sets(handler)
        self.is_evil = False
        #ITOPOD
        self.ictpod_perk_dict = dict(zip(itopod_perk_name, handler.handler.get("adventure/value/itopod/value/perkLevel/value")['_items']['value']))
        self.ictpod_highest_level = handler.handler.get("adventure/value/highestItopodLevel/value")

        self.ngu_magic_exp = handler.handler.get("NGU/value/magicSkills/value/_items")['value'][1]['level']['value']
        self.ngu_energy_pp = handler.handler.get("NGU/value/skills/value/_items")['value'][8]['level']['value']

        self.spooky_set_bonus = self.maxed_sets['spoopy']
    def process_sets(self, handler):
        get_items_maxed_tf = [bool(x) for x in handler.handler.get('inventory/value/itemList/value/itemMaxxed/value/_items/value')]
        items_maxed = dict(zip(range(len(get_items_maxed_tf)), get_items_maxed_tf))
        sets_new = {}
        for key, value in sets.items():
            sets_new[key] = all(items_maxed[x] for x in value)
        return sets_new

    def process_ratios_stats(self, handler):
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