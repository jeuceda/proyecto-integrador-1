import readchar
import os

'''nombre_jugador = input('Ingresa el nombre del Jugador: ')

print('Bienvenido al juego, {}!'.format(nombre_jugador))

#Parte 2:

while True:
    keypress = readchar.readkey()
    if keypress == readchar.key.UP:
        break
    print(keypress)

# Parte 3:

def limpiar_terminal():
  import os
  import subprocess
  if os.name == 'nt':
    subprocess.call('cls')
  else:
    subprocess.call('clear')

def imprimir_numero(numero):
  print(numero)

num = 0

while num <= 50:
  limpiar_terminal()
  imprimir_numero(num)
  num += 1
  entrada = input("Pulse n para continuar: ")
  if entrada == "n":
    continue
  else:
    break
'''
#parte 4:
def mapa_a_matriz(mapa_string: str) -> list[list[str]]:
    #separamos por filas
    filas = mapa_string.strip().split('\n')
    
    #Cada fila a lista de carcteres
    matriz = [list(fila) for fila in filas]
    matriz[-1].append('#')
    matriz[-2].append('#')
    
    return matriz


def limpiar_pantalla() -> None:
    os.system("clear")

def mostrar_matriz(matriz: list[list[str]]) -> None:
    for fila in matriz:
        print(" ".join(fila))

def main(mapa: list[list[str]], posicion_inicial: tuple[int, int], posicion_final: tuple[int, int]) -> None:
    px, py = posicion_inicial
    mapa[px][py] = 'P'

    while (px, py) != posicion_final:
        limpiar_pantalla()
        mostrar_matriz(mapa)
        tecla = readchar.readkey()

        #prev_px, prev_py = px, py
        nuevo_px, nuevo_py = px, py

        if tecla == readchar.key.UP:
            nuevo_px -= 1
        elif tecla == readchar.key.DOWN:
            nuevo_px += 1
        elif tecla == readchar.key.LEFT:
            nuevo_py -= 1
        elif tecla == readchar.key.RIGHT:
            nuevo_py += 1

        if 0 <= nuevo_px < len(mapa) and 0 <= nuevo_py < len(mapa[0]) and mapa[nuevo_px][nuevo_py] != '#':
            mapa[px][py] = '.'
            px, py = nuevo_px, nuevo_py
            mapa[px][py] = 'P'
        else:
            print('posicion invalida', px, py)
    
    # Muestra el mapa con el jugador en la posición final.
    limpiar_pantalla()
    mostrar_matriz(mapa)
    print("¡Enhorabuena! Has llegado al final del laberinto.")
    print(len(mapa), len(mapa[0]))
    print(px, py)

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
mostrar_matriz(mapa)
#print(mapa)
main(mapa, (0, 0), (10, 9))


