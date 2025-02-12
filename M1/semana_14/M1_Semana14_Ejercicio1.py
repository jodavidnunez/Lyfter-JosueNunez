"""1. Cree una estructura de objetos que asemeje un Stack.
    1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
    2. Debe incluir un método para hacer `print` de toda la estructura.
    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`."""


class EmptyDataStructure(Exception):
    "Will raise an error if user tries to remove a node from an empty data structure"
    pass


class Node:
    data: str

    def __init__(self, data, next=None):
        self.next = next
        self.data = data


class Stack:
    
    head: Node
    
    def __init__(self, head):
        self.head = head

    def print_nodes(self):
        node = self.head
        #next_node_data = "<NEXT_NODE_DOES_NOT_EXIST>"
        while node is not None:
            if node.next is not None:
                next_node = node.next
                print(f'{node.data} => {next_node.data}')
            #else: 
            #    print(f'{node.data} => {next_node_data}')
            node = node.next


    def push(self, new_node):
        current_node = self.head
        self.head = new_node
        self.head.next = current_node

    def pop(self):
        try:
            if self.head.next is None:
                raise EmptyDataStructure
        except EmptyDataStructure:
            print(f'-E-: Stack is already empty.')
        else:
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
stack_inst.print_nodes()
stack_inst.pop()
stack_inst.pop()
stack_inst.pop()
stack_inst.pop()
stack_inst.pop()
print("\n------------\n")
stack_inst.print_nodes()
stack_inst.pop()