from components import component


class Queue:
    def __init__(self):
        self.items: list[component.Component] = []
    
    def enqueue(self, item: component.Component):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self, component: component.Component) -> None:
        """Remove a specific item from the queue."""
        if not len(self.items) > 0:
            self.items.remove(component)
        raise ValueError("Component not found in queue")
    
