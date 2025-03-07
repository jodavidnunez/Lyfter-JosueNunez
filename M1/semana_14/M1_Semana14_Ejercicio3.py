"""3. Cree una estructura de objetos que asemeje un Binary Tree.
    1. Debe incluir un método para hacer `print` de toda la estructura.
    2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`."""


class Node:
    data: str

    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


class Tree:
     
    def __init__(self, root):
        self.root = root

    def print_tree(self):
        if self.root is None:
            print(f'-E-(print_tree): BinaryTree is empty.')
        else:
            self._print_tree_recursive(self.root)

    def _print_tree_recursive(self, node, level=0):
        if node != None:
            self._print_tree_recursive(node.left, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.data))
            self._print_tree_recursive(node.right, level + 1)


b = Node("B")
c = Node("C")
a = Node("A", b, c)
d = Node("D")
e = Node("E")
b.left = d
b.right = e
f = Node("F")
g = Node("G")
c.left = f
c.right = g

tree = Tree(a)
tree.print_tree()

tree.root = None
tree.print_tree()