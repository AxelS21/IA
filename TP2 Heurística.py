import heapq

# Definimos la posición inicial "B"
posicion_inicial = 0

# Definimos el rango de búsqueda en la horizontal H
rango_busqueda = (-5, 5)

# Función heurística que estima la distancia desde una posición hasta la solución "A"
def heuristica(posicion):
    # Aquí iría la lógica para calcular una estimación heurística de la distancia
    # Ahora la solución es 4
    return abs(posicion - 4)

# Función para realizar la búsqueda A*
def busqueda_a_estrella():
    # Inicializamos una cola de prioridad para almacenar los nodos a explorar
    cola_prioridad = [(0, posicion_inicial)]  # (f(n), posicion)
    costo_acumulado = {posicion_inicial: 0}  # Costo acumulado desde el inicio hasta cada posición
    explorados = []  # Registro de posiciones exploradas

    while cola_prioridad:
        _, posicion_actual = heapq.heappop(cola_prioridad)
        explorados.append(posicion_actual)

        # Verificamos si encontramos la posición de montaje "A"
        if es_solucion(posicion_actual):
            # Mostramos el paso a paso de la búsqueda
            print("Paso a paso de la búsqueda A*:")
            for posicion in explorados:
                print(f"Posición explorada: {posicion}")
            return posicion_actual, costo_acumulado[posicion_actual]

        # Exploramos los nodos vecinos (posiciones adyacentes)
        for nueva_posicion in [posicion_actual - 1, posicion_actual + 1]:
            if rango_busqueda[0] <= nueva_posicion <= rango_busqueda[1]:
                nuevo_costo = costo_acumulado[posicion_actual] + 1  # Asumimos un costo unitario por movimiento
                if nueva_posicion not in costo_acumulado or nuevo_costo < costo_acumulado[nueva_posicion]:
                    costo_acumulado[nueva_posicion] = nuevo_costo
                    prioridad = nuevo_costo + heuristica(nueva_posicion)
                    heapq.heappush(cola_prioridad, (prioridad, nueva_posicion))

    # Si no se encontró la solución, retornamos None
    return None, None

# Función para verificar si una posición es la solución
def es_solucion(posicion):
    # Aquí iría la lógica para determinar si la posición es la solución "A"
    # Ahora la solución es 4
    return abs(posicion - 4) < 0.1  # Consideramos una tolerancia de 0.1

# Ejecutamos la búsqueda A*
solucion, costo = busqueda_a_estrella()

if solucion is not None:
    print(f"\nLa posición de montaje 'A' es: {solucion}, encontrada con un costo acumulado de {costo}")
else:
    print("No se encontró la solución 'A' dentro del rango de búsqueda")