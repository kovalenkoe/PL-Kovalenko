c = int(input())
n = int(input())

a = []

for i in range(c):
    b = []
    for j in range(n):
        b.append(randint(1,10))
    a.append(b)

for i in range(c):
    for j in range(n):
        print(a[i][j],end=' ')
    print()

print()

for i in a:
    i[i.index(max(i))],i[0] = i[0],i[i.index(max(i))]
    i[i.index(min(i))],i[-1] = i[-1],i[i.index(min(i))]


for i in range(c):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
