from dataclasses import dataclass
from typing import List

@dataclass
class Proficiency:
    index: str
    name: str
    url: str

    def __str__(self):
        return self.name