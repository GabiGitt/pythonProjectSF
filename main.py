per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
result = []
for v in per_cent.values():
    result.append(int(money * v / 100))
print('deposit = ', result)
