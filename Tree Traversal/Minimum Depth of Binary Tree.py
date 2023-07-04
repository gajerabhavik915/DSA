# time complexity of algorithm is O(n) (in worst case)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        queue = []
        if root:
            queue.append(root)
            while queue:
                leng = len(queue)
                # res = []
                for i in range(leng):
                    node = queue.pop(0)
                    
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    if node.left is None and node.right is None:
                        print('a')
                        count += 1
                        return count
                count += 1

        return count
            
