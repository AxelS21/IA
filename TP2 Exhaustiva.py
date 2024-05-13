from collections import deque

# Definimos la posición inicial "B"
posicion_inicial = 0

# Definimos el rango de búsqueda en la horizontal H
rango_busqueda = (-5, 5)

# Función para realizar la búsqueda exhaustiva en anchura
def busqueda_en_anchura():
    # Creamos una cola para almacenar los nodos a explorar
    cola = deque([(posicion_inicial, 0)])  # (posicion, nivel)
    explorados = [(posicion_inicial, 0)]  # Registro de posiciones exploradas

    while cola:
        posicion_actual, nivel = cola.popleft()

        # Verificamos si encontramos la posición de montaje "A"
        if es_solucion(posicion_actual):
            # Mostramos el paso a paso de la búsqueda
            print("Paso a paso de la búsqueda en anchura:")
            for posicion, nivel in explorados:
                print(f"Nivel {nivel}: Posición {posicion}")
            return posicion_actual, nivel

        # Exploramos los nodos vecinos (posiciones adyacentes)
        for nueva_posicion in [posicion_actual - 1, posicion_actual + 1]:
            if rango_busqueda[0] <= nueva_posicion <= rango_busqueda[1] and (nueva_posicion, nivel + 1) not in explorados:
                cola.append((nueva_posicion, nivel + 1))
                explorados.append((nueva_posicion, nivel + 1))

    # Si no se encontró la solución, retornamos None
    return None, None

# Función para verificar si una posición es la solución
def es_solucion(posicion):
    # Aquí iría la lógica para determinar si la posición es la solución "A"
    # Por simplicidad, supongamos que la solución es -5
    return abs(posicion - (-5)) < 0.1  # Consideramos una tolerancia de 0.1

# Ejecutamos la búsqueda en anchura
solucion, nivel = busqueda_en_anchura()

if solucion is not None:
    print(f"\nLa posición de montaje 'A' es: {solucion}, encontrada en el nivel {nivel}")
else:
    print("No se encontró la solución 'A' dentro del rango de búsqueda")