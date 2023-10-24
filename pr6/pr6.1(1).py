n=int(input())
a=[]
for i in range(n):
	a.append(int(input()))
max_elem=max(a)
print('Максимальный элемент',max_elem)
print(a[::-1])
