from dataclasses import dataclass

@dataclass
class Equipment:
    index: str
    name: str
    quantity: int
    url: str