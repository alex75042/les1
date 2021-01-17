answer = int(input('Введи число от 11  '))
max_1 = 0
answer1 = answer

while answer != 0:
    ma = 0
    ma = int((answer - ma) % 10)
    answer = (answer - ma) / 10
    if ma >= max_1:
        max_1 = ma

print('Вы ввели число ', answer1, "\n Максимальная цифра в этом числе - ", max_1)


