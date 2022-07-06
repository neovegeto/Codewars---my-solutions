def duplicate_count(text):
    # Your code goes here
    '''Python string hat eine eingebaute lower()-Methode,
    die alle Zeichen in der Zeichenkette in Kleinbuchstaben umwandelt.
    Sie gibt eine Zeichenkette zurück, in der alle Zeichen in Kleinbuchstaben umgewandelt sind.
    Wir können zwei Zeichenketten mit der Methode lower() in Kleinbuchstaben umwandeln
    und sie dann case-insensitiv vergleichen.
    -->The input string can be assumed to contain
    only alphabets (both uppercase and lowercase) and numeric digits.'''
    neuer_text = text.lower()

    zaehler = 0
    dictionary = {}

    for i in range(0,len(neuer_text)):
        dictionary[neuer_text[i]] = 0

    for key in dictionary:
        for i in range(0,len(neuer_text)):
            if(key == new_text[i]):
                dictionary[key] = dictionary[key] + 1

    for key in dictionary:
        if(dictionary[key] > 1):
            count = zaehler + 1

    print(dictionary)
    return count