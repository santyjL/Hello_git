from Hello_git import color_text, lenguaje_hacker
from opciones_replace import numeros_romanos, reverso

#colores
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BLANCO = "\033[37m"

#clase
class LenguajeElegido:
    def __init__(self , nombre : str , color : None , traducion : str , original) :
        self.nombre = nombre
        self.color = color
        self.traducion = traducion
        self.original = original

    def presenteacion(self):
        print(MAGENTA)
        print("/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|")

        print(self.color)
        print(f"valor introducido en el lenguaje : {self.nombre}:")
        print(self.traducion)

        print(MAGENTA)
        print("/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|")
        print(self.color)
        print("texto original : ")
        print(self.original)


#presenteacion

print(BLANCO)
print("este es un traductor de varios lenguajes un poco raros --vercion Beta_0.3")

while True:
    print(MAGENTA)
    print("/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|")
    print(BLANCO)

    print("""Que lenguaje va a utilizar ?
                1.lenguaje_hacker (Leet)
                2.reverso
                3.decimal_a_romano""")

    lenguaje = int(input("introduce el lenguaje a utilizar segun el indice : "))

    if lenguaje == 1 or lenguaje == 2:
        texto : str = input("introduce el texto a traducir : ")

        if lenguaje == 1:
            traducion , color = lenguaje_hacker(texto)
            llamado = LenguajeElegido("lenguaje_hacker" , color , traducion , texto)
            llamado.presenteacion()

        elif lenguaje == 2:
            traducion , color = reverso.texto_reverso(texto)
            llamado = LenguajeElegido("reverso" , color , traducion , texto)
            llamado.presenteacion()

    elif lenguaje == 3:
        numero = int(input("introduce el numero a combertir : "))

        combercion , color = numeros_romanos.decimal_a_romano(numero)
        llamado = LenguajeElegido("natural a romano" ,color , combercion , numero)
        llamado.presenteacion()

    else :
        print("esa no es una opcion a elegir")

    seguir =  input("va a seguir usando el traductor , yes/no : ")

    if seguir.lower() == "yes":
        continue

    else :
        break