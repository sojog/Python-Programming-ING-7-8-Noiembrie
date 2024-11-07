
numere = [2,11, 23, 3, 553, 32, 30, 10, 30, 20]

pare = []
impare = []

for nr in numere:
    print(f"Numarul {nr} este par { nr %  2 ==0}")
    if nr %  2 ==0:
        pare.append(nr)
    else:
        impare.append(nr)

print("Numere pare sunt", pare)
print("Numere impare sunt", impare)


# List comprehention
pare = [nr for nr in numere if nr %  2 == 0]
impare = [nr  for nr in numere if nr %  2 == 1]
print("Numere pare sunt", pare)
print("Numere impare sunt", impare)

