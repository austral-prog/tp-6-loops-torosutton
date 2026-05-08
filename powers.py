def power(base, exp):
    resultado = 1
    for i in range(exp):
         resultado = resultado * base
    return resultado




def sum_of_powers(base, max_exp):
    """
    Retorna la suma de base^0 + base^1 + ... + base^max_exp.
    Debe USAR la funcion power.

    Ejemplo: sum_of_powers(2, 3) -> 15  (1+2+4+8)
    """
    resultado =0
    for i in range(max_exp + 1):
        resultado = resultado+power(base,i)

    return resultado
