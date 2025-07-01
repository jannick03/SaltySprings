class steckbrief:
    counter = 1

    def __init__(self, items):
        self.id = steckbrief.counter
        steckbrief.counter += 1
        self.items = items

    def __str__(self):
        result = f"Steckbrief ID: {self.id}\n"
        result += "Erkannte Objekte:\n"
        for id, name in self.items:
            result += f"ID: {id}, Name: {name}\n"
        return result