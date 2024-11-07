
def functie(*args, **kargs):
    print("args=", args, type(args))
    print("kargs=", kargs, type(kargs))
    print("Functia este apelata")

# functie()
# functie(2)
# functie(2, 3)
functie(2, 4, 5, 6, cheie="alb", cheie2="rosu")

print("alb", "rosu", "verde", "albastru", sep="--", end='^^^^')
print("alb", "rosu", "verde", "albastru", sep="--")