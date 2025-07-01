import Component


class Queue:
    def __init__(self):
        self.items: list[Component.Component] = []
    
    def enqueue(self, item: Component.Component):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self, component: Component.Component) -> None:
        """Remove a specific item from the queue."""
        if not len(self.items) > 0:
            self.items.remove(component)
        raise ValueError("Component not found in queue")
    
