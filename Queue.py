from components import component


class queue:
    def __init__(self):
        self.items = []

    def enqueue(self, comp: component):
        """Add an item to the end of the queue."""
        self.items.append(comp)

    def dequeue(self, comp: component) -> None:
        """Remove a specific item from the queue."""
        if not len(self.items) > 0:
            self.items.remove(comp)
        raise ValueError("Component not found in queue")
