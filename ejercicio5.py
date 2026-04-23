class Agenda:
    def __init__(self):
        self.contactos = []
        self.menu
    def menu(self):
        opcion = ""
        while opcion != "5":
            print("---AGENDA DE CONTACTOS---")
            print("1.Añadir contacto")
            print("2.Lista de contactos")
            print("3.Buscar contacto")
            print("4.Editar contacto")
            print("5.Cerrar agenda")
            
            opcion = input("Elija una opcion:")
            
            if opcion == "1":
                self.añadir()
            elif opcion == "2":
                self.listar()
            elif opcion == "3":
                self.buscar()
            elif opcion == "4":
                self.editar()
            elif opcion == "5":
                print("Saliendo de la agenda")
            else:
                print("Opcion no valida, intente de nuevo")
    def añadir(self):
        print("---Nuevo Contacto---")
        nombre = input("Nombre:")
        telefono = input("Telefono:")
        email = input("Email:")
        self.contactos.append({"nombre":nombre,"telefono":telefono,"email":email})
        print("se guardo correctamente")
    def listar(self):
        print("---LISTA DE CONTACTOS---")
        if len(self.contactos) > 0:
            for i,c in enumerate(self.contactos):
                print(f"{i}.{c["nombre"]}| {c["telefono"]}| c{["email"]}")
        else:
            print("no se registra ningun contacto")
    def buscar(self):
        nom_buscar = input("Nombre a buscar:")
        for c in self.contactos:
            if nom_buscar == c["n"]:
                print("Encntrado:",c["n"], c["t"],c["e"])
    def editar(self):
        if len(self.contactos) == 0:
            print("no hay contactos")
        else:
            indice = int(input("ID a editar: "))
            self.contactos[indice]["n"] = input("nuevo nombre:")
            self.contactos[indice]["t"] = input("nuevo telefono:")
            self.contactos[indice]["e"] = input("nuevo email:")
            print("se edito correctamente")
Agenda()
            
            