class Alumno:
    def inicializar(self, nom, nt):
        self.nombre = nom
        self.nota = nt
    
    def Mostrar(self):
        print("Nombre",self.nombre)
        print("Nota:",self.nota)
    
    def Evaluar(self):
        if self.nota>=6:
            print("el alumno:aprobo")
        else:
            print("el alumno:no aprobo")
alumno1 = Alumno()
alumno1.inicializar("Ignacio", 5) 
alumno1.Mostrar()
alumno1.Evaluar()

    
    
    
            
    