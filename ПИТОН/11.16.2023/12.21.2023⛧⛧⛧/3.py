def find_the_ploshad(a, b=0):
    if b != 0:
        ploshad=a*b
        return ploshad
    else:
        ploshad = a*a
        return ploshad

print(find_the_ploshad(8, 22))
