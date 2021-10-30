# En las colas o queues los elementos se eliminan al principio y se añaden al final first-in first-out
# Datos que se procesan por orden de llegada

from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def add(self, val):
        self.q.append(val)

    def remove(self):
        self.q.popleft()

    def show(self):
        print(f"{self.q}")

queue = Queue()
queue.add(1)
queue.add(3)
queue.add('Hola')
queue.add('Chao')
queue.remove()
queue.show()
