first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second and first == third:
    print('3 числа совпадают')
elif first == second or first == third or second == third:
    print('2 из трех чисел свпадают')
else:
    print('0 чисел совпадают')