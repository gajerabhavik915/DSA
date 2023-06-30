
'''
Hint
-created two list, one for left and second for right side
-and fially match all element
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: [TreeNode]) -> bool:
        def left_res1():
            queue = []
            left_res = []
            queue.append(root)

            i = 1
            while queue:
                node = queue.pop(0)
                if node == 'null':
                    left_res.append('null')
                    continue

                if node:
                    left_res.append(node.val)
                    queue.append(node.left) if node.left else queue.append('null')
                    if i > 1 and node.right:
                        queue.append(node.right)
                    elif i > 1:
                        queue.append('null')
                    i = i + 1
            return (left_res)

        def right_res1():
            queue = []
            right_res = []
            queue.append(root)

            i = 1
            while queue:
                node = queue.pop(0)
                if node == 'null':
                    right_res.append('null')
                    continue

                if node:
                    right_res.append(node.val)
                    queue.append(node.right) if node.right else queue.append('null')

                    if i > 1 and node.left:
                        queue.append(node.left)
                    elif i > 1:
                        queue.append('null')

                    i = i + 1

            return (right_res)

        right = right_res1()
        left = left_res1()

        print(right)
        print(left)

        if right == left:
            return True
        else:
            return False



