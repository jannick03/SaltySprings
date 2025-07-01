class components:
    component_id = 1

    def __init__(self, name):
        self.name = name
        self.component_id = components.component_id
        components.component_id += 1

