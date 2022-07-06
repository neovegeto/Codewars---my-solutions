def nb_year(p0, percent, aug, p):
    # your code
    population = abs(p0)
    prozent = abs(percent)
    newinhab = int(aug)
    finalpop = abs(p)
    years = 0

    while population < finalpop:
        population = population + int(((population * prozent) / 100)) + newinhab
        years = years + 1
    return years
