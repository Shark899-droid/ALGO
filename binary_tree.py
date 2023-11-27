from Tree import Tree
class BinaryTree(Tree):
    def left(self,p):
        raise NotImplementedError("must be implemented by subclass")
    
    
    def right(self,p):
        raise NotImplementedError("must be implemented by subclass")
    
    
    def sibling(self,p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p==self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
            
            
    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
            
    def inorder(self):
        """Generate an inorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    
    # override positions method from Tree class to make the inorder the default
    def positions(self):
        """Generate an iteration of the tree's positions"""
        return self.inorder()   # make inorder default
    
    def _subtree_inorder(self,p):
        """Generate an inorder iteration of positions in subtree rooted at p"""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other