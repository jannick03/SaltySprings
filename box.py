from typing import List

from components import component


class box:
    counter = 1

    def __init__(self, items: List['component']):
        self.id = box.counter
        box.counter += 1
        self.items = items

    def __str__(self):
        result = f"Box ID: {self.id}\n"
        result += "Erkannte Objekte:\n"
        for comp in self.items:
            result += f"ID: {comp.component_id}, Name: {comp.name}\n"
        return result
