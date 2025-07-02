from machine import machine
from components import components

class production_step:
    step_id = 1

    def __init__(self, name: str, description: str, workstation: machine, needed_components: list[components]):
        self.name = name
        self.id = production_step.step_id
        production_step.step_id += 1
        self.description = description
        self.workstation = workstation
        #vorschlag
        self.needed_components = needed_components # List of components needed for this step

