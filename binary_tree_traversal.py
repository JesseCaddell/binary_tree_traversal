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
    return result

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
#basic tree
basic_root = TreeNode(1)
basic_root.left = TreeNode(2)
basic_root.right = TreeNode(3)

#large tree
larger_root = TreeNode(1)
larger_root.left = TreeNode(2)
larger_root.right = TreeNode(3)
larger_root.left.left = TreeNode(4)
larger_root.left.right = TreeNode(5)
larger_root.right.left = TreeNode(6)
larger_root.right.right = TreeNode(7)
larger_root.right.right.right = TreeNode(8)

#empty tree
edge_root = None

#one sided tree
one_sided_tree = TreeNode(1)
one_sided_tree.left = TreeNode(2)
one_sided_tree.left.left = TreeNode(3)
one_sided_tree.left.left.left = TreeNode(4)

#mixed data tree
mixed_data_tree = TreeNode(1)
mixed_data_tree.left = TreeNode("A")
mixed_data_tree.right = TreeNode("B")
mixed_data_tree.left.left = TreeNode(2)
mixed_data_tree.left.right = TreeNode("C")
mixed_data_tree.right.left = TreeNode(3)
mixed_data_tree.right.right = TreeNode(4)

#preorder
print("PREORDER TREES:")
print("Basic Tree: ", preorder(basic_root))
print("Larger Tree: ", preorder(larger_root))
print("Edge Case: ", preorder(edge_root))
print("One Sided Tree:", preorder(one_sided_tree))
print("Mixed Data Tree:", preorder(mixed_data_tree))

#inorder
print("\nINORDER TREES:")
print("Basic Tree: ", inorder(basic_root))
print("Larger Tree: ", inorder(larger_root))
print("Edge Case: ", inorder(edge_root))
print("One Sided Tree:", inorder(one_sided_tree))
print("Mixed Data Tree:", inorder(mixed_data_tree))


#postorder
print("\nPOSTORDER TREES:")
print("Basic Tree: ", postorder(basic_root))
print("Larger Tree: ", postorder(larger_root))
print("Edge Case: ", postorder(edge_root))
print("One Sided Tree:", postorder(one_sided_tree))
print("Mixed Data Tree:", postorder(mixed_data_tree))
