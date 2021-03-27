class Node:


    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxDepth(node):
    if node is None:
        return 0;

    else:

        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1
root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)

print("Height of tree is %d" % (maxDepth(root)))