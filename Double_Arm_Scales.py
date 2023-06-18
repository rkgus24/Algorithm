import sys
input = sys.stdin.readline

num_pends = int(input())
pends = list(map(int, input().split()))
num_marbles = int(input())
marbles = list(map(int, input().split()))

dp = [[0]*(30*500+1) for _ in range(num_pends+1)] 

result = set()

def get_result(pends, n, now, left, right):
    
    new = abs(left - right)

    if new not in result:
        result.add(new)

    if now == n :
        return 0

    if dp[now][new] == 0:
        get_result(pends, n, now+1, left + pends[now], right)
        get_result(pends, n, now+1, left, right + pends[now])
        get_result(pends, n, now+1, left, right)
        dp[now][new] = 1

get_result(pends, num_pends, 0, 0, 0)
answer = []

for marble in marbles:
    if marble in result:
        answer.append("Y")
    else:
        answer.append("N")

print(*answer)
