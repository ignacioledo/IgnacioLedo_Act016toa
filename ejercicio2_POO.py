class Persona:
    def inicializar(self, nom, ed):
        self.nombre = nom
        self.edad = ed
        
    def Mostrar(self):
        print("Nombre",self.nombre)
        print("Edad:",self.edad)
    
    def Evaluar(self):
        if self.edad>=18:
            print("la persona es mayor de edad")
        else:
            print("la persona no es mayor de edad")
Persona1 = Persona()
Persona1.inicializar("Ignacio", 15) 
Persona1.Mostrar()
Persona1.Evaluar()    