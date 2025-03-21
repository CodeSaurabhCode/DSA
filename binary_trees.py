class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right_node = None
        self.left_node = None
    def insert_left(self, value):
        if self.left_node == None:
            self.left_node = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_node = self.left_node
            self.left_node = new_node

tree = BinaryTree("Jitendra")
tree.insert_left("Vinayak")
tree.insert_left("Kumar")
print(tree.value)
print(tree.right_node)
print(tree.left_node.value)
print(tree.left_node.left_node.value)