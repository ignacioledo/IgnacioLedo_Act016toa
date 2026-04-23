class Cuenta:
    def __init__(self,titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad
    def imprimir_datos(self):
        print("Titular",self.titular)
        print("Cantidad",self.cantidad)

class CajaAhorro(Cuenta):
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
    def mostrar_informacion(self):
        print("---INFO CAJA DE AHORRO---")
        self.imprimir_datos()

class PlazoFijo(Cuenta):
    def __init__(self,titular,cantidad,plazo,interes):
        super().__init__(titular,cantidad)
        self.plazo = plazo
        self.interes = interes
    def obtener_importe_interes(self):
        return self.cantidad * self.interes/100
    
    def mostrar_informacion(self):
        print("---INFO PLAZO FIJO---")
        self.imprimir_datos()
        print("PLAZO;",self.plazo)
        print("INTERES %:",self.interes)
        print("total de interes",self.obtener_importe_interes())
caja = CajaAhorro("Juan Perez",5000)
caja.mostrar_informacion()

print("-"*30)

plazo = PlazoFijo("Maria Garcia",10000,30,5.5)
plazo.mostrar_informacion()

        
    