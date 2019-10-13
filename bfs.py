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
    
