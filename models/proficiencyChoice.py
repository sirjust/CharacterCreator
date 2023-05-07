import json
from dataclasses import dataclass
from typing import List

@dataclass
class ProficiencyChoice:
    desc: str
    choose: int
    type: str
    from_: dict