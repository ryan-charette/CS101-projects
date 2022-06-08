import random

stat_list = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 8
        self.stats = []
        self.hit = 0
        self.damage = 8
        self.armor = 13
    def __repr__(self):
        print_statement = self.name + ":\n"
        for stat in range(len(self.stats)):
            print_statement += "{}: {}\n".format(stat_list[stat], self.stats[stat])
        return print_statement
    def roll_stats(self):
        rolls = []
        # Takes the highest 3 of 4 dice rolls and adds them to stats
        for stat in range(6):
            current_roll = [random.randint(1, 6) for i in range(4)]
            current_roll.sort()
            current_roll.pop(0)
            rolls.append(sum(current_roll))
        print("Your rolls are: " + str(rolls))
        for stat in stat_list:
            selection = input("Please select which roll to assign as your {} stat.\n".format(stat))
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
        self.hit += self.stats[0]
        self.armor += self.stats[1]
    def level_up(self):
        if self.level < 20:
            self.level += 1
            self.hp += random.randint(1, 8) + self.stats[2]
            if self.level % 4 == 0:
                ability_score_increase = int(input("Which stat would you like to increase? \n[1] STR\n[2] DEX\n[3] CON\n[4] INT\n[5] WIS\n[6] CHA\n"))
                if ability_score_increase in [1, 2, 3, 4, 5, 6]:
                    self.stats[ability_score_increase - 1] += 1
                else:
                    print("Invalid input.")
    def attack(self, monster):
        hit_roll = self.hit + random.randint(1, 20)
        if hit_roll > monster.armor:
            damage = random.randint(1, self.damage)
            monster.hp -= damage
            print("You hit the {} for {} damage!".format(monster.name, damage))
        else:
            print("You miss!")
        if monster.hp <= 0:
            print("You killed the {}!".format(monster.name))
        return

class Monster:
    def __init__(self, name = "monster", level = 1, size = "medium"):
        self.name = name
        self.level = level
        self.size = size
        self.hit = self.level // 2
        self.armor = self.hit + 11
        if self.size == "small":
            self.hp = 8
            self.damage = 4
            for lvl in range(level - 1):
                self.hp += random.randint(1, 8)
        elif self.size == "medium":
            self.hp = 12
            self.damage = 8
            for lvl in range(level - 1):
                self.hp += random.randint(1, 12)
        elif self.size == "large":
            self.hp = 20
            self.damage = 12
            for lvl in range(level - 1):
                self.hp += random.randint(1, 20)
    def __repr__(self):
        return "The {} is a level {} {} creature.".format(self.name, self.level, self.size)
    def attack(self, hero):
        hit_roll = self.hit + random.randint(1, 20)
        if hit_roll > hero.armor:
            damage = random.randint(1, self.damage)
            hero.hp -= damage
            print("The {} hit you for {} damage!".format(self.name, damage))
        else:
            print("The {} missed!".format(self.name))
        if hero.hp <= 0:
            print("You were killed by the {}!".format(self.name))
        return

sir_galahad = Hero("Sir Galahad")
sir_galahad.roll_stats()
for level in range(7):
    sir_galahad.level_up()

black_knight = Monster("Black Knight", 5, "medium")

print(sir_galahad)
print(black_knight)

print("The {} approaches!".format(black_knight.name))
while sir_galahad.hp > 0 and black_knight.hp > 0:
    if input() != "q":
        sir_galahad.attack(black_knight)
    if input() != "q" and black_knight.hp > 0:
        black_knight.attack(sir_galahad)
