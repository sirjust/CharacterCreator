from models.spell import Spell
from models.equipment import Equipment
from models.savingThrow import SavingThrow
from models.proficiency import Proficiency
from models.stat import Stat
from typing import List

class Character:
    def __init__(self, name):
        self.name = name

class Character:
    def __init__(self, name, dndClass, race, stats, hitDie, hitPoints, proficiencies, savingThrows, equipment, level, subclass, spells, apiReference):
        self.name : str = name
        self.dndClass :str = dndClass
        self.race : str = race
        self.level : int = level
        self.stats : List[Stat] = stats
        self.hitDie : int = hitDie
        self.hitPoints : int = hitPoints
        self.proficiencies : List[Proficiency] = proficiencies
        self.savingThrows : List[SavingThrow] = savingThrows
        self.equipment : List[Equipment] = equipment
        self.subclass : str = subclass
        self.spells : List[Spell] = spells
        self.apiReference : str = apiReference

    def __str__(self):
        return f"Character(name='{self.name}'"

    def addEquipment(self, item : Equipment):
        self.equipment += item
    