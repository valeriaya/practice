per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('How much do you plan to deposit:'))
deposit_TKB = int((per_cent['ТКБ']) * (money/100))
deposit_CKB = int((per_cent['СКБ']) * (money/100))
deposit_VTB = int((per_cent['ВТБ']) * (money/100))
deposit_SBER = int((per_cent['СБЕР']) * (money/100))
deposit= deposit_TKB, deposit_CKB, deposit_VTB, deposit_SBER
print (deposit)
print(f"Максимальное значение составляет: {max(deposit)}")










