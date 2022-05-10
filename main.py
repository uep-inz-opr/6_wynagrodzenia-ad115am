class Pracownik:
    koszt_pracodawcy_suma = 0
    def __init__(self, imie, wynagrodzenie_brutto):
        self.imie = imie
        self.wynagrodzenie_brutto = wynagrodzenie_brutto
    def oblicz_skladke_emerytalna(self) -> float:
        return round(0.0976 * self.wynagrodzenie_brutto, 2)
    def oblicz_skladke_rentowa(self, procent) -> float:
        return round(procent/100 * self.wynagrodzenie_brutto, 2)

    def oblicz_wynagrodzenie_netto(self) -> float:
        skladka_emerytalna = self.oblicz_skladke_emerytalna()
        skladka_rentowa = self.oblicz_skladke_rentowa(1.5)
        skladka_chorobowa = round(0.0245*self.wynagrodzenie_brutto, 2)
        skladki_na_ubezpieczenia_spoleczne = round(skladka_emerytalna+skladka_chorobowa+skladka_rentowa, 2)
        podstawa_skladki_na_zdrowotne = self.wynagrodzenie_brutto - skladki_na_ubezpieczenia_spoleczne
        skladka_na_zdrowotne_z_wynagrodzenia = round(0.09*podstawa_skladki_na_zdrowotne, 2)
        skladka_na_zdrowotne_z_podatku = round(0.0775*podstawa_skladki_na_zdrowotne, 2)
        koszty_uzyskania_przychodu = 111.25
        podstawa_zaliczki_na_dochodowy = round(self.wynagrodzenie_brutto - koszty_uzyskania_przychodu - skladki_na_ubezpieczenia_spoleczne, 0)
        zaliczka_na_dochodowy_przed_obliczeniem_zdrowotnej = round(0.18*podstawa_zaliczki_na_dochodowy - 46.33, 2)
        zaliczka_na_dochodowy_do_pobrania = round(zaliczka_na_dochodowy_przed_obliczeniem_zdrowotnej-skladka_na_zdrowotne_z_podatku, 0)
        kwota_do_wyplaty = self.wynagrodzenie_brutto - skladki_na_ubezpieczenia_spoleczne - skladka_na_zdrowotne_z_wynagrodzenia - zaliczka_na_dochodowy_do_pobrania
        return kwota_do_wyplaty

    def oblicz_skladki_pracodawcy(self) -> float:
        skladka_emerytalna = self.oblicz_skladke_emerytalna()
        skladka_rentowa = self.oblicz_skladke_rentowa(6.5)
        skladka_wypadkowa = round(self.wynagrodzenie_brutto*0.0193, 2)
        skladka_na_FP = round(self.wynagrodzenie_brutto*0.0245, 2)
        skladka_na_FGŚP = round(self.wynagrodzenie_brutto*0.001, 2)
        skladki_pracodawcy = skladka_emerytalna + skladka_rentowa + skladka_wypadkowa + skladka_na_FP + skladka_na_FGŚP
        return skladki_pracodawcy

    def oblicz_koszt_pracodawcy(self) -> float:
        koszt_pracodawcy = self.wynagrodzenie_brutto + self.oblicz_skladki_pracodawcy()
        return koszt_pracodawcy

liczba_pracownikow = int(input())
pracownicy = []

for pracownik in range(liczba_pracownikow):
    dane_pracownika = list(input().split(' ', maxsplit=1))
    pracownicy.append(Pracownik(dane_pracownika[0], float(dane_pracownika[1])))
for pracownik in pracownicy:
    print(f"{pracownik.imie} {pracownik.oblicz_wynagrodzenie_netto():.2f} {pracownik.oblicz_skladki_pracodawcy():.2f} {pracownik.oblicz_koszt_pracodawcy()}")
    Pracownik.koszt_pracodawcy_suma += (pracownik.oblicz_koszt_pracodawcy())
print(Pracownik.koszt_pracodawcy_suma)


