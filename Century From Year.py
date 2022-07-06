def century(year):
    listenjahr = year
    Quersumme = (lambda x: sum([int(y) for y in str(x)]))
    listen = [int(i) for i in str(listenjahr)]
    jahr = 0
    # Finish this :)
    print(listen)
    if len(str(year)) == 1 or len(str(year)) == 2:
        return 1
    elif len(str(year)) == 3:
        jahr = str(year)
        jahr = jahr[0:1]
        jahr = int(jahr)
        return int(jahr) + 1

    elif len(str(year)) == 4:
        if year % 10 == 0 and Quersumme(year) <= 10:
            if listen[2] == 0 and listen[3] == 0:
                jahr = str(year)
                jahr = jahr[0:2]
                jahr = int(jahr)
                return int(jahr)
            elif listen[2] != 0 or listen[3] != 0:
                jahr = str(year)
                jahr = jahr[0:2]
                jahr = int(jahr)
                return int(jahr) + 1
            else:
                jahr = str(year)
                jahr = jahr[0:2]
                jahr = int(jahr)
                return int(jahr)
        else:
            jahr = str(year)
            jahr = jahr[0:2]
            jahr = int(jahr)
            return int(jahr) + 1
print(century(2410))
