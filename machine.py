import Hub
import product


class machine:
    def __init__(self, mashine_id: int, name: str, funktion: str, status: str = "offline"):
        self.mashine_id = mashine_id
        self.name = name
        self.funktion = funktion
        self.status = None
        self.set_status(status)
        self.queue = []

    def set_status(self, status: str):
        if status not in ["offline", "online"]:
            raise ValueError("Status must be 'offline' or 'online'.")
        self.status = status

    def execute_function(self, prod: product.product, needed_items: list, hub: Hub) -> None:
        while prod.get_current_step().workstation == self:
            self.set_status("online")
            self.queue.remove(product)
            prod.production_steps += 1
            print(f"Maschine {self.mashine_id} ({self.name}) is performing step for product '{prod.name}'.")

        print(f"Maschine {self.mashine_id} ({self.name}) has completed all steps for product '{prod.name}'.")
        self.set_status("offline")
        if hub.machines.__contains__(prod.current_productionstep.workstation):
            hub.produced_product(prod)
        else:
            # Here we ould deliver our product to antoher hub to directly give it to the right
            hub.produced_product(prod)

    def get_info(self) -> str:
        return f"Maschine ID: {self.mashine_id}, Name: {self.name}, Funktion: {self.funktion}, Status: {self.status}"

    def add_to_queue(self, prod: 'product.product'):
        self.queue.append(prod)


def execute_function(prod, current_needed_components):
    return None
