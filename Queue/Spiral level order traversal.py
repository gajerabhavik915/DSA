
def findSpiral(root):
    if root is None:
        return []
    res = []
    Q1 = []
    # Q2 = []
    count = 1
    Q1.append(root)

    while Q1:
        len1 = len(Q1)
        Q2 = []
        for i in range(len1):
            node = Q1.pop(0)
            if node:
                Q2.append(node.data)
                Q1.append(node.left)
                Q1.append(node.right)

        if count % 2 != 0:
            Q2 = [i for i in Q2[::-1]]
        res.extend(Q2)
        count += 1

    return res
