

def functie(x):
    return x ** 2

patrat_x = functie(10)
print(patrat_x)

patrat_x = functie(20)
print(patrat_x)



def generare_nre_pare(lista):
    return [nr for nr in lista if nr %  2 == 0]

print(generare_nre_pare([2,11, 23, 3, 553, 32, 30, 10, 30, 20]))