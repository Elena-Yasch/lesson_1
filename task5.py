#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
revenue = int(input("Введите значение выручки:"))
costs = int(input("Введите значение издержек фирмы:"))
if revenue > costs:
    print("Фирма получает прибыль")
    profit = revenue - costs
    profitability = (profit/revenue)*100
    print("Рентабельность равна", profitability, "%")
elif revenue < costs:
    print("Фирма работает в убыток")
employee = int(input("Введите количество сотрудников:"))
employee_profit = profit/employee
print("Прибыль фирмы в расчете на одного сотрудиника =", employee_profit)
