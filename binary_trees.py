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
    def insert_right(self, value):
        if self.right_node == None:
            self.right_node = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_node = self.right_node
            self.right_node = new_node
    def pre_order(self):
        print(self.value)
        if self.left_node:
            self.left_node.pre_order()
        if self.right_node:
            self.right_node.pre_order()
    def in_order(self):
        if self.left_node:
            self.left_node.in_order()
        print(self.value)
        if self.right_node:
            self.right_node.in_order()

    def post_order(self):
        if self.left_node:
            self.left_node.post_order()
        if self.right_node:
            self.right_node.post_order()
        print(self.value)

    def bfs(self):
        queue = []
        queue.append(self)
        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.value)
            if current_node.left_node:
                queue.append(current_node.left_node)
            if current_node.right_node:
                queue.append(current_node.right_node)


# tree traversal
# DFS(Depth-first search) --> one starts from root and explores as far as possible along each branch before backtracking
# BFS (Breadth-first search) --> one starts at the root and explores the neighbor nodes first, before moving to the next level neighbors
# breadth-first search we travel level by level
# pre-order traversal



tree = BinaryTree("1")
tree.insert_left("2")
tree.left_node.insert_left("3")
tree.left_node.insert_right("4")
tree.insert_right("5")
tree.right_node.insert_left("6")
tree.right_node.insert_right("7")

# tree.pre_order()
# print("In order")
# tree.in_order()
# print("Post order")
# tree.bfs()


#Binary search tree (orederd or sorted binary tree)



class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    
    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)
    def pre_order(self):
        print(self.value)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()
    def bfs(self):
        queue = []
        queue.append(self)
        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.value)
            if current_node.left_child:
                queue.append(current_node.left_child)   
            if current_node.right_child:
                queue.append(current_node.right_child)
    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)
        return value == self.value
    
insert_values = [76, 21, 4, 32, 100, 64, 52]
bst = BinarySearchTree(50)
for value in insert_values:
    bst.insert_node(value)

bst.bfs()
print(bst.find_node(101))
