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
r = True
while r:
    print("")
    print("t: mostrar el tiempo")
    print("d: dormir")
    print("c: accion")
    print("s: salir")


    opciones = input("elija una opcion:")

    if opciones == 't':
        tiempo.seguir_tiempo()
        print(f"Días: {tiempo.dias}, Accion: {tiempo.accion}")


    elif opciones == 'd':
        print("El jugador va a dormir:")
        if tiempo.accion == 0 :
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
        
    elif opciones == "c":
        tiempo.accionN()
        tiempo.seguir_tiempo()
    
    elif opciones == "s":
        r = False
    
    else :
        print("Opcion invalida")