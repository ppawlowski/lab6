# stowrzenie klasy Pracownik z wymaganymi zmiennymi (polami) - pkt 2 i 3
class Pracownik:
    imie = ""
    nazwisko = ""
    staz = 0.0
    wynagrodzenie = 0.0
    dodatek = 0.0

    def __init__(self, imie, nazwisko, staz, wynagrodzenie, dodatek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.staz = staz
        self.wynagrodzenie = wynagrodzenie
        self.dodatek = dodatek

# do testowania tworzenia obiektu
# nowy_pracownik = Pracownik("test", "testowy", "1.0", "1234", "123")
# print(nowy_pracownik.imie_nazwisko + '\n' + nowy_pracownik.staz + '\n' + nowy_pracownik.wynagrodzenie + '\n' + nowy_pracownik.dodatek)

# stworzenie tablicy 100 obiektow klasy Pracownik z losowymi wartosciami zmiennych (pol)
# importowanie modulow niezbednych do wygenerowania losowych wartosci zmiennych (pol)
import random
import string
# stworzenie tablicy
pracownicy = []
# wygenerowanie 100 obiektow i umieszczenie w tablicy
for a in range(0, 100):
    pracownicy.append(Pracownik("".join([random.choice(string.letters) for i in xrange(7)]),
                                "".join([random.choice(string.letters) for i in xrange(15)]),
                                random.uniform(0.0, 105.0), random.uniform(0.0, 50000.0), random.uniform(0.0, 5000.0)))

# do testowania dlugosci tablicy
# print(len(pracownicy))
