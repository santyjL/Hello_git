from Hello_git import color_text


@color_text
def decimal_a_romano(numero : int):
    """
    resive numeros naturales y retorna su valor en romano
    """

    valores = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    simbolos = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    resultado = ''
    i = 0

    #algoritmo
    while numero > 0:
        for _ in range(numero // valores[i]):
            resultado += simbolos[i]
            numero -= valores[i]
        i += 1
    return resultado


