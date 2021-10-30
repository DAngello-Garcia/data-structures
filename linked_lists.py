# Los elementos de una lista enlazada se almacenan en posiciones de memoria no contiguas
# Una lista enlazada se compone de nodos con campo información (valor) y campo enlace (puntero)
# El puntero apunta a la posición del siguiente elemento de la lista
# El último campo de la lista enlazada es un puntero nulo

# Python no cuenta con listas enlazadas en sus librerías estándar

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def insert_at_beggining(self, node):
        node.next = self.head
        self.head = node

    def insert_anywhere(self, before, node):
        if self.head is None:
            raise Exception("List is empty")

        for new in self:
            if new.data == before.data:
                node.next = new.next
                new.next = node
                return

        raise Exception(f"Node with data '{before.data}' not found")

    def insert_at_final(self, node):
        if self.head is None:   # Si no hay elementos en la lista, añade el nuevo nodo a ella
            self.head = node
            return

        for current_node in self:   # Recorre toda la lista hasta que llega al último nodo
            pass
        current_node.next = node

    def remove_node(self, node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == node.data:
            self.head = self.head.next
            return

        previous_node = self.head
        for i in self:
            if i.data == node.data:
                previous_node.next = node.next
                return
            previous_node = i

        raise Exception(f"Node with data '{node.data}' not found")

llist = LinkedList()
first_node = Node('nodo 1')
second_node = Node('nodo 2')
third_node = Node('nodo 3')
llist.head = first_node
first_node.next = second_node
second_node.next = third_node
print(llist)
new_node = Node('new')
llist.insert_at_beggining(new_node)
print(llist)
any_node = Node('any')
llist.insert_anywhere(second_node, any_node)
print(llist)
last_node = Node('last')
llist.insert_at_final(last_node)
print(llist)
llist.remove_node(first_node)
print(llist)
