import os
import random
#import juego

acorazado = 0
submarino = 0
destructor = 0
fragata = 0
portavion = 0
naves_hundidas = 0


acorazado2 = 0
submarino2 = 0
destructor2 = 0
fragata2 = 0
portavion2 = 0
naves_hundidas2 = 0



def imprimir_tabla(matriz):
    print("   " + "   ".join([str(i+1) for i in range(10)]))  # Encabezado de columnas
    print("-----------------------------------------")
    for i in range(10):
        print(f"{i+1} | " + " | ".join(matriz[i]) + " |")
        print("-----------------------------------------")
    return matriz




def nave(matriz, fila, columna, direccion,barco,size):
    while matriz[fila][columna] != " ":
        os.system('cls')
        print("No se puede colocar el barco en esa posicion,espacio ocupado\n")
        fila = int(input("Ingrese la fila donde desea colocar el barco: "))-1
        columna = int(input("Ingrese la columna donde desea colocar el barco: "))-1
        direccion = input("Ingrese la direccion del barco (H/V): ").upper()
    
    if direccion == "H":
        orientacion = input("Ingrese la orientacion del barco (I/D): ").upper()
        
        while (orientacion == "I" and  fila ==0) or (orientacion == "D" and fila == 9):
            os.system('cls')
            print("No se puede colocar el barco en esa posicion")
            orientacion = input("Ingrese la orientacion del barco (I/D): ").upper()
                   
        if orientacion == "I":
        
            if columna + size >= 10:
                print("No se puede colocar el barco en esa posicion")
                return False
            else:
                for i in range(size):
                    matriz[fila][columna + i] = barco
        elif orientacion == "D":
            if columna - size < 0:
                print("No se puede colocar el barco en esa posicion")
                return False
            else:
                for i in range(size):   
                    matriz[fila][columna - i] = barco
    elif direccion == "V":
        
        if (fila + size) >= 10:
            print("No se puede colocar el barco en esa posicion")
            return
        else:
            for _ in range(size):
                matriz[fila + _][columna] = barco
        if fila - size < 0:
            print("No se puede colocar el barco en esa posicion")
            return
        else:
            for i in range(size):
                matriz[fila - i][columna] = barco
    return matriz


def nave_enemy(matriz, fila, columna, direccion,barco,size):
    while matriz[fila][columna] != " ":
        
        os.system('cls')
        fila=random.randint(0,9)
        columna=random.randint(0,9)
        direccion=random.choice(["H","V"])
            
    if direccion == "H":
        
        orientacion=random.choice(["I","D"])    
        while (orientacion == "I" and  fila ==0) or (orientacion == "D" and fila == 9):
            os.system('cls')
            orientacion=random.choice(["I","D"])              
        if orientacion == "I":
        
            if columna + size >= 10:
                print("No se puede colocar el barco en esa posicion")
                return False
            else:
                for i in range(size):
                    matriz[fila][columna + i] = barco
        elif orientacion == "D":
            if columna - size < 0:
                print("No se puede colocar el barco en esa posicion")
                return False
            else:
                for i in range(size):   
                    matriz[fila][columna - i] = barco
    elif direccion == "V":
        
        if (fila + size) >= 10:
            print("No se puede colocar el barco en esa posicion")
            return
        else:
            for _ in range(size):
                matriz[fila + _][columna] = barco
        if fila - size < 0:
            print("No se puede colocar el barco en esa posicion")
            return
        else:
            for i in range(size):
                matriz[fila - i][columna] = barco
    return matriz



    
def generate_enemy(matriz):
    
    fila=random.randint(0,9)
    columna=random.randint(0,9)
    direccion=random.choice(["H","V"])
    
    nave(matriz, fila, columna, direccion, "P",4)
    
    for _ in range(3):
        barco = random.choice(["A","S"])
        fila=random.randint(0,9)
        columna=random.randint(0,9)
        direccion=random.choice(["H","V"])
        nave_enemy(matriz, fila, columna, direccion, barco,3)
    
    for _ in range(3):
        fila=random.randint(0,9)
        columna=random.randint(0,9)
        direccion=random.choice(["H","V"])
        nave_enemy(matriz, fila, columna, direccion, "D",2)
    
    for _ in range(2):
        fila=random.randint(0,9)
        columna=random.randint(0,9)
        direccion=random.choice(["H","V"])
        nave_enemy(matriz, fila, columna, direccion, "F",1)
    return matriz


def turno(matriz, horizontal, vertical):
    global acorazado, submarino, destructor, fragata, portavion, naves_hundidas

    if matriz[horizontal][vertical] == " ":
        print("AGUA")
        matriz[horizontal][vertical] = "~"
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("Mapa con disparo realizado\n")
        imprimir_tabla(matriz)
    elif matriz[horizontal][vertical] == "X" or matriz[horizontal][vertical] == "~":
        print("Ya has disparado en esa posicion, intenta de nuevo")
        horizontal = int(input("Ingrese la fila donde desea disparar: ")) - 1
        vertical = int(input("Ingrese la columna donde desea disparar: ")) - 1
        return turno(matriz, horizontal, vertical)
    else:
        print("SE IMPACTADO UN BARCO ENEMIGO, TIENES UN TURNO EXTRA")
        tipo_barco = matriz[horizontal][vertical]
        matriz[horizontal][vertical] = "X"
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("Mapa con disparo realizado\n")
        imprimir_tabla(matriz)
        
        if tipo_barco == "A":
            acorazado += 1
            if acorazado == 3:
                print("HAS HUNDIDO UN ACORAZADO")
                naves_hundidas += 1
        elif tipo_barco == "S":
            submarino += 1
            if submarino == 3:
                print("HAS HUNDIDO UN SUBMARINO")
                naves_hundidas += 1
        elif tipo_barco == "D":
            destructor += 1
            if destructor == 3:
                print("HAS HUNDIDO UN DESTRUCTOR")
                naves_hundidas += 1
        elif tipo_barco == "F":
            fragata += 1
            if fragata == 2:
                print("HAS HUNDIDO UNA FRAGATA")
                naves_hundidas += 1
        elif tipo_barco == "P":
            portavion += 1
            if portavion == 4:
                print("HAS HUNDIDO UN PORTAVION")
                naves_hundidas += 1
        
        if naves_hundidas == 9:
            print("HAS GANADO - ¡FELICIDADES!")
            imprimir_tabla(matriz)
            return matriz  # Termina el juego
        else:
            return turno(matriz, horizontal, vertical)  # Turno extra

    return matriz


def turno_enemy(matriz):
    global acorazado2, submarino2, destructor2, fragata2, portavion2, naves_hundidas2

    horizontal = random.randint(0, 9)
    vertical = random.randint(0, 9)

    if matriz[horizontal][vertical] == " ":
        print("AGUA")
        matriz[horizontal][vertical] = "~"
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("Mapa con disparo realizado\n")
        imprimir_tabla(matriz)
    elif matriz[horizontal][vertical] == "X" or matriz[horizontal][vertical] == "~":
        print("Ya has disparado en esa posicion, intenta de nuevo")
        return turno_enemy(matriz)
    else:
        print("SE IMPACTADO UN BARCO ENEMIGO, TIENES UN TURNO EXTRA")
        tipo_barco = matriz[horizontal][vertical]
        matriz[horizontal][vertical] = "X"
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("Mapa con disparo realizado\n")
        imprimir_tabla(matriz)
        
        if tipo_barco == "A":
            acorazado2 += 1
            if acorazado2 == 3:
                print("HAS HUNDIDO UN ACORAZADO")
                naves_hundidas2 += 1
        elif tipo_barco == "S":
            submarino2 += 1
            if submarino2 == 3:
                print("HAS HUNDIDO UN SUBMARINO")
                naves_hundidas2 += 1
        elif tipo_barco == "D":
            destructor2 += 1
            if destructor2 == 3:
                print("HAS HUNDIDO UN DESTRUCTOR")
                naves_hundidas2 += 1
        elif tipo_barco == "F":
            fragata2 += 1
            if fragata2 == 2:
                print("HAS HUNDIDO UNA FRAGATA")
                naves_hundidas2 += 1
            ##########################################
            elif tipo_barco == "P":
                portavion2 += 1
            if portavion2 == 4:
                print("HAS HUNDIDO UN PORTAVION")
                naves_hundidas2 += 1
        
        if naves_hundidas2 == 9:
            print("HAS PERDIDO,GANO EL COMPUTADOR")
            imprimir_tabla(matriz)
            return matriz  # Termina el juego
        else:
            return turno(matriz, horizontal, vertical)  # Turno extra

    