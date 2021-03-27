class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Function to calculate the difference between the sum of all nodes present
# at odd levels and the sum of all nodes present at even level
def findDiff(root, diff=0, level=1):
    # base case
    if root is None:
        return diff

    # if the current level is odd
    if level % 2 == 1:
        diff = diff + root.data

    # if the current level is even
    else:
        diff = diff - root.data

    # recur for the left and right subtree
    diff = findDiff(root.left, diff, level + 1)
    diff = findDiff(root.right, diff, level + 1)

    return diff


if __name__ == '__main__':
    ''' Construct the following tree
              15
            /     \
           /       \
          10        20
         /  \      /  \
        /    \    /    \
       8     12  16    25
             
    '''

    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.right.left = Node(16)
    root.right.right = Node(25)
    root.right.left.left = Node(12)
    root.right.left.right = Node(25)

    print(findDiff(root))

























