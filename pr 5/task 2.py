s=input()
s1=s.count(':')
if ':' in s:
	s=s.replace(':','%')
print(s1, s)
