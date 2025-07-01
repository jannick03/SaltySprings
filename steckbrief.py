class steckbrief:
    counter = 1

    def __init__(self, items):
        self.id = steckbrief.counter
        steckbrief.counter += 1
        self.items = items

    def __str__(self):
        result = f"Steckbrief ID: {self.id}\n"
        result += "Erkannte Objekte:\n"
        for class_id, name in self.items:
            result += f"ID: {class_id}, Name: {name}\n"
        return result
