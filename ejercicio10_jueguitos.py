import random

class Auto:
    def __init__(self, nombre, marca):
        self.nombre = nombre
        self.marca = marca
        self.distancia = 0

    def avanzar(self, km):
        self.distancia = self.distancia + km

    def mostrar(self):
        pista = "-" * (self.distancia // 5)
        print(self.nombre, "(", self.marca, ")", pista, "🏎️")

class Carrera:
    def __init__(self):
        self.autos = []
        self.meta = 100
        self.ganador = ""
        
        print("--- BIENVENIDOS A LA GRAN CARRERA ---")
        # Ingreso de datos del usuario
        nom = input("Tu nombre de piloto: ")
        mar = input("Marca de tu auto: ")
        
        self.jugador = Auto(nom, mar)
        
        # Agregamos rivales a la lista
        self.autos.append(Auto("Rayo", "Ferrari"))
        self.autos.append(Auto("Trueno", "Mercedes"))
        
        self.correr()

    def correr(self):
        while self.ganador == "":
            print("\n" + "="*30)
            self.jugador.mostrar()
            for a in self.autos:
                a.mostrar()

            print("\nTU TURNO:")
            print("1. Acelerar normal (10km)")
            print("2. Nitro (20km con riesgo de falla)")
            print("3. Frenar un poco (5km para enfriar)")
            accion = input("Elegir accion: ")

            if accion == "1":
                self.jugador.avanzar(10)
            elif accion == "2":
                suerte = random.randint(1, 10)
                if suerte <= 3:
                    print("¡El motor fallo! Avanzas solo 2km")
                    self.jugador.avanzar(2)
                else:
                    print("¡NITRO ACTIVADO!")
                    self.jugador.avanzar(20)
            elif accion == "3":
                self.jugador.avanzar(5)

            for a in self.autos:
                a.avanzar(random.randint(8, 15))

            # Revisar si alguien gano
            self.revisar_meta()

        print("\n" + "*"*30)
        print("EL GANADOR ES:", self.ganador)
        print("GAME OVER")

    def revisar_meta(self):
        if self.jugador.distancia >= self.meta:
            self.ganador = self.jugador.nombre
        
        for a in self.autos:
            if a.distancia >= self.meta:
                self.ganador = a.nombre

Carrera()