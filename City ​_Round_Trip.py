import sys
from collections import deque
input = sys.stdin.readline

INF = 2147000000
MAX_N = 401
answer = 0

def BFS(source, sink, visited):
    que = deque()
    que.append(source)

    while que and visited[sink] == -1:
        sv = que.popleft()
        
        for dv in graph[sv]:
            if capacity[sv][dv] - flow[sv][dv] > 0 and visited[dv] == -1:
                que.append(dv)
                visited[dv] = sv
                
                if dv == sink:
                    break
	
    if visited[sink] == -1:
        return True
    else:
        return False


def edmonds_karp(source, sink):
    answer = 0
    while True:
        visited = [-1 for _ in range(MAX_N)]
        if BFS(source, sink, visited):
            break

        min_flow = INF
        
        j = sink
        while j != source:
            i = visited[j]
            min_flow = min(min_flow, capacity[i][j] - flow[i][j])
            j = i

        j = sink
        while j != source:
            i = visited[j]
            flow[i][j] += min_flow
            flow[j][i] -= min_flow
            j = i
		
        answer += min_flow

    return answer


N, P = map(int, input().split())

graph = [[] for _ in range(MAX_N)]
capacity = [[0]*MAX_N for _ in range(MAX_N)]
flow = [[0]*MAX_N for _ in range(MAX_N)]

for _ in range(P):
    sv, dv = map(int, input().split())
    graph[sv].append(dv)
    graph[dv].append(sv)
    capacity[sv][dv] = 1

print(edmonds_karp(1, 2))
