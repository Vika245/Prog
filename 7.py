numbers = [10, 20, 30, 40, 50]
n = int(input("Введите число: "))
a = False
for i in range(0, len(numbers)):
    if numbers[i] == n:
        print(i)
        a = True
        break
if not a:
        print("Нет такого числа")