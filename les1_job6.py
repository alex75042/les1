finish = int(input('сколько надо пробежать в итоге прибавляя от ежедневного результата 10% (в км.)'))
start = int(input('сколько надо бежать в первый день (в км)'))
tag = 1
print('\n Результат')
while start <= finish:
    print(str(tag) + '-й день -', start, ' км.')
    start = int(start * 1.1 * 100) / 100
    tag = tag + 1
print(str(tag) + '-й день -', start, ' км.')
print('На ', str(tag) + '-й день спортсмен достигнет результата \n не менее ', finish, ' км.')
