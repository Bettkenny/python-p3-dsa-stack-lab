class Stack:

    def __init__(self, items = [], limit = 100):
        self.items= items if items is not None else []
        self.limit = limit
        pass

    def isEmpty(self):
        return len(self.items)==0
        pass

    def push(self, item):
         if not self.is_full():
            self.items.append(item)
         else:
            raise ValueError("Stack is full. Cannot push more items.")
        

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return IndexError("pop from empty stack")
        pass

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return IndexError("peek from an empty stack")
        pass
    
    def size(self):
        return len(self.items)
        pass

    def full(self):
        return len(self.items) == self.limit
        pass

    def search(self, target):
        try:
            index= self.items.index(target)
            return len(self.items)-index
        except ValueError:
            return -1

        pass
