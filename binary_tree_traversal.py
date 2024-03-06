## PART ONE ##

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    if not root:
        return []
    result = [root.value]
    result.extend(preorder(root.left))
    result.extend(preorder(root.right))
    return result

def inorder(root):
    if not root:
        return []
    result = []
    result.extend(inorder(root.left))
    result.append(root.value)
    result.extend(inorder(root.right))

def postorder(root):
    if not root:
        return []
    result = []
    result.extend(postorder(root.left))
    result.extend(postorder(root.right))
    result.append(root.value)
    return result

## PART TWO ##

#trees
basic_root = TreeNode(1)
basic_root.left = TreeNode(2)
basic_root.right = TreeNode(3)

larger_root = TreeNode(1)
larger_root.left = TreeNode(2)
larger_root.right = TreeNode(3)
larger_root.left.left = TreeNode(4)
larger_root.left.right = TreeNode(5)
larger_root.right.left = TreeNode(6)
larger_root.right.right = TreeNode(7)
larger_root.right.right.right = TreeNode(8)

edge_root = []

#preorder
print("Basic Tree: ", preorder(basic_root))
print("Larger Tree: ", preorder(larger_root))
print("Edge Case: ", preorder(edge_root))

#inorder
print("Basic Tree: ", inorder(basic_root))
print("Larger Tree: ", inorder(larger_root))
print("Edge Case: ", inorder(edge_root))

#postorder
print("Basic Tree: ", postorder(basic_root))
print("Larger Tree: ", postorder(larger_root))
print("Edge Case: ", postorder(edge_root))
