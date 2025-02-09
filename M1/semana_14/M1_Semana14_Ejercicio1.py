"""1. Cree una estructura de objetos que asemeje un Stack.
    1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
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


class Stack(LinkedList):

    def push(self, new_node):
        current_node = self.head
        self.head = new_node
        self.head.next = current_node

    def pop(self):
        self.head = self.head.next

cuarto  = Node("Test4")
tercero = Node("Test3", cuarto)
segundo = Node("Test2", tercero)
primero = Node("Test1", segundo)
stack_inst = Stack(primero)
new_node = Node("NEW!")
stack_inst.push(new_node)
new_node = Node("NEW2!")
stack_inst.push(new_node)
stack_inst.pop()
stack_inst.print_nodes()