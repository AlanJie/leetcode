from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
#       1
#     /   \
#    0     2
#   / \    /
# -1   0  2
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        def inorder(root: TreeNode, nodes: List):
            if not root:
                return 

            inorder(root.left, nodes)
            nodes.append(root.val)
            inorder(root.right, nodes)

        if not root:
            return 

        nodes = []
        inorder(root, nodes)

        return nodes


if __name__ == '__main__':
    node2_1 = TreeNode(-1, None, None)
    node2_2 = TreeNode(0, None, None)
    node2_3 = TreeNode(2, None, None)
    node1_1 = TreeNode(0, node2_1, node2_2)
    node1_2 = TreeNode(2, node2_3, None)
    root = TreeNode(1, node1_1, node1_2)

    print(Solution().findMode(root))

            


