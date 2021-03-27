# Binary tree yüksekliğini hesaplayan bir algoritma yazınız. 
# Yükseklik veya derinlik, kök düğümden (root node) yaprak düğüme (leaf node) 
# giden en uzun yoldaki toplam düğüm(node) sayısıdır.
# (Program, en uzun yoldaki toplam düğüm sayısını dikkate almalıdır. Örneğin, 
# boş bir ağacın yüksekliği 0'dır ve yalnızca bir düğümü olan ağacın yüksekliği 1'dir.)
# Oluşturduğunuz programda aşağıdaki ağacı oluşturup yazdığınız algoritmayı test edin.
# Programınız sonuç olarak bu ağacın maximum yüksekliğini 3 olarak vermelidir.
# (İpucu: Recursive çözüm kullanabilirsiniz.)


#              15
#           /      \
#          /        \
#         10        20
#        /  \       / \
#       /    \     /   \
#      8     12   16   25



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def derinlik(root):
    if root is None:
        return 0
    else :
        left = derinlik(root.left)
        right = derinlik(root.right)
 
        if (left > right):
            return left+1
        else:
            return right+1
 
root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(15)
print (f"Maximum Derinlik: {derinlik(root)}")