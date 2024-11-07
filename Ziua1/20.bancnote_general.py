
bancnote = [100, 50, 20, 10, 5]
suma = 2534

rezultat_dict = {
 
}

rezultat_tuplu = []  #((100, 50), (50, 0))

for nota in bancnote:
    nr_bancnote = suma // nota
    # print(f"{nr_bancnote} bancnote de {nota} lei" )

    rezultat_dict[nota] = nr_bancnote
    rezultat_tuplu.append((nota, nr_bancnote))
    suma = suma % nota

print(rezultat_dict)

# iterare prin dictionar
for i in rezultat_dict:
    print("i=", i, "valorea=", rezultat_dict[i])

for k, v in rezultat_dict.items():
    print("k=", k, "valorea=", v)

print(rezultat_tuplu)

for i in rezultat_tuplu:
    print("i=", i)
    print("k=", i[0], "valorea=", i[1])

for k, v in rezultat_tuplu:
    print("k=", k, "valorea=", v)