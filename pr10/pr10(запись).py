from random import randint

n = int(input())
m = int(input())
a = []
for i in range(n):
    b=[]
    for j in range(m):
        b.append(randint(10, 100))
    a.append(b)

fi = open('C:/Users/admin/OneDrive/Рабочий стол/kovalenkoE_UB-31_vvod.txt', 'w')
for i in a:
    for j in i:
        fi.write(str(j))
        fi.write(' ')
    fi.write('\n')
fi.close()
