import sys

input = sys.stdin.readline
INF = int(1e9)

def dfs(now, visited):
    if visited[now]:
        return False
    visited[now] = True
    
    for _next in adj[now]:
        if bMatch[_next] == 0 or dfs(bMatch[_next], visited):
            bMatch[_next] = now
            return True
    return False

def solution():
    global k
    cnt = 0

    for start in range(1, n+1):
        visited = [False for _ in range(n+1)]
        if dfs(start, visited):
            cnt += 1

    for start in range(1, n+1):
        while k > 0:
            visited = [False for _ in range(n+1)]
            if dfs(start, visited):
                cnt += 1
                k -= 1
            else:
                break

    print(cnt)

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    adj = [[]]
    for _ in range(1, n+1):
        adj.append(list(map(int, input().split()))[1:])

    bMatch = [0 for _ in range(m+1)]

    solution()
