# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

academic_year = 0
all_expenses = 0
while academic_year < 10:
    all_expenses += expenses
    print('Ежемесячные расходы составляют', expenses, 'рублей')
    expenses = round(expenses + (expenses * 0.03))
    academic_year += 1
print('Расходы за 10 месяцев составляют', all_expenses, 'рублей')
all_grant = educational_grant * academic_year
print('Стипендия за 10 месяцев составляет', all_grant, 'рублей')
parents_money = all_expenses - all_grant
print('Студенту надо попросить', parents_money, 'рублей')

# зачет!
