#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
num = int(input("Введите целое положительное число:"))
num_max = 0
while num !=0:
    if num % 10 > num_max:
        num_max = num % 10
    num = num//10
print("Самая большая цифра в числе:", num_max)