
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

# method 2

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None or root.right is None:
            return False

        Q1 = [root.left]
        Q2 = [root.right]

        # if root.left.val != root.right.val:
        #     return False

        while Q1 and Q2:
            node_left = Q1.pop(0)
            node_right = Q2.pop(0)
            if node_left and node_right:
                print(node_left.left)
                print(node_right.right)

                if node_left.left is None and node_right.right is None:
                    continue
                if node_left.right is None and node_right.left is None:
                    continue

                if (node_left.left and node_right.right):
                    if node_left.left.val == node_right.right.val:
                        print(node_left.left.val)
                        print(node_right.right.val)
                        Q1.append(node_left.left)
                        Q2.append(node_right.right)
                if (node_left.right and node_right.left):
                    if node_left.right.val == node_right.left.val:
                        print(node_left.right.val)
                        print(node_right.left.val)
                        Q1.append(node_left.right)
                        Q2.append(node_right.left)

                else:
                    return False

        return True













