class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if self.size() == 0:
            return True
        return False


    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            return

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        pass

    def size(self):
        return len(self.items)

    def full(self):
        if self.size() == self.limit:
            return True
        return False

    def search(self, target):
        for val in self.items:
            if target == val:
                return (self.size() - 1) - self.items.index(target)
        return -1
