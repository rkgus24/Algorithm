n = int(input('값 입력: '))
bt = [0] * (n + 1)
at = [0] * (n + 1)
abt = [0] * (n + 1)
for i in range(n):
	abt[i] = int(input('버스트 시간 {} : '.format(i + 1)))
	at[i] = int(input('프로세스 도착 시간 {} : '.format(i + 1))) 
	bt[i] = [abt[i], at[i], i]

bt.pop(-1)
print(abt)
print(bt)
sumbt = 0 
i = 0
ll = []
for i in range(0, sum(abt)):
	l = [j for j in bt  if j[1] <= i]
	l.sort(key=lambda x: x[0])
	print(l, l[0][2])
	bt[bt.index(l[0])][0] -= 1
	for k in bt:
		if k[0] == 0:
			t = bt.pop(bt.index(k))
			ll.append([k, i + 1])
print(ll)
ct = [0] * (n + 1)
tat = [0] * (n + 1)
wt = [0] * (n + 1)
for i in ll:
	print(i, i[0], i[1], i[0][2])
	ct[i[0][2]] = i[1] 

for i in range(len(ct)):
	tat[i] = ct[i] - at[i]
	wt[i] = tat[i] - abt[i]
ct.pop(-1)
wt.pop(-1)
tat.pop(-1)
abt.pop(-1)
at.pop(-1)
print('BT\tAT\tCT\tTAT\tWT')
for i in range(len(ct)):
	print("{}\t{}\t{}\t{}\t{}\n".format(abt[i], at[i], ct[i], tat[i], wt[i]))
print('평균 대기 시간 = ', sum(wt)/len(wt))
print('평균 처리 시간 = ', sum(tat)/len(tat))
