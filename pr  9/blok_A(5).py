n=int(input())
def f(n):
	if n > 10:
		print(n%10)
		return f(n//10)
	else:
		print(n%10)
f(n)
