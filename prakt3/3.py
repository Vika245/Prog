num1 = input("Введите число 1: ")
num2 = input("Введите число 2: ")
try:
    num1 = int(num1)
    num2 = int(num2)
    print("Результат: ", num1 + num2)
except ValueError:
    print("Вы ввели не число")
