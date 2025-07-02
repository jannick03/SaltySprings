from Hub import Hub
from product import product


class machine:
    def __init__(self, id: int, name: str, funktion: str, status: str = "offline", queue: list  = []):
        self.id = id
        self.name = name
        self.funktion = funktion
        self.status = None
        self.set_status(status)
        self.queue = queue # contains

    def set_status(self, status: str):
        if status not in ["offline", "online"]:
            raise ValueError("Status must be 'offline' or 'online'.")
        self.status = status

    def execute_function(self, product: product, needed_items: list, hub: Hub) -> None:
        while product.get_current_step().workstation == self:
            self.queue.remove(product) # remove from machine queue
            product.production_steps += 1
            print(f"Maschine {self.id} ({self.name}) is performing step for product '{product.name}'.")

        print(f"Maschine {self.id} ({self.name}) has completed all steps for product '{product.name}'.")

        if hub.machines.__contains__(product.current_productionstep.workstation):
            hub.produced_product(product);
        else:
            # Here we ould deliver our product to antoher hub to directly give it to the right
            hub.produced_product(product);

    def get_info(self) -> str:
        return f"Maschine ID: {self.id}, Name: {self.name}, Funktion: {self.funktion}, Status: {self.status}"

    def add_to_queue(self, product: 'product'):
        self.queue.append(product)
