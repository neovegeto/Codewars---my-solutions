def longest(a1, a2):
    # your code
    '''
    Since strings and tuples are immutable, there is no sort() method that updates the original object.
    sorted() is a built-in function.
    Specifying a list to sorted() returns a sorted list.'''
    new_str_list = sorted(a1 + (a2))
    # sorted returns a list, so you can make it a string again using join:
    new_str = ''.join(new_str_list)
    # print(new_str_list)
    # print(new_str)
    # Variabeln zur weiteren Bearbeitung erstellen
    result = []  # Liste
    result2 = ''  # String
    j = 0  # Zahl

    for i in new_str_list:  # Die neue, sortierte Liste durchlaufen
        if new_str_list[j] == new_str_list[j - 1]:  # aktuellen Inhalt mit dem vorherigen Inhalt vergleichen
            # sind die Werte gleich, so wird zu pruefende Inhalt nach oben gesetzt
            j = j + 1

        else:  # ist der Inhalt nicht gleich
            result.append(i)  # so wird der Inhalt von i in die Liste "result" eingefuegt
            result2 = ''.join(result)  # Liste in String umwandlen
            j = j + 1  # Zaehler ebenfalls nach oben setzen
            # print(result2)
    # Aus den Schleifen raus gehen und das Ergebnis zurueck ans System liefern
    return result2

