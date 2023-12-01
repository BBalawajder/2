'''
    Ćwiczenie 9
    a. Napisz program łamiący szyfr Cezara metodą siłową.
'''

def deszyfrujCezar(klucz, tekst):
    jawny = ""
    dl = len(tekst)

    for i in range(0, dl):
        if tekst[i] == " ":
            kod = ord(" ")
        else:
            kod = ord(tekst[i]) - klucz
            if (kod < ord("A")):
                kod = kod + 26
        jawny = jawny + chr(kod)

    return jawny

szyfrogram = input("Podaj szyfrogram: ")

for i in range(1,26):
    print(deszyfrujCezar(i, szyfrogram), "  Klucz:", i)

