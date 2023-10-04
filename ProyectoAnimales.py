import random

class Tiempo:
    def __init__(self,dias):
        self.accion = 0
        self.dias = dias

    def seguir_tiempo(self):
       to = True
       while to:
        if self.accion >= 7:
            self.dias += 1
            self.accion -= 7 
        else :
            to = False

    def accionN(self):
        self.accion = 1 + self.accion

tiempo = Tiempo(0)

class Animales(Tiempo):
    def __init__(self,dias, nombreA, tiempo_broteA, tiempo_crecimientoA, tiempo_maduracionA, productosA):
        super().__init__(dias)
        self.nombreA = nombreA
        self.tiempo_broteA = tiempo_broteA
        self.tiempo_crecimientoA = tiempo_crecimientoA 
        self.tiempo_maduracionA = tiempo_maduracionA
        self.etapaA = 'Cria'
        self.productosA = productosA
        self.rendimiento = random.randint(1, 5)
        self.dias_transcurridosA = 0
        self.regadoA = False

    def cosechar(self):
        cantidad_productosA = self.rendimiento
        return cantidad_productosA

vaca = Animales(tiempo.dias,'Vaca', 2, 3, 4, 'carne')
pollo = Animales(tiempo.dias,'Pollo', 1, 3, 2, 'carne')
cerdo = Animales(tiempo.dias,'Cerdo', 3, 2, 2, 'carne')
conejo = Animales(tiempo.dias,'Conejo', 1, 2, 3, 'carne')
pato = Animales(tiempo.dias,'Pato', 2, 2, 3, 'carne')


class TerrenoAnimal(Tiempo):
    def __init__(self, dias,filas2, columnas2):
        super().__init__(dias)
        self.filas2 = filas2
        self.columnas2 = columnas2
        self.terreno2 = [['-' for c in range(self.columnas2)] for f in range(self.filas2)]

    def sembrar_cultivo(self, fila2, columna2, cultivo2):
        if 0 <= fila2 < self.filas2 and 0 <= columna2 < self.columnas2:
            if isinstance(self.terreno2[fila2][columna2], Animales):
                print('Ya hay un animal en esta parcela.')
            else:
                nuevo_cultivo2 = Animales(tiempo.dias,cultivo2.nombreA, cultivo2.tiempo_broteA, cultivo2.tiempo_crecimientoA + tiempo.dias , cultivo2.tiempo_maduracionA, cultivo2.productosA)
                self.terreno2[fila2][columna2] = nuevo_cultivo2
                print(f'Se ha colocado un animal {nuevo_cultivo2.nombreA} en la parcela {fila2+1},{columna2+1}.')
        else:
            print("Ubicación no válida")

    def regar(self, fila2, columna2):
        if 0 <= fila2 < self.filas2 and 0 <= columna2 < self.columnas2:
            cultivo2 = self.terreno2[fila2][columna2]
            if isinstance(cultivo2, Animales) and cultivo2.etapaA == 'Brote':
                if not cultivo2.regadoA:
                    cultivo2.regadoA = True
                    print(f'Se ha alimentado a {cultivo2.nombreA} en la parcela {fila2 + 1},{columna2 + 1}.')
                else:
                    print(f'El animal en la parcela{fila2 + 1},{columna2 + 1} ya ha sido alimentado.')
            else:
                print(f'No se puede alimentar al animal en la parcela {fila2 + 1},{columna2 + 1}.')
        else:
            print('Ubicación no válida.')

    def cosechar_cultivo2(self, fila2, columna2):
        if 0 <= fila2 < self.filas2 and 0 <= columna2 < self.columnas2:
            cultivo2 = self.terreno2[fila2][columna2]
            if cultivo2 != '-':
                if cultivo2.etapaA == 'Cosecha':
                    cantidad_productos2 = cultivo2.cosechar()
                    print(f'Se han cosechado {cantidad_productos2} productos de {cultivo2.nombreA} en la parcela {fila2+1},{columna2+1}')
                    self.terreno2[fila2][columna2] = '-'
                else:
                    print('El animal no esta listo para cosechar.')
            else:
                print('no hay animales para cosechar en esta parcela.')
        else:
            print('Ubicación no válida')

    def mostrar_terreno(self):
        emojis = {
            'Vaca': '🐄',
            'Pollo': '🐔',
            'Cerdo': '🐖',
            'Conejo': '🐇',
            'Pato': '🦆'
        }
        for i in self.terreno2:
            print('+----' * self.columnas2 + '+')
            print('| ' + '  | '.join(emojis[cultivo2.nombreA] if isinstance(cultivo2, Animales) else str(cultivo2) for cultivo2 in i) + '  |')
        print('+----' * self.columnas2 + '+')

        cuadrícula_llena = False

        print("Listado de animales:")
        for fila2 in range(self.filas2):
            for columna2 in range(self.columnas2):
                cultivo2 = self.terreno2[fila2][columna2]
                if isinstance(cultivo2, Animales):
                    if cultivo2.etapaA == 'Cria' and cultivo2.regadoA:
                          cultivo2.etapaA = 'Joven'
                    elif cultivo2.etapaA == 'Joven' and tiempo.dias >= cultivo2.tiempo_crecimientoA:
                        cultivo2.etapaA = 'Adulto'
                    elif cultivo2.etapaA == 'Adulto' and tiempo.dias >= cultivo2.tiempo_crecimientoA + cultivo2.tiempo_maduracionA:
                        cultivo2.etapaA = 'Cosecha'
                    estado_regado2 = "Alimentado" if cultivo2.regadoA else "No alimentado"
                    print(f'Fila: {fila2 + 1}, Columna: {columna2 + 1} | Cultivo: {cultivo2.nombreA} | Etapa: {cultivo2.etapaA} | Estado: {estado_regado2}')
                    cuadrícula_llena = True

        if not cuadrícula_llena:
            print("No hay animales criados.")

animal = TerrenoAnimal(tiempo.dias,3, 3)

class Mejoras:
    def __init__(self, animal):
        self.animal = animal

    def aumentar_filas(self, nuevas_filas):
        nueva_fila = ['-' for _ in range(self.animal.columnas2)]
        for _ in range(nuevas_filas):
            self.animal.terreno2.append(nueva_fila)
        self.animal.filas2 += nuevas_filas

    def aumentar_columnas(self, nuevas_columnas):
        for fila in self.animal.terreno2:
            fila.extend(['-' for _ in range(nuevas_columnas)])
        self.animal.columnas2 += nuevas_columnas

r = True
while r:
    print("---Menu principal---")
    print("1. Ver granja")
    print("2. Mostrar el tiempo")
    print("3. Dormir")
    print("4. Mejoras")
    print("5. Salir")

    opciones = input("Elija una opcion: ")

    if opciones == '1':
        print("")
        print('1. Criar animal')
        print("2. Alimentar animal")
        print("3. Cosechar")
        print("4. Mostrar terreno")
        opcio = input("Elija una opcion: ")
        tiempo.accionN()

        if opcio == '1':
            fila = int(input('Ingrese la fila para criar: ')) - 1
            columna = int(input('Ingrese la columna para criar: ')) - 1
            print('')
            print('Seleccione el tipo de animal')
            print('1. Vaca')
            print('2. Pollo')
            print('3. Cerdo')
            print('4. Conejo')
            print('5. Pato')
            cultivo_opcion = input('Ingrese el número correspondiente al animal: ')
            tiempo.accionN()

            if cultivo_opcion == '1':
                cultivo2 = vaca
            elif cultivo_opcion == '2':
                cultivo2 = pollo
            elif cultivo_opcion == '3':
                cultivo2 = cerdo
            elif cultivo_opcion == '4':
                cultivo2 = conejo
            elif cultivo_opcion == '5':
                cultivo2 = pato
            else:
                print('Opción no válida. Intente de nuevo.')
                continue

            animal.sembrar_cultivo(fila, columna, cultivo2)

        elif opcio == '2':
            fila2 = int(input('Ingrese la fila del animal a alimentar: ')) - 1
            columna2 = int(input('Ingrese la columna del animal a alimentar: ')) - 1
            animal.regar(fila2, columna2)
            tiempo.accionN()

        elif opcio == '3':
            fila2 = int(input('Ingrese la fila para cosechar: ')) - 1
            columna2 = int(input('Ingrese la columna para cosechar: ')) - 1
            animal.cosechar_cultivo2(fila2, columna2)
            tiempo.accionN()
        
        elif opcio == '4':
            tiempo.accionN()
            tiempo.seguir_tiempo()
            animal.mostrar_terreno()

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
        print("1: Aumento del arrea de cria")

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
                    print("la mejora de su arrea de cria se a realizaado")
                    print("")
                    nuevas_filas = 1
                    mejora = Mejoras(animal)
                    mejora.aumentar_filas(nuevas_filas)

                    print("Nuevas dimenciones:")
                    animal.mostrar_terreno()

                else:
                    print("No tiene suficiente dinero para poder realizar la mejora de su fila")

            if opcion == '2':
                tiempo.accionN()
                tiempo.seguir_tiempo()
                if bolsa >= coste:
                    print("la mejora de su arrea de cria se a realizaado")
                    print("")
                    nuevas_columnas = + 1
                    mejora = Mejoras(animal)
                    mejora.aumentar_columnas(nuevas_columnas)

                    print("Nuevas dimenciones:")
                    animal.mostrar_terreno()

                else:
                    print("No tiene suficiente dinero para poder realizar la mejora de su columna")



    elif opciones == "5":
        r = False

    else:
        print("Elija otra opcion")