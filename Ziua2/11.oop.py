
## cu litera mica la inceput - conventie
def functie():
    pass

## cu litera mare la inceput - conventie
class Animal:
    ## INITIALIZATOR (constructor)
    def __init__(self, nume, varsta):
        # ATRIBUT (varibila a clasei) - CE ARE obiectul
        self.nume = nume
        self.varsta = varsta

    # METODA (functie a clasei) - CE FACE obiectul
    def merge(self):
        print(f"Animalul {self.nume} cu varsta {self.varsta}ani... merge...")

print(Animal)
print(type(10))

rino = Animal("Rino", 5)
print(rino)
rino.merge()

tazz = Animal("Tazz", 7)
print(tazz)
tazz.merge()