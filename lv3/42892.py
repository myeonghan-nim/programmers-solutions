def solution(nodeinfo):
    # x 오름차순으로 노드를 훑으며 스택으로 트리를 만든다(재귀 없이 한 번에 구성).
    # y가 클수록(위 레벨일수록) 부모이므로, 새 노드보다 y가 작은 스택 위 노드들은 새 노드의 왼쪽 자식으로, 새 노드는 남은 스택 꼭대기의 오른쪽 자식으로 붙는다.
    # 순회도 재귀 대신 스택을 써서 깊은 트리(깊이 1,000)에서도 안전하다.
    # 시간 복잡도: O(n log n) (정렬)
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

            # 새 노드보다 아래 레벨인 노드들은 새 노드의 왼쪽 서브 트리가 된다
            while stack and stack[-1].y < node.y:
                left_child = stack.pop()

            if stack:
                stack[-1].right = node  # 기존 오른쪽 자식은 위에서 새로 연결됨
            if left_child:
                node.left = left_child

            stack.append(node)

        return stack[0]  # 스택 맨 아래 = y가 가장 큰 루트

    def preorder(root):
        # 전위 순회(나 -> 왼쪽 -> 오른쪽): 오른쪽을 먼저 쌓아 왼쪽이 먼저 나오게 함
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
        # 후위 순회(왼쪽 -> 오른쪽 -> 나): 두 번째 방문(visited)일 때만 기록
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
