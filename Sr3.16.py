a = int(input())
if a % 5 == 0 and a % 3 == 0:
    print('Число кратно 3 и 5')
elif a % 3 == 0:
    print('Число кратно 3')
elif a % 5 == 0:
    print('Число кратно 5')
else:
    print('Число не кратно ни 3, ни 5')