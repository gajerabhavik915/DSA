# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        temp = root
        res = []
        if root:
            def leftNode(temp):
                while temp:
                    stack.append(temp)
                    if temp.left:
                        temp = temp.left
                    else:
                        break
                # return temp.val
            
            leftNode(temp)

            while stack:    
                nod = (stack.pop())
                res.append(nod.val)
                if nod.right:
                    temp = nod.right
                    leftNode(temp)

        return res





            

