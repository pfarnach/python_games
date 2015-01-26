# Written by Pat Farnach and Ben Balzer
# 3rd week @ PDX Code Guild, Winter 2015

# add a Continue Game function?

# maybe use graphics.py to add intermediate windows for between fights (updated stat blocks, loot, etc)


import sys, random

class Hero(object):
    def __init__(self, name):
        self.name = name
        self.honorific = honorifics[random.randint(0,len(honorifics) -1)]
        self.weapon = "Shovel of Digging +1"
        self.hp = 100
        self.defense = 5
        self.magic = 10
        self.gold = 0
        
    def update_stats(self, reward_info, reward):
        if reward == 'heal':
            self.hp += 10
        elif reward == 'weapon':
            self.weapon = reward_info[reward]['val']
        elif reward == 'gold':
            self.gold += 1000    
        elif reward == 'db':
            self.defense += 10    
        elif reward == 'mb':
            self.magic += 10    
            
            
        
        print "Your handsome reward for victory today was " + str(reward_info[reward]['val']) + " " + reward_info[reward]['desc'] + "."
        
        
        
    def attack(self):
        if self.weapon == "Shovel of Digging +1":
            self.damage = random.randrange(5,11)
        elif self.weapon == "A Pick of Flicking":
            self.damage = random.randrange(8,15)
        elif self.weapon == "A Spade of Flattening":
            self.damage = random.randrange(12,20)
        elif self.weapon == "The Bastard Gnome of Grinning Death":
            self.damage = random.randrange(21,31)
        return self.damage
    
    def burn(self, magic_amt):
        damage_to_monster = 0
        if magic_amt <= self.magic:
            if self.magic > 0:
                if magic_amt / float(self.magic) > 0.5:
                    self.recoil = magic_amt - (0.5 * self.magic)
                    damage_to_monster = magic_amt
                    print "You pushed the amulet to its limits and caused a recoil of %d damage." % self.recoil
                else:
                    self.recoil = 0
                    damage_to_monster = magic_amt
            else:
                self.recoil = 5
                print "There isn't enough magic in the amulet.  It sparks you in spite causing %d damage." % self.recoil
        else: 
            self.recoil = 5
            print "You got greedy and tried to use more magic than what you had.  The amulet sparks you in spite causing %d damage." % self.recoil
            # print "The amulet is drained of its energy and yet the spell still blasts from the gem, \nleeching your life force to fuel it's flames. \nCrom's nuts, that HAD to've hurt!"
        return int(self.recoil), damage_to_monster
    
class Monster(object):
    def __init__(self, adj, name, hp, strength, level):
        self.adj = adj
        self.name = name
        self.hp = hp
        self.strength = strength
        self.level = level
        
    def attack(self):
        self.damage = random.randrange(2,7) + (self.strength) + (self.level)
        return self.damage

class Treasure(object):
    def __init__(self, weapons):
        # self.heal = {'heal':10}
        # self.gold = {'gold':1000}
        # self.defense_boost = {'db':10}
        # self.magic_boost = {'mb':10}
        self.weapons = weapons
        
    def get_weapon(self):
        self.weapon_choice = random.choice(self.weapons)
        return self.weapon_choice
        
    def get_reward(self):
        # self.reward = random.choice([self.heal, self.gold, self.defense_boost, self.magic_boost, self.get_weapon()])
        # print self.reward
        self.weapon = self.get_weapon()
        self.rewards = ['heal', 'gold', 'db', 'mb', 'weapon']
        self.reward = random.choice(self.rewards)
        
        rewardinfo = {
            'heal': {'val':10, 'desc':' HP'},
            'weapon': {'val':self.weapon, 'desc':''},
            'gold': {'val':1000, 'desc':' gold'},
            'mb': {'val':10, 'desc':' additional magic'},
            'db': {'val':10, 'desc':' additional defense'},
        }
        
        hero.update_stats(rewardinfo, self.reward)
        
# function to print current stats of our hero on screen
def stats_hero():
    print "\nCurrent stats of %s:" % (hero.name) # +hero.honorific?
    print "HP: %d\nDEFENSE: %d\nSWINGING: %s\nMAGIC: %d\n" % (hero.hp, hero.defense, hero.weapon, hero.magic)
    
def stats_monster():
    print "\nCurrent stats of a{} {}:".format (monster.adj, monster.name)
    print "HP: %d\nSTRENGTH: %d\n" % (monster.hp, monster.strength)


hero_name = raw_input(">> What's your name?: ").title()
hero_home = raw_input(">> From where do you hail?: ").title()

hero_name = "%s of %s" % (hero_name, hero_home)
honorifics = [", The Plucky Pimpernel", ", The Brash Brawler", ", The Doomed Doggerel", ", The Mincing Milquetoast", ", The Sorely Unprepared", ", The All-Too Full of Themself", ", The Blanket-Dragger", ", The Truly, Truly, Truly Outrageous", ", The Wyld Stallyn", ", The Meat Popsicle"]

# weapons list
weapon_list = ["The Bastard Gnome of Grinning Death", "A Spade of Flattening", "A Pick of Flicking"]

# make instance of our hero
hero = Hero(hero_name)

hero_name = hero_name + " " + hero.honorific

treasure = Treasure(weapon_list)

# monster names - boss monster will also come from this list
monster_names = ["Bill the Bad Burrito Bandit", "Fred the Zombie Fry Cook", "Marjorie the Malformed Malcontent", "Helga 'Holymotherofgawd' Horror-Hag", "Biff Biffgore of Biffton", "Trevor Troglodyte, the Creep from the Chevron", "Gelatinous Jolene the Man-Stealer", "Larry Lizardman with the Lazy-Eye", "Ravenous Pack of Purse-Dogs", "Cargo-cult Cannibal who'll kill for your Holy Doohickey of Murder", "Baba Yogurt, the Swamp Culture"]
# monster adjectives - randomized, too (but not removed as they're called, maybe?)
monster_adjs = [" nefarious", "n abominable", "n unapologetically Republican", " lecherous", " noxious", "n incessantly vulgar", " hairy-beyond-description", "n unfortunately nude", " (not actually all that scary, now that you see it)", " gaggingly flatulent"]


# for while loop
alive = True

# start game at level/door 1
current_level = 1

# flavor text
print "\nOur hero, %s, upon hearing tell of a hive of scum and villainy in the Forest of Debauchery," % hero_name
print "set out to return balance and sobriety to the land by passing the Challenge of the Five Doors in one piece."
print "Bringing along their trusty Shovel of Digging +1, and the eldritch-fire amulet they'd"
print "recently found in the Ruins of Long-held Dreams, the slim chance of survival grew slightly. They hoped."
print "\n\nGood luck, %s!\n" % hero_name
stats_hero()
print "\nYou stand in the entryway of the aforementioned hive, staunchly determined, with your trusty trowel clenched in your fists. \nThere are two doors before you, hero. \nBehind one surely lies your destiny, but behind the other waits certain dooooom."

while current_level < 5:
    # take a door choice from user
    door_choice = raw_input("\n>> Which do you choose? 1 or 2?: ")
    
    # if door choice is neither 1 nor 2, kick 'em through using random.choice
    if door_choice != "1" and door_choice != "2":
        door_choice = random.choice(["1","2"])
        print "Sorry, inexplicably, you weren't currently capable of simply typing a '1' or a '2', so I've gone ahead and opened Door '%s' for you." % door_choice
    
    # initiates monster from Monster class using random name from monster list then deletes that name from monster_names
    monster = Monster(random.choice(monster_adjs), random.choice(monster_names), current_level*4, current_level*3, current_level)
    if monster.adj in monster_adjs:
        monster_adjs.remove(monster.adj)
        
    if monster.name in monster_names:
       monster_names.remove(monster.name)
    
    
    print "You kick open the door, weapon at the ready, as a%s %s stands in your way." % (monster.adj, monster.name)
    stats_monster()
    monster_xp = monster.hp + current_level
    
    #describe what commands the player has available, and what they each can do    
    print "\nTo swing your current weapon of badassness and smash this foe, type 's' for Smash;"
    print "If, instead, you would prefer to immolate it with the green fire of the arcane amulet, press 'b' for Burninate;"
    print "Of course, you could always try to heal some of your wounds with the amulet by pressing 'h';"
    print "Or, perhaps you're out of breath, and would rather have a Hot Pocket, type 'z' for going from hero to Zero.\n" 
    print "\nFight!"
    combat_choice = raw_input(">> What do you choose, then? ").lower()
    
    skip = True
    
#print monster.hp, hero.hp
    
    while monster.hp > 0 and hero.hp > 0:  
        
        if skip == False:
            # abridged version of player options below
            print "Type 's' for Smash; press 'b' for Burninate; choose 'h' to heal; or hit 'z' to bravely run away."
            combat_choice = raw_input(">> What do you choose, then? ").lower()
        
        skip = False
            
        monster_strike = monster.attack()
        if combat_choice == "s":
            hero_strike = hero.attack()
            print "\nYou hit a%s %s for %d!" % (monster.adj, monster.name, hero_strike)
            print "\nIt landed a hit on you for %d damage!" % monster_strike
            monster.hp -= hero_strike
            hero.hp -= monster_strike
            
        elif combat_choice == "b":
            magic_amt = int(raw_input("How much magic do you want to use?  Careful, if you use more than half, there's blowback -- you'll get burned: "))
            recoil, hero_magic_strike = hero.burn(magic_amt)
            print "\nBy the Power of Flayskull, you sear %s's flesh for %d damage!! Watch where you point that thing." % (monster.name, hero_magic_strike)
            print "\nIt landed a hit on you for %d damage!" % monster_strike
            hero.magic -= hero_magic_strike
            monster.hp -= hero_magic_strike
            hero.hp = hero.hp - monster_strike - recoil
        
        elif combat_choice == "h":
            magic_amt = int(raw_input("How much healing do you need, hero? Its a one for one trade-off, mind you. "))
            hero.hp += magic_amt
            stats_hero()
            #HEALING
            
        elif combat_choice == "z":
            print "You've chosen to end your first steps on the path toward becoming a legend all the bards sing about, all the children wish they could be..." 
            print "So, back to the doldrums of common life with you. Back to the muck, where it's safe."
            print "Next time an heroic opportunity knocks, try to be less of a wuss? That's a good meatbag."
            print "Try again, %s?" % hero.honorific
            sys.exit(0)
        else:
            print "What was that? Hamster style? Certainly wasn't any kind of recognizable command, but... monster don't care!"
             
            print "\nThe little bugger landed a hit on you for %d damage anyway!" % monster_strike
            hero.hp -= monster_strike
            
        # update hp stats
        print "\nAfter that round of martial tomfoolery:"
        stats_hero()
        stats_monster()
    
    if current_level <= 4:
        if hero.hp <= 0:
            print "Oh, damn. You dead."
            print "Don't you have a cousin that could pick up your banner and soldier on, or is the local populace doomed?"
            sys.exit(0)   
            #menu/restart?

        elif monster.hp <= 0:
            print "Yippe-kaiyay, you ended the monstrosity behind Door #%d!" % current_level
            hero.magic += monster_xp
            hero_magic_up = monster_xp
            print "The amulet gulps down the monster's life force and pulses a bit brighter on it's chain, now."
            print "Your magic reserves have increased by %d!" % hero_magic_up 
            treasure.get_reward()
            stats_hero()
            print "\nHow about that next door, %s?" % hero.name

        current_level += 1

while current_level == 5:
    #BOSS FIGHT!
    
    # take a door choice from user
    door_choice = raw_input("\n>> The final door, hero. Make sure its the right one! \nWhich do you choose? 1 or 2?: ")
    
    # if door choice is neither 1 nor 2, kick 'em through using random.choice
    if door_choice != "1" and door_choice != "2":
        door_choice = random.choice(["1","2"])
        print "I get it. Even the most courageous gets nervous, looking Death in the face, so I've gone ahead and opened Door '%s' for you." % door_choice
    
    # initiates monster from Monster class using random name from monster list then deletes that name from monster_names
    monster = Monster(random.choice(monster_adjs), random.choice(monster_names), current_level*4, current_level*3, current_level)
    if monster.adj in monster_adjs:
        monster_adjs.remove(monster.adj)
        
    if monster.name in monster_names:
       monster_names.remove(monster.name)
    
    
    print "You kick open the door, weapon at the ready, the [BOSS MONSTER] - \na%s %s - stares you down, murder burning hot in their eyes." % (monster.adj, monster.name)
    stats_monster()
    monster_xp = monster.hp + current_level
    
    #describe what commands the player has available, and what they each can do    
    print "\nTo swing your current weapon of badassness and smash this foe, type 's' for Smash;"
    print "If, instead, you would prefer to immolate it with the green fire of the arcane amulet, press 'b' for Burninate;"
    print "Of course, you could always try to heal some of your wounds with the amulet by pressing 'h';"
    print "Or, perhaps you're out of breath, and would rather have a Hot Pocket, type 'z' for going from hero to Zero.\n" 
    print "\nFight!"
    combat_choice = raw_input(">> How will you dispatch this evil? ").lower()
    
    skip = True
    
    print monster.hp, hero.hp
    
    while monster.hp > 0 and hero.hp > 0:  
        
        if skip == False:
            # abridged version of player options below
            print "Type 's' for Smash; press 'b' for Burninate; choose 'h' to heal; or hit 'z' to bravely run away."
            combat_choice = raw_input(">> How will you dispatch this evil? ").lower()
        
        skip = False
            
        monster_strike = monster.attack()
        if combat_choice == "s":
            hero_strike = hero.attack()
            print "\nYou hit a%s %s the [BOSS MONSTER] for %d!" % (monster.adj, monster.name, hero_strike)
            print "\nIn return, the [BOSS MONSTER] landed a hit on you for %d damage!" % monster_strike
            monster.hp -= hero_strike
            hero.hp -= monster_strike
            
        elif combat_choice == "b":
            magic_amt = int(raw_input("How much magic do you want to use?  Careful, if you use more than half, there's blowback -- you'll get burned: "))
            recoil, hero_magic_strike = hero.burn(magic_amt)
            print "\nBy the Power of Flayskull, you sear the [BOSS MONSTER]'s flesh for %d damage!! Watch where you point that thing." % (hero_magic_strike)
            print "\nIt landed a hit on you for %d damage!" % monster_strike
            hero.magic -= hero_magic_strike
            monster.hp -= hero_magic_strike
            hero.hp = hero.hp - monster_strike - recoil
        
        elif combat_choice == "h":
            magic_amt = int(raw_input("How much healing do you need, hero? Its a one for one trade-off, so give me a number: "))
            hero.hp += magic_amt
            stats_hero()
            #HEALING
        
        elif combat_choice == "z":
            print "You've chosen to end your first steps on the path toward becoming a legend all the bards sing about, all the children wish they could be..." 
            print "So, back to the doldrums of common life with you. Back to the muck, where it's safe."
            print "Next time an heroic opportunity knocks, try to be less of a wuss? That's a good meatbag."
            print "Try again, %s?" % hero.name
            sys.exit(0)
        else:
            print "What was that? Hamster style? Certainly wasn't any kind of recognizable command, but... monster don't care!"
             
            print "\nThe [BOSS MONSTER] landed a hit on you for %d damage anyway!" % monster_strike
            hero.hp -= monster_strike
            
        # update hp stats
        print "\nAfter that round of martial tomfoolery:"
        stats_hero()
        stats_monster()
    
#if current_level == 5:
    if hero.hp <= 0:
        print "Oh, damn. You dead. And you were so close, too!"
        print "Better luck next time the world needs saving, I guess?"
        sys.exit(0)   
#menu/restart?

    elif monster.hp <= 0:
        print "Beyond all odds, you vanquished the [BOSS MONSTER], plaguing the area from behind Door #%d!" % current_level
        hero.magic += monster_xp
        hero_magic_up = monster_xp
        print "The amulet gulps down the monster's life force and pulses a bit brighter on it's chain, now."
        print "Your magic reserves have increased by %d!" % hero_magic_up 
        treasure.get_reward()
        
        print "\nWith all that gold and well-earned fame from an afternoon's work, maybe you could retire to a nice, quiet life, and enjoy the rest of your years in relative happy simplicity." 
        print "Or, you could hit the road again and wander the earth, righting wrongs and butting into other people's problems for cash and notoriety, \ndying an early death at the hands of some random mutant."
        print "Its really up to you, but congrats on this victory all the same, %s%s. Well done!!" % (hero.name, hero.honorific)
        sys.exit(0)
 
 

