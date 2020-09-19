from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        lefts = []

        if not root:
            return 0 

        nodes = deque()
        nodes.append(root)

        while nodes:
            node = nodes.popleft()

            if node.left:
                nodes.append(node.left)
                if not node.left.left and not node.left.right:
                    lefts.append(node.left.val)
            if node.right:
                nodes.append(node.right)

        return sum(lefts)


if __name__ == '__main__':
    # node2_1 = TreeNode(15, None, None)
    # node2_2 = TreeNode(7, None, None)
    # node1_1 = TreeNode(9, None, None)
    # node1_2 = TreeNode(20, node2_1, node2_2)
    # root = TreeNode(3, node1_1, node1_2)

    node2_1 = TreeNode(4, None, None)
    node2_2 = TreeNode(5, None, None)
    node1_1 = TreeNode(2, node2_1, node2_2)
    node1_2 = TreeNode(3, None, None)
    root = TreeNode(1, node1_1, node1_2)

    print(Solution().sumOfLeftLeaves(root))






