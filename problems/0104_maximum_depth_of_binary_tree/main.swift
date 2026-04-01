
 //Definition for a binary tree node.
public class TreeNode {
     public var val: Int
     public var left: TreeNode?
     public var right: TreeNode?
     public init() { self.val = 0; self.left = nil; self.right = nil; }
     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
         self.val = val
         self.left = left
         self.right = right
     }
}

class Solution {
    func maxDepth(_ root: TreeNode?) -> Int {
        //Implement Depth Fist Search (DFS) Time: O(n)
        //base case
        guard let root = root else {return 0}

        //return max between left subtree and right subtree
        return 1 + max(maxDepth(root.left),maxDepth(root.right))
    }
}


let s = Solution()
//building tree
let root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right?.left = TreeNode(15)
root.right?.right = TreeNode(7)

print(s.maxDepth(root))