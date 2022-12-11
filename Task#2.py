stroka = input("Введите строку с числом ")
flag = False
for i in range(len(stroka) - 1):
    if stroka[i] == "." or stroka[i] == ",":
        flag = True
if flag == True:
    print("В строке дробное число!")
else:
    print("Дробного числа нет!")