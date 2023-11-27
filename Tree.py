from linked_queue import LinkedQueue
class Tree:
    
    
    class Position:
        def element(self):
            raise NotImplementedError("must be implemented by subclass")
        
        
        def __eq__(self, other):
            raise NotImplementedError("must be implemented by subclass")
        
        
        def __ne__(self, other): 
            return not (self == other)
        
        
        
    def root(self):
        raise NotImplementedError("must be implemented by subclass")
    
    
    def parent(self):
        raise NotImplementedError("must be implemented by subclass")
    
    
    def num_children(self):
        raise NotImplementedError("must be implemented by subclass")
    
    
    def children(self):
        raise NotImplementedError("must be implemented by subclass")
    
    
    def __len__(self):
        raise NotImplementedError("must be implemented by subclass")
    
    
    def is_root(self,p):
        return self.root == p
    
    
    def is_leaf(self,p):
        return self.num_children(p) == 0
    
    
    def is_empty(self):
        return len(self) == 0
    
    def __iter__(self):
        """Generate an iteration of the tree's elements"""
        return self.preorder()
            
    def preorder(self):
        """Generate a preorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p
    
    def _subtree_preorder(self,p):
        """Generate a preorder iteration of positions in subtree rooted at p"""
        yield p # visit p before its subtrees
        for c in self.children(p):  # for each child in c
            for other in self._subtree_preorder(c): #do preorder of c's subtree
                yield other # yielding each to our caller
    
    def postorder(self):
        """Generate a postorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()): # start recursion
                yield p
                
    def _subtree_postorder(self,p):
        """Generate a postorder iteration of positions in subtree rooted at p"""
        for c in self.children(p): # for each child p
            for other in self._subtree_postorder(c): # do postorder of c's subtree
                yield other # yielding each to our caller
        yield p # visit p after its subtrees
        
    def breadthfirst(self):
        if not self.is_empty():
            fringe = LinkedQueue()  # known positions not yet yielded
            fringe.enqueue(self.root()) # starting with the root
            while not fringe.is_empty():
                p = fringe.dequeue() # remove from the front of the queue
                yield p # report this position
                for c in self.children(p):
                    fringe.enqueue(c) # add children to back of the queue
    
    