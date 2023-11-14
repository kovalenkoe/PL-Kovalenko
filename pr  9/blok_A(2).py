def f(a, b):
	if a < b:
		return a 
	return f(a%b, b)
a=int(input('Введите значение a: '))
b=int(input('Введите значение b: '))
print(f(a,b))
