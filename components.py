class component:
    component_id = 1

    def __init__(self, class_id: int,  name: str):
        self.component_id = class_id
        self.name = name

    def __str__(self):
        return self.name

