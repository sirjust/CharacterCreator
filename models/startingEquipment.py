from dataclasses import dataclass
from models.equipment import Equipment

@dataclass
class StartingEquipment:
    equipment: Equipment
    quantity: int