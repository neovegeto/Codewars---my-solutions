def get_sum(a, b):
    # good luck!
    ergebnis = 0  # Variable deklarieren und auf 0 setzen
    if a == b:  # pruefen ob die beiden Variablen gleich sind, entsprechend vorgabe
        return a  # Rueckgabe von a oder b moeglich
    # Pruefen ob a oder b groesser sind, von der kleineren Variablen beginnen
    elif a > b:
        ergebnis = b
        while b < a:
            b = b + 1
            ergebnis = ergebnis + b

        return ergebnis
    elif b > a:
        ergebnis = a
        while a < b:
            a = a + 1
            ergebnis = ergebnis + a

        return ergebnis
