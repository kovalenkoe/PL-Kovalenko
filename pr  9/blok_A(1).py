x=int(input('Введите значение х: '))
n=int(input('Введите значение n: '))
def f(n):
	if n == 0:
		return 1
	return f(n-1)*n
print((x**n)/f(n))
