class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.height = 1

class Tree:
    def __init__(self):
        self.root = None
    
    # returns 0 if not a node
    def get_height(self, node):
        if node != None:
            return node.height
        return 0
    
    # returns 0 if not a node
    def get_balance(self, node):
        if node != None:
            return self.get_height(node.left) - self.get_height(node.right)
        return 0
    
    def rotate_left(self, x):
        y = x.right
        ß = y.left

        y.left = x
        x.right = ß

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    def rotate_right(self, y):
        x = y.left
        ß = x.right

        x.right = y
        y.left = ß

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return y

    # recursive, if reaches a point where there is no node, adds the new node there
    def insert(self, node, key, value):
        # base case
        if node == None:
            return Node(key, value)
        
        if key < node.key:
            node.left = self.insert(node.left, key, value)
        elif key > node.key:
            node.right = self.insert(node.right, key, value)
        else:
            node.value = value
            return node
        
        # balkance tree
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1:
            if key < node.left.key:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:
            if key > node.right.key:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

    def insert_node(self, key, value):
        self.root = self.insert(self.root, key, value)

    
    def min_value_node(self, node):
        current = node
        while current.left != None:
            current = current.left
        return current
    
    # recursively rebalances tree til reaches empty nodes  
    def delete(self, node, key):
        # base case
        if node == None:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            # if 1 child, make that new root, if 0 children, just delete it
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left

            # if 2 children, replaces with right node
            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self.delete(node.right, temp.key)

        # base case again
        if node == None:
            return node

        # balance tree
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1:
            if self.get_balance(node.left) >= 0:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:
            if self.get_balance(node.right) <= 0:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node
    
    def delete_node(self, key):
        self.root = self.delete(self.root, key)
    

    # returns None if key isnt in the tree
    def search(self, node, key):
        if node == None or node.key == key:
            return node

        if key < node.key:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def search_key(self, key):
        result = self.search(self.root, key)
        if result != None:
            return result.value
        return None
    

    def inorder_traversal(self, node, result):
        if node != None:
            self.inorder_traversal(node.left, result)
            result.append(node.key)
            self.inorder_traversal(node.right, result)

    def inorder(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result
    
    def preorder_traversal(self, node, result):
        if node != None:
            result.append(node.key)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

    def preorder(self):
        result = []
        self.preorder_traversal(self.root, result)
        return result
    
    def postorder_traversal(self, node, result):
        if node != None:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.key)

    def postorder(self):
        result = []
        self.postorder_traversal(self.root, result)
        return result
    
    def breadth_first_order(self):
        if not self.root:
            return []

        # https://www.w3schools.com/python/ref_list_pop.asp
        queue = [self.root]
        result = []

        while queue:
            current = queue.pop(0)
            result.append(current.key)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result
    
    def count_nodes(self, node):
        if node == None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    
    def size (self):
        return self.count_nodes(self.root)