def is_valid_walk(walk):
    #determine if walk is valid
    # Variabeln fuer jede Himmelsrichtung anlegen
    nord = 0
    sued = 0
    west = 0
    ost = 0
    # Liste mit For-Schleife durchlaufen und die Richtungen pruefen
    for direction in walk:
        # gueltige Himmelsrichtungen den entsprechenden Variablen zuordnen
        # nach oben zaehlen
        if direction == 'n':
            nord = nord + 1
        elif direction == 's':
            sued = sued + 1
        elif direction == 'w':
            west = west + 1
        elif direction == 'e':
            ost = ost + 1
    # die Laenge der Liste berechnen
    count = len(walk)
    # Print zum preufen
    print(nord)
    print(sued)
    print(ost)
    print(west)
    print(count)
    # pruefen ob die Anzahl der Bewegungen gleich sind
    # Ausgangspunkt muss wieder erreicht werden
    # Liste darf auch nicht laenger als 10 sein (siehe Aufgabe)
    if nord == sued and west == ost and count == 10:
        return True
    else:
        return False