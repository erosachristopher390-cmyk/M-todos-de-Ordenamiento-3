"""
Ejercicio 1: INTERCALACIÓN
Dos grupos entregan su lista de alumnos ya ordenada por promedio (de menor a mayor).
Se intercalan ambas listas para obtener una sola lista general, también ordenada,
sin volver a ordenar todo desde cero.
"""


def intercalar(lista_a, lista_b):
    """Intercala dos listas ya ordenadas (por promedio) y regresa una sola ordenada."""
    resultado = []
    i = 0  # índice de lista_a
    j = 0  # índice de lista_b

    # Mientras ambas listas tengan elementos, se pasa el menor al resultado
    while i < len(lista_a) and j < len(lista_b):
        if lista_a[i][0] <= lista_b[j][0]:
            resultado.append(lista_a[i])
            i += 1
        else:
            resultado.append(lista_b[j])
            j += 1

    # Si una lista se acaba, lo que queda de la otra ya está ordenado: se copia completo
    while i < len(lista_a):
        resultado.append(lista_a[i])
        i += 1
    while j < len(lista_b):
        resultado.append(lista_b[j])
        j += 1

    return resultado


def mostrar(titulo, lista):
    print(titulo)
    for promedio, nombre in lista:
        print(f"  {promedio:5.1f}  {nombre}")
    print()


if __name__ == "__main__":
    # (promedio, nombre) - cada grupo ya viene ordenado de menor a mayor
    grupo_3sa = [(68.5, "Ana"), (75.0, "Luis"), (82.3, "Marta"), (90.1, "Pedro"), (96.0, "Sofía")]
    grupo_3sb = [(60.0, "Diego"), (72.4, "Carla"), (79.9, "Jorge"), (85.5, "Lucía")]

    mostrar("Grupo 3SA (ordenado):", grupo_3sa)
    mostrar("Grupo 3SB (ordenado):", grupo_3sb)

    general = intercalar(grupo_3sa, grupo_3sb)
    mostrar("Lista general intercalada:", general)
