from Maschine import Maschine

class production_step:
    step_id = 1

    def __init__(self, name: str, description: str, workstation: Maschine):
        self.name = name
        self.id = production_steps.step_id
        production_steps.step_id += 1
        self.description = description
        self.workstation = workstation

