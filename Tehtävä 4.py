import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

class Kilpailu:
    def __init__(self, nimi, autot, maali):
        self.nimi = nimi
        self.autot = autot
        self.maali = maali
        self.tunti = 0

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)
        self.tunti += 1

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.maali:
                return True
            return False

    def tulosta_tilanne(self):
        print(f"\nKilpailun tilanne tunnin {self.tunti} jälkeen:")
        print(f"{'Rekisteritunnus':<15} {'Huippunopeus (km/h)':<20} {'Nopeus (km/h)':<15} {'Kuljettu matka (km)':<20}")
        print("=" * 70)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<15} {auto.huippunopeus:<20} {auto.nopeus:<15} {auto.kuljettu_matka:<20.1f}")


if __name__ == '__main__':
    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)  # Arvotaan huippunopeus
        auto = Auto(rekisteritunnus, huippunopeus)
        autot.append(auto)

    kilpailu = Kilpailu("Suuri romuralli", autot, 8000)
    kilpailu_käynnissä = True

    while kilpailu_käynnissä:
        kilpailu.tunti_kuluu()
        if kilpailu.tunti % 10 == 0:
            kilpailu.tulosta_tilanne()

        if kilpailu.kilpailu_ohi():
            kilpailu_käynnissä = False

    print("\nKilpailu on ohi")
    kilpailu.tulosta_tilanne()