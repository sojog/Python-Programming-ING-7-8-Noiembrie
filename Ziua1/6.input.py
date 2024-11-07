# Creaţi un program care ia două numere de la utilizator, le adună şi afişează rezultatul.
# Valorile de la utilizator se introduc cu comanda input() 

nr1 = input('Introdu un numar\n')
nr2 = input('Introdu alt numar\n')

# print(type(nr1), type(nr2))
if nr1.isnumeric() and nr2.isnumeric():
    nr1 = int(nr1)
    nr2 = int(nr2)
    print(nr1 + nr2)
else:
    print("Adunarea nu a putut fi facuta")
