class Stack:
    def __init__(self, items=[], limit=100):
        # Initialize the stack with an optional list of items and a limit
        self.items = items
        self.limit = limit

    def isEmpty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top of the stack if not full
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
             return None 

    def pop(self):
        # Remove and return the top item from the stack if not empty
        if not self.isEmpty():
            return self.items.pop()
        else:
             return None 

    def peek(self):
        # Return the top item from the stack without removing it
        if not self.isEmpty():
            return self.items[-1]
        else:
             return None 

    def size(self):
        # Return the current size of the stack
        return len(self.items)

    def full(self):
        # Check if the stack is full
        return len(self.items) == self.limit

    def search(self, target):
        # Search for an item in the stack and return its position (1-based index) or -1 if not found
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - 1 -i
        return -1