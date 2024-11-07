
euro = 4.98
usd = 4.62

def conversie(suma, moneda):
    if moneda == "euro":
        return round(suma/euro, 2)
    elif moneda == "usd":
        return round(suma/usd, 2)
    return 0

while True:
    suma = input("Introduceti suma de bani in RON\n")
    while not suma.isnumeric():
        suma = input("Introduceti suma de bani in RON\n")

    suma = int(suma)
    print("Am convertit suma")

    moneda = input("Care este moneda in care vrei sa convertesti? euro/usd\n")
    moneda = moneda.lower().replace(" ", "")

    while moneda not in ("euro", "usd"):
        moneda = input("Care este moneda in care vrei sa convertesti? euro/usd\n")

    print(f"Suma in euro este {conversie(suma, moneda):}")