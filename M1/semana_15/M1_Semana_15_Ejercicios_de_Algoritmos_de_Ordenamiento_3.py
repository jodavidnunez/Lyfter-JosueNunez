"""Implemente un bubble_sort que funcione para @Linked Lists."""


class Node:
    data: int
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head: Node
    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def my_bubble_sort(self):
        if not self.head:
            return
        outer_loop_node = self.head
        swapped = True
        while outer_loop_node is not None or swapped is True:
            swapped = False
            inner_loop_node = self.head
            while inner_loop_node.next is not None: 
                if inner_loop_node.data > inner_loop_node.next.data:
                    inner_loop_node.data, inner_loop_node.next.data = inner_loop_node.next.data, inner_loop_node.data
                    swapped = True
                inner_loop_node = inner_loop_node.next
            outer_loop_node = outer_loop_node.next


third_node = Node(-3)
second_node = Node(3, third_node)
first_node = Node(0, second_node)

linked_list = LinkedList(first_node)
linked_list.my_bubble_sort()
linked_list.print_structure()