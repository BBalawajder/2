'''
    Ćwiczenie 8
    a. Napisz program deszyfrujący tekst zaszyfrowany metodą Cezara ze znaną
       wartością klucza. Sprawdź działanie programu dla szyfrogramu
       PKYZKY SOYZXFKS QXEVZUMXGLOO i klucza 6.
    b. RSGNMTFCKOBWS GNMTFI QSNOFO NS NBOBMA YZIQNSA XSGH DFCGHS oraz klucza 14.
    
Komentarz:
Tekst jawny: 
a. JESTES MISTRZEM KRYPTOGRAFII
b. DESZYFROWANIE SZYFRU CEZARA ZE ZNANYM KLUCZEM JEST PROSTE
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
klucz = int(input("Podaj klucz szyfrowania: "))

print("\nTekst jawny:", deszyfrujCezar(klucz, szyfrogram))