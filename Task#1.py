num = int(input("Введите десятичное число: "))
litter = ""
if num < 10 and num >= 0:
    print(num)
elif num >= 10:
    while num > 0:
        help = int(num % 16)
        if help == 10:
            help = "A"
        elif help == 11:
            help = "B"
        elif help == 12:
            help = "C"
        elif help == 13:
            help = "D"
        elif help == 14:
            help = "E"
        elif help == 15:
            help = "F"
        litter = str(help) + litter
        num //= 16
    print(litter)
else:
    print("Про минус разговора не было)")