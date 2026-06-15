marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]
five = 0
two = 0
for i in marks:
    if i == 5:
        five += 1
    elif i == 2:
        two += 1
print(f" Количество пятерок: {five}")
print(f" Количество двоек: {two}")