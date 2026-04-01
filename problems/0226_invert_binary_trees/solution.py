# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: 
        #base of the pyramid
        if isinstance(root,int) or root is None:
            return root
        #recursively return treenode with left and right switched
        else:
            return TreeNode(root.val,self.invertTree(root.right),self.invertTree(root.left))

s = Solution()
#Define root
root = TreeNode(4,TreeNode(2,1,3),TreeNode(7,6,9))
print(s.invertTree(root))