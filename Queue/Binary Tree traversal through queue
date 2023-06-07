# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: [TreeNode]):
        result = []
        que = collections.deque()  # this is for creating queue
        que.append(root)

        while que:
            len_que = len(que)
            append_list = []
            for i in range(len_que):
                node = que.popleft()
                if node:
                    append_list.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if append_list:
                result.append(append_list)
        return result
