"""Aceasta este documentatia pentru modulul an_bisect
"""
def filtreaza_anii(*colectie):
    """filtreaza anii dupa regula anului bisect

    Returns:
        rezultat: o lista de ani..
    """
    print("tuplu:", colectie)
    rezultat = []
    for an in colectie:
        if an % 400 == 0 or (an % 4 ==0 and an % 100 !=0 ):
            rezultat.append(an)
    return rezultat
print(__name__)

if __name__ == "__main__":
    filtreaza_anii(300, 400, 500)