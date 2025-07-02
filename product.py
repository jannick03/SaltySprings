from typing import List

from components import component
from productionstep import production_step


class product:
    product_id = 1

    def __init__(self, name: str, steps: List['production_step'], components: List['component'], 
                 nessecary_components_for_step: List[List['component']]):
        self.name = name
        self.id = product.product_id
        product.product_id += 1
        self.production_steps = steps
        self.components = components
        self.current_step = 0
        self.nessecary_components_for_step = nessecary_components_for_step


    def next_production_step(self) -> 'production_step':
        """Returns the next production step."""
        if self.current_step is not None:
            current_index = self.production_steps.index(self.current_step)
            if current_index + 1 < len(self.production_steps):
                self.current_step += 1
                return self.production_steps[current_index + 1]
        return None
    
    def get_current_step(self) -> 'production_step':
        """Returns the current production step."""
        if self.current_step is not None:
            return self.production_steps[self.current_step]
        return None
