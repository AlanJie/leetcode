from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    """
    DFS
    """
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        def construct_path(root, path):
            if root:
                path += str(root.val)

                if not root.left and not root.right:
                    # 如果是叶子节点，证明此路径已结束，将路径信息添加到结果中
                    paths.append(path)
                else:
                    path += '->'
                    # 将 path 继续传递下去
                    # 如果 left 或 right 有一个为空，则会直接跳过
                    construct_path(root.left, path)
                    construct_path(root.right, path)
            
        paths = []
        construct_path(root, '')

        return paths 


class Solution:
    """
    DFS
    """
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        if not root:
            return []

        paths = []
        node_deque = deque([root])
        path_deque = deque([str(root.val)])

        while node_deque:
            node = node_deque.popleft()
            path = path_deque.popleft()

            if not node.left and not node.right:
                paths.append(path)
            else:  
                # 这里使用 else 而不是 elif 单独判断左右是因为: 当此节点为叶子节点时，就不必再判断左右是否为空了
                # 或者可以在 if 中加入 continue，然后用 elif 单独判断左右是否为空
                if node.left:
                    node_deque.append(node.left)
                    path_deque.append(f'{path}->{node.left.val}')
                if node.right:
                    node_deque.append(node.right)
                    path_deque.append(f'{path}->{node.right.val}')

        return paths


if __name__ == '__main__':
    node3_1 = TreeNode(5, None, None)
    node2_1 = TreeNode(2, None, node3_1)
    node2_2 = TreeNode(3, None, None)
    node1 = TreeNode(1, node2_1, node2_2)

    print(Solution().binaryTreePaths(node1))
