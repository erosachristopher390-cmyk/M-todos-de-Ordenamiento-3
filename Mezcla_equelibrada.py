"""
Ejercicio 3: MEZCLA EQUILIBRADA (Balanced Merge, de N vías)
Una escuela tiene matrículas capturadas sin orden. Se ordenan con mezcla
equilibrada de 3 vías: se usan 6 secuencias (3 de entrada y 3 de salida).
Los tramos ordenados se reparten en forma equilibrada entre las 3 de entrada,
se mezclan de 3 en 3 hacia las 3 de salida, y en la siguiente pasada se
intercambian los papeles, hasta que queda un solo tramo.
"""

N = 3  # número de vías


def obtener_tramos(secuencia):
    """Separa la secuencia en tramos ascendentes (tramos naturales)."""
    tramos = []
    actual = [secuencia[0]]
    for x in secuencia[1:]:
        if x >= actual[-1]:
            actual.append(x)
        else:
            tramos.append(actual)
            actual = [x]
    tramos.append(actual)
    return tramos


def mezclar_tramos(tramos):
    """Mezcla varios tramos ordenados en uno solo, tomando siempre el menor frente."""
    posiciones = [0] * len(tramos)
    resultado = []
    while True:
        menor = None
        for k, tramo in enumerate(tramos):
            if posiciones[k] < len(tramo):
                if menor is None or tramo[posiciones[k]] < tramos[menor][posiciones[menor]]:
                    menor = k
        if menor is None:
            break
        resultado.append(tramos[menor][posiciones[menor]])
        posiciones[menor] += 1
    return resultado


def mezcla_equilibrada(secuencia):
    # Fase de distribución: los tramos se reparten por turno en las N secuencias de entrada
    entrada = [[] for _ in range(N)]
    for idx, tramo in enumerate(obtener_tramos(secuencia)):
        entrada[idx % N].append(tramo)

    print("Distribución inicial en las secuencias de entrada:")
    for k in range(N):
        print(f"  F{k + 1} = {entrada[k]}")

    pasada = 0
    # Fase de mezcla: mientras haya más de un tramo en total
    while sum(len(f) for f in entrada) > 1:
        salida = [[] for _ in range(N)]
        destino = 0
        # Se toma un tramo de cada secuencia de entrada y se mezclan en uno solo
        while any(entrada):
            grupo = [f.pop(0) for f in entrada if f]
            salida[destino % N].append(mezclar_tramos(grupo))
            destino += 1
        pasada += 1
        print(f"\nPasada {pasada}:")
        for k in range(N):
            print(f"  F{k + 1} = {salida[k]}")
        entrada = salida  # las de salida se vuelven de entrada

    # El tramo final es el resultado
    for f in entrada:
        if f:
            return f[0]


if __name__ == "__main__":
    matriculas = [2031, 1745, 3320, 1102, 2954, 4088, 1500, 3777, 2210, 1899, 4501, 1260]
    print("Matrículas originales:", matriculas)
    print()
    ordenadas = mezcla_equilibrada(matriculas)
    print()
    print("Matrículas ordenadas:", ordenadas)
