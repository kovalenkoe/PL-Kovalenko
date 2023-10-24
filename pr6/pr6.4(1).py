n=int(input())
a=[]
for i in range(n):
	a.append(int(input()))
max_elem=max(a)
his_index=a.index(max_elem)
print(max_elem, his_index)
