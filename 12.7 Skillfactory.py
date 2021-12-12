per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите Вашу сумму: "))
deposit = []
for i in  list(per_cent.values()):

 deposit.append(float(money * i / 100))

print(deposit)
print("Вводимая сумма: ", money)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit), "(Банк СКБ)")
