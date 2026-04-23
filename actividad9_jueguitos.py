import random

class Item:
    def __init__(self, nombre, tipo, color="ninguno"):
        self.nombre = nombre
        self.tipo = tipo # arma, llave, tesoro
        self.color = color

class Cofre:
    def __init__(self, id):
        self.id = id
        self.estado = "cerrado"
        # Probabilidad de 30% de que sea un cofre de color (más difícil)
        if random.randint(1, 10) <= 3:
            self.color = random.choice(["rojo", "azul", "dorado"])
            self.tipo_cofre = "especial"
        else:
            self.color = "madera"
            self.tipo_cofre = "comun"
        
        self.contenido = Item("Tesoro Valioso", "tesoro")

class Explorador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.mochila = [Item("Espada vieja", "arma")] # Empieza con arma para defenderse
        self.cueva = [Cofre(1), Cofre(2), Cofre(3)]
        self.jugar()

    def jugar(self):
        opcion = ""
        while opcion != "5" and self.vida > 0:
            print("\n--- EXPLORADOR:", self.nombre, "| VIDA:", self.vida, "---")
            print("1. Ver cueva | 2. Inspeccionar | 3. Abrir | 4. Saquear | 5. Salir")
            opcion = input("Elegir: ")

            if opcion == "1": self.ver()
            elif opcion == "2": self.inspeccionar()
            elif opcion == "3": self.abrir()
            elif opcion == "4": self.saquear()

            # Probabilidad de bicho al azar
            if random.randint(1, 10) <= 2 and opcion != "5":
                self.bicho()

        print("GAME OVER")

    def ver(self):
        for c in self.cueva:
            print("Cofre", c.id, "detectado.")

    def inspeccionar(self):
        n = int(input("¿Qué cofre quieres inspeccionar? (1-3): ")) - 1
        cofre = self.cueva[n]
        print("Inspeccionando...")
        print("Es un cofre de tipo:", cofre.tipo_cofre)
        print("Color:", cofre.color)
        if cofre.tipo_cofre == "especial":
            print("AVISO: Necesitas una llave", cofre.color, "para abrirlo.")

    def abrir(self):
        n = int(input("Número de cofre: ")) - 1
        cofre = self.cueva[n]
        
        if cofre.tipo_cofre == "comun":
            cofre.estado = "abierto"
            print("Abriste el cofre común sin problemas.")
        else:
            # Buscar llave del color correcto
            encontrada = False
            for i in self.mochila:
                if i.tipo == "llave" and i.color == cofre.color:
                    encontrada = True
            
            if encontrada == True:
                cofre.estado = "abierto"
                print("¡Usaste la llave", cofre.color, "y el cofre se abrió!")
            else:
                print("Está bloqueado. Necesitas la llave", cofre.color)

    def bicho(self):
        print("\n¡UN MONSTRUO TE EMBOSCA! 👾")
        tiene_arma = False
        for i in self.mochila:
            if i.tipo == "arma":
                tiene_arma = True
        
        if tiene_arma == True:
            print("Usas tu arma y sales ileso.")
        else:
            daño = random.randint(15, 25)
            self.vida = self.vida - daño
            print("¡No tienes armas! Pierdes", daño, "de vida.")

    def saquear(self):
        n = int(input("Número de cofre: ")) - 1
        cofre = self.cueva[n]
        if cofre.estado == "abierto":
            if cofre.contenido != "vacio":
                print("Recogiste:", cofre.contenido.nombre)
                self.mochila.append(cofre.contenido)
                cofre.contenido = "vacio"
            else:
                print("Ya está vacío.")
        else:
            print("El cofre aún está cerrado.")

# Iniciar
Explorador(input("Tu nombre: "))