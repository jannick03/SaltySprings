from box import box


class Queue:
    def __init__(self):
        self.items: list[box] = []
    
    def enqueue(self, item: box) -> None:
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self, component: box) -> None:
        """Remove a specific item from the queue."""
        if not len(self.items) > 0:
            self.items.remove(component)
        raise ValueError("Component not found in queue")
    
