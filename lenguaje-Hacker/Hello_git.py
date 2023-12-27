texto : str = input("introduzca el texto : ")

def lenguaje_hacker(texto: str) -> str:

    texto_modificado = texto.lower()

    def palanca_simple(texto_modificado):

        texto_modificado = texto_modificado.replace("a", "4")
        texto_modificado = texto_modificado.replace("e", "3")
        texto_modificado = texto_modificado.replace("i", "1")
        texto_modificado = texto_modificado.replace("o", "0")
        texto_modificado = texto_modificado.replace("u", "(_)")

        return texto_modificado

    def palanca_media(texto):

        nuevo_texto = palanca_simple(texto)

        texto_modificado = nuevo_texto.replace("s", "5")
        texto_modificado = nuevo_texto.replace("b", "8")
        texto_modificado = nuevo_texto.replace("g", "9")
        texto_modificado = nuevo_texto.replace("c" , "[")
        texto_modificado = nuevo_texto.replace("d", "[)")
        texto_modificado = nuevo_texto.replace("f", "/=")
        texto_modificado = nuevo_texto.replace("h", "#")
        texto_modificado = nuevo_texto.replace("j" , "._]")
        texto_modificado = nuevo_texto.replace("k", "|<")
        texto_modificado = nuevo_texto.replace("l" , "|_")

        return texto_modificado

    texto_modificado = palanca_media(texto_modificado)
    return texto_modificado

print(lenguaje_hacker(texto))