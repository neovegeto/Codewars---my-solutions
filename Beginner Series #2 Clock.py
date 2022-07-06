def past(h, m, s):
    # Good Luck!
    #Umrechnung der Werte in Millisekunde
    if h == 0 and m == 0 and s == 0: # wenn alle Zeiten Null sind,
        return 0                    # dann gib 0 zureuck
    else:
        hour = h #Variabeln erstellen
        min = m
        sec = s
        # Umrechnen der Variablen in Millisekunden
        MilHour = h * 3600000 #  1 Stunde entspricht 3600000 ms

        MilMin = min * 60000 #  1 minute entspricht 60000 ms

        MilSec = s * 1000 #  1 s entspricht 1000 ms
        # Werte addieren und an das Programm zurueck geben
        return MilHour + MilMin + MilSec
print(past(1,4,5))