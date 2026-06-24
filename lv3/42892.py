def solution(nodeinfo):
    class Node:
        __slots__ = ("x", "y", "index", "left", "right")

        def __init__(self, x, y, index):
            self.x = x
            self.y = y
            self.index = index
            self.left = None
            self.right = None

    def build_tree(nodes):
        stack = []

        for node in nodes:
            left_child = None

            while stack and stack[-1].y < node.y:
                left_child = stack.pop()

            if stack:
                stack[-1].right = node
            if left_child:
                node.left = left_child

            stack.append(node)

        return stack[0]

    def preorder(root):
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.index)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def postorder(root):
        result = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if visited:
                result.append(node.index)
                continue

            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))

        return result

    nodes = [Node(x, y, i + 1) for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda n: n.x)
    root = build_tree(nodes)

    return [preorder(root), postorder(root)]
