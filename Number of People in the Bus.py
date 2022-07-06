def number(bus_stops):
    # Good Luck!
    bus = 0
    for people in bus_stops:
        inside = people[0]
        outside = people[1]
        bus = bus + (inside - outside)
    return bus

def number(bus_stops):
    passagiere = 0
    for i in bus_stops:
        passagiere = passagiere + i[0]
        passagiere = passagiere - i[1]

    return passagiere

def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])