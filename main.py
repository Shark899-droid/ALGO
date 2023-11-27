from linked_binary_tree import LinkedBinaryTree

my_tree = LinkedBinaryTree()
my_tree._add_root(4)
first_left = my_tree._add_left(my_tree.root(),5)
first_right = my_tree._add_right(my_tree.root(),3)
my_tree._add_right(first_left,3)
my_tree._add_left(first_left,53)
my_tree._add_right(first_right,66)
my_tree.num_children(first_right)
for i in iter( my_tree):
    print(i.element())
print("Finish")
for b in my_tree.postorder():
    print(b.element())
print("Finish")
for c in my_tree.breadthfirst():
    print(c.element())