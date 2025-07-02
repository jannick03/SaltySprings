import components
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import machine

class production_step:
    step_id = 1

    def __init__(self, name: str, description: str, workstation: 'machine.machine', needed_components: list['components.component']):
        self.name = name
        self.id = production_step.step_id
        production_step.step_id += 1
        self.description = description
        self.workstation = workstation
        self.needed_components = needed_components