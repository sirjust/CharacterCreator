from dataclasses import dataclass
from typing import List
from models.option import Option

@dataclass
class ProficiencyChoiceOption:
    option_set_type: str
    options: List[Option]