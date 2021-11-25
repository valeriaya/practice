try:
    tickets = int(input('Сколько билетов Вы хотите приобрести? Количество билетов: '))
    if tickets <= 0:
        print('Неверное значение')
except ValueError as error:
    print("Неверное значение")
count = 0
a = 990
b = 1390
for i in range(tickets):
    print('Сколько лет покупателю билета?')
    age = int(input('Введите Ваш возраст: '))
    if age < 18:
        count += 0
    if 18 <= age < 25:
        count += a
    if 25 <= age:
        count += b
if tickets > 3:
    count = count*0.9
    print(f'Сумма покупки со скидкой 10%: {count} рублей')
else:
    print(f'Сумма покупки: {count} рублей')
