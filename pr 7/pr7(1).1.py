figyra=input('Введите название фигуры (прямоугольник, круг, квадрат, треугольник): ')
import math
def f():
	if figyra == 'прямоугольник':
		def rectangle(a,b):
			return a*b
		a=int(input('Введите 1 сторону прямоугольника: '))
		b=int(input('Введите 2 сторону прямоугольника: '))
		result_rectangle=rectangle(a,b)
		print('Площадь прямоугольника: ', result_rectangle)
	elif figyra == 'круг':
		def circle(r):
			return math.pi * r**2
		r=int(input('Введите радиус круга: '))
		result_circle=circle(r)
		print('Площадь круга: ',result_circle)
	elif figyra == 'квадрат':
		def square(number):
			return number**2
		number=int(input('Введите сторону квадрата: '))
		result_square=square(number)
		print('Площадь квадрата: ', result_square)
	elif figyra == 'треугольник':
		def triangle(a,h):
			plosh=(a*h/2)
			return plosh
		a=int(input('Введите длину основания: '))
		h=int(input('Введите высоту: '))
		plosh=triangle(a, h)
		print(plosh)
f()