from binary_tree_node import BinaryTreeNode


def is_symmetric(tree):
    def check_symmetric(left, right):
        if left is None and right is None:
            return True
        elif (left is None and right is not None) or (left is not None and right is None):
            return False
        
        return ((left.data == right.data) and
                (check_symmetric(left.left, right.right) and 
                    check_symmetric(left.right, right.left)))
    if tree is None:
        return True  
    return check_symmetric(tree.left, tree.right)


from sys import exit
from test_framework import generic_test, test_utils

if __name__ == '__main__':
    # The timeout is set to 30 seconds.
    # If your program ends with TIMEOUT error probably it stuck in an infinity loop,
    # You can extend the limit by changing the following line.
    timeout_seconds = 30

    exit(
        generic_test.generic_test_main(timeout_seconds,
                                       'is_tree_symmetric.tsv', is_symmetric))
