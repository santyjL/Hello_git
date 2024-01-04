from Hello_git import color_text


@color_text
def codigo_morse(texto: str) -> str:
    "combierte el texto natural a codigo morse"

    texto = texto.lower()

    texto_modificado = texto.replace(" ", "/ ")

    def caracteres(texto):

        #vocales
        texto_modificado = texto.replace("a", ".- ")
        texto_modificado = texto_modificado.replace("e", ". ")
        texto_modificado = texto_modificado.replace("i", ".. ")
        texto_modificado = texto_modificado.replace("o", "--- ")
        texto_modificado = texto_modificado.replace("u", "..- ")

        #cosonantes
        texto_modificado = texto_modificado.replace("b", "-... ")
        texto_modificado = texto_modificado.replace("c", "-.-. ")
        texto_modificado = texto_modificado.replace("d", "-.. ")
        texto_modificado = texto_modificado.replace("f", "..-. ")
        texto_modificado = texto_modificado.replace("g", "--. ")
        texto_modificado = texto_modificado.replace("h", ".... ")
        texto_modificado = texto_modificado.replace("j", ".--- ")
        texto_modificado = texto_modificado.replace("k", "-.- ")
        texto_modificado = texto_modificado.replace("l", ".-.. ")
        texto_modificado = texto_modificado.replace("m", "-- ")
        texto_modificado = texto_modificado.replace("n", "-. ")
        texto_modificado = texto_modificado.replace("p", ".--. ")
        texto_modificado = texto_modificado.replace("q", "--.- ")
        texto_modificado = texto_modificado.replace("r", ".-. ")
        texto_modificado = texto_modificado.replace("s", "... ")
        texto_modificado = texto_modificado.replace("t", "- ")
        texto_modificado = texto_modificado.replace("v", "...- ")
        texto_modificado = texto_modificado.replace("w", ".-- ")
        texto_modificado = texto_modificado.replace("x", "-..- ")
        texto_modificado = texto_modificado.replace("y", "-.-- ")
        texto_modificado = texto_modificado.replace("z", "--.. ")

        #numero
        texto_modificado = texto_modificado.replace("1", ".---- ")
        texto_modificado = texto_modificado.replace("2", "..--- ")
        texto_modificado = texto_modificado.replace("3", "...-- ")
        texto_modificado = texto_modificado.replace("4", "....- ")
        texto_modificado = texto_modificado.replace("5", "..... ")
        texto_modificado = texto_modificado.replace("6", "-.... ")
        texto_modificado = texto_modificado.replace("7", "--... ")
        texto_modificado = texto_modificado.replace("8", "---.. ")
        texto_modificado = texto_modificado.replace("9", "----. ")
        texto_modificado = texto_modificado.replace("0", "----- ")

        return texto_modificado

    texto_modificadoo = caracteres(texto_modificado)

    return texto_modificadoo
