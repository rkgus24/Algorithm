import sys
input = sys.stdin.readline

k = int(input())
a = []

for i in range(k):
    n = int(input())
    if n == 0:
        del a[-1]
    else:
        a.append(n)
print(sum(a))
