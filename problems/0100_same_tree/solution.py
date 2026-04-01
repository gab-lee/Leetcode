# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Import deque for BFS
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Create queue for both trees
        pQueue = deque([p])
        qQueue = deque([q])
        while pQueue and qQueue:
            for i in range(len(pQueue)):
                pNode = pQueue.popleft()
                qNode = qQueue.popleft()
                #weed out None error
                if (pNode is None) != (qNode is None): 
                    return False
                elif pNode is None and qNode is None:
                    continue 
                #if any value is not the same return False
                if pNode.val != qNode.val:
                    return False
                #explore next level of Binary tree
                pQueue.append(pNode.left)
                qQueue.append(qNode.left)
                pQueue.append(pNode.right)
                qQueue.append(qNode.right)
        #Return True if loop is completed
        return True            
        
s = Solution()
#define root
p: TreeNode = TreeNode(1,TreeNode(2),TreeNode(3))
q: TreeNode = TreeNode(1,TreeNode(2),TreeNode(3))
print(s.isSameTree(p,q))
p: TreeNode = TreeNode(1,TreeNode(2))
q: TreeNode = TreeNode(1,None,TreeNode(3))
print(s.isSameTree(p,q))