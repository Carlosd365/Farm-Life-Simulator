import random

class Tiempo:
    def __init__(self,dias):
        self.accion = 0
        self.dias = dias

    def seguir_tiempo(self):
        if self.accion == 7:
            self.dias += 1
            self.accion = 0

    def accionN(self):
        self.accion = 1 + self.accion

tiempo = Tiempo(0)

class Cultivos(Tiempo):
    def __init__(self,dias, nombre, tiempo_brote, tiempo_crecimiento, tiempo_maduracion, productos):
        super().__init__(dias)
        self.nombre = nombre
        self.tiempo_brote = tiempo_brote
        self.tiempo_crecimiento = tiempo_crecimiento 
        self.tiempo_maduracion = tiempo_maduracion
        self.etapa = 'Brote'
        self.productos = productos
        self.rendimiento = random.randint(1, 5)
        self.dias_transcurridos = 0
        self.regado = False

    def cosechar(self):
        cantidad_productos = self.rendimiento
        return cantidad_productos

manzanas = Cultivos(tiempo.dias,'Manzana', 2, 3, 4, 'manzanas')
trigo = Cultivos(tiempo.dias,'Trigo', 1, 3, 2, 'grano de trigo')
papas = Cultivos(tiempo.dias,'Papa', 3, 2, 2, 'papas')
fresas = Cultivos(tiempo.dias,'Fresa', 1, 2, 3, 'fresas')
zanahorias = Cultivos(tiempo.dias,'Zanahoria', 2, 2, 3, 'zanahorias')


class TerrenoCultivo(Tiempo):
    def __init__(self, dias,filas, columnas):
        super().__init__(dias)
        self.filas = filas
        self.columnas = columnas
        self.terreno = [['-' for c in range(self.columnas)] for f in range(self.filas)]

    def sembrar_cultivo(self, fila, columna, cultivo):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            if isinstance(self.terreno[fila][columna], Cultivos):
                print('Ya hay un cultivo en esta parcela.')
            else:
                nuevo_cultivo = Cultivos(tiempo.dias,cultivo.nombre, cultivo.tiempo_brote, cultivo.tiempo_crecimiento + tiempo.dias , cultivo.tiempo_maduracion, cultivo.productos)
                self.terreno[fila][columna] = nuevo_cultivo
                print(f'Se ha sembrado {nuevo_cultivo.nombre} en la parcela {fila+1},{columna+1}.')
        else:
            print("Ubicación no válida")

    def regar(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            cultivo = self.terreno[fila][columna]
            if isinstance(cultivo, Cultivos) and cultivo.etapa == 'Brote':
                if not cultivo.regado:
                    cultivo.regado = True
                    print(f'Se ha regado y comenzado el crecimiento del cultivo de {cultivo.nombre} en la parcela {fila + 1},{columna + 1}.')
                else:
                    print(f'El cultivo en la parcela {fila + 1},{columna + 1} ya ha sido regado en la etapa de "Brote".')
            else:
                print(f'No se puede regar el cultivo en la parcela {fila + 1},{columna + 1}.')
        else:
            print('Ubicación no válida.')

    def cosechar_cultivo(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            cultivo = self.terreno[fila][columna]
            if cultivo != '-':
                if cultivo.etapa == 'Cosecha':
                    cantidad_productos = cultivo.cosechar()
                    print(f'Se han cosechado {cantidad_productos} productos de {cultivo.nombre} en la parcela {fila+1},{columna+1}')
                    self.terreno[fila][columna] = '-'
                else:
                    print('El cultivo no está listo para ser cosechado.')
            else:
                print('No hay cultivo para cosechar en esta parcela.')
        else:
            print('Ubicación no válida')

    def mostrar_terreno(self):
        emojis = {
            'Manzana': '🍎',
            'Trigo': '🌾',
            'Papa': '🥔',
            'Fresa': '🍓',
            'Zanahoria': '🥕'
        }
        for i in self.terreno:
            print('+----' * self.columnas + '+')
            print('| ' + '  | '.join(emojis[cultivo.nombre] if isinstance(cultivo, Cultivos) else str(cultivo) for cultivo in i) + '  |')
        print('+----' * self.columnas + '+')

        cuadrícula_llena = False

        print("Listado de cultivos:")
        for fila in range(self.filas):
            for columna in range(self.columnas):
                cultivo = self.terreno[fila][columna]
                if isinstance(cultivo, Cultivos):
                    if cultivo.etapa == 'Brote' and cultivo.regado:
                          cultivo.etapa = 'Crecimiento'
                    elif cultivo.etapa == 'Crecimiento' and tiempo.dias >= cultivo.tiempo_crecimiento:
                        cultivo.etapa = 'Maduración'
                    elif cultivo.etapa == 'Maduración' and tiempo.dias >= cultivo.tiempo_crecimiento + cultivo.tiempo_maduracion:
                        cultivo.etapa = 'Cosecha'
                    estado_regado = "Regado" if cultivo.regado else "No Regado"
                    print(f'Fila: {fila + 1}, Columna: {columna + 1} | Cultivo: {cultivo.nombre} | Etapa: {cultivo.etapa} | Estado: {estado_regado}')
                    cuadrícula_llena = True

        if not cuadrícula_llena:
            print("No hay cultivos sembrados.")

terreno = TerrenoCultivo(tiempo.dias,3, 3)

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
    print("---Menu principal---")
    print("1. Ver Cultivos")
    print("2. Mostrar el tiempo")
    print("3. Dormir")
    print("4. Mejoras")
    print("5. Salir")

    opciones = input("Elija una opcion: ")

    if opciones == '1':
        print("")
        print('1. Sembrar cultivo')
        print("2. Regar cultivo")
        print("3. Cosechar cultivo")
        print("4. Mostrar terreno")
        opcio = input("Elija una opcion: ")
        tiempo.accionN()

        if opcio == '1':
            fila = int(input('Ingrese la fila para sembrar: ')) - 1
            columna = int(input('Ingrese la columna para sembrar: ')) - 1
            print('')
            print('Seleccione el tipo de cultivo')
            print('1. Manzanas')
            print('2. Trigo')
            print('3. Papas')
            print('4. Fresas')
            print('5. Zanahorias')
            cultivo_opcion = input('Ingrese el número correspondiente al cultivo: ')
            tiempo.accionN()

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
            fila = int(input('Ingrese la fila del cultivo a regar: ')) - 1
            columna = int(input('Ingrese la columna del cultivo a regar: ')) - 1
            terreno.regar(fila, columna)
            tiempo.accionN()

        elif opcio == '3':
            fila = int(input('Ingrese la fila para cosechar: ')) - 1
            columna = int(input('Ingrese la columna para cosechar: ')) - 1
            terreno.cosechar_cultivo(fila, columna)
            tiempo.accionN()
        
        elif opcio == '4':
            tiempo.accionN()
            tiempo.seguir_tiempo()
            terreno.mostrar_terreno()

        else:
            print('Opción no válida. Intente de nuevo.')

    elif opciones == '2':
        tiempo.seguir_tiempo()
        print(f"Días: {tiempo.dias}, Accion: {tiempo.accion}")


    elif opciones == '3':
        print("El jugador va a dormir")
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
                tiempo.accionN()
                tiempo.seguir_tiempo()
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
                tiempo.accionN()
                tiempo.seguir_tiempo()
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