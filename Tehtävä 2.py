class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.alin_kerros or kohdekerros > self.ylin_kerros:
            print("Virhe: Kohdekerros on sallitun alueen ulkopuolella.")
            return
        while kohdekerros > self.nykyinen_kerros:
            self.kerros_ylös()
        while kohdekerros < self.nykyinen_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Nykyinen kerros: {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Nykyinen kerros: {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.hissit = []
        for _ in range(hissien_maara):
            hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if hissin_numero < 0 or hissin_numero >= len(self.hissit):
            print("Virhe: Hissin numero on virheellinen.")
            return
        hissi = self.hissit[hissin_numero]
        hissi.siirry_kerrokseen(kohdekerros)

talo = Talo(1, 5, 3)

print("Ajetaan hissiä 0 kerrokseen 3:")
talo.aja_hissiä(0, 3)

print("\nAjetaan hissiä 1 ylimpään kerrokseen (5):")
talo.aja_hissiä(1, 5)

print("\nAjetaan hissiä 2 alimpaan kerrokseen (1):")
talo.aja_hissiä(2, 1)
