texto : str = input("introduzca el texto : ") #se introduce el texto en lenguaje natural

#funcion para cambiar de lenguaje natural a lenguaje_hacker
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
        texto_modificado = texto.replace("e", "3")
        texto_modificado = texto.replace("i", "1")
        texto_modificado = texto.replace("o", "0")
        texto_modificado = texto.replace("u", "(_)")

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