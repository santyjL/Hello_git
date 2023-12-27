texto : str = input("introduzca el texto : ")

def lenguaje_hacker(texto: str) -> str:
    texto_modificado = texto.lower()
    texto_modificado = texto_modificado.replace("a", "4")
    texto_modificado = texto_modificado.replace("e", "3")
    texto_modificado = texto_modificado.replace("i", "1")
    texto_modificado = texto_modificado.replace("o", "0")
    texto_modificado = texto_modificado.replace("u", "(_)")

    return texto_modificado

print(lenguaje_hacker(texto))