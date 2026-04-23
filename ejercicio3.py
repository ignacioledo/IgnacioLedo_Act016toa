class Triangulo:
    def Inicializar(self,l1,l2,l3):
        self.lado1 = l1
        self.lado2 = l2
        self.lado3 = l3
    def Mostrar_lados(self):
        print("Lado1:",self.lado1)
        print("Lado2:",self.lado2)
        print("Lado3:",self.lado3)
    def Mostrar_mayor(self):
        if self.lado1 >= self.lado2 and self.lado1 >= self.lado3:
            mayor = self.lado1
        elif self.lado2 >= self.lado1 and self.lado2 >= self.lado3:
            mayor = self.lado2
        else:
            mayor = self.lado3
        
        print("el lado mayor del triangulo es:",mayor)
    def Tipo_triangulo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print(" Es un triángulo Equilátero")
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3:
            print(" Es un triángulo Escaleno")
        else:
            print(" Es un triangulo isósceles")
triangulo1 = Triangulo()
triangulo1.Inicializar(11,11,10) 
triangulo1.Mostrar_lados()
triangulo1.Mostrar_mayor()
triangulo1.Tipo_triangulo()     
            
            
            
        
        