class Stack:
    def __init__(self):
        self.data= []
    def push(self,value):
        self.data.append(value)
    def pop(self):
        last_value=self.data.pop()
        return last_value


class Queue:
    def __init__(self):
        self.data = []
    def push(self, value):
        self.data.append(value)
    def pop(self):
        self.data.pop(0)
