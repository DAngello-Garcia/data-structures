# En las pilas o stacks los elementos se añaden o eliminan solo por un extremo (el superior) last-in first-out
# Push y pop son los métodos de añadir y eliminar

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data):
        self.stack.append(data)

    def show(self):
        return self.stack[-1]

    def remove(self):
        if len(self.stack) == 0:
            print("No elements in stack")
        else:
            self.stack.pop()

new_stack = Stack()
new_stack.add(2)
print(new_stack.show())
new_stack.add(4)
print(new_stack.show())