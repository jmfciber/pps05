def esPalindromo(cadena):
    
    limpito = ''.join(c for c in cadena if c.isalnum()).lower()
    return limpito == limpito[::-1]

def main():
    
    print("Vamos a comprobar si tu frase es palíndroma")
    frase = input("Escribe tu frase: ")
    if esPalindromo(frase):
        print("Bingo es palíndromo")
    else:
        print("Lo siento no es palíndromo")

if __name__ == "__main__":
    main()
