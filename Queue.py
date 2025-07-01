from box import box
from typing import List

class queue:
    def __init__(self, box: List[box]):
        self.boxes = box

    def enqueue(self, box: box):
        """Add an item to the end of the queue."""
        self.boxes.append(box)

    def dequeue(self, box: box) -> None:
        """Remove a specific item from the queue."""
        if not len(self.boxes) > 0:
            self.boxes.remove(box)
        raise ValueError("box not found in queue")
