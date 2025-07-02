from product import product

class machine:
    def __init__(self, id: int, name: str, funktion: str, status: str = "offline"):
        self.id = id
        self.name = name
        self.funktion = funktion
        self.status = None
        self.set_status(status)

    def set_status(self, status: str):
        if status not in ["offline", "online"]:
            raise ValueError("Status must be 'offline' or 'online'.")
        self.status = status

    def execute_function(self, product: 'product'):
        if product.production_steps:
            current_step = product.production_steps.pop(0)  # Remove the first step
            return f"Maschine {self.id} ({self.name}) is performing step '{current_step}' for product '{product.name}'."
        else:
            return f"Maschine {self.id} ({self.name}) has completed all steps for product '{product.name}'."
        # kommentar

    def get_info(self) -> str:
        return f"Maschine ID: {self.id}, Name: {self.name}, Funktion: {self.funktion}, Status: {self.status}"