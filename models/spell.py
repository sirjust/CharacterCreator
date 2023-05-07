class Spell:
    def __init__(self, name, apiReference):
        self.name = name
        self.apiReference = apiReference

    def __str__(self):
        return f"Spell(name='{self.name}'"