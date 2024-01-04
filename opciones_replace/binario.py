from Hello_git import color_text


@color_text
def numero_a_binario(numero):
    if isinstance(numero, int):
        return bin(numero)[2:]  # Convierte el número a binario y quita el prefijo '0b'
