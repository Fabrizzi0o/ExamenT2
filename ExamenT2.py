import random

# 1. Crear matriz NxN
def crear_matriz(n):
    return [[random.randint(99, 999) for _ in range(n)] for _ in range(n)]

# 2. Mostrar matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento}", end="\t")
        print()

# 3. Divide y vencerás para contar múltiplos en una lista
def contar_en_lista(lista, inicio, fin):
    if inicio == fin:
        if lista[inicio] % 5 == 0 or lista[inicio] % 7 == 0:
            return 1
        else:
            return 0
    
    medio = (inicio + fin) // 2
    
    izquierda = contar_en_lista(lista, inicio, medio)
    derecha = contar_en_lista(lista, medio + 1, fin)
    
    return izquierda + derecha

# 4. Divide y vencerás para la matriz
def contar_matriz(matriz, inicio, fin):
    if inicio == fin:
        return contar_en_lista(matriz[inicio], 0, len(matriz[inicio]) - 1)
    
    medio = (inicio + fin) // 2
    
    arriba = contar_matriz(matriz, inicio, medio)
    abajo = contar_matriz(matriz, medio + 1, fin)
    
    return arriba + abajo

# PROGRAMA PRINCIPAL
n = int(input("Ingrese el tamaño de la matriz NxN: "))

matriz = crear_matriz(n)

print("\nMatriz generada:\n")
mostrar_matriz(matriz)

cantidad = contar_matriz(matriz, 0, n - 1)

print(f"\nCantidad de múltiplos de 5 o 7: {cantidad}")