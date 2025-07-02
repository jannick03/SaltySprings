from queue import Queue
from machine import machine
from product import product

class Hub:
    # Public attributes
    id: str # Unique identifier for the hub
    connected_machines: list # List of machines connected to the hub 
    hubs: list # List of other hubs connected to this hub
    item_queue: Queue # Queue for processing tasks
    product_queue: Queue
    products_in_production: list # List of products currently in production
    tasklist: list # List of product to be produced


    def __init__(self, id: str, machines: list, hubs: list, queue: Queue, machines_producing: list, products_in_production: list):
        self.id = id
        self.machines = machines
        self.hubs = hubs
        self.queue = queue
        self.machines_producing = machines_producing
        self.products_in_production = products_in_production

    def initiate_production(self) -> None:
        for machine in self.machines: # check if any machines in free or producing
            if machine.offline:
                for product in self.product_queue: # check if any products is in queue for this machine
                    if machine.can_produce(product): # check if machine can produce this product
                        for item in product.items:
                            pass #send items to machine machine
                        
# checking if machines are producing
# checking current state of items and products
#check if product needs machines of other hubs



    def check_machines_needed_for_product(self, product: product) -> Hub:
        for product in self.product_queue:
            if (product.next_production == self.connected_machines):#check which machines are needed for the next prouction step
                return self
            else : 
                for hub in self.hubs:
                    if (product.next_production == hub.connected_machines):
                        return hub
        