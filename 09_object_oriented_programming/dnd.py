from ctypes.wintypes import HPALETTE
import random

class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 8
        # Stats are, in order: Strength, Dexterity, Constitution, Intelligence, Wisdom, & Charisma
        self.stats = []
        self.hit = 0
        self.attack = 1
    def roll_stats(self):
        rolls = []
        stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        # Takes the highest 3 of 4 dice rolls and adds them to stats
        for stat in range(6):
            current_roll = [random.randint(1, 6) for i in range(4)]
            current_roll.sort()
            current_roll.pop[-1]
            rolls.append(sum(current_roll))
        print("Your rolls are: " + str(rolls))
        for i in stats:
            selection = input("Please select which roll to assign as your {} stat.".format(i))
            try:
                selection = int(selection)
            except: ValueError
            else:
                if selection in rolls:
                    rolls.remove(selection)
                    self.stats.append(selection // 2 - 5)
                    print("Your remaining rolls are: " + str(rolls))
                else:
                    print("Select a value equal to one of your remaining rolls.")
        self.hp += self.stats[2]
    def level_up(self):
        if self.level < 20:
            self.level += 1
            self.hp += random.randint(1, 8) + self.stats[2]
            if self.level // 4 == 0:
                ability_score_increase = input("Which stat would you like to increase? \n[1] STR\n[2] DEX\n[3] CON\n[4] INT\n[5] WIS\n[6] CHA")
                if ability_score_increase in 
                    self.stats[ability_score_increase]
