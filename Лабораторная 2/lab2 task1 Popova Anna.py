money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0

while money_capital > 0:
    need_from_capital = spend - salary
    money_capital -= need_from_capital
    if money_capital > 0:
        months += 1
        spend = spend + (spend * 0.05)

print("Количество месяцев, которое можно протянуть без долгов:", months)
