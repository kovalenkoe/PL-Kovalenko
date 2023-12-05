f1 = open('C:/Users/admin/OneDrive/Рабочий стол/kovalenkoE_UB-31_vvod.txt', 'r')

m = []
for i in f1:
    n = []
    s = i.split(' ')
    for j in s:
        if j == '\n':
            continue
        n.append(int(j))
    m.append(n)
print(m)
f1.close()

for i in m:
    mn = i.index(min(i))
    mx = i.index(max(i))
    i[mx], i[0] = i[0], i[mx]
    i[mn], i[-1] = i[-1], i[mn]

f2 = open('C:/Users/admin/OneDrive/Рабочий стол/kovalenkoE_UB-31_vvod.txt', 'w')
for i in m:
    for j in i:
        f2.write(str(j))
        f2.write(' ')
    f2.write('\n')
f2.close()
