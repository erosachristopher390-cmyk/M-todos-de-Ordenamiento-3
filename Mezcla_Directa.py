"""
Ejercicio 2: MEZCLA DIRECTA (Straight Merge Sort)
Una tienda tiene una secuencia de folios de venta desordenados. Se ordenan con
mezcla directa: se reparte la secuencia en dos auxiliares (B y C) y se fusionan
tramos de longitud 1, 2, 4, 8... hasta que quede un solo tramo ordenado.
"""


def distribuir(secuencia, longitud):
    """Reparte la secuencia en B y C alternando tramos de tamaño 'longitud'."""
    b, c = [], []
    destino_b = True
    for inicio in range(0, len(secuencia), longitud):
        tramo = secuencia[inicio:inicio + longitud]
        if destino_b:
            b.extend(tramo)
        else:
            c.extend(tramo)
        destino_b = not destino_b
    return b, c


def fusionar(b, c, longitud):
    """Fusiona tramos de tamaño 'longitud' de B y C (par a par) en una sola secuencia."""
    resultado = []
    i = j = 0
    while i < len(b) or j < len(c):
        # Límites del tramo actual en cada auxiliar
        fin_b = min(i + longitud, len(b))
        fin_c = min(j + longitud, len(c))
        # Mezcla de un tramo de B con un tramo de C
        while i < fin_b and j < fin_c:
            if b[i] <= c[j]:
                resultado.append(b[i])
                i += 1
            else:
                resultado.append(c[j])
                j += 1
        # Se copia lo que sobre de cualquiera de los dos tramos
        while i < fin_b:
            resultado.append(b[i])
            i += 1
        while j < fin_c:
            resultado.append(c[j])
            j += 1
    return resultado


def mezcla_directa(secuencia, mostrar_pasos=True):
    a = list(secuencia)
    longitud = 1
    pasada = 0
    while longitud < len(a):
        b, c = distribuir(a, longitud)
        a = fusionar(b, c, longitud)
        pasada += 1
        if mostrar_pasos:
            print(f"Pasada {pasada} (tramos de {longitud}):")
            print(f"  B = {b}")
            print(f"  C = {c}")
            print(f"  A = {a}")
        longitud *= 2
    return a


if __name__ == "__main__":
    folios = [3407, 1205, 5810, 2290, 4471, 1033, 6002, 3999, 2718, 4120]
    print("Folios originales:", folios)
    print()
    ordenados = mezcla_directa(folios)
    print()
    print("Folios ordenados:", ordenados)
