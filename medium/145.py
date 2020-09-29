from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        def traversal(root, res):
            if not root:
                return 

            traversal(root.left, res)
            traversal(root.right, res)
            res.append(root.val)

        res = []
        traversal(root, res)

        return res 


class Solution2:
    """
    后序遍历：左节点 -> 右节点 -> 当前节点
    使用 当前节点 -> 右节点 -> 左节点 的反序
    """
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        ans = []

        if not root:
            return ans

        stack = deque([root])

        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return ans[::-1]


if __name__ == '__main__':
    # node2_1 = TreeNode(3, None, None)
    # node1_1 = TreeNode(2, node2_1, None)
    # root = TreeNode(1, None, node1_1)
    node3_1 = TreeNode(4, None, None)
    node3_2 = TreeNode(5, None, None)
    node2_1 = TreeNode(2, node3_1, node3_2)
    node2_2 = TreeNode(3, None, None)
    root = TreeNode(1, node2_1, node2_2)

    res = Solution3().postorderTraversal(root)

    print(res)

"""
    1
    \
        2
    /
    3 
"""