# M-todos-de-Ordenamiento-3

Tres ejercicios en Python que aplican métodos de ordenamiento por intercalación y mezcla: **Intercalación**, **Mezcla Directa** y **Mezcla Equilibrada**. Cada programa resuelve un problema distinto y muestra paso a paso cómo se van combinando las secuencias hasta obtener el resultado ordenado.

Trabajo de la materia de **Estructura de datos**, grupo 3SA, Ingeniería en Sistemas Computacionales, Instituto Tecnológico de Mérida (TecNM).

## Contenido

| Archivo | Método | Ejercicio |
| --- | --- | --- |
| [`Intercalacion.py`](Intercalacion.py) | Intercalación | Combina las listas de alumnos de dos grupos, ya ordenadas por promedio, en una sola lista general |
| [`Mezcla_Directa.py`](Mezcla_Directa.py) | Mezcla Directa | Ordena 10 folios de venta desordenados con tramos de longitud 1, 2, 4 y 8 |
| [`Mezcla_equelibrada.py`](Mezcla_equelibrada.py) | Mezcla Equilibrada | Ordena 12 matrículas con 3 vías (6 secuencias) |

## Requisitos

- Python 3.8 o superior
- No requiere instalar librerías externas

## Cómo ejecutarlos

Desde la carpeta del repositorio:

```bash
python Intercalacion.py
python Mezcla_Directa.py
python Mezcla_equelibrada.py
```

En algunos sistemas el comando es `python3` en lugar de `python`.

## Descripción de cada método

### 1. Intercalación

Recibe dos listas que **ya están ordenadas** y produce una sola lista ordenada. Usa un índice por lista: en cada paso compara los elementos apuntados, pasa el menor al resultado y avanza ese índice. Cuando una lista se termina, copia lo que queda de la otra.

- Complejidad: O(n + m), cada lista se recorre una sola vez.

### 2. Mezcla Directa

Ordena una secuencia desordenada en varias pasadas. En cada una, la secuencia **A** se reparte en dos auxiliares **B** y **C** alternando tramos de longitud fija, y luego se fusiona un tramo de B con uno de C de vuelta en A. La longitud del tramo empieza en 1 y se duplica en cada pasada, hasta que un solo tramo cubre toda la secuencia.

- Complejidad: O(n log n).
- Es estable y sirve para datos que no caben en memoria.

### 3. Mezcla Equilibrada

Parecida a la mezcla directa, pero de **N vías** (aquí N = 3). Se detectan los tramos ascendentes que ya existen en los datos y se reparten por turno entre 3 secuencias de entrada. En cada pasada se toma un tramo de cada una, se mezclan en uno solo y se escriben en las 3 secuencias de salida; después las de salida pasan a ser de entrada. Se repite hasta que queda un solo tramo.

- Al mezclar N tramos a la vez, se hacen menos pasadas que con 2 vías (en el ejemplo, 2 pasadas en lugar de 3).

## Salida de ejemplo

<details>
<summary>Intercalación</summary>

```text
Grupo 3SA (ordenado):
   68.5  Ana
   75.0  Luis
   82.3  Marta
   90.1  Pedro
   96.0  Sofía

Grupo 3SB (ordenado):
   60.0  Diego
   72.4  Carla
   79.9  Jorge
   85.5  Lucía

Lista general intercalada:
   60.0  Diego
   68.5  Ana
   72.4  Carla
   75.0  Luis
   79.9  Jorge
   82.3  Marta
   85.5  Lucía
   90.1  Pedro
   96.0  Sofía
```

</details>

<details>
<summary>Mezcla Directa</summary>

```text
Folios originales: [3407, 1205, 5810, 2290, 4471, 1033, 6002, 3999, 2718, 4120]

Pasada 1 (tramos de 1):
  B = [3407, 5810, 4471, 6002, 2718]
  C = [1205, 2290, 1033, 3999, 4120]
  A = [1205, 3407, 2290, 5810, 1033, 4471, 3999, 6002, 2718, 4120]
Pasada 2 (tramos de 2):
  B = [1205, 3407, 1033, 4471, 2718, 4120]
  C = [2290, 5810, 3999, 6002]
  A = [1205, 2290, 3407, 5810, 1033, 3999, 4471, 6002, 2718, 4120]
Pasada 3 (tramos de 4):
  B = [1205, 2290, 3407, 5810, 2718, 4120]
  C = [1033, 3999, 4471, 6002]
  A = [1033, 1205, 2290, 3407, 3999, 4471, 5810, 6002, 2718, 4120]
Pasada 4 (tramos de 8):
  B = [1033, 1205, 2290, 3407, 3999, 4471, 5810, 6002]
  C = [2718, 4120]
  A = [1033, 1205, 2290, 2718, 3407, 3999, 4120, 4471, 5810, 6002]

Folios ordenados: [1033, 1205, 2290, 2718, 3407, 3999, 4120, 4471, 5810, 6002]
```

</details>

<details>
<summary>Mezcla Equilibrada</summary>

```text
Matrículas originales: [2031, 1745, 3320, 1102, 2954, 4088, 1500, 3777, 2210, 1899, 4501, 1260]

Distribución inicial en las secuencias de entrada:
  F1 = [[2031], [1500, 3777], [1260]]
  F2 = [[1745, 3320], [2210]]
  F3 = [[1102, 2954, 4088], [1899, 4501]]

Pasada 1:
  F1 = [[1102, 1745, 2031, 2954, 3320, 4088]]
  F2 = [[1500, 1899, 2210, 3777, 4501]]
  F3 = [[1260]]

Pasada 2:
  F1 = [[1102, 1260, 1500, 1745, 1899, 2031, 2210, 2954, 3320, 3777, 4088, 4501]]
  F2 = []
  F3 = []

Matrículas ordenadas: [1102, 1260, 1500, 1745, 1899, 2031, 2210, 2954, 3320, 3777, 4088, 4501]
```

</details>

## Autor

Arévalo Erosa Christopher Abraham
Ingeniería en Sistemas Computacionales, Instituto Tecnológico de Mérida
