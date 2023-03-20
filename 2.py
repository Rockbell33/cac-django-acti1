#2. Escribir una función que calcule el mínimo común múltiplo entre dos números 

#2.a
from imp import find_module


def lcm(a, b):
    lcm = find_module(a, b)
    return (a * b) // lcm

print(lcm(120,116))

#2.b
def lcm(numbers):
    if len (numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]
    else:
        lcm_so_far = numbers[0]
        for i in range(1, len(numbers)):
            mcd = find_module(lcm_so_far, numbers[i])
            lcm_so_far = (lcm_so_far * numbers[i]) // mcd
        return lcm_so_far

