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




    def delete(self, root, nodeProperty):

        if not root:
            return root

        elif nodeProperty < root.first:
            root.left = self.delete(root.left, nodeProperty)

        elif nodeProperty > root.first:
            root.right = self.delete(root.right, nodeProperty)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.first = temp.first
            root.second = temp.second
            root.third = temp.third
            root.right = self.delete(root.right, temp.first)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root




    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        y.left = z
        z.right = T2
 
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
 
        return y
 



    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        y.right = z
        z.left = T3
 
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
 
        return y



    
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height



    
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)




    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)




    def searchNode(self, root, propertyValue):

        if root is None or root.first == propertyValue:
            return root

        if root.first < propertyValue:
            return self.searchNode(root.right, propertyValue)

        return self.searchNode(root.left, propertyValue)
    