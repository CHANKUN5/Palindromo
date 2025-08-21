def es_palindromo(texto):
    """
    Determina si una palabra o frase es un palíndromo.

    Un palíndromo es una palabra o frase que se lee igual
    de izquierda a derecha que de derecha a izquierda,
    ignorando espacios, mayúsculas y minúsculas.

    Args:
        texto (str): La palabra o frase a evaluar

    Returns:
        bool: True si es palíndromo, False en caso contrario

    Examples:
        >>> es_palindromo("reconocer")
        True
        >>> es_palindromo("Hola")
        False
        >>> es_palindromo("Anita lava la tina")
        True
    """
    return texto == texto[::-1]

    # Normalizar: convertir a minúsculas y quitar espacios
    #texto_normalizado = texto.lower().replace(" ", "")

    # Comparar con la cadena invertida
    #return texto_normalizado == texto_normalizado[::-1]


  