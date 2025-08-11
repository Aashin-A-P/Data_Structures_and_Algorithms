n = int(input())
a = list(map(int,input().split()))
d = dict()
b = []
for i in range(1,len(a)+1):
	d[a[i-1]] = i 
for i in range(1,len(a)+1):
	b.append(d[i])
print(b)