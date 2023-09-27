import random

class Tiempo:
    def __init__(self):
        self.accion = 0
        self.dias = 0

    def seguir_tiempo(self):
        if self.accion == 7:
            self.dias += 1
            self.accion = 0

    def accionN(self):
        self.accion = 1 + self.accion

tiempo = Tiempo()

class Cultivos:
    def __init__(self, nombre, tiempo_brote, tiempo_crecimiento, tiempo_maduracion, productos):
        self.nombre = nombre
        self.tiempo_brote = tiempo_brote
        self.tiempo_crecimiento = tiempo_crecimiento
        self.tiempo_maduracion = tiempo_maduracion
        self.etapa = 'Brote'
        self.productos = productos
        self.rendimiento = random.randint(1, 10)

    def crecer(self, tiempo):
        if self.etapa == 'Brote' and tiempo.dias >= self.tiempo_brote:
            self.etapa = 'Crecimiento'
        elif self.etapa == 'Crecimiento' and tiempo.dias >= self.tiempo_crecimiento:
            self.etapa = 'Maduración'
        elif self.etapa == 'Maduración' and tiempo.dias >= self.tiempo_maduracion:
            self.etapa = 'Cosecha'

    def cosechar(self):
        cantidad_productos = self.rendimiento
        return cantidad_productos

manzanas = Cultivos('Manzana', 2, 5, 9, 'manzanas')
trigo = Cultivos('Trigo', 1, 4, 6, 'grano de trigo')
papas = Cultivos('Papa', 3, 5, 7, 'papas')
fresas = Cultivos('Fresa', 1, 3, 5, 'fresas')
zanahorias = Cultivos('Zanahoria', 2, 4, 7, 'zanahorias')


class TerrenoCultivo:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.terreno = [['-' for c in range(self.columnas)] for f in range(self.filas)]

    def sembrar_cultivo(self, fila, columna, cultivo):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            self.terreno[fila][columna] = cultivo
        else:
            print("Ubicación no válida")

    def cosechar_cultivo(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            cultivo = self.terreno[fila][columna]
            if cultivo != '-':
                cantidad_productos = cultivo.cosechar()
                print(f'Se han cosechado {cantidad_productos} productos de {cultivo.nombre}')
                self.terreno[fila][columna] = '-'
            else:
                print('No hay cultivo para cosechar en esta parcela.')
        else:
            print('Ubicación no válida')

    def mostrar_terreno(self):
        for i in self.terreno:
            print('+----' * self.columnas + '+')
            print('| ' + '  | '.join(cultivo.nombre[0] if isinstance(cultivo, Cultivos) else str(cultivo) for cultivo in i) + '  |')
        print('+----' * self.columnas + '+')

terreno = TerrenoCultivo(3, 3)

class Mejoras:
    def __init__(self, terreno):
        self.terreno = terreno

    def aumentar_filas(self, nuevas_filas):
        nueva_fila = ['-' for _ in range(self.terreno.columnas)]
        for _ in range(nuevas_filas):
            self.terreno.terreno.append(nueva_fila)
        self.terreno.filas += nuevas_filas

    def aumentar_columnas(self, nuevas_columnas):
        for fila in self.terreno.terreno:
            fila.extend(['-' for _ in range(nuevas_columnas)])
        self.terreno.columnas += nuevas_columnas

r = True
while r:
    print("")
    print("0. Ver Cultivos")
    print("1: Mostrar el tiempo")
    print("2: Dormir")
    print("3: Accion")
    print("4: Mejoras")
    print("5: Salir")

    opciones = input("Elija una opcion: ")

    if opciones == '0':
        print("")
        print('1. Sembrar cultivo')
        print("2. Cosechar cultivo")
        print("3. Mostrar terreno")

        opcio = input("Elija una opcion: ")

        if opcio == '1':
            fila = int(input('Ingrese la fila para sembrar: ')) - 1
            columna = int(input('Ingrese la columna para sembrar: ')) - 1
            print('Seleccione el tipo de cultivo')
            print('1. Manzanas')
            print('2. Trigo')
            print('3. Papas')
            print('4. Fresas')
            print('5. Zanahorias')
            cultivo_opcion = input('Ingrese el número correspondiente al cultivo: ')

            if cultivo_opcion == '1':
                cultivo = manzanas
            elif cultivo_opcion == '2':
                cultivo = trigo
            elif cultivo_opcion == '3':
                cultivo = papas
            elif cultivo_opcion == '4':
                cultivo = fresas
            elif cultivo_opcion == '5':
                cultivo = zanahorias
            else:
                print('Opción no válida. Intente de nuevo.')
                continue

            terreno.sembrar_cultivo(fila, columna, cultivo)

        elif opcio == '2':
            fila = int(input('Ingrese la fila para cosechar: ')) - 1
            columna = int(input('Ingrese la columna para cosechar: ')) - 1
            terreno.cosechar_cultivo(fila, columna)
        elif opcio == '3':
            terreno.mostrar_terreno()

        else:
            print('Opción no válida. Intente de nuevo.')

    elif opciones == '1':
        tiempo.seguir_tiempo()
        print(f"Días: {tiempo.dias}, Accion: {tiempo.accion}")


    elif opciones == '2':
        print("El jugador va a dormir:")
        if tiempo.accion == 0:
            tiempo.accion += 7
        elif tiempo.accion == 1:
            tiempo.accion += 6
        elif tiempo.accion == 2:
            tiempo.accion += 5
        elif tiempo.accion == 3:
            tiempo.accion += 4
        elif tiempo.accion == 4:
            tiempo.accion += 3
        elif tiempo.accion == 5:
            tiempo.accion += 2
        elif tiempo.accion == 6:
            tiempo.accion += 1

    elif opciones == "3":
        tiempo.accionN()
        tiempo.seguir_tiempo()

    elif opciones == '4':
        print("")
        print("1: Aumento del arrea de siembra")

        op = input("elija una opcion:")

        if op == '1':
            print("")
            print("1: aumentar fila")
            print("2: aumentar columna")
            opcion = input("elija una opcion")
            coste = 0
            bolsa = 0

            if opcion == '1':
                if bolsa >= coste:
                    print("la mejora de su arrea de siembra se a realizaado")
                    print("")
                    nuevas_filas = 1
                    mejora = Mejoras(terreno)
                    mejora.aumentar_filas(nuevas_filas)

                    print("Nuevas dimenciones:")
                    terreno.mostrar_terreno()

                else:
                    print("No tiene suficiente dinero para poder realizar la mejora de su fila")

            if opcion == '2':
                if bolsa >= coste:
                    print("la mejora de su arrea de siembra se a realizaado")
                    print("")
                    nuevas_columnas = + 1
                    mejora = Mejoras(terreno)
                    mejora.aumentar_columnas(nuevas_columnas)

                    print("Nuevas dimenciones:")
                    terreno.mostrar_terreno()

                else:
                    print("No tiene suficiente dinero para poder realizar la mejora de su columna")



    elif opciones == "5":
        r = False

    else:
        print("Elija otra opcion")