
euro = 4.98
usd = 4.62

while True:
    suma = input("Introduceti suma de bani in RON\n")
    while not suma.isnumeric():
        suma = input("Introduceti suma de bani in RON\n")

    suma = int(suma)
    print("Am convertit suma")

    
    moneda = input("Care este moneda in care vrei sa convertesti? euro/usd\n")
    moneda = moneda.lower().replace(" ", "")

    # while not (moneda == "euro" or moneda == "usd"):
    # while moneda != "euro" and moneda != "usd":
    while moneda not in ("euro", "usd"):
        moneda = input("Care este moneda in care vrei sa convertesti? euro/usd\n")

    if moneda == "euro":
        print(f"Suma in euro este {round(suma/euro, 2)}")
    elif moneda == "usd":
        print(f"Suma in dolari este {round(suma/usd, 2)}")