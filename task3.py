#3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
print("Введите число:")
num = input()
sum = num
sum2 = num * 2
sum3 = num * 3
print("Сумма чисел:", int(sum) + int(sum2) + int(sum3))