stroka = input("Введите строку ")
firstIndexI = 0
lastindexI = 0
count = 0
numIndexReverse = 0
stroka1 = ""
for i in range(len(stroka)):
    if stroka[i] == "о" or stroka[i] == "o":
        count += 1
        if count == 1:
            firstIndexI = i
        lastIndexI = i
        print("last", lastIndexI)
        print("first", firstIndexI)
if count < 2:
    print("В строке нет буквы о или она одна!")
else:
    for i in range(len(stroka)):
        if i > firstIndexI and i < lastIndexI :
            numIndexReverse = numIndexReverse + 1
            stroka1 = stroka1 + stroka[lastIndexI - numIndexReverse]
        else:
            stroka1 = stroka1 + stroka[i]
    print(stroka1)