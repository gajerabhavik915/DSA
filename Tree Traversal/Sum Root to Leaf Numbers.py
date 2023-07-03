class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(curr=None,path=''):
            nonlocal ans
            if curr:
                path += str(curr.val)
                dfs(curr.left,path)
                dfs(curr.right,path)
                if curr.left == None and curr.right == None:ans += int(path)
            return
        dfs(root)
        return ans
