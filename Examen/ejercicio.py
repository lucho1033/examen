def calcular_promedio(lista):
    return sum(lista) / len(lista)

def main():
    numeros = []
    for i in range(10):
        numero = float(input(f"Ingrese el número {i+1}: "))
        numeros.append(numero)

    promedio = calcular_promedio(numeros)
    print("El promedio de los números ingresados es:", promedio)

if __name__ == "__main__":
    main()
