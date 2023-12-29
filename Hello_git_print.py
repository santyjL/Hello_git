from Hello_git import color_text, lenguaje_hacker

#colores
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BLANCO = "\033[37m"

#presenteacion

print(BLANCO)
print("este es el traductor de lenguaje hacker , funciona solo en el abecedario ingles")

while True:
    print(MAGENTA)
    print("/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|")
    print(BLANCO)

    #variables
    texto : str = input("introduce el texto a traducir : ")
    traducion , color = lenguaje_hacker(texto)

    print(MAGENTA)
    print("/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|")
    print(color)
    print("texto en lenguaje hacker :")
    print(traducion)

    print(MAGENTA)
    print("/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|")
    print(color)
    print("texto original : ")
    print(texto)

    continuar = input("seguiras utilizando el traductor del lenguaje hacker , S/N : ")

    if continuar.lower() == "s":
        continue

    else :
        print("fin del traductor hasta la proxima")
        break