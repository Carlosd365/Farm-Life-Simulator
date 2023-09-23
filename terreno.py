class TerrenoCultivo:
    def __init__(self):
        self.filas = 5
        self.columnas = 5
        self.terreno = [['-' for f in range(self.filas)] for c in range(self.columnas)]

    def sembrar_cultivo(self, fila, columna, cultivo):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            self.terreno[fila][columna] = cultivo
        else:
            print("Ubicación no válida")

    def cosechar_cultivo(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            if self.terreno[fila][columna] != '-':
                self.terreno[fila][columna] = '-'
            else:
                print('No hay cultivo para cosechar en esta parcela.')
        else:
            print('Ubicación no válida')

    def mostrar_terreno(self):
        for i in self.terreno:
            print('+----' * self.columnas + '+')
            print('| ' + '  | '.join(i) + '  |')
        print('+----' * self.columnas + '+')

terreno = TerrenoCultivo()

while True:
    print('Opciones:')
    print('1. Sembrar cultivo')
    print("2. Cosechar cultivo")
    print("3. Mostrar terreno")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        fila = int(input('Ingrese la fila para sembrar(1-5): ')) - 1
        columna = int(input('Ingrese la columna para sembrar(1-5): ')) - 1
        cultivo = input("Ingrese el tipo de cultivo: ")
        terreno.sembrar_cultivo(fila, columna, cultivo)
    elif opcion == '2':
        fila = int(input('Ingrese la fila para cosechar: ')) - 1
        columna = int(input('Ingrese la columna para cosechar: ')) - 1
        terreno.cosechar_cultivo(fila, columna)
    elif opcion == '3':
        terreno.mostrar_terreno()
    elif opcion == '4':
        break
    else:
        print('Opción no válida. Intente de nuevo.')