from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    """Morris 中序遍历"""

    def findMode(self, root: TreeNode) -> List[int]:

        def update(x, base, count, maxCount, res):
            """
            遍历每一个元素
                * 如果该元素和 base 相等
                    * count+=1
                * 如果该元素与 base 不相等
                    * 用该数字替换 base，并将 count 置为 1
                
                * 如果 count == MaxCount, 说明 base 为众数（之一），将其加入到res列表中
                * 如果 count > MaxCount, 则清空原 res 列表，将 base 添加到 res 中，并将当前 count 赋值给 MaxCount    
            """
            if x == base:
                count += 1 
            else:
                base = x 
                count = 1 

            if count == maxCount:
                res.append(base)
            
            if count > maxCount:
                res = [base]
                maxCount = count 

            return base, count, maxCount, res 

        if not root:
            return []
        
        base = root.val
        count, maxCount = 0, 0 
        res = []

        cur, pre = root, None 

        while cur:
            if not cur.left:
                # 如果没有左子树，就直接遍历这个点，然后跳到右子树
                base, count, maxCount, res  = update(cur.val, base, count, maxCount, res)
                cur = cur.right 
                continue
            
            # 如果当前节点有左子树，那么当前节点的前驱结点一定在左子树上，最有可能是整个左子树最右侧的点
            pre = cur.left 
            while pre.right and pre.right != cur:
                # 我们顺着当前节点的左子树，沿着右节点一路向下找
                pre = pre.right 

            if not pre.right:
                # 直到前驱结点不再有右子节点，我们将该节点的右节点指向当前节点，可保证遍历完左子树后能返回当前节点
                pre.right = cur 
                # 转移到左子树上继续判断（因为是中序遍历，所以需要先遍历左子树）
                cur = cur.left
            else:
                # 不满足上面的while循环，但是pre.right存在，说明pre.right已经指向当前节点(已经遍历过)
                pre.right = None 
                base, count, maxCount, res = update(cur.val, base, count, maxCount, res)
                cur = cur.right

        return res 


if __name__ == '__main__':
    node2_1 = TreeNode(-1, None, None)
    node2_2 = TreeNode(0, None, None)
    node2_3 = TreeNode(2, None, None)
    node1_1 = TreeNode(0, node2_1, node2_2)
    node1_2 = TreeNode(2, node2_3, None)
    root = TreeNode(1, node1_1, node1_2)

    print(Solution().findMode(root))

"""
      1
    /   \
   0     2
  / \    /
-1   0  2
"""

