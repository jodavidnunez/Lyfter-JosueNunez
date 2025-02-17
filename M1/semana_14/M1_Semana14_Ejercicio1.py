"""1. Cree una estructura de objetos que asemeje un Stack.
    1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
    2. Debe incluir un método para hacer `print` de toda la estructura.
    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`."""


class Node:
    data: str

    def __init__(self, data, next=None):
        self.next = next
        self.data = data


class Stack:
    
    def __init__(self, head=None):
        self.head = head

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
            print(f'-E-(print_nodes): Stack is currently empty.')

    def push(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            print(f'-E-: Stack is already empty.')
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next


# 1. Define nodes
node_minus_two = Node("-2")
node_minus_one = Node("-1")
node_zero = Node("0")
node_one = Node("1")
node_two = Node("2")

# 2. Connect nodes
"""
node_minus_two.next = node_minus_one
node_minus_one.next = node_zero
node_zero.next = node_one
node_one.next = node_two
"""

# 3. Create stack
stack_inst = Stack()

# 4. Testing print of empty stack
print("\n--------PRINT #1: Testing print of empty stack---------------\n")
stack_inst.print_nodes()

# 5. Add head node and print
print("\n--------PRINT #2: Add head node and print--------------\n")
stack_inst.push(node_two)
stack_inst.print_nodes()

# 6. Add all the nodes and print
print("\n--------PRINT #3: Add all nodes and print--------------\n")
stack_inst.push(node_one)
stack_inst.push(node_zero)
stack_inst.push(node_minus_one)
stack_inst.push(node_minus_two)
stack_inst.print_nodes()

# 7. Do one pop and print
print("\n--------PRINT #4: Do one pop and print--------------\n")
stack_inst.pop()
stack_inst.print_nodes()

# 8. Empty the data structure by doing pops
print("\n--------PRINT #5: Empty the data structure by doing pop--------------\n")
stack_inst.pop()
stack_inst.pop()
stack_inst.pop()
stack_inst.pop()
stack_inst.pop()
stack_inst.print_nodes()
