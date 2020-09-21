from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            nonlocal val
            if root:
                dfs(root.right)
                val += root.val 
                root.val = val 
                dfs(root.left)

        val = 0
        dfs(root)

        return root 


def printBST(root: TreeNode):
    if not root:
        return 

    res = []
    nodes = deque()
    nodes.append(root)

    while nodes:
        node = nodes.popleft()
        res.append(node.val)

        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

    print(res)


if __name__ == '__main__':
    node1_1 = TreeNode(2, None, None)
    node1_2 = TreeNode(13, None, None)
    root = TreeNode(5, node1_1, node1_2)

    root = Solution().convertBST(root)

    printBST(root)


