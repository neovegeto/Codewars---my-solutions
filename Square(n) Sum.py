def square_sum(numbers):

    #your code here
    summe = 0 # Variable erstellen und auf 0 setzen
    # Durlaufen des Arrays
    for i in numbers:
        # Berechnung der Summe, wie im Bespiel gefodert
        summe = summe + i**2
    return summe