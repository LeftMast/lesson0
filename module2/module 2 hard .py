def pass_(number):
    pass_ = ''
    for i in range(1, number + 1):
        for k in range(i + 1, number + 1):
            if (number % (i + k)) == 0:
                pass_ += str(i) + str(k)
    return pass_


num = 3
password = pass_(num)
print(f'{num} - {password}')