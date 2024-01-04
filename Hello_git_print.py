import os
import time

from Hello_git import color_text, lenguaje_hacker
from opciones_replace import binario, morse, numeros_romanos, reverso

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
        os.system("cls")
        print(MAGENTA)
        print("/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|")
        time.sleep(0.2)


        print(self.color)
        print(f"valor introducido en el lenguaje : {self.nombre}:")
        time.sleep(0.2)
        print(self.traducion)
        time.sleep(0.2)


        print(MAGENTA)
        print("/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|")
        time.sleep(0.2)
        print(self.color)
        print("texto original : ")
        time.sleep(0.2)
        print(self.original)


        input("precione enter para seguir : ")
        os.system("cls")


#presenteacion

print(BLANCO)
print("este es un traductor de varios lenguajes un poco raros --vercion Beta_0.3")

while True:

    print(MAGENTA)
    print("/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|")
    print(BLANCO)


    print("""
          Que lenguaje va a utilizar ?
                1.lenguaje_hacker (Leet)
                2.reverso
                3.decimal_a_romano
                4.codigo_morse
                5.binario
        """)

    try:

        lenguaje = int(input("introduce el lenguaje a utilizar segun el indice : "))

    except ValueError as error :

        print(MAGENTA)
        print("/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|")

        print(BLANCO)
        print("recalco que del indice , osea un numero no un texto u otra cosa , error optenido : " , error)
        input("precione enter para continuar : ")
        os.system("cls")
        continue


    os.system("cls")
    time.sleep(0.2)


    if (lenguaje == 1 or
        lenguaje == 2 or
        lenguaje == 4 ):

        texto : str = input("introduce el texto a traducir : ")
        os.system("cls")
        time.sleep(0.2)

        if lenguaje == 1:
            try:
                traducion , color = lenguaje_hacker(texto)
                llamado = LenguajeElegido("lenguaje_hacker" , color , traducion , texto)
                llamado.presenteacion()
            except:
                print("es enserio , todo iba tan bien y tu la cagas ")
                input("precione enter para continuar : ")
                time.sleep(0.2)
                os.system("cls")
                continue


        elif lenguaje == 2:

            traducion , color = reverso.texto_reverso(texto)
            llamado = LenguajeElegido("reverso" , color , traducion , texto)
            llamado.presenteacion()


        elif lenguaje == 4:

            traducion , color = morse.codigo_morse(texto)
            llamado = LenguajeElegido("morse" , color , traducion , texto)
            llamado.presenteacion()


    elif (lenguaje == 3 or
          lenguaje == 5):

        try:

            numero = int(input("introduce el numero a combertir : "))

        except ValueError as error:

            print(MAGENTA)
            print("/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|")

            print(BLANCO)
            print("en este caso estas trabajando con combersores numericos , entoces se te pide un numero , error : " , error)
            input("precione enter para continuar : ")
            time.sleep(0.2)
            os.system("cls")
            continue

        os.system("cls")
        time.sleep(0.2)


        if lenguaje == 3 :
            combercion , color = numeros_romanos.decimal_a_romano(numero)
            llamado = LenguajeElegido("natural a romano" ,color , combercion , numero)
            llamado.presenteacion()


        elif lenguaje == 5 :
            combercion , color = binario.numero_a_binario(numero)
            llamado = LenguajeElegido("binario" ,color , combercion , numero)
            llamado.presenteacion()


    else :

        os.system("cls")
        time.sleep(0.2)
        print("esa no es una opcion a elegir")
        input("precione enter para continuar : ")


    print(MAGENTA)
    print("/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|/|-\|\n")

    print(color)
    seguir =  input("va a seguir usando el traductor , yes/no : ")


    if seguir.lower() == "yes":
        continue

    else :
        break

