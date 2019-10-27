########################################### PAERNT/GENERIC CLASS #
class character:
    def __init__(self, name, health, dmg):
        self.name = name
        self.health = health
        self.dmg = dmg

    def attack(self, target):
        print(f"{self.name} attacked {target.name} for {self.dmg}")
        target.health -= self.dmg

    def special(self, target):
        print("You have no speical moves")

    def info(self):
        print(f"{self.name} has {self.health} health")

############################## CLASSES INHERITING FROM CHARACTER #
# low health, high dmg, one time big dmg
class jedi(character):
    def __init__(self, name):
        super().__init__(name, 80, 25)
        self.special_usedup = False

    def special(self, target):
        if(self.special_usedup):
            print("You go to use the force again, but you're tapped out")
        else:
            print(f"{self.name} used their jedi powers to deal a POWERFUL BLOW. You cannot use this power again")
            self.special_usedup = True
            target.health -= self.dmg*2

# mid health, mid dmg, stun special
class wizard(character):
    def __init__(self, name):
        super().__init__(name, 100, 20)

    def special(self, target):
        print(f"{self.name} threw a  mysterious potion on the ground, hitting {target.name} for 10 damage, and healing themselves for 10")
        target.health -= 10
        self.health += 15

# high health, low dmg, buff special
class ninja(character):
    def __init__(self, name):
        super().__init__(name, 120, 15)

    def special(self, target):
        print(f"Ninja Master {self.name} used the power of algorithms to optimize their attacks.  Their damage went up!")
        self.dmg *= 1.75
        self.dmg = round(self.dmg)

# broken easter egg class
class kitty(character):
    def __init__(self):
        super().__init__("Nick Furry", 1000000, 999)
    
    def special(self, target):
        print(f"""
            Nick Furry purrs and shows his belly for pets. 
            Awwwww, who could fight a kitty that cuuuute!
            {target.name} forfeits!
        """)
        target.health = -1000000