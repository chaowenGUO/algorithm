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
    queue = collections.deque(root)
    seen = set()
    while queue:
        node = queue.pop()
        queue += graph.get(node) - seen
        seen | graph.get(node)
        print(node)
