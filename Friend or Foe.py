def friend(x):
    # leere Variable als Liste ersellen
    friends = []
    # Code
    for i in x:  # bestehende Liste durchlaufen
        if len(i) == 4:  # wenn ein Elemente aus der Liste die Laenge 4 hat
            friends.append(i)  # das Element in die neue, leere Liste eintragen
        else:  # ansonsten nichts tun
            pass
    return friends
