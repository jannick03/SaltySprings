from typing import List

from components import component


class product:
    product_id = 1

    def __init__(self, name: str, steps: List[str], components: List['component']):
        self.name = name
        self.id = product.product_id
        product.product_id += 1
        self.production_steps = steps
        self.components = components
