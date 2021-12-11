from Cat import Cat

cat1 = Cat("Барон", "мальчик", 2)
cat2 = Cat("Сэм", "мальчик", 2)

print("Имя кошки:", cat1.name)
print("Пол :", cat1.gender)
print("Возраст :", cat1.getAge())
print("------")
print("Имя кошки", cat2.name)
print("Пол :", cat2.gender)
print("Возраст :", cat2.getAge())