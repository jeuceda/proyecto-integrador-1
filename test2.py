from typing import List, Tuple
import readchar
import os

def mapa_a_matriz(mapa_string: str) -> List[List[str]]:
    #separamos por filas
    filas = mapa_string.strip().split('\n')
    
    #Cada fila a lista de carcteres
    matriz = [list(fila) for fila in filas]
    
    return matriz

def limpiar_pantalla() -> None:
    os.system("clear")

def mostrar_matriz(matriz: List[List[str]]) -> None:
    for fila in matriz:
        print(" ".join(fila))

def main(mapa: List[List[str]], posicion_inicial: Tuple[int, int], posicion_final: Tuple[int, int]) -> None:
    px, py = posicion_inicial
    mapa[px][py] = 'P'

    while (px, py) != posicion_final:
        limpiar_pantalla()
        mostrar_matriz(mapa)
        tecla = readchar.readkey()

        prev_px, prev_py = px, py
        new_px, new_py = px, py

        if tecla == readchar.key.UP:
            new_px -= 1
        elif tecla == readchar.key.DOWN:
            new_px += 1
        elif tecla == readchar.key.LEFT:
            new_py -= 1
        elif tecla == readchar.key.RIGHT:
            new_py += 1

        if 0 <= new_px < len(mapa) and 0 <= new_py < len(mapa[0]) and mapa[new_px][new_py] != '#':
            mapa[px][py] = '.'
            px, py = new_px, new_py
            mapa[px][py] = 'P'
        else:
            print('posicion invalida', px, py)
    
    # Muestra el mapa con el jugador en la posición final.
    limpiar_pantalla()
    mostrar_matriz(mapa)
    print("¡Enhorabuena! Has llegado al final del laberinto.")

mapa_str = """
..#########
..#.......#
#.#.#.#####
#...#.....#
#.#####.#.#
#.#.....#.#
#.#####.###
#.#...#.#.#
#.###.#.#.#
#...#.....
#########.
"""

mapa = mapa_a_matriz(mapa_str)
print(mapa)
#main(mapa, (0, 0), (10, 9))
