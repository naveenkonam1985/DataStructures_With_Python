# Program for implementation of Binary Tree
# Naveen Kumar Konam

# class for node
class Node:
    """ Class for Node. Node consists of data value 
    and reference for left child and right child"""

    def __init__(self, data=None):
        self.data = data
        self.right_child = None
        self.left_child = None

    def __str__(self):
        return f'{self.data}'

class BinaryTree:
    """A binary tree is a collection of nodes, 
    where the nodes in the tree can have zero, one, or two child nodes."""
    
    def __init__(self):
        pass


    def inorder_traversal(self):
        pass


    def preorder_traversal(self):
        pass


    def postorder_traversal(self):
        pass

    


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.left_child = n2
    n1.right_child = n3

    print("Node left child:", n1.left_child)
    print("Node right child:",n1.right_child)



