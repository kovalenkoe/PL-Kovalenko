s=0
pr=1
g=[int(i) for i in input().split()]
for a in g:
	s+=a
	pr*=a
print(s, pr)
