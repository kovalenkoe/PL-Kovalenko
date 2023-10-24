n=[int(input()) for i in range(10)]
for a in range(len(n)):
	if n[a]<0 and n[a+1]<0:
		print(n[a], n[a+1])
