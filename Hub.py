
from queue import Queue
from product import product
from productionstep import production_step
from machine import machine
from order import order

class Hub:
    # Public attributes
    id: str # Unique identifier for the hub
    connected_machines: list # List of machines connected to the hub 
    hubs: list # List of other hubs connected to this hub
    component_queue: list # Queue for processing tasks
    products_in_production: list # List of products currently in production
    product_list: list # list of products # eine liste an anstehenden Produkten, kann auch in Aufträgen wieter klassifiziert werden
    tasks: list(order) # List of product to be produced

    def __init__(self, id: str, machines: list, hubs: list, queue: Queue, machines_producing: list, products_in_production: list):
        self.id = id
        self.machines = machines
        self.hubs = hubs
        self.queue = queue
        # self.machines_producing = machines_producing
        self.products_in_production = products_in_production

    def loop(self) -> None:
        if self.tasklist:
            self.initiate_production(self)
            
            # check if products needs to be produced at this hub or at another hub
            for product in self.product_list: # check if any products is in queue
                nextHub = product.current_productionstep
                if self != nextHub:
                    nextHub.receive(product)
            else :
                print("all tasks done!")


# checks if machine is free is some product needs the free machine at the current moment and if there are enough items to produce the product at this machine
    def initiate_production(self) -> None:
        for free_machine in self.get_free_machines(self): # check if any machines in free or producing
                for product in self.product_list: # check if any products is in queue for this machine
                    if product.current_step.workstation == free_machine : # check if machine can produce this product
                        for item in product.needed_components.get(product.current_step): # check if machine has all items needed for this product
                                if item not in self.component_queue: # check if item is available in the queue
                                    break  # if an item for a product is not available, break the loop
                            
                        current_needed_components = product.needed_components.get(product.current_step)
                        machine.execute_function(product, current_needed_components)  # start production if all items are available
                        self.products_in_production.append(product)
                        self.remove_used_components(current_needed_components)

# checking if machines are producing
# checking current state of items and products
# check if product needs machines of other hubs

    # check if hub has needed machines
    def check_machines_needed_for_product(self, product: product) -> 'Hub':
        for product in self.products_in_production:
            if (product.production_steps == self.machines): #check which machines are needed for the next production step
                return self
            else :
                for hub in self.hubs:
                    if (product.production_steps == hub.machines):
                        return hub
        return self

    #
    #Machines
    #
    def get_free_machines(self) -> list:
        available_machines = []
        for machine in self.machines:
            if machine.status == "offline":
                available_machines.append(machine)
            else:
                continue
        return available_machines;

    def produced_product(self, product: product):
        self.products_in_production.remove(product)
        self.product_list.append(product)





    # # check if hub has needed machines
    # def check_machines_needed_for_product(self, product: product) -> Hub:
    #     for product in self.product_list:
    #         if (product.production_steps == connected_machines): #check which machines are needed for the next prouction step
    #             return self;
    #         else :
    #             for hub in self.hubs:
    #                 if (product.next_production == hub.connected_machines):
    #                     return hub

    # checks which machines are producing (accessible form this(self) hub)
    def get_producing_machines(self) -> list:
        producing_machines = []
        for machine in self.machines:
            if machine.status == "online":
                producing_machines.append(machine)
        return producing_machines
    
#
# Components
#
# adding new scanned components
    def add_scanned_components(self, new_components: list) -> None:
        for each_component in new_components:
            self.component_queue.append(each_component)

    def get_production_step_of(self, product) -> production_step:
        return product.current_step;

    def needed_products_for_next_step(self, product: product) -> list:
        needed_products = []
        # product  # This line seems incomplete, commenting out
        for step in product.production_steps:  # Fixed syntax error
            if step == product.current_step:
                needed_products.append(step)
        return needed_products

    def remove_used_components(self, used_items: list) -> None:
        for item in used_items:
            self.component_queue.remove(item)


# def get_production_step_of(product) -> productionstep:
#     return product.current_step;

# def needed_products_for_next_step(self, product: product) -> list:
#     needed_products = []
#     product
#     for step in product.production_steps:nessecary_components_for_step
#         if step == product.current_step:
#             needed_products.append(step)
#     return needed_products


    # possibility to add and remove tasks(Aufträge)  
    @property
    def tasklist(self):
        pass

    @tasklist.setter
    def tasklist(self, value):
        pass
