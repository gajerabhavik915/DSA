
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# method-1 : by returning length of result list


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        que = collections.deque()
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
        print(len(result))
        return result

# method-2 : setting count from initial

class Solution1:
    def levelOrder(self, root: Optional[TreeNode]) -> int:
        result = []
        que = collections.deque()
        que.append(root)
        count = 0

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
                count += 1
        # print(len(result))
        return count
