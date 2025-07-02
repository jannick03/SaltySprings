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
