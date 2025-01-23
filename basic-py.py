#Simple Syntax to print a message
print("Greetings, Codex!")

#Variables
mana = 100  # Stores an integer
spell_name = "Fireball"  # Stores a string
is_dark_magic = False  # Stores a boolean

#Printing Variables
print(mana)
print(spell_name)
print(is_dark_magic)

print("Mana:", (mana), "Spell Name:", (spell_name), "Is Dark Magic:", (is_dark_magic))

#Conditional Statements
if mana > 50:
    print("Cast Fireball!")
else:
    print("Not enough mana!")

#Loops
for i in range(3):  # Cast the spell 3 times
    print(f"Fireball {i+1}!")

#functions
def cast_spell(name, power):
    print(f"{name} deals {power} damage!")

cast_spell("Lightning Bolt", 75)
cast_spell("Fireball", 50)

#Importing Modules
import math

print(math.sqrt(16))  # Outputs 4, the square root of 16