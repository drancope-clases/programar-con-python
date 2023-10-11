# FUNCIONES
def tabla_multiplicar(numA):
    for i in range(1, 11):
        print(i, " por ", numA, " = ", i*numA)

def factorial(num):
    if (num < 2):
        return num * 1
    else:
        return num * factorial(num-1)
