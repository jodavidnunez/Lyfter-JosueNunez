"""Implemente un bubble_sort que funcione para @Linked Lists."""


class Node:
    def __init__(self, data):
        self.data = int(data)
        self.next = None

class Stack:

    def __init__(self, head=None):
        self.head = head
        self.count = 0

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

    def print_stack(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("-E-(pop): Pop from empty stack")
        data = self.head.data
        self.head = self.head.next
        self.count -= 1
        return data

    def size(self):
        return self.count

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            raise IndexError("-E-(peek): Peek from empty stack")
        return self.head.data

    def bubble_sort(self):
        if self.is_empty():
            return

        for _ in range(self.size()):
            already_sorted_flag = True
            tmp_stack = Stack()
            while not self.is_empty():
                tmp_data = self.pop()
                if not tmp_stack.is_empty(): 
                    current_head_data = tmp_stack.peek()
                    if int(current_head_data) > int(tmp_data):
                        tmp_stack.push(tmp_data)
                        tmp_data = tmp_stack.pop()
                        already_sorted_flag = False
                    #print(f'{current_head_data} vs {tmp_data}')
                tmp_stack.push(tmp_data)
            while not tmp_stack.is_empty():
                tmp = tmp_stack.pop()
                self.push(tmp)
            if already_sorted_flag is True:
                break    

# 1. Create stack
stack_inst = Stack()

# 2. Add elements to stack in wrong order
stack_inst.push(0)
stack_inst.push(-1)
stack_inst.push(1)
stack_inst.push(-2)
stack_inst.push(2)

# 3.stack_inst.print_nodes()
stack_inst.bubble_sort()
stack_inst.print_stack()