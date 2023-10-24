n=int(input())
a=[]
for i in range(n):
	a.append(input())
min_elem=min(a)
his_index=a.index(min_elem)
print(min_elem, his_index)
