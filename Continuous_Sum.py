input()
s=[*map(int,input().split())]
d=[s[0]]
for i in s[1:]:
    d.append(max(d[-1]+i,i))
print(max(d))
