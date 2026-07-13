#ARITHMETICS

def sqrt(number: int | float) -> float:
    return number ** (1/2)

def power(number, exponent):
    return number**exponent

def squared(number):
    return number**2

def tetration(a, b):
    result = 1
    for _ in range(b):
        result = a ** result

    return result

def pentation(a, b):
    result = 1
    for _ in range(b):
        result = tetration(a, result)

    return result

def hexation(a, b):
    result = 1
    for _ in range(b):
        result = pentation(a, result)

    return result
#endregion
