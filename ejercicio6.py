class Cliente:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cantidad = 0
    def depositar(self,monto):
        self.cantidad = self.cantidad + monto
    def extraer(self,monto):
        self.cantidad = self.cantidad - monto
    def Mostrar_total(self):
        print(self.nombre,"tiene acumulado:",self.cantidad)
class Banco(Cliente):
    def __init__(Cliente):
        self.cliente1 = Cliente("juan")
        self.cliente2 = Cliente("walter")
        self.cliente3 = Cliente("santiago")
    def operar(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(500)
        self.cliente3.depositar(200)
        self.cliente1.etraer(200)
    def deposito_total(self):
        total = self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad
        print("Total depositado en el banco",total)
        self.cliente1.mostrar_total()
        self.cliente2.mostrar_total()
        self.cliente3.mostrar_total()
        
mi_banco = Banco()
mi_banco.operar()
mi_banco.deposito_total
    