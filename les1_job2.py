time = int(input('Введи время...  В СЕКУНДАХ!!!'))
time_sec = time % 60
time_min = int((time - time_sec) / 60 % 60)
time_ur = int((( time - time_sec)/60 - time_min) /60)
print("\nВы ввели ", time, " секунд.\n\n ЧЧ. ММ. СС.")
print('{:02}. {:02}. {:02}.'.format( time_ur, time_min, time_sec))