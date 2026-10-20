# A) oppretter en klasse som jeg kaller for Film

class Film:
# Lager en funksjon som bruker init metoden for å sette startverdien på objektet når det blir opprettet.
# () i funksjonen(setter vi parametere som tittel, utgivelsesår og IMDB-raing.
    def __init__(self, title, year, score):

# attributer som lagrer verdiene når et objekt blir laget.
        self.title = title
        self.year = year
        self.score = score




# ny metode som jeg kaller for komprimert som returnerer verdiene av et objekt og tekst inni en f-string
    def komprimert(self):
        return f"{self.title} was released in {self.year} and currently has a score of {self.score}"



# Variabler for å opprette objekter som jeg kaller for film1, film2, film3 med argumenter i ()
film1 = Film("Inception", 2010, 8.8)
film2 = Film("The Martian", 2015, 8.0)
film3 = Film("Joker", 2019, 8.4)

#print funksjon med f-string som henter ut verdiene til objekten og printer teksten.
print(f"{film1.title} was released in {film1.year} and currently has a score of {film1.score}")
print(f"{film2.title} was released in {film2.year} and currently has a score of {film2.score}")
print(f"{film3.title} was released in {film3.year} and currently has a score of {film3.score}")

#print funksjon som skriver ut det metoden komprimert returnerer
print(film1.komprimert())
print(film2.komprimert())
print(film3.komprimert())


