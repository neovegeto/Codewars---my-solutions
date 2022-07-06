def is_triangle(a, b, c):
    # Eingaben in Variablen ueberfuehren
    sidea = a
    sideb = b
    sidec = c
    # Pruefen ob alle Seiten positiv sind
    if sidea > 0 and sideb > 0 and sidec > 0:
        # Pruefen ob aus den Seiten ein Dreick erstellt werden kann
        '''How to Determine if Three Side Lengths Are a Triangle
        Determining if three side lengths can make a triangle is easier 
        than it looks. All you have to do is use the 
        Triangle Inequality Theorem, which states that 
        the sum of two side lengths of a triangle is always greater 
        than the third side. 
        If this is true for all three combinations of added side lengths, 
        then you will have a triangle.
        a+b > c, a+c > b, and b+c > a
        Muss fuer alle drei Faelle gelten

        '''
        if sidea + sideb > sidec and sideb + sidec > sidea and sidec + sidea > sideb:
            return True
        else:
            return False
    else:
        return False
