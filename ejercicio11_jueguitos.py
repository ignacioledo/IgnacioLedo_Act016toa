import random

class Hechicero:
    def __init__(self, nombre, vida, magia):
        self.nombre = nombre
        self.vida = vida
        self.magia = magia

    def mostrar_estado(self):
        print(self.nombre, "| Vida:", self.vida, "| Magia:", self.magia)

    def esta_vivo(self):
        if self.vida > 0:
            return True
        return False

class Batalla:
    def __init__(self):
        print("--- BATALLA DE HECHICEROS ---")
        nombre_usu = input("Nombre de tu Hechicero: ")
        
        self.jugador = Hechicero(nombre_usu, 100, 50)
        self.rival = Hechicero("Mago Oscuro", 100, 50)
        self.duelo()

    def duelo(self):
        while self.jugador.esta_vivo() == True and self.rival.esta_vivo() == True:
            print("\n" + "="*30)
            self.jugador.mostrar_estado()
            self.rival.mostrar_estado()

            print("\nTU TURNO:")
            print("1. Bola de Fuego (10 PM - Daño 20)")
            print("2. Rayo Basico (0 PM - Daño 10)")
            print("3. Meditar (Recupera 20 PM)")
            print("4. EXPLOSION ARCANA (Gasta TODO el PM - Daño segun magia)")
            opcion = input("Elige tu accion: ")

            if opcion == "1":
                if self.jugador.magia >= 10:
                    print("¡Lanzas una Bola de Fuego!")
                    self.rival.vida = self.rival.vida - 20
                    self.jugador.magia = self.jugador.magia - 10
                else:
                    print("No tienes suficiente magia...")
            
            elif opcion == "2":
                print("Lanzas un Rayo Basico.")
                self.rival.vida = self.rival.vida - 10
            
            elif opcion == "3":
                print("Recuperas energia magica.")
                self.jugador.magia = self.jugador.magia + 20

            elif opcion == "4":
                if self.jugador.magia > 0:
                    # El daño es la mitad de la magia que tengas
                    daño_especial = self.jugador.magia / 2
                    print("¡LIBERAS TODA TU ENERGIA!")
                    print("Causas", daño_especial, "de daño fulminante.")
                    self.rival.vida = self.rival.vida - daño_especial
                    self.jugador.magia = 0 # Se gasta todo
                else:
                    print("No tienes energia para la explosion.")

            if self.rival.esta_vivo() == True:
                print("\nTurno del rival...")
                accion_rival = random.randint(1, 2)
                if accion_rival == 1:
                    d_rival = random.randint(10, 15)
                    print(self.rival.nombre, "te ataca y quita", d_rival)
                    self.jugador.vida = self.jugador.vida - d_rival
                else:
                    print(self.rival.nombre, "esta acumulando poder...")
                    self.rival.magia = self.rival.magia + 15

        print("\n" + "*"*30)
        if self.jugador.esta_vivo() == True:
            print("¡VICTORIA MAGICA!")
        else:
            print("HAS SIDO DERROTADO...")
        
        print("GAME OVER")

Batalla()