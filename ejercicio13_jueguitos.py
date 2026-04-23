import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0

    def lanzar_dado(self):
        # El dado tiene 6 caras
        tiro = random.randint(1, 6)
        self.puntos = self.puntos + tiro
        return tiro

class JuegoDados:
    def __init__(self):
        self.rivales = []
        self.rondas_totales = 3 # Vamos a jugar 3 rondas
        
        print("--- BIENVENIDO AL DESAFIO DE DADOS ---")
        nom = input("Tu nombre de jugador: ")
        self.usuario = Jugador(nom)
        
        # Agregamos dos rivales automaticos a la lista
        self.rivales.append(Jugador("Pedro"))
        self.rivales.append(Jugador("Ana"))
        
        self.empezar()

    def empezar(self):
        ronda_actual = 1
        
        while ronda_actual <= self.rondas_totales:
            print("\n" + "-"*20)
            print("RONDA NUMERO:", ronda_actual)
            input("Presiona ENTER para lanzar tu dado...")
            
            # Turno del usuario
            sacaste = self.usuario.lanzar_dado()
            print("Sacaste un:", sacaste)
            print("Tu puntaje total es:", self.usuario.puntos)
            
            # Turno de los rivales
            print("\nTurno de los demas...")
            for r in self.rivales:
                tiro_r = r.lanzar_dado()
                print(r.nombre, "saco un", tiro_r, "| Total:", r.puntos)
            
            ronda_actual = ronda_actual + 1

        self.finalizar()

    def finalizar(self):
        print("\n" + "="*30)
        print("RESULTADOS FINALES:")
        print(self.usuario.nombre, ":", self.usuario.puntos, "puntos")
        ganador_nombre = self.usuario.nombre
        max_puntos = self.usuario.puntos
        
        for r in self.rivales:
            print(r.nombre, ":", r.puntos, "puntos")
            if r.puntos > max_puntos:
                max_puntos = r.puntos
                ganador_nombre = r.nombre
        
        print("\nEL GANADOR ES:", ganador_nombre)
        print("GAME OVER")

JuegoDados()