import random
class Personaje:
    def __init__(self, nombre, vida, daño):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño

    def atacar(self, objetivo):
        suerte = random.randint(1, 100)
        daño_final = self.daño

        if suerte <= 20: 
            daño_final = self.daño * 1.5 
            print("¡GOLPE CRÍTICO! 💥")
        print(self.nombre, "ataca a", objetivo.nombre, "causando", daño_final, "de daño")
        objetivo.vida = objetivo.vida - daño_final

    def esta_vivo(self):
        return self.vida > 0
print("--- DUELO EN LA ARENA ---")
nombre_usuario = input("Nombre de tu personaje: ")
jugador = Personaje(nombre_usuario, 100, 15)
rival = Personaje("Rival", 100, 12)

while jugador.esta_vivo() and rival.esta_vivo():
    print("Tu Vida:", jugador.vida, "| Vida Rival:", rival.vida)
    print("1. Atacar | 2. Esperar")
    opcion = input("Acción: ")

    if opcion == "1":
        jugador.atacar(rival)
    if rival.esta_vivo():
        print("Turno del enemigo...")
        rival.atacar(jugador)

print("\n" + "="*20)
if jugador.esta_vivo():
    print("¡GANASTE!")
else:
    print("PERDISTE")

print("GAME OVER")