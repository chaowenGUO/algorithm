graph = {
    'A': {*'BC'},
    'B': {*'ACD'},
    'C': {*'ABDE'},
    'D': {*'BCEF'},
    'E': {*'CD'},
    'F': {'D'}
}

import collections

def bfs(root):
    result = []
    queue = collections.deque(root)
    seen = {root}
    while queue:
        node = queue.popleft()
        queue += graph.get(node) - seen
        seen |= graph.get(node)
        result += node,
    return result
