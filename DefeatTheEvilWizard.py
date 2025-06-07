
# Import necessary modules
from asyncio.windows_events import NULL
import math
import random

# Function to find an ability by command name
def get_abilitie(command, abilities_list):
    for t in abilities_list:
        if(t.command.lower() == command.lower()):
            return(t)

# Class representing an ability
class abilitie:
    def __init__(self, name="", attack_power=0, shild=1, drain=0, heal=0, effect=NULL, effect_description="", command="", max_summon=0, attack_type="basic attack"):
        self.name = name
        self.attack_power = attack_power
        self.shild = shild
        self.drain = drain
        self.heal = heal
        self.effect = effect
        self.effect_description = effect_description
        self.command = command
        self.max_summon = max_summon
        self.minions = 0
        self.attack_type = attack_type
        # Summon minions if max_summon is set
        if(self.max_summon > 0):
            self.minions = self.summon_minions(max_summon)

    # Method to summon minions and apply damage effect
    def summon_minions(self, max_minions):
        if(self.max_summon > 0):
            minions = random.randint(1, max_minions)
            self.effect_description = f"This Effect summoned {minions} minions to attack the apponent dealing upto a maximum of {self.attack_power} damage per minion of added damage points"
            self.attack_power = minions * self.attack_power
            return(minions)

# Base character class
class Character:
    def __init__(self, name, health, abilities, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.shild = 1
        self.ability_points = 100
        self.abilites = abilities
        self.active_abilitie = 0
        self.active_effect = NULL
        self.attack_power = attack_power

    # Attack method
    def attack(self, opponent, abilitie_command):
        ab = get_abilitie(abilitie_command, self.abilites)
        damage = 0
        if self.ability_points >= ab.drain:
            self.active_abilitie = abilitie_command

            # Modify opponent's shield
            if opponent.shild < 1:
                opponent.shild += (ab.attack_power + self.attack_power)/100
                if opponent.shild > 1:
                    opponent.shild = 1

            # Calculate damage
            if opponent.shild == 1:
                damage = random.randint(self.attack_power + math.floor(ab.attack_power/2), (ab.attack_power + self.attack_power))
            else:
                damage = 0

            opponent.health -= damage

            # Apply shield
            if ab.shild != 1:
                self.shild = ab.shild

            # Update ability points
            self.ability_points -= ab.drain
            if ab.drain == 0:
                self.ability_points += ab.attack_power

            # Heal if applicable
            if ab.heal > 0:
                if self.health < self.max_health:
                    self.health += ab.heal
                    if self.health > self.max_health:
                        self.health = self.max_health
                else:
                    self.health = self.max_health

            # Display attack results
            if ab.attack_power != 0:
                print(f"{self.name} attacked {opponent.name} with {ab.name} {ab.attack_type} for {damage} damage {opponent.name}'s Remaining Health:{opponent.health}")

            if opponent.shild < 1:
                if get_abilitie(opponent.active_abilitie, opponent.abilites).effect == 0:
                    shld = "a Shild"
                else:
                    shld = get_abilitie(opponent.active_abilitie, opponent.abilites).effect
                print(f"{opponent.name} has {shld} activated taking {damage}/{ab.attack_power + self.attack_power} damage dealt by {self.name}")

            if ab.drain > 0:
                print(f"{self.name} used {ab.drain} abilitie points. Remaining Points:{self.ability_points}")
                if ab.effect != NULL:
                    print(f"{self.name} activated {ab.effect} {ab.effect_description}")

            if ab.heal != 0:
                print(f"{self.name} has healed by {ab.heal} points new current health:{self.health} ")

        else:
            print(f"{self.name} does not have enough abilitie points to use {ab.name} Current points:{self.ability_points} Required:{ab.drain}")

    # Display character stats
    def display_stats(self):
        ab = get_abilitie("attack", self.abilites)
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health},Attack Power:{self.attack_power} Ability Points: {self.ability_points}")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name, abilities, attack_power,health):
        attack = abilitie()
        attack.command = "Axe"
        attack.attack_power = 25
        attack.attack_type = "basic attack"
        attack.name = "Axe"
        abilities.append(attack)
        
        attack2 = abilitie()
        attack2.command = "Sword"
        attack2.attack_power = 30
        attack2.attack_type = "basic attack"
        attack2.name = "Sword"
        abilities.append(attack2)
        
        attack3 = abilitie()
        attack3.command = "Poisonus Slash"
        attack3.attack_power = 25
        attack3.attack_type = "basic attack"
        attack3.name = "Poisonus Slash"
        abilities.append(attack3)
        

        special_attack = abilitie()
        special_attack.heal = 10
        special_attack.attack_power = 60
        special_attack.name = "Slash of fire"
        special_attack.command = "Slash of fire"
        special_attack.attack_type = "special attack"
        special_attack.drain = 65;
        abilities.append(special_attack)
        
        super().__init__(name, health=health,abilities=abilities,attack_power=attack_power)

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name, abilities, attack_power,health):
        attack = abilitie()  
        attack.command = "Freeze Ball"
        attack.attack_type = "basic attack"
        attack.attack_power = 35
        attack.heal = 5
        attack.name = "Freeze Ball"
        abilities.append(attack)
        
        attack2 = abilitie()
        attack2.command = "Fire Ball"
        attack2.attack_type = "basic attack"
        attack2.attack_power = 10
        attack2.heal = 10
        attack2.name = "Fire Ball"
        abilities.append(attack2)
        
        attack3 = abilitie()
        attack3.name = "Sword"
        attack3.attack_power = 15
        attack3.command = "Sword"
        attack3.attack_type = "basic attack"
        attack3.heal = 10
        abilities.append(attack3)
        
        special_attack = abilitie()
        special_attack.command = "Hurrican"
        special_attack.heal = 10
        special_attack.name = "Hurrican"
        special_attack.attack_type = "special attack"
        special_attack.attack_power = 50
        special_attack.drain = 50
        abilities.append(special_attack)
        
        
        super().__init__(name, health=health, abilities=abilities,attack_power=attack_power)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name, abilities,attack_power,health):
        attack1 = abilitie()
        attack1.command = "Magic"
        attack1.attack_type = "basic attack"
        attack1.attack_power = 15
        attack1.heal = 10  
        attack1.name = "Magic"
        abilities.append(attack1)
        
        attack2 = abilitie()
        attack2.command = "Spell"
        attack2.attack_type = "basic attack"
        attack2.attack_power = 10
        attack2.heal = 10
        attack2.name = "Spell"
        abilities.append(attack2)
        
        attack3 = abilitie()
        attack3.name = "Sword"
        attack3.attack_power = 15
        attack3.command = "Sword"
        attack3.attack_type = "basic attack"
        attack3.heal = 10
        abilities.append(attack3)
        
        special_attack = abilitie()
        special_attack.heal = 10
        special_attack.attack_power = 5
        special_attack.name = "Summon Minions"
        special_attack.command = "Summon Minions"
        special_attack.max_summon = 6
        special_attack.attack_type = "special attack"
        special_attack.drain = 65;
        abilities.append(special_attack)
        
        special_attack2 = abilitie()
        special_attack2.command = "Lightning Storm"
        special_attack2.heal = 10
        special_attack2.name = "Lightning Storm"
        special_attack2.attack_type = "special attack"
        special_attack2.attack_power = 35
        special_attack2.drain = 50
        abilities.append(special_attack2)
        
        super().__init__(name, health=health, abilities=abilities,attack_power=attack_power)


# Create Archer class
class Archer(Character):
    
    def __init__(self, name, abilities,attack_power,health):
        attack = abilitie()
        attack.name = "Arrows"
        attack.command = "Arrows"
        attack.attack_type = "basic attack"
        attack.attack_power = 15
        abilities.append(attack)
       
        special_attack1 = abilitie()   
        special_attack1.attack_type = "special attack"
        special_attack1.command = "Quick Shot"
        special_attack1.drain = 40
        special_attack1.effect = "Evade"
        special_attack1.effect_description = "This Effect when activated shilds the player from from at least 1 attack on the next attack"
        special_attack1.attack_power = 30
        special_attack1.name = "Quick Shot"
        abilities.append(special_attack1)
        
        speical_attack2 = abilitie() 
        speical_attack2.command = "Summon Minions"
        speical_attack2.attack_power = 10
        speical_attack2.attack_type = "special attack"
        speical_attack2.max_summon = 5
        speical_attack2.drain = 65
        speical_attack2.effect = "Summon Minions"
        speical_attack2.name = "Summon Minions"
        abilities.append(speical_attack2)

       
        super().__init__(name, health = health,abilities=abilities,attack_power=attack_power)
        
# Create Paladin class 

class Paladin(Character):
    
    def __init__(self, name, abilities,attack_power,health):
        attack = abilitie()
        attack.name = "Sword"
        attack.command = "Sword"
        attack.attack_type = "basic attack"
        attack.attack_power = 20
        abilities.append(attack)
       
        special_attack1 = abilitie()   
        special_attack1.attack_type = "special attack"
        special_attack1.command = "Shild"
        special_attack1.drain = 40
        special_attack1.effect = "Devine Shild"
        special_attack1.attack_power = 15
        special_attack1.effect_description = f"This Effect when activated deals {special_attack1.attack_power} damage and shilds the player from any damage until the shild is destroyed"
        special_attack1.name = "Devine Shild"
        special_attack1.shild = 0
        abilities.append(special_attack1)
        
        speical_attack2 = abilitie() 
        speical_attack2.command = "Mercy Heal"
        speical_attack2.attack_type = "special attack"
        speical_attack2.drain = 65
        speical_attack2.effect = "Mercy Healing"
        speical_attack2.name = "Mercy Heal"
        speical_attack2.heal = health/2
        abilities.append(speical_attack2)

        super().__init__(name, health = health,abilities=abilities,attack_power=attack_power)

# Function to create a character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name, [], 10, 100)
    elif class_choice == '2':
        return Mage(name, [], 15, 100)
    elif class_choice == '3':
        return Archer(name, [], 10, 100)
    elif class_choice == '4':
        return Paladin(name, [], 10, 100)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name, [], 10, 100)

# Core game loop to run the battle between player and wizard
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")

        # Display abilities
        for i in range(len(player.abilites)):
            print(f"[{i}] {player.abilites[i].name} - {player.abilites[i].attack_type}")

        print(f"[{len(player.abilites)}] View Stats")
        choice = input("Choose an action: ")

        # Perform player action
        if int(choice) == len(player.abilites):
            player.display_stats()
        elif int(choice) < len(player.abilites):
            player.attack(wizard, player.abilites[int(choice)].command)
        else:
            print("Invalid choice. you lost your turn")

        # Wizard attacks if still alive
        if wizard.health > 0:
            rand_attack = random.randint(0, len(wizard.abilites) - 1)
            if wizard.abilites[rand_attack].drain <= wizard.ability_points:
                wizard.attack(player, wizard.abilites[rand_attack].command)
            else:
                while wizard.abilites[rand_attack].drain > wizard.ability_points:
                    rand_attack = random.randint(0, len(wizard.abilites) - 1)
                    wizard.attack(player, wizard.abilites[rand_attack].command)

        # Check for defeat conditions
        if player.health <= 0:
            print(f"Game Over {player.name} has been defeated by the {wizard.name}!")
            break
        if wizard.health <= 0:
            print(f"Congradulations you win {wizard.name} has been defeated by {player.name}!")

# Entry point of the game
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard", [], 15, 100)
    battle(player, wizard)

# Run game if file is executed directly
if __name__ == "__main__":
    main()

