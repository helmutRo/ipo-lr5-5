x = input("Введите строку: ") #ввод строки от пользователя
g = "уеёыаоэяию" #гласные которые должен считать
s = 0 #обозначение счетчика
for i in x: # проверяет наличие g
    if i in g: # если в строке есть гласные то засчитывает +1 к счетчику
        s += 1 
    else: 0 # если в строке нет гласных то засчитывает 0
print(f"колво гласных букв в строке: {s}")
