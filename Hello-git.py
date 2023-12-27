texto : str = input("introduzca el texto")

def lenguaje_hacker (texto : str):
    caracteres : list = texto.split(None)
    text : str = ""

    for i in range(len(caracteres)):

        if caracteres[i].lower() == "a":
            text += "4"

        elif caracteres[i].lower() == "e":
            text += "3"

        elif caracteres[i].lower() == "i":
            text += "1"

        elif caracteres[i].lower() == "o":
            text += "0"

        elif caracteres[i].lower() == "u":
            text += "(_)"

        else :
            text += caracteres[i]

    print(text)


lenguaje_hacker(texto)