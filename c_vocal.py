palabra = "buenos días a todos".strip().lower()


def contar_vocales(i):

    vocales = "aeiou"

    contador_vocales = 0

    for letra in i:
        if letra in vocales:
            contador_vocales += 1

    print(f"En su palabra hay {contador_vocales} vocales")


contar_vocales(palabra)

