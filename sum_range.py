def sum_to_n(n):
    if n>0:
        caja=0
        for i in range(1,n+1):
            caja=caja+i
        return caja
    else:
        return 0


def sum_evens(n):
    """
    Retorna la suma de todos los numeros pares desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_evens(10) -> 30  (2+4+6+8+10)
    """
    if n>0:
        caja=0
        for i in range(1,(n+1)):
            if i%2==0:
                caja=caja+i
        return caja
    else:
         return 0


def factorial(n):
    resultado = 1
    for i in range(1,n+1):
        resultado = resultado * i
    return resultado
