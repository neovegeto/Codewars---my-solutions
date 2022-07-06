def open_or_senior(data):
    # Variable fuer den Status der Mitgliedschaft, als Liste
    membership = []

    # Durchlaufen der Liste um den Status zu pruefen.
    # Es werden immer zwei Werte uebergeben
    for i in data:
        # Pruefen der Anforderung entsprechend der Aufgabe
        if i[0] >= 55 and i[1] > 7:
            # Anfuegen des Status
            membership.append('Senior')
        else:
            # Anfuegen des Status
            membership.append('Open')
    return membership