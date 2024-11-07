# Creaţi un program în care utilizatorul va insera o sumă întreagă.
# Programul trebuie să calculeze şi să afişeze numărul corespunzător de bancnote, unde în program sunt definite bancnotele cu valorile: 10, 5, 2 şi 1

100, 50, 20, 10, 5

suma = 2534

bancnote_10 = suma // 10
print("bancnote_10:", bancnote_10)

suma = suma % 10
bancnote_5 = suma // 5

print("bancnote_5:", bancnote_5)

suma = suma % 5
bancnote_2 = suma // 2
print("bancnote_2:", bancnote_2)

suma = suma % 2
bancnote_1 = suma // 1
print("bancnote_1:", bancnote_1)
