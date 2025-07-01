class component:
    component_id = 1

    def __init__(self, name: str):
        self.name = name
        self.component_id = component.component_id
        component.component_id += 1

    def __str__(self):
        return self.name

