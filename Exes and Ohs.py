def xo(s):
    '''The count() method returns the number of occurrences of a substring in the given string.
    count() method only requires a single parameter for execution.
    The lower() method converts all uppercase characters
     in a string into lowercase characters and returns it.
     '''
    # Varablen fuer x und o deklarieren
    o = s.lower().count('o') # Suche nach Buchstabe o, in klein
    x = s.lower().count('x') # Suche nach Buchstaben x, in klein

    # wenn der Inhalt der Variablen o und x gleich sind, dann
    if o == x :
        return True # True zurueck geben
    # wenn der Inhalt nicht gleich ist
    elif o != x :
        return False # False zureck geben
    else:
        # ansonsten immer False zureck geben
        return True
