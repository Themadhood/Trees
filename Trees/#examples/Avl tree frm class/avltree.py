
#8 left


class AVLTree:
    
    def __init__(self):
        self.root = None
    
    def lookup(self,value):
        if self.root == None:
            return False
        else:
            self.root.lookup(value)
    
    def add(self,value):
        if self.root is None:
            self.root = AVLTreeNode(None,value)
        else:
            self.root.add(value)
    
    def remove(self,value):
        if self.root != None:
            self.root.remove(value)
    
    def __len__(self):
        if self.root is None:
            return 0
        else:
            return self.root.size()
            
    def display(self):
        if self.root is None:
            print("[Empty tree]")
        else:
            self.root.display()
    
    def assert_valid(self):
        if self.root is not None:
            self.root.assert_avl()
            self.root.assert_tree()
            self.root.assert_sorted()

class AVLTreeNode:
    
    def __init__(self,parent,value):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
    
    def lookup(self,value):
        #If the value is present at this node return True.
        if self.value == value:
            return True
        
        #determine whether the value is in the left or right subtree.
        #If said subtree is absent,return False.        
        if value <= self.value and self.left != None:
            return self.left.lookup()
        elif value > self.value and self.right != None:
            return self.right.lookup()
        else:
            return False
    
    def root(self):
        try:
            self.parent.root()
        except:
            return self.value
    
    def add(self,value):
        if value < self.value:
            if self.left != None:
                self.left.add(value)
            else:
                self.left = AVLTreeNode(self,value)
        elif value > self.value:
            if self.right != None:
                self.right.add(value)
            else:
                self.right = AVLTreeNode(self,value)
                
#self.check_up()
    
    def rightmost_descendent(self):
        #Recursively find and return the rightmost descendent
        if self.right == None:
            return self
        else:
            return self.right.rightmost_descendent()
        
    
    def notify_parent(self,new):
        if self.parent.left is self:
            self.parent.left = new
        elif self.parent.right is self:
            self.parent.right = new

    
    def remove(self,value):
        if value < self.value:
            if self.left != None:
                self.left.remove(value)
            else:
                return self.root()
        elif value > self.value:
            if self.right != None:
                self.right.remove(value)
            else:
                return self.root()
        
        #remove is the current one, identify which of the 
        #three BST removal cases we’re in:
        #zero-child, one-child, or two-child.
        if self.value == value:
            child = 0
            L = R = False
            if self.left != None:
                child += 1
                L = True
            if self.right != None:
                child += 1
                R = True
            
            if child == 0:
                self.notify_parent(None)
            elif child == 1:
                if L == True:
                    moveChild = self.left
                elif R == True:
                    moveChild = self.right
                self.notify_parent(moveChild)
            elif child == 2:
                L_CH_RMost = self.left.rightmost_descendent()
                self.value = L_CH_RMost.value
                L_CH_RMost.value = value
                return self.left.remove(value)
            
#self.check_up()
    
    def height(self):
        #check sub tree heights
        if self.right == None:
            right = -1
        else:
            right = self.right.height()
            
        if self.left == None:
            left = -1
        else:
            left = self.left.height()

        #return biger hight pluss self
        if right > left:
            return right +1
        else:
            return left +1
        
    
    def balance_factor(self):
        #get hights
        if self.right != None and self.left != None:
            rightHeite = self.right.height()
            leftHeight = self.left.height()
            #Calculate the balance of this node
            #the height of right subtree minus the height of left subtree.
            balance = rightHeite - leftHeight
        else:
            balance = None
            
        return balance
    
    def rotate_right(self):
#if root change root
        #     A
        #   /   \
        #  B     C
        # / \   / \
        #D   E F   G

        #Perform a right rotation, wherein this node’s left child becomes
        #its parent,((B would take A’s place in the tree,with A becoming B’s
        #right child))and this node takes over that left child’s right subtree
        #as this node’s new left subtree.(( E becoming A’s left child.))
        self.notify_parent(self.left)
        #change parent right child
        left = self.left.right
        self.left.right = self
        #change self left child
        self.left = left
    
    def rotate_left(self):
#if root change root
        #     A
        #   /   \
        #  B     C
        # / \   / \
        #D   E F   G


        #Perform a left rotation, wherein this node’s right child becomes
        #its parent,((C would take A’s place in the tree,with A becoming C’s
        #right child))and this node takes over that right child’s left subtree
        #as this node’s new right subtree. ((F becoming A’s right child.))
        self.notify_parent(self.right)
        #change parent right child
        right = self.right.left
        self.right.left = self
        #change self left child
        self.right = right
    
    def check_up(self):
        balance = self.balance_factor()

        if balance >= 2: #right-heavy
            R_CH_Balance = self.right.balance_factor()
            if R_CH_Balance >= 0: #either balanced or rightskewed
                self.rotate_left()

            elif R_CH_Balance <= 1:#slightly left skewed
                self.right.rotate_right()
                self.rotate_left()
                
        if balance <= -2:#left-heavy
            L_CH_Balance = self.left.balance_factor()
            if L_CH_Balance >= 0: #either balanced or left skewed
                self.rotate_right()

            elif L_CH_Balance <= 1:#slightly right skewed
                self.left.rotate_left()
                self.rotate_right()

        try:
            self.parent.check_up()
        except:
            pass

    
    def display(self,prefix="X"):
        print(f"{prefix}: [{self.value}]")
        if self.left is None:
            print(f"{prefix}L: -")
        else:
            self.left.display(prefix+"L")
        if self.right is None:
            print(f"{prefix}R: -")
        else:
            self.right.display(prefix+"R")
    
    def __repr__(self):
        return f"[AVLTreeNode:{self.value}]"
    
    def assert_sorted(self):
        if self.left is not None:
            assert self.value > self.left.value, f"Binary search violation: {self} has a left child of {self.left}"
            self.left.assert_sorted()
        if self.right is not None:
            assert self.value < self.right.value, f"Binary search violation: {self} has a right child of {self.right}"
            self.right.assert_sorted()
    
    def assert_avl(self):
        assert -1 <= self.balance_factor() <= 1, f"AVL violation: {self} reports a balance factor of {self.balance_factor()}"
        if self.left is not None:
            self.left.assert_avl()
        if self.right is not None:
            self.right.assert_avl()
    
    def assert_tree(self):
        if self.left is not None:
            assert self.left.parent is self, f"Tree violation: {self}'s left child is {self.left} but {self.left}'s parent is {self.left.parent}" 
            self.left.assert_tree()
        if self.right is not None:
            assert self.right.parent is self, f"Tree violation: {self}'s right child is {self.right} but {self.right}'s parent is {self.right.parent}"
            self.right.assert_tree()
    
    def size(self):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size()
        right_size = 0
        if self.right is not None:
            right_size = self.right.size()
        return left_size+right_size+1

if __name__ == "__main__":
    
    # Note that this IS NOT how you will actually build your trees.
    # This testing_tree is constructed by hand so that you can test
    # simpler methods before fully implementing the add and remove
    # functions.
    
    testing_tree = AVLTree()
    a_node = AVLTreeNode(None,4)
    testing_tree.root = a_node
    
    b_node = AVLTreeNode(a_node,2)
    a_node.left = b_node
    
    c_node = AVLTreeNode(a_node,6)
    a_node.right = c_node
    
    d_node = AVLTreeNode(b_node,1)
    b_node.left = d_node
    
    e_node = AVLTreeNode(b_node,3)
    b_node.right = e_node
    
    f_node = AVLTreeNode(c_node,5)
    c_node.left = f_node
    
    g_node = AVLTreeNode(c_node,7)
    c_node.right = g_node
    
    testing_tree.display()
