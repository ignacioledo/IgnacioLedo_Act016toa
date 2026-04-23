import random

class Objeto:
    def __init__(self, nombre, tipo, valor_efecto):
        self.nombre = nombre
        self.tipo = tipo  # Comida, Medicina, Material
        self.valor_efecto = valor_efecto

class Aventurero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.energia = 50
        self.mochila = []
        self.jugando = True
        self.bucle_principal()

    def bucle_principal(self):
        print("--- BIENVENIDO A LA AVENTURA EXPANDIDA ---")
        while self.jugando == True and self.vida > 0:
            print("\n" + "="*30)
            print("ESTADO:", self.nombre, "| VIDA:", self.vida, "| ENERGIA:", self.energia)
            print("1. Explorar zona")
            print("2. Abrir mochila")
            print("3. Intentar fabricar algo")
            print("4. Descansar (Recupera energia, pero puede ser peligroso)")
            print("5. Abandonar aventura")
            
            opc = input("¿Que quieres hacer?: ")

            if opc == "1": self.explorar()
            elif opc == "2": self.gestionar_mochila()
            elif opc == "3": self.fabricar()
            elif opc == "4": self.descansar()
            elif opc == "5": self.jugando = False

            # Si la energia llega a 0, el hambre te quita vida
            if self.energia <= 0:
                print("¡Estas agotado! Pierdes 10 de vida por cansancio.")
                self.vida = self.vida - 10
                self.energia = 0

        print("\nHas finalizado tu viaje.")
        print("GAME OVER")

    def explorar(self):
        print("\nCaminando por tierras desconocidas...")
        self.energia = self.energia - 10 # Explorar cansa
        
        suerte = random.randint(1, 10)
        
        if suerte <= 4: # 40% Encontrar objeto
            items = [Objeto("Baya", "Comida", 15), Objeto("Hierba", "Material", 0), Objeto("Venda", "Medicina", 20)]
            encontrado = random.choice(items)
            print("¡Encontraste un objeto:", encontrado.nombre, "!")
            self.mochila.append(encontrado)
            
        elif suerte <= 7: # 30% Evento de trampa
            daño = random.randint(10, 20)
            print("¡Caiste en una trampa de espinas! Pierdes", daño, "de vida.")
            self.vida = self.vida - daño
            
        else: # 30% No hay nada
            print("No encontraste nada interesante esta vez.")

    def gestionar_mochila(self):
        print("\n--- TU MOCHILA ---")
        if len(self.mochila) == 0:
            print("Vacia.")
        else:
            for i, obj in enumerate(self.mochila):
                print(i, "-", obj.nombre, "(Type:", obj.tipo, ")")
            
            print("\n¿Quieres usar algun objeto? (Escribe el numero o 'n' para volver)")
            eleccion = input("Seleccion: ")
            if eleccion != "n":
                idx = int(eleccion)
                item = self.mochila.pop(idx)
                
                if item.tipo == "Comida":
                    self.energia = self.energia + item.valor_efecto
                    print("Comiste", item.nombre, ". +Energia!")
                elif item.tipo == "Medicina":
                    self.vida = self.vida + item.valor_efecto
                    print("Usaste", item.nombre, ". +Vida!")
                else:
                    print("No puedes usar este material asi, intenta fabricar algo.")
                    self.mochila.append(item) # Lo devuelve si no sirve

    def fabricar(self):
        print("\n--- MESA DE TRABAJO ---")
        materiales = []
        for i in self.mochila:
            if i.tipo == "Material":
                materiales.append(i)
        
        if len(materiales) >= 2:
            print("Tienes materiales suficientes. ¿Fabricar un Botiquin Super?")
            print("1. Si | 2. No")
            conf = input(": ")
            if conf == "1":
                contador = 0
                nueva_lista = []
                for x in self.mochila:
                    if x.tipo == "Material" and contador < 2:
                        contador = contador + 1
                    else:
                        nueva_lista.append(x)
                self.mochila = nueva_lista
                self.mochila.append(Objeto("Botiquin Super", "Medicina", 50))
                print("¡Fabricacion exitosa!")
        else:
            print("Necesitas al menos 2 objetos de tipo 'Material' para fabricar algo.")

    def descansar(self):
        print("\nTe sientas a descansar un momento...")
        suerte = random.randint(1, 10)
        if suerte <= 3: 
            print("¡Un animal te ataco mientras dormias!")
            self.vida = self.vida - 15
        else:
            print("Descansaste bien. Recuperas 30 de energia.")
            self.energia = self.energia + 30


nom = input("Introduce el nombre de tu aventurero: ")
Aventurero(nom)