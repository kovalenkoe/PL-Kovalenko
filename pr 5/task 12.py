s=input()
r=[]
words=s.split()
for word in words:
	if word.endswith('я'):
		r.append(word)
print(r)
