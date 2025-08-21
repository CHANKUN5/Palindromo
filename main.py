
from palindromo import es_palindromo

def main():
    print("🔍 DETECTOR DE PALÍNDROMOS")
    print("=" * 40)

    # Casos de prueba para demostración
    casos_prueba = [
        "reconocer",
        "Hola",
        "Anita lava la tina",
        "A man a plan a canal Panama",
        "racecar",
        "python",
        "Somos o no somos"
    ]

    for caso in casos_prueba:
        resultado = es_palindromo(caso)
        estado = "✅ SÍ" if resultado else "❌ NO"
        print(f"'{caso}' -> {estado} es palíndromo")

    print("\n" + "=" * 40)
    print("🎯 MODO INTERACTIVO")
    print("Ingresa salir para terminar:")

    while True:
        entrada = input("\n> ")

        if entrada.lower() == 'salir':
            print("¡Hasta luego! 👋")
            break

        if entrada.strip():
            resultado = es_palindromo(entrada)
            estado = "✅ SÍ" if resultado else "❌ NO"
            print(f"'{entrada}' -> {estado} es palíndromo")
        else:
            print("Por favor, ingresa una palabra o frase válida.")


if __name__ == "__main__":
    main()