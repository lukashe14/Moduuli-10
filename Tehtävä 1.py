class hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.alin_kerros or kohdekerros > self.ylin_kerros:
            print("Virhe: Kohdekerros on sallitun alueen ulkopuolella.")
            return

            # Siirrytään haluttuun kerrokseen
        while kohdekerros > self.nykyinen_kerros:
            self.kerros_ylös()

        while kohdekerros < self.nykyinen_kerros:
            self.kerros_alas()



    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Nykyinen kerros: {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Nykyinen kerros: {self.nykyinen_kerros}")



hissi = hissi(1,5)

hissi.siirry_kerrokseen(5)

hissi.siirry_kerrokseen(1)







