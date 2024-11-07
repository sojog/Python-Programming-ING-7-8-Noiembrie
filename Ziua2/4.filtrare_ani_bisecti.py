

def filtreaza_anii(*colectie):
    print("tuplu:", colectie)
    rezultat = []
    for an in colectie:
        if an % 400 == 0 or (an % 4 ==0 and an % 100 !=0 ):
            rezultat.append(an)
    return rezultat


print(filtreaza_anii(2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024))

print(filtreaza_anii(2000, 2023, 2033))
print("Nu am o valoare:", filtreaza_anii())


print(2000, 2001, 2002)
print([2000, 2001, 2002])