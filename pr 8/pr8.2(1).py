a = list()

n = int(input())

for i in range(n):
    b = list()
    for j in range(n):
        b.append(5)
    a.append(b)

for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()


first = sum(a[0])
b = 0

for k in a:
    if sum(k) != first:
        b += 1
        break

for k in range(0, n):
    if sum([row[k] for row in a]) != first:
        b += 1
        break

if b == 0:
    print('Матрица является магическим квадратом')
else:print('Матрица не является магическим квадратом')
