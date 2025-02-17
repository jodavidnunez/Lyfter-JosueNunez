"""2. Cree una estructura de objetos que asemeje un Double Ended Queue.
    1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
    2. Debe incluir un método para hacer `print` de toda la estructura.
    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`."""


class Node:

    data: str

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleEndedQueue:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def print_nodes(self):
        node = self.head
        next_node_data = "None"
        while node is not None:
            if node.next is not None:
                next_node = node.next
                print(f'{node.data} => {next_node.data}')
            else: 
                print(f'{node.data} => {next_node_data}')
            node = node.next
        if self.head is None:
            print(f'-E-: DoubleEndedQueue is currently empty.')

    def push_left(self, new_node):
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, new_node):
        if self.head is None:
            self.head = self.tail = new_node
        else: 
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            self.tail = None
            print(f'-E-(pop_left): DoubleEndedQueue is already empty.')
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def pop_right(self):
        if self.tail is None:
            self.head = None
            print(f'-E-(pop_right): DoubleEndedQueue is already empty.')
        elif self.tail.prev is None:
            self.tail = None
        else:
            self.tail = self.tail.prev  
            self.tail.next = None


# 1. Define nodes
node_minus_two = Node("-2")
node_minus_one = Node("-1")
node_zero = Node("0")
node_one = Node("1")
node_two = Node("2")

# 2. Connect nodes
"""
node_minus_two.next = node_minus_one
node_minus_one.prev = node_minus_two
node_minus_one.next = node_zero
node_zero.prev = node_minus_one
node_zero.next = node_one
node_one.prev = node_zero
node_one.next = node_two
node_two.prev = node_one
"""

# 3. Create double ended queue
double_ended_queue_inst = DoubleEndedQueue()

# 4. Testing print of empty double ended queue
print("\n--------PRINT #1: Testing print of empty double ended queue---------------\n")
double_ended_queue_inst.print_nodes()

# 5. Add head node and print
double_ended_queue_inst.push_right(node_zero)
print("\n--------PRINT #2: Add head node and print--------------\n")
double_ended_queue_inst.print_nodes()

# 6. Test push right and print
print("\n--------PRINT #3: Test push right and print--------------\n")
double_ended_queue_inst.push_right(node_one)
double_ended_queue_inst.push_right(node_two)
double_ended_queue_inst.print_nodes()

#7. Test push left and print
print("\n--------PRINT #4: Test push left and print--------------\n")
double_ended_queue_inst.push_left(node_minus_one)
double_ended_queue_inst.push_left(node_minus_two)
double_ended_queue_inst.print_nodes()

#8. Test one pop left and print
print("\n--------PRINT #5: Test one pop left and print--------------\n")
double_ended_queue_inst.pop_left()
double_ended_queue_inst.print_nodes()

#9. Test one pop right and print
print("\n--------PRINT #6: Test one pop right and print--------------\n")
double_ended_queue_inst.pop_right()
double_ended_queue_inst.print_nodes()

# 10. Test empty the whole DoubleEndedQueue with pop left
print("\n--------PRINT #7:Test empty the whole DoubleEndedQueue with pop left --------------\n")
double_ended_queue_inst.pop_left()
double_ended_queue_inst.pop_left()
double_ended_queue_inst.pop_left()
double_ended_queue_inst.print_nodes()
double_ended_queue_inst.pop_left()

# 10. Reset the data structure and test empty the whole DoubleEndedQueue with pop right
print("\n--------PRINT #8:  Reset the data structure and test empty the whole DoubleEndedQueue with pop right --------------\n")
double_ended_queue_inst.push_left(node_zero)
double_ended_queue_inst.push_right(node_one)
double_ended_queue_inst.push_right(node_two)
double_ended_queue_inst.push_left(node_minus_one)
double_ended_queue_inst.push_left(node_minus_two)
print("\n--------Initial Double Ended Queue--------------\n")
double_ended_queue_inst.print_nodes()
double_ended_queue_inst.pop_right()
double_ended_queue_inst.pop_right()
double_ended_queue_inst.pop_right()
double_ended_queue_inst.pop_right()
double_ended_queue_inst.pop_right()
double_ended_queue_inst.pop_right()
print("\n--------Final Double Ended Queue--------------\n")
double_ended_queue_inst.print_nodes()