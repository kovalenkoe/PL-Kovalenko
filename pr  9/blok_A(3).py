n=int(input())
def f(n):
	if n < 10:
		return n
	return str(n%10)+str(f(n//10))
print(f(n))
