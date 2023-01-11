import node

class AVL_Tree(object):
 
    def insert(self, root, newNode):
        if not root:
            return newNode
        elif newNode.first < root.first:
            root.left = self.insert(root.left, newNode)
        else:
            root.right = self.insert(root.right, newNode)
 
        root.height = 1 + max(self.getHeight(root.left),
                          self.getHeight(root.right))
 
        balance = self.getBalance(root)
 
        if balance > 1 and newNode.first < root.left.first:
            return self.rightRotate(root)
 
        if balance < -1 and newNode.first > root.right.first:
            return self.leftRotate(root)
 
        if balance > 1 and newNode.first > root.left.first:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and newNode.first < root.right.first:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root