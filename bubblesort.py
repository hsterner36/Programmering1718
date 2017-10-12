import random

def generer_tal():
    tal = [random.randint(0, 100) for c in range(10)]
    return tal


def print_tal(tal, tekst):
    print(tekst)
    print(tal)


def bubblesort(tal):
    i = len(tal) - 1

    while i >= 1:
        for j in range(0, i):
            x = tal[j]
            y = tal[j+1]
            if x > y:
                tal[j] = y
                tal[j+1] = x
        i = i-1


def main():
    tal = generer_tal()
    print_tal(tal, "Foer sortering:")
    bubblesort(tal)
    print_tal(tal, "Efter sortering:")


main()
