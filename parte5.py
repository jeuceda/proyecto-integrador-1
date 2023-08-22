import random
import readchar
import os

class Juego:
    def __init__ (self, mapa,posicion_inicial: tuple[int, int], posicion_final: tuple[int, int]):
        self.mapa = self.mapa_a_matriz(mapa)
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final 
    
    def mapa_a_matriz(self,mapa_string):
        filas = mapa_string.strip().split('\n')
        matriz = [list(fila) for fila in filas]
        return matriz
    
    def limpiar_pantalla(self):
        os.system("clear")
    
    def mostrar_matriz(self):
        for fila in self.mapa:
            print(" ".join(fila))
    
    def jugar(self):
        px, py = self.posicion_inicial
        self.mapa[px][py] = 'P'
        
        while (px, py) != self.posicion_final:
            self.limpiar_pantalla()
            self.mostrar_matriz()
            tecla = readchar.readkey()
            
            nuevo_px, nuevo_py = px, py
            
            if tecla == readchar.key.UP:
                nuevo_px -= 1
            elif tecla == readchar.key.DOWN:
                nuevo_px += 1
            elif tecla == readchar.key.LEFT:
                nuevo_py -= 1
            elif tecla == readchar.key.RIGHT:
                nuevo_py += 1
            
            if 0 <= nuevo_px < len(self.mapa) and 0 <= nuevo_py < len(self.mapa[0]) and self.mapa[nuevo_px][nuevo_py] != '#':
                self.mapa[px][py] = '.'
                px, py = nuevo_px, nuevo_py
                self.mapa[px][py] = 'P'
            else:
                print('posicion invalida', px, py)
        self.limpiar_pantalla()
        self.mostrar_matriz()
        print('Ganaste')
        print(len(self.mapa), len(self.mapa[0]))
        print(px, py)

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        mapa_str, posicion_inicial, posicion_final = self.leer_mapa_aleatorio(path_a_mapas)
        super().__init__(mapa_str, posicion_inicial, posicion_final)
    
    def leer_mapa_aleatorio(self, path_a_mapas):
        lista_archivos = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(lista_archivos)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)
        
        with open(path_completo, 'r') as archivo:
            # Leer archivo linea por linea
            lineas = archivo.readlines()
            mapa_str = "".join(lineas[1:]).strip()
            print(mapa_str)
                        
            print(type(lineas[0]))
            
            posiciones = lineas[0].split()
            
            posicion_inicial = tuple(map(int,posiciones[0:2]))            
            print(posicion_inicial)
            
            posicion_final = tuple(map(int,posiciones[2:4]))
            print(posicion_final)
            return mapa_str, posicion_inicial, posicion_final
        
def main():
    path_a_mapas = '/Users/josiaseuceda/ADA/proyecto-integrador-1/maps'
    juego = JuegoArchivo(path_a_mapas)
    juego.jugar()

if __name__ == "__main__":
    main()



'''    
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
..###################
......#...#.......#.#
#.#####.###.#######.#
#.............#.#.#.#
###.#.#.#.###.#.#.#.#
#...#.#.#...#.......#
###.###.#.###.#####.#
#.#.#...#.#.......#.#
#.#.#.#######.#.#####
#...#.#...#.#.#.....#
###.###.#.#.#######.#
#.....#.#.........#.#
#####.#######.###.#.#
#.#...#.#.....#.#...#
#.#.###.###.###.#.###
#.....#...#...#...#.#
###.###.#########.#.#
#.#.#.#...#...#.....#
#.#.#.###.###.#.#####
#.....#.............
###################.
"""

mapa = mapa_a_matriz(mapa_str)
print(mapa)
mostrar_matriz(mapa)
#print(mapa)
main(mapa, (0, 0), (20, 19))


'''