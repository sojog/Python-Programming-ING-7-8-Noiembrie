import time
import math


def time_dec(func):

    def inner_func(x):
        start_time = time.time()

        rezultat = func(x)
        
        stop_time = time.time()
        print(f"Functia {func.__name__} a fost executata in {stop_time - start_time}")
        
        return rezultat
    
    return inner_func


@time_dec
def putere_lui_2(x):
    return 2 ** x

@time_dec
def radical_din(x):
    return math.sqrt(x)

print(putere_lui_2(3))

print(radical_din(9))