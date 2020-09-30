# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    * 如果是空树，将要添加的点作为根节点返回
    * 如果树不为空，将pos设置为root
        * 如果 val < pos.val，则应添加到当前节点的左子树中
            * 如果 pos 没有左节点，那么将要添加的节点作为 pos 的左节点，然后直接返回
            * 如果 pos 有左节点，将 pos 更改为 pos的左节点，继续循环
        * 如果 val >= pos.val，则应添加到当前节点的右子树中
            * 如果 pos 没有右节点，那么将要添加的节点作为 pos 的右节点，然后直接返回
            * 如果 pos 有右节点，将 pos 更改为 pos的右节点，继续循环
    """
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        pos = root 
        while pos:
            if val < pos.val:
                if not pos.left:
                    pos.left = TreeNode(val)
                    break
                else:
                    pos = pos.left 
            else:
                if not pos.right:
                    pos.right = TreeNode(val)
                    break
                else:
                    pos = pos.right

        return root 
