
#decorador


def color_text(funcion):

    def modificar_funcion():

        ROJO = "\033[31m"
        VERDE = "\033[32m"
        AZUL = "\033[34m"
        MAGENTA = "\033[35m"
        CYAN = "\033[36m"
        BLANCO = "\033[37m"

        color = int(input("""en que color le gustaria el texto
                            1.ROJO
                            2.VERDE
                            3.AZUL
                            4.MAGENTA
                            5.CYAN
                            6.BLANCO
                            (eliga segun el indice) : """))



        if color == 1 :
            print(ROJO)
            return ROJO

        elif color == 2 :
            print(VERDE)
            return VERDE

        elif color == 3:
            print(AZUL)
            return AZUL

        elif color == 4:
            print(MAGENTA)
            return MAGENTA

        elif color == 5:
            print(CYAN)
            return CYAN

        elif color == 6 :
            print(BLANCO)
            return BLANCO

        else :
            print("algo salio mal")
            return

    def wrapper(*args, **kwargs):
        selected_color = modificar_funcion()  # Almacenamos el color seleccionado
        translated_text = funcion(*args, **kwargs)  # Obtenemos el texto traducido
        print(selected_color)  # Imprimimos el color seleccionado para asegurarnos de tenerlo
        return translated_text, selected_color

    return wrapper  # Devolvemos la función wrapper

#funcion para cambiar de lenguaje natural a lenguaje_hacker
@color_text
def lenguaje_hacker(texto: str) -> str:
    """
    funcion que combierte el texto natural a
    lenguaje_hacker que te permite decidir si en
    palanca_simple ; palanca_media o palanca_avanza
    """

    texto = texto.lower()


    def palanca_simple(texto):
        "cambia las vocales"
        texto_modificado = texto.replace("a", "4")
        texto_modificado = texto_modificado.replace("e", "3")
        texto_modificado = texto_modificado.replace("i", "1")
        texto_modificado = texto_modificado.replace("o", "0")
        texto_modificado = texto_modificado.replace("u", "(_)")
        return texto_modificado


    def palanca_media(texto):
        nuevo_texto = palanca_simple(texto)

        texto_modificado = nuevo_texto.replace("s", "5")
        texto_modificado = texto_modificado.replace("b", "8")
        texto_modificado = texto_modificado.replace("g", "9")
        texto_modificado = texto_modificado.replace("c", "[")
        texto_modificado = texto_modificado.replace("d", "[)")
        texto_modificado = texto_modificado.replace("f", "/=")
        texto_modificado = texto_modificado.replace("h", "#")
        texto_modificado = texto_modificado.replace("j", "._]")
        texto_modificado = texto_modificado.replace("k", "|<")
        texto_modificado = texto_modificado.replace("l", "|_")

        return texto_modificado


    def palanca_avanza(texto):
        nuevo_texto = palanca_media(texto)

        texto_modificado = nuevo_texto.replace("m", "|\/|")
        texto_modificado = texto_modificado.replace("n", "И")
        texto_modificado = texto_modificado.replace("o", "Ø")
        texto_modificado = texto_modificado.replace("p", "|*")
        texto_modificado = texto_modificado.replace("q", "()_")
        texto_modificado = texto_modificado.replace("r", "Я")
        texto_modificado = texto_modificado.replace("t", "†")
        texto_modificado = texto_modificado.replace("v", "\/")
        texto_modificado = texto_modificado.replace("w", "(n)")
        texto_modificado = texto_modificado.replace("x", "}{")
        texto_modificado = texto_modificado.replace("y", "Ч")
        texto_modificado = texto_modificado.replace("z", "2")

        return texto_modificado



    opciones : str = input("vas a usar la palanca basica , media o avanzada : ")

    if opciones.lower() == "basica":
        texto_modificado = palanca_simple(texto)

    elif opciones.lower() == "media":
        texto_modificado = palanca_media(texto)

    elif opciones.lower() == "avanzada":
        texto_modificado = palanca_avanza(texto)


    return texto_modificado