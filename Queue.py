from box import box


class Queue:
    def __init__(self):
        self.boxes: list[box] = []
    
    def enqueue(self, item: box) -> None:
        """Add an item to the end of the queue."""
        self.boxes.append(item)

    def dequeue(self, component: box) -> None:
        """Remove a specific item from the queue."""
        if not len(self.boxes) > 0:
            self.boxes.remove(component)
        raise ValueError("Component not found in queue")
    
