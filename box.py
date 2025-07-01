class box:
    counter = 1

    def __init__(self, items):
        self.id = box.counter
        box.counter += 1
        self.items = items

    def __str__(self):
        result = f"Box ID: {self.id}\n"
        result += "Erkannte Objekte:\n"
        for class_id, name in self.items:
            result += f"ID: {class_id}, Name: {name}\n"
        return result
