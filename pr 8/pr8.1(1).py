n=int(input())
a=[]
s=0
c=0
for i in range(n):
	b=[]
	for j in range(n):
		b.append(int(input()))
	a.append(b)
for i in a:
	print()
	for j in i:
		print(j, end=' ')
for i in range(n):
	for j in range(i+1, n):
		if a[i][j]>0:
			c+=1
			s+=a[i][j]
print()
print(s,c)
