n=int(input())
a=[]
a_pol=[]
a_otr=[]
for i in range(n):
	a.append(int(input()))
for elem in a:
	if elem > 0:
		a_pol.append(elem)
	else:
		a_otr.append(elem)
print("Положительный массив:", a_pol, 'Отрицательный массив:', a_otr)                                                                                                                                                                                                                    
