def find_needle(haystack):
    # your code here
    lst = haystack # Die Liste zur anderen Bearbeitung "kopieren"
    #durchlaufen der Liste (kein Array in Python)
    for i in haystack:
        if i == "needle": #Wenn der Wert "needle" entspricht, dann
            result = lst.index('needle') # die Position auslesen
            # und den geforderten String sowie die Position zurueck geben
            return "found the needle at position " + str(result)
        else: # ansonsten
            pass # nichts tun