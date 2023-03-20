#1.Escribir una función que calcule el máximo común divisor entre dos números.

#1.a

def mcd(a,b):
    if b == 0:
        return a
    else:
        return mcd(b, a%b)

print(mcd(120,116))

#1.b

def mcd(x, y):
    if x > y:
        menor = y
    else: 
        menor = x
    for i in range (1, menor +1):
        if x % i == 0 and y % 1 ==0:
            mcd = i
        return x

print(mcd(120,116))

#1.c

def mcd (a, b):
    while b:
        a, b = b, a % b
    return a

print(mcd(120,116))
