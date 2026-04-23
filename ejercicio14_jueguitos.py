import random

class Torre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.resistencia = 100
        self.escudo = 20
        self.municion = 5

    def mostrar_estado(self):
        print("\n--- ESTADO DE LA DEFENSA ---")
        print("Torre:", self.nombre)
        print("Resistencia (Vida):", self.resistencia)
        print("Escudo (Proteccion):", self.escudo)
        print("Municion de Cañon:", self.municion)
        print("-" * 25)

    def esta_en_pie(self):
        if self.resistencia > 0:
            return True
        return False

class JuegoDefensa:
    def __init__(self):
        print("--- BIENVENIDO A LA ULTIMA DEFENSA ---")
        n_torre = input("Dale un nombre a tu Torre: ")
        self.mi_torre = Torre(n_torre)
        self.dia = 1
        self.jugar()

    def jugar(self):
        while self.mi_torre.esta_en_pie() == True:
            self.mi_torre.mostrar_estado()
            print("DIA", self.dia, "- Una horda de enemigos se acerca...")
            
            print("¿Que orden das a la torre?")
            print("1. Fuego de Cañon (Elimina enemigos, gasta municion)")
            print("2. Reforzar Escudos (Aumenta proteccion)")
            print("3. Reparaciones de Emergencia (Recupera resistencia)")
            print("4. Buscar Municion (Recupera balas)")
            
            accion = input("Elige (1-4): ")

            # Acciones del usuario
            if accion == "1":
                if self.mi_torre.municion > 0:
                    print("¡BOOM! El cañon diezmo a los enemigos.")
                    self.mi_torre.municion = self.mi_torre.municion - 1
                    daño_enemigo = random.randint(5, 10) # Daño bajo
                else:
                    print("¡No tienes balas! Los enemigos cargan con todo.")
                    daño_enemigo = random.randint(20, 30) # Daño alto
            
            elif accion == "2":
                self.mi_torre.escudo = self.mi_torre.escudo + 15
                print("Escudos reforzados.")
                daño_enemigo = random.randint(15, 20)
            
            elif accion == "3":
                self.mi_torre.resistencia = self.mi_torre.resistencia + 20
                print("Los ingenieros reparan los muros.")
                daño_enemigo = random.randint(15, 20)
                
            elif accion == "4":
                self.mi_torre.municion = self.mi_torre.municion + 3
                print("Has encontrado mas balas.")
                daño_enemigo = random.randint(15, 25)

            if self.mi_torre.escudo > 0:
                self.mi_torre.escudo = self.mi_torre.escudo - daño_enemigo
                print("El escudo absorvio el impacto.")
                if self.mi_torre.escudo < 0:
                    self.mi_torre.escudo = 0
            else:
                self.mi_torre.resistencia = self.mi_torre.resistencia - daño_enemigo
                print("¡Impacto directo! La torre sufre daños.")

            self.dia = self.dia + 1

        print("\n" + "!" * 30)
        print("LA TORRE", self.mi_torre.nombre, "HA CAIDO.")
        print("Resististe un total de", self.dia, "dias.")
        print("GAME OVER")


JuegoDefensa()