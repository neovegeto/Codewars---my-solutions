def digitize(n):
    x = []

    x = [int(a) for a in str(n)]
    x.reverse()
    print(x)

    return x