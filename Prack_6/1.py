temperature = float(input('Введите температуру: '))
pressure = float(input('Введите давление: '))
pulse = float(input('Введите пульс: '))
Normal_condition = (35 < temperature < 38 and 109 < pressure < 131 and 59 < pulse < 101)
Mild_malaise = ((34 < temperature < 37 or 36 < temperature < 39) and (104 < pressure < 111 or 129 < pressure < 141) and (54 < pulse < 61 or 99 < pulse < 111))
Doctor_required = ((temperature < 35 or temperature > 38) and (pressure < 105 or pressure > 140) and (pulse < 55 or pulse > 110))
if Normal_condition:
    print('Нормальное состояние')
elif pressure:
    print('Легкое недомогание')
elif pulse:
    print('Требуется врач')
else:
    print('ошибка')