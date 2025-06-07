🧙‍♂️ Defeat the Evil Wizard - Turn-Based Battle Game
Defeat the Evil Wizard is a text-based turn-based battle game written in Python. Choose your hero, master your abilities, and challenge a powerful dark wizard in a strategic combat system powered by custom character classes, randomized attacks, and magical effects.

🎮 Features
🧝 Choose from 4 unique hero classes: Warrior, Mage, Archer, or Paladin

🧙‍♂️ Fight against the Evil Wizard, who uses random abilities with powerful summons

⚔️ Turn-based combat system with attack, healing, shield, and summoning mechanics

🎯 Dynamic ability system with customizable effects and energy (ability points)

🧠 Strategic choices with limited ability points and effect-based shields

🧪 How to Play
Run the game with Python:

bash
Copy
Edit
python defeat_the_evil_wizard.py
Choose your hero class:

Warrior: Balanced melee fighter

Mage: Ranged magic user with healing

Archer: Agile shooter with evasion and summons

Paladin: Defensive powerhouse with divine healing

Pick abilities during your turn by entering the number shown.

Watch stats and outcomes printed to the console after each action.

Defeat the Evil Wizard before he defeats you!

🧩 Game Structure
Character: Base class for all playable and enemy characters

abilitie: Defines the structure of each skill (attack, heal, shield, summon)

Subclasses: Warrior, Mage, Archer, Paladin, and EvilWizard all inherit from Character and define custom ability sets

battle(): The game loop that handles turns, checks for victory or defeat, and handles inputs

create_character(): Lets the player choose a class and create a hero

🛠 Requirements
Python 3.x

No external libraries required (only built-in modules: random, math)
