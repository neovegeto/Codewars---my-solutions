import math # Modul Mathe importieren fuer Wurzel-Funktion
def find_next_square(sq):
    wurzel = 0 # Variable deklarieren und auf 0 setzen
    # Return the next square if sq is a square, -1 otherwise
    if math.sqrt(sq)//1 == math.sqrt(sq)/1:
        '''The “//” operator is used to return the closest integer value 
        which is less than or equal to a specified expression or value. 
        So from the above code, 5//2 returns 2. You know that 5/2 is 2.5, 
        and the closest integer which is less than or equal is 2[5//2].
        ( it is inverse to the normal maths, in normal maths the value is 3).'''
        #print(wurzel)
        wurzel = math.sqrt(sq)

        #print(wurzel)
        wurzel = wurzel + 1

        #print(wurzel)
        wurzel = wurzel * wurzel

       # print(wurzel)
        return wurzel
    else:
        return -1
