from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        def parse_level(nodes):
            tmp = []
            for node in nodes:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            return tmp

        res = [[root.val]]
        # nodes 存储一层的节点
        nodes = [root]
        while True:
            # 传入当前层的节点，返回下一层所有的节点
            nodes = parse_level(nodes)
            if len(nodes) == 0:
                # 如果下一层没有节点，说明遍历完毕，返回结果
                break
            # 如果下一层有节点，则将下一层所有节点的值添加到一个新的列表，并添加到res中
            res.append([node.val for node in nodes])

        return res[::-1]

    
class Solution2:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        res = []
        nodes = deque([root])
        while nodes:
            tmp = []
            # 先记录nodes的长度，即为当前层所有节点的个数
            length = len(nodes)
            # 只遍历当前层的节点(在下面的操作中会将下一层的节点添加到队列中)
            for _ in range(length):
                node = nodes.popleft()
                tmp.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            res.append(tmp)

        return res[::-1]



if __name__ == '__main__':
    root2_1 = TreeNode(15, None, None)
    root2_2 = TreeNode(7, None, None)
    root1_1 = TreeNode(9, None, None)
    root1_2 = TreeNode(20, root2_1, root2_2)
    root = TreeNode(3, root1_1, root1_2)

    print(Solution2().levelOrderBottom(root))
