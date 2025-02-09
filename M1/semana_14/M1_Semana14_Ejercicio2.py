"""2. Cree una estructura de objetos que asemeje un Double Ended Queue.
    1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
    2. Debe incluir un método para hacer `print` de toda la estructura.
    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`."""


class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.next = next
        self.data = data


class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_nodes(self):
        node = self.head
        while node is not None:
            print(f'Data: {node.data}')
            node = node.next


class DoubleEndedQueue(LinkedList):

    def push_left(self, new_node):
        current_node = self.head
        self.head = new_node
        self.head.next = current_node

    def pop_left(self):
        self.head = self.head.next
    
    def push_right(self, new_node):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def pop_right(self):
        current_node = self.head
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None


cuarto  = Node("Test4")
tercero = Node("Test3", cuarto)
segundo = Node("Test2", tercero)
primero = Node("Test1", segundo)
linked_list = DoubleEndedQueue(primero)
new_node = Node("NEW_left!")
linked_list.push_left(new_node)
new_node = Node("NEW_left2!")
linked_list.push_left(new_node)
new_node = Node("NEW_right!")
linked_list.push_right(new_node)
new_node = Node("NEW_right2!")
linked_list.push_right(new_node)
linked_list.pop_left()
linked_list.pop_right()
linked_list.print_nodes()