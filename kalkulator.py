liczba = input("podaj liczbe")
liczba=int(liczba)
liczbaa = input("podaj 2 liczbe ")
liczbaa=int(liczbaa)
operator = input("podaj dzialanie ")



if operator=="+":
    wynik=liczba+liczbaa
    print(wynik)
elif operator== "-":
    #wynik=liczba-liczbaa
    print(liczba-liczbaa)
elif operator=="*":
    wynik=liczba*liczbaa
    print(wynik)
elif operator=="/":
    wynik=liczba/liczbaa
    print(wynik)
else:
    print("Kalkulator nie obejmuje takiego dzialania")