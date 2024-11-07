"""
Construiti clasa Account(cont bancar) care sa abstractizeze un cont bancar
Clasa deţine următoarele implementari cu verificarile necesare:
widthdraw(scoateBani) - se scot bani din portofel
add_money(adaugaBani)  - se adaga bani in portofel
show_balance(arataBalanta) - se printeaza balanta curenta

"""

class Account:
    
    def __init__(self, value = 0):
        # fara _ - atribut public
        # cu 1 _ - atribut intern/protected
        # cu 2 __ - atribut private 
        self.__balance = value

    @property
    def balance(self):
        return self.__balance

    # str(obiect)
    def __str__(self):
        return f"Contul are {self.__balance} lei"
    
    # int(obiect)
    def __int__(self):
        return self.__balance
    

    def add_money(self, value):
        self.__balance += value

    def widthdraw(self, value):
        if value <= self.__balance:
            self.__balance -= value

    def show_balance(self):
        print(self)



cont1 = Account(0)
print(cont1)
cont1.show_balance()

cont2 = Account(100)
print(cont2)
cont2.show_balance()
cont2.add_money(200)
cont2.show_balance()

cont2.widthdraw(50)
cont2.show_balance()

cont2.widthdraw(150)
cont2.show_balance()

cont2.widthdraw(250)
cont2.show_balance()

## name mangling
cont2._Account__balance = 456

valoare = int(cont2)
print("Valoare convertita la int", valoare)

print("Valorea cu getter este:", cont2.balance)