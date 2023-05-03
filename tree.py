from node import Node


class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """ function for deleting tree """
        self.root = None

    def printTree(self):
        """ function for printing tree """
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """ function for inorder printing of tree """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, root):
        """ function for preorder printing of tree """
        
        if root is not None:
    
            # First print the data of node
            print(str(root.data) + ' ')
    
            # Then recur on left child
            self._printPreorderTree(root.left)
    
            # Finally recur on right child
            self._printPreorderTree(root.right)

    def _printPostorderTree(self, root):
        """ function for postorder printing of tree """
        if root is not None:
    
            # First recur on left child
            self._printPostorderTree(root.left)
    
            # the recur on right child
            self._printPostorderTree(root.right)
    
            # now print the data of node
            print(str(root.data) + ' ')


