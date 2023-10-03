import random

class CantidadItems:
    def __init__(self, oro):
        self.oro = oro
        self.inventario = {
            'Frutos': {
                'Manzana': 0,
                'Trigo': 0,
                'Papa': 0,
                'Zanahoria': 0,
                'Fresa': 0
            },
            'Fertilizantes': {
                'Básico': 0,
                'Intermedio': 0,
                'Avanzado': 0
            },
            'Semillas': {
                'Manzana': 0,
                'Trigo': 0,
                'Papa': 0,
                'Zanahoria': 0,
                'Fresa': 0
            }
        }

    def mostrar_inventario(self):
        print("Inventario del jugador:")
        print("Oro:", self.oro)
        for categoria, items in self.inventario.items():
            print(f"{categoria}:")
            for item, cantidad in items.items():
                if cantidad > 0:
                    print(f"{item}: {cantidad}")

    def agregar_frutos(self, nombre, cantidad):
        if nombre in self.inventario['Frutos']:
            self.inventario['Frutos'][nombre] += cantidad

inventario_jugador = CantidadItems(300)

class Tienda(CantidadItems):
    def __init__(self, inventario_jugador):
        super().__init__(0)
        self.inventario_jugador = inventario_jugador
        self.tienda = {
            'Frutos': {
                'Manzana': 50,
                'Trigo': 30,
                'Papa': 60,
                'Zanahoria': 70,
                'Fresa': 65
            },
            'Fertilizantes': {
                'Básico': 50,
                'Intermedio': 100,
                'Avanzado': 220
            },
            'Semillas': {
                'Manzana': 30,
                'Trigo': 15,
                'Papa': 25,
                'Zanahoria': 35,
                'Fresa': 20
            }
        }

    def comprar_semilla(self, semilla, cantidad):
        precio = self.tienda['Semillas'][semilla]
        costo_total = precio * cantidad
        if costo_total <= self.inventario_jugador.oro:
            self.inventario_jugador.oro -= costo_total
            self.inventario_jugador.inventario['Semillas'][semilla] += cantidad
            print(f"Has comprado {cantidad} semillas de {semilla}.")
        else:
            print("No tienes suficiente oro para comprar estas semillas.")

    def comprar_fertilizante(self, fertilizante, cantidad):
        precio = self.tienda['Fertilizantes'][fertilizante]
        costo_total = precio * cantidad
        if costo_total <= self.inventario_jugador.oro:
            self.inventario_jugador.oro -= costo_total
            self.inventario_jugador.inventario['Fertilizantes'][fertilizante] += cantidad
            print(f"Has comprado {cantidad} fertilizantes de {fertilizante}.")
        else:
            print("No tienes suficiente oro para comprar estos fertilizantes.")

    def vender_fruto(self, fruto, cantidad):
        if self.inventario_jugador.inventario['Frutos'][fruto] >= cantidad:
            precio = self.tienda['Frutos'][fruto]
            ganancia = precio * cantidad
            self.inventario_jugador.oro += ganancia
            self.inventario_jugador.inventario['Frutos'][fruto] -= cantidad
            print(f"Has vendido {cantidad} {fruto}(s) por {ganancia} de oro.")
        else:
            print("No tienes suficientes productos para vender.")

    def mostrar_semillas_disponibles(self):
        print("Semillas disponibles en la tienda:")
        for i, (semilla, precio) in enumerate(self.tienda['Semillas'].items(), start=1):
            print(f"{i}. {semilla} - Precio: {precio} oro")

    def mostrar_fertilizantes_disponibles(self):
        print("Fertilizantes disponibles en la tienda:")
        for i, (fertilizante, precio) in enumerate(self.tienda['Fertilizantes'].items(), start=1):
            print(f"{i}. {fertilizante} - Precio: {precio} oro")

    def mostrar_frutos_para_vender(self):
        print("Frutos que puedes vender:")
        for i, (fruto, precio) in enumerate(self.tienda['Frutos'].items(), start=1):
            cantidad_jugador = self.inventario_jugador.inventario['Frutos'][fruto]
            if cantidad_jugador > 0:
                print(f"{i}. {fruto} - Precio: {precio} oro - Cantidad en inventario: {cantidad_jugador}")

    def menu_tienda(self):
        while True:
            print('')
            print("===== Tienda =====")
            print("1. Comprar semillas")
            print("2. Comprar fertilizantes")
            print("3. Vender frutos")
            print("4. Salir de la tienda")

            opcion = input("Elige una opción: ")

            if opcion == '1':
                self.mostrar_semillas_disponibles()
                eleccion = int(input("Elige el número de la semilla que deseas comprar: "))
                if 1 <= eleccion <= len(self.tienda['Semillas']):
                    semilla = list(self.tienda['Semillas'].keys())[eleccion - 1]
                    cantidad = int(input(f"Ingresa la cantidad de semillas de {semilla} que deseas comprar: "))
                    self.comprar_semilla(semilla, cantidad)
                else:
                    print("Opción no válida. Intente de nuevo.")

            elif opcion == '2':
                self.mostrar_fertilizantes_disponibles()
                eleccion = int(input("Elige el número del fertilizante que deseas comprar: "))
                if 1 <= eleccion <= len(self.tienda['Fertilizantes']):
                    fertilizante = list(self.tienda['Fertilizantes'].keys())[eleccion - 1]
                    cantidad = int(input(f"Ingresa la cantidad de {fertilizante} que deseas comprar: "))
                    self.comprar_fertilizante(fertilizante, cantidad)
                else:
                    print("Opción no válida. Intente de nuevo.")

            elif opcion == '3':
                self.mostrar_frutos_para_vender()
                eleccion = int(input("Elige el número del fruto que deseas vender: "))
                if 1 <= eleccion <= len(self.tienda['Frutos']):
                    fruto = list(self.tienda['Frutos'].keys())[eleccion - 1]
                    cantidad = int(input(f"Ingresa la cantidad de {fruto} que deseas vender: "))
                    self.vender_fruto(fruto, cantidad)
                else:
                    print("Opción no válida. Intente de nuevo.")

            elif opcion == '4':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

tienda1 = Tienda(inventario_jugador)

class Tiempo:
    def __init__(self, dias):
        self.accion = 0
        self.dias = dias

    def seguir_tiempo(self):
        to = True
        while to:
            if self.accion >= 7:
                self.dias += 1
                self.accion = 0
            else:
                to = False

    def accionN(self):
        self.accion = 1 + self.accion

tiempo = Tiempo(0)

class Cultivos(Tiempo):
    def __init__(self, dias, nombre, tiempo_brote, tiempo_crecimiento, tiempo_maduracion, productos):
        super().__init__(dias)
        self.nombre = nombre
        self.tiempo_brote = tiempo_brote
        self.tiempo_crecimiento = tiempo_crecimiento
        self.tiempo_maduracion = tiempo_maduracion
        self.etapa = 'Semilla'
        self.productos = productos
        self.dias_transcurridos = 0
        self.regado = False
        self.fertilizado = False
        self.plagas = False 
        self.tratado = False 
        self.ha_tenido_plagas = False 

    def calcular_rendimiento(self):
        if self.plagas:
            if self.tratado:
                return random.randint(1, 5)
            else:
                return random.randint(0, 3)
        else:
            return random.randint(1, 7)   

    def cosechar(self):
        cantidad_productos = self.calcular_rendimiento()
        return cantidad_productos

manzanas = Cultivos(tiempo.dias,'Manzana', 2, 3, 4, 'manzanas')
trigo = Cultivos(tiempo.dias,'Trigo', 1, 3, 5, 'grano de trigo')
papas = Cultivos(tiempo.dias,'Papa', 2, 4, 4, 'papas')
fresas = Cultivos(tiempo.dias,'Fresa', 1, 4, 3, 'fresas')
zanahorias = Cultivos(tiempo.dias,'Zanahoria', 2, 3, 3, 'zanahorias')

class TerrenoCultivo(Tiempo):
    def __init__(self, dias, filas, columnas, inventario_jugador):
        super().__init__(dias)
        self.filas = filas
        self.columnas = columnas
        self.terreno = [['-' for c in range(self.columnas)] for f in range(self.filas)]
        self.inventario_jugador = inventario_jugador

    def sembrar_cultivo(self, fila, columna, cultivo):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            if isinstance(self.terreno[fila][columna], Cultivos):
                print('Ya hay un cultivo en esta parcela.')
            else:
                cantidad_semillas = self.inventario_jugador.inventario['Semillas'][cultivo.nombre]
                if cantidad_semillas > 0:
                    nuevo_cultivo = Cultivos(tiempo.dias, cultivo.nombre, cultivo.tiempo_brote, cultivo.tiempo_crecimiento + tiempo.dias, cultivo.tiempo_maduracion, cultivo.productos)
                    nuevo_cultivo.plagas = random.random() < 0.4
                    nuevo_cultivo.tratado = False
                    self.terreno[fila][columna] = nuevo_cultivo
                    print(f'Se ha sembrado {nuevo_cultivo.nombre} en la parcela {fila+1},{columna+1}.')
                    self.inventario_jugador.inventario['Semillas'][cultivo.nombre] -= 1
                else:
                    print(f"No tienes suficientes semillas de {cultivo.nombre} para sembrar este cultivo.")
        else:
            print("Ubicación no válida")


    def regar(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            cultivo = self.terreno[fila][columna]
            if isinstance(cultivo, Cultivos) and cultivo.etapa == 'Semilla':
                if not cultivo.regado:
                    cultivo.regado = True
                    print(f'Se ha regado y comenzado el crecimiento del cultivo de {cultivo.nombre} en la parcela {fila + 1},{columna + 1}.')
                else:
                    print(f'El cultivo de {cultivo.nombre} en la parcela {fila + 1},{columna + 1} ya ha sido regado en la etapa de "Brote".')
            else:
                print('No hay cultivo en esta parcela para regar.')
        else:
            print('Ubicación no válida.')

    def fertilizar(self, fila, columna, tipo_fertilizante):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            cultivo = self.terreno[fila][columna]
            if isinstance(cultivo, Cultivos):
                if not cultivo.fertilizado:
                    if cultivo.etapa != 'Cosecha':
                        cantidad_fertilizante = self.inventario_jugador.inventario['Fertilizantes'][tipo_fertilizante]
                        if cantidad_fertilizante > 0:
                            if cultivo.etapa == 'Brote':
                                if tipo_fertilizante == 'Básico':
                                    cultivo.tiempo_crecimiento - 1
                                elif tipo_fertilizante == 'Intermedio':
                                    cultivo.tiempo_crecimiento - 2
                                elif tipo_fertilizante == 'Avanzado':
                                    cultivo.tiempo_crecimiento - 3
                            elif cultivo.etapa == 'Crecimiento':
                                if tipo_fertilizante == 'Básico':
                                    cultivo.tiempo_maduracion - 1
                                elif tipo_fertilizante == 'Intermedio':
                                    cultivo.tiempo_maduracion - 2
                                elif tipo_fertilizante == 'Avanzado':
                                    cultivo.tiempo_maduracion - 3
                            elif cultivo.etapa == 'Maduración':
                                if tipo_fertilizante == 'Básico':
                                    cantidad_semillas = 1
                                elif tipo_fertilizante == 'Intermedio':
                                    cantidad_semillas = 2
                                elif tipo_fertilizante == 'Avanzado':
                                    cantidad_semillas = 3
                                self.inventario_jugador.inventario['Semillas'][cultivo.nombre] += cantidad_semillas
                                print(f'Se ha aplicado fertilizante {tipo_fertilizante} a {cultivo.nombre} y se han agregado {cantidad_semillas} semillas adicionales de {cultivo.nombre} al inventario.')
                            self.inventario_jugador.inventario['Fertilizantes'][tipo_fertilizante] -= 1
                            cultivo.fertilizado = True
                            print(f'Se ha fertilizado el cultivo de {cultivo.nombre} en la parcela {fila + 1},{columna + 1}.')
                        else:
                            print(f"No tienes suficiente fertilizante {tipo_fertilizante} para fertilizar este cultivo.")
                    else:
                        print(f'El cultivo de {cultivo.nombre} en la parcela {fila + 1},{columna + 1} ya está en cosecha y no se puede fertilizar.')
                else:
                    print(f'El cultivo de {cultivo.nombre} en la parcela {fila + 1},{columna + 1} ya ha sido fertilizado.')
            else:
                print('No hay cultivo en esta parcela para fertilizar.')
        else:
            print('Ubicación no válida.')

    def tratar_plagas_cultivo(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            cultivo = self.terreno[fila][columna]
            if isinstance(cultivo, Cultivos):
                if cultivo.plagas:
                    cultivo.plagas = False
                    cultivo.tratado = True
                    cultivo.ha_tenido_plagas = True
                    print(f'Se han tratado las plagas en el cultivo de {cultivo.nombre} en la parcela {fila + 1},{columna + 1}.')
                else:
                    print(f'El cultivo de {cultivo.nombre} en la parcela {fila + 1},{columna + 1} no tiene plagas.')
            else:
                print('No hay cultivo en esta parcela para tratar.')
        else:
            print('Ubicación no válida.')

    def cosechar_cultivo(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            cultivo = self.terreno[fila][columna]
            if cultivo != '-':
                if cultivo.etapa == 'Cosecha':
                    cantidad_productos = cultivo.cosechar()
                    self.inventario_jugador.agregar_frutos(cultivo.nombre, cantidad_productos)
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
                    if cultivo.etapa == 'Semilla' and cultivo.regado:
                          cultivo.etapa = 'Brote'
                    elif cultivo.etapa == 'Brote' and tiempo.dias >= cultivo.tiempo_brote:
                          cultivo.etapa = 'Crecimiento'
                    elif cultivo.etapa == 'Crecimiento' and tiempo.dias >= cultivo.tiempo_brote + cultivo.tiempo_crecimiento:
                        cultivo.etapa = 'Maduración'
                    elif cultivo.etapa == 'Maduración' and tiempo.dias >= cultivo.tiempo_brote + cultivo.tiempo_crecimiento + cultivo.tiempo_maduracion:
                        cultivo.etapa = 'Cosecha'

                    if cultivo.regado:
                        estado_regado = "Regado"
                    else:
                        estado_regado = "No regado"
                    
                    if cultivo.plagas:
                        plagas_info = "Con plagas"
                    elif cultivo.ha_tenido_plagas:
                        plagas_info = "Ha tenido plagas"
                    else:
                        plagas_info = "Sin plagas"

                    if cultivo.fertilizado:
                        estado_fertilizado = 'Fertilizado'
                    else:
                        estado_fertilizado = 'No fertilizado'

                    print(f'Fila: {fila + 1}, Columna: {columna + 1} | Cultivo: {cultivo.nombre} | Etapa: {cultivo.etapa} | Estado: {estado_regado} | Plagas: {plagas_info} | Fertilizante: {estado_fertilizado}')
                    cuadrícula_llena = True

        if not cuadrícula_llena:
            print("No hay cultivos sembrados.")

terreno = TerrenoCultivo(tiempo.dias, 3, 3,inventario_jugador)

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

while True:
    print("")
    print("== Menu principal ==")
    print("1. Ver Cultivos")
    print("2. Mostrar el tiempo")
    print("3. Dormir")
    print("4. Tienda")
    print("5. Mejoras")
    print("6. Inventario")
    print("7. Salir")
    
    opciones = input("Elija una opcion: ")

    if opciones == '1':
        while True:
            print("")
            print('=== Cultivos ===')
            print('1. Sembrar cultivo')
            print("2. Regar cultivo")
            print('3. Fetilizar')
            print("4. Tratar Cultivo")
            print("5. Cosechar cultivo")
            print("6. Mostrar terreno")
            print('7. Salir')
            opcio = input("Elija una opcion: ")

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
                tiempo.seguir_tiempo() 
                
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
                tiempo.seguir_tiempo() 

            elif opcio == '3':
                fila = int(input('Ingrese la fila del cultivo a fertilizar: ')) - 1
                columna = int(input('Ingrese la columna del cultivo a fertilizar: ')) - 1
                print('')
                print('Seleccione el tipo de fertilizante')
                print('1. Básico')
                print('2. Intermedio')
                print('3. Avanzado')
                fertilizante_opcion = input('Ingrese el número correspondiente al tipo de fertilizante: ')

                if fertilizante_opcion == '1':
                    tipo_fertilizante = 'Básico'
                elif fertilizante_opcion == '2':
                    tipo_fertilizante = 'Intermedio'
                elif fertilizante_opcion == '3':
                    tipo_fertilizante = 'Avanzado'
                else:
                    print('Opción no válida. Intente de nuevo.')
                    continue

                terreno.fertilizar(fila, columna, tipo_fertilizante)
                tiempo.accionN()
                tiempo.seguir_tiempo() 

            elif opcio == '4':
                fila = int(input('Ingrese la fila del cultivo a tratar: ')) - 1
                columna = int(input('Ingrese la columna del cultivo a tratar: ')) - 1
                terreno.tratar_plagas_cultivo(fila, columna)
                tiempo.accionN()
                tiempo.seguir_tiempo() 

            elif opcio == '5':
                fila = int(input('Ingrese la fila para cosechar: ')) - 1
                columna = int(input('Ingrese la columna para cosechar: ')) - 1
                terreno.cosechar_cultivo(fila, columna)
                tiempo.accionN()
                tiempo.seguir_tiempo() 

            elif opcio == '6':
                terreno.mostrar_terreno()
                tiempo.accionN()
                tiempo.seguir_tiempo()

            elif opcio == '7':
                break 

            else:
                print('Opción no válida. Intente de nuevo.')

    elif opciones == '2':
        tiempo.seguir_tiempo()
        print('')
        print('=== Tiempo ===')
        print(f"Días: {tiempo.dias}, Accion: {tiempo.accion}")

    elif opciones == '3':
        print('')
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

    elif opciones == "4":
        tiempo.accionN()
        tiempo.seguir_tiempo()
        tienda1.menu_tienda()
        
    elif opciones == '5':
        print("")
        print('== Mejoras ==')
        print("1. Aumento del arrea de siembra")

        tiempo.accionN()
        tiempo.seguir_tiempo()

        op = input("Elija una opcion: ")

        if op == '1':
            print("")
            print("1. aumentar fila")
            print("2. aumentar columna")
            opcion = input("Elija una opción: ")

            if opcion == '1':
                coste = 1000
                aumento = 500

                if inventario_jugador.oro >= coste:
                    print(f"La mejora de su área de siembra se ha realizado. Costo de la mejora: {coste}")
                    print("")
                    nuevas_filas = 1
                    mejora = Mejoras(terreno)
                    mejora.aumentar_filas(nuevas_filas)

                    inventario_jugador.oro -= coste
                    coste += aumento

                    print("Nuevas dimensiones:")
                    terreno.mostrar_terreno()
                    print("el nuevo coosto de la siguiente mejora sera:",coste)
                else:
                    print("No tiene suficiente dinero para poder realizar la mejora de filas")
                    print("el costo de su mejora es de:",coste)

            if opcion == '2':
                coste = 1000
                aumento = 500

                if inventario_jugador.oro >= coste:
                    print(f"La mejora de su área de siembra se ha realizado. Costo de la mejora: {coste}")
                    print("")
                    nuevas_columnas = + 1
                    mejora = Mejoras(terreno)

                    mejora.aumentar_columnas(nuevas_columnas)
                    inventario_jugador.oro -= coste
                    coste += aumento

                    print("Nuevas dimensiones:")
                    terreno.mostrar_terreno()
                    print("el nuevo coosto de la siguiente mejora sera:", coste)
                else:
                    print("No tiene suficiente dinero para poder realizar la mejora de filas")
                    print("el costo de su mejora es de:", coste)

    elif opciones == "6":
        print('')
        print('== Inventario ==')
        inventario_jugador.mostrar_inventario()

        tiempo.accionN()
        tiempo.seguir_tiempo()

    elif opciones == "7":
        break

    else:
        print("Elija otra opcion")     