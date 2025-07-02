from queue import queue
from machine import machine
from queue import Queue
from product import product

class Hub:
    # Public attributes
    id: str # Unique identifier for the hub
    connected_machines: list # List of machines connected to the hub 
    hubs: list # List of other hubs connected to this hub
    item_queue: queue # Queue for processing tasks
    product_queue: queue
    products_in_production: list # List of products currently in production
    tasklist: list # List of product to be produced


    def __init__(self, id: str, machines: list, hubs: list, queue: Queue, machines_producing: list, products_in_production: list):
        self.id = id
        self.machines = machines
        self.hubs = hubs
        self.queue = queue
        self.machines_producing = machines_producing
        self.products_in_production = products_in_production



# checks if machine is free is some product needs the free machine at the current moment and if there are enough items to produce the product at this machine
    def initiate_production(self) -> None:
        for machine in self.machines: # check if any machines in free or producing
            if machine.status == "offline": # check if machine is online
                for product in self.product_queue: # check if any products is in queue for this machine
                    if product.current_step == machine # check if machine can produce this product
                        for item in product.components_at_step.get(product.current_step): # check if machine has all items needed for this product
                                if item not in item_queue_current_steps[product.current_step]: # check if item is available in the queue
                                    break  # if an item for a product is not available, break the loop
                            
                        current_needed_items = product.item_queue_current_steps[product.current_step]
                        machine.start_production(product, current_needed_items)  # start production if all items are available                        
    
# checking if machines are producing
# checking current state of items and products
#check if product needs machines of other hubs

    def check_machines_needed_for_product(self, product: product) -> Hub:
        for product in self.product_queue:
            if (product.next_production == connected_machines): #check which machines are needed for the next prouction step
                return self;
            else : 
                for hub in self.hubs:
                    if (product.next_production == hub.connected_machines):
                        return hub
        