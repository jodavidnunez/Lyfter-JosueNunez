"""2. Cree una estructura de objetos que asemeje un Double Ended Queue.
    1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
    2. Debe incluir un método para hacer `print` de toda la estructura.
    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`."""


class EmptyDataStructure(Exception):
    "Will raise an error if user tries to remove a node from an empty data structure"
    pass


class Node:

    data: str

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleEndedQueue:
    
    head: Node
    tail: Node

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def print_nodes(self):
        node = self.head
        while node is not None:
            if node.next is not None:
                next_node = node.next
                print(f'{node.data} => {next_node.data}')
            node = node.next

    def push_left(self, new_node):
        current_node = self.head
        self.head = new_node
        self.head.next = current_node

    def pop_left(self):
        try:
            if self.head.next is None:
                raise EmptyDataStructure
        except EmptyDataStructure:
            print(f'-E-(pop_left): DoubleEndedQueue needs at least two elements -head and tail-.')
        else:
            self.head = self.head.next
    
    def push_right(self, new_node):
        previous_tail = self.tail
        previous_tail.next = new_node
        new_node.prev = previous_tail
        self.tail = new_node

    def pop_right(self):
        try:
            if self.tail.prev is None:
                raise EmptyDataStructure
        except EmptyDataStructure:
            print(f'-E-(pop_right): DoubleEndedQueue needs at least two elements -head and tail-.')
        else:
            self.tail = self.tail.prev
            self.tail.next = None


cuarto  = Node("Test4")
tercero = Node("Test3", cuarto)
segundo = Node("Test2", tercero)
primero = Node("Test1", segundo)
segundo.prev = primero
tercero.prev = segundo
cuarto.prev = tercero

double_ended_queue_inst = DoubleEndedQueue(primero, cuarto)
new_node = Node("NEW_left!")
double_ended_queue_inst.push_left(new_node)
new_node = Node("NEW_left2!")
double_ended_queue_inst.push_left(new_node)
new_node = Node("NEW_right!")
double_ended_queue_inst.push_right(new_node)
new_node = Node("NEW_right2!")
double_ended_queue_inst.push_right(new_node)
double_ended_queue_inst.pop_left()
double_ended_queue_inst.pop_right()
double_ended_queue_inst.print_nodes()
double_ended_queue_inst.pop_right()
print("\n---------------------------\n")
double_ended_queue_inst.print_nodes()
double_ended_queue_inst.pop_right()
print("\n---------------------------\n")
double_ended_queue_inst.print_nodes()
double_ended_queue_inst.pop_right()
print("\n---------------------------\n")
double_ended_queue_inst.print_nodes()
double_ended_queue_inst.pop_right()
print("\n---------------------------\n")
double_ended_queue_inst.print_nodes()
double_ended_queue_inst.pop_right()
print("\n---------------------------\n")
double_ended_queue_inst.print_nodes()
double_ended_queue_inst.pop_right()