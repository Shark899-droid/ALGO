from linked_binary_tree import LinkedBinaryTree

my_tree = LinkedBinaryTree()
my_tree._add_root(4)
first_left = my_tree._add_left(my_tree.root(),5)
first_right = my_tree._add_right(my_tree.root(),3)
my_tree._add_right(first_left,3)
my_tree._add_left(first_left,53)
my_tree._add_right(first_right,66)

def preorder_indent(T,p,d):
        """Print preorder representation of subtree of T rooted at p at depth d"""
        print(4*d*" " + str(p.element()))
        for c in T.children(p):
            preorder_indent(T,c,d+1)

preorder_indent(my_tree,my_tree.root(),2)