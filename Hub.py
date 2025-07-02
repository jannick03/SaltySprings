from queue import queue
from machine import machine
from queue import Queue
from product import product
from Hub import Hub
from productionstep import productionstep

class Hub:
    # Public attributes
    id: str # Unique identifier for the hub
    connected_machines: list # List of machines connected to the hub 
    hubs: list # List of other hubs connected to this hub
    component_queue: queue # Queue for processing tasks
    product_queue: queue
    products_in_production: list # List of products currently in production
    tasklist: list # List of product to be produced


    def __init__(self, id: str, machines: list, hubs: list, queue: Queue, machines_producing: list, products_in_production: list):
        self.id = id
        self.machines = machines
        self.hubs = hubs
        self.queue = queue
        # self.machines_producing = machines_producing
        self.products_in_production = products_in_production

    def delegate(self) -> None:
        self.initiate_production(self)
        
        # check if products needs to be produced at this hub or at another hub
        for product in self.product_queue: # check if any products is in queue
            nextHub = self.check_machines_needed_for_product(product)
            if self != nextHub:
                nextHub.receive(product)
                
        



# checks if machine is free is some product needs the free machine at the current moment and if there are enough items to produce the product at this machine
    def initiate_production(self) -> None:
        for machine in self.machines: # check if any machines in free or producing
            if machine.status == "offline": # check if machine is online
                for product in self.product_queue: # check if any products is in queue for this machine
                    if product.current_step.workstation == machine : # check if machine can produce this product
                        for item in product.components_at_step.get(product.current_step): # check if machine has all items needed for this product
                                if item not in item_queue_current_steps[product.current_step]: # check if item is available in the queue
                                    break  # if an item for a product is not available, break the loop
                            
                        current_needed_items = product.item_queue_current_steps[product.current_step]
                        machine.execute_funktion(product, current_needed_items)  # start production if all items are available                        
    
# checking if machines are producing
# checking current state of items and products
# check if product needs machines of other hubs

    # check if hub has needed machines
    def check_machines_needed_for_product(self, product: product) -> Hub:
        for product in self.product_queue:
            if (product.production_steps == connected_machines): #check which machines are needed for the next prouction step
                return self;
            else : 
                for hub in self.hubs:
                    if (product.next_production == hub.connected_machines):
                        return hub
    
    # checks which machines are producing (accessible form this(self) hub)
    def get_producing_machines(self) -> list:
        producing_machines = []
        for machine in self.machines:
            if machine.status == "online":
                producing_machines.append(machine)
        return producing_machines
    

    def get_production_step_of(product) -> productionstep: 
        return product.current_step;

    def needed_products_for_next_step(self, product: product) -> list:
        needed_products = []
        product
        for step in product.production_steps:nessecary_components_for_step
            if step == product.current_step:
                needed_products.append(step)
        return needed_products




       # possibility to add and remove tasks(Aufträge)  
    @property
    def tasklist(self):
        pass

    @tasklist.setter
    def tasklist(self, value):
        pass
