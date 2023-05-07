from dataclasses import dataclass
from typing import List

@dataclass
class StartingEquipmentOption:
    option_type: str
    items: List[dict]