l=int(input())
n=[int(input()) for i in range(l)]
s=0
for j in n:
	s+=j
	sa=s/l
for k in range(len(n)):
	if n[k]==0:
		n[k]==sa
print(n)