a = list()

n = int(input())
g = int(input())

for i in range(n):
    b = list()
    for j in range(g):
        b.append(randint(1,9))
    a.append(b)


for i in range(n):
    for j in range(g):
        print(a[i][j],end = ' ')
    print()

for i in a:
    i[0],i[3] = i[3],i[0]

print()

for i in range(n):
    for j in range(g):
        print(a[i][j],end = ' ')
    print()
