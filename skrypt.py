# importowanie klasy Pracownik z modulu pracownik (warunek - modul pracownik snajduje sie w ym samym katalgu co ten skrypt
# from pracownik import Pracownik

# importowanie klasy Pracownik z modulu pracownik znajdujacego sie w pakiecie lab6
from lab6.pracownik import Pracownik

# tworzenie obiektu z klasy Pracownik
nowy_pracownik = Pracownik("Piotr", "Pawlowski", 2, 10000, 2000)
# zmiana wartosc zmiennej (pola) imie na nowy
nowy_pracownik.imie = "Pawel"
# wypisanie danych pracownika
print("Imie i nazwisko: " + nowy_pracownik.imie + " " + nowy_pracownik.nazwisko
      + "\nStaz pracy: " + str(nowy_pracownik.staz)
      + "\nWynagrodznie: " + str(nowy_pracownik.wynagrodzenie)
      + "\nDodatek: " + str(nowy_pracownik.wynagrodzenie))
