# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        
        @lru_cache(None)
        def dfs(root, flag):
            """
            flag 代表3中状态:
                0: 要在当前节点安装监视器， 则其子节点会收到监视
                1: 当前节点没有被覆盖，我们可以在当前节点安装监视器，也可以在其子节点安装监视器
                2: 当前节点已经被覆盖，可以装监视器，也可以不装
            """
            if not root:
                # 如果 flag 为0，则当前节点已经决定要装监视器，则返回1，否则返回0
                return 1 if flag == 0 else 0

            left, right = root.left, root.right 

            # 这里的 f0 对应的是当前节点装监视器的情况, 即flag=0的情况
            # 当前节点要装监视器，故f0先加一，则其子节点已经被覆盖，为flag=2的情况
            f0 = 1 + dfs(left, 2) + dfs(right, 2)

            if flag == 0:  # 当前节点装监视器，那么它的子节点都将被覆盖
                return f0  
            if flag == 1:  # 当前节点没有被覆盖，可以自己装监视器，也可以让其子节点装监视器
                # 自己装监视器: f0
                # 子节点装监视器: min([dfs(left, 0) + dfs(right, 1), dfs(left, 1) + dfs(right, 0)])
                return min([dfs(left, 0) + dfs(right, 1), dfs(left, 1) + dfs(right, 0), f0])
            if flag == 2:  # 当前节点已经被覆盖（父节点有监视器），可以装监视器，如果当前不装，那么他的子节点都没有被覆盖
                # 自己装监视器: f0
                # 自己不装监视器，则其子节点没有被覆盖，属于flag=1的情况
                return min(dfs(left, 1) + dfs(right, 1), f0)

        # root属于flag=1的情况，即可以自己装，也可以让其子节点装
        return dfs(root, 1)
