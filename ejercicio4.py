class IngresoDatos:
    def __init__(self):
        print("Cargando valores...")
        self.valor1 = int(input("Ingresa el primer valor entero: "))
        self.valor2 = int(input("Ingresa el segundo valor entero: "))
class Calculadora(IngresoDatos):
    
    def sumar(self):
        resultado = self.valor1 + self.valor2
        print("La suma es:", resultado)

    def restar(self):
        resultado = self.valor1 - self.valor2
        print("La resta es:", resultado)

    def multiplicar(self):
        resultado = self.valor1 * self.valor2
        print("La multiplicación es:", resultado)

    def dividir(self):
        # Un if básico para que no tire error si ponen un 0
        if self.valor2 != 0:
            resultado = self.valor1 / self.valor2
            print("La división es:", resultado)
        else:
            print("Error: No se puede dividir por cero.")
mi_calculo = Calculadora()
mi_calculo.sumar()
mi_calculo.restar()
mi_calculo.multiplicar()
mi_calculo.dividir()