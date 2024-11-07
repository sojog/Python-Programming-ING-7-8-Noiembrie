import math as mate

print(mate.pi)

while True:
    raza = input("Introduceti raza\n")

    # while type(raza) != float:
    while not isinstance(raza, float):
        try: ## pot sa convertesc 
            raza = float(raza)
        except:
            raza = input("Va rog introduceti raza o valoare numerica\n")

    #aria = mate.pi * mate.pow(raza, 2)
    aria = mate.pi * raza ** 2
    print(f"Aria cercului este:{aria}")