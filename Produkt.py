class product:
    product_id = 1

    def __init__(self, name, steps, components):
        self.name = name
        self.id = product.product_id
        product.product_id += 1
        self.production_steps = steps
        self.components = components

