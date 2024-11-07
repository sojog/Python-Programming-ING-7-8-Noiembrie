
def hardcodat(x):
    return x

def decorator(func):
    return hardcodat


@decorator
def putere_lui_2(x):
    return 2 ** x



print(putere_lui_2(3))