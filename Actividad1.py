class Coche:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__combustible = 100  #Comenzamos siempre en 100

    def conducir(self, km):
        litros_usados = km / 10  # Cada 10 km usa 1 litro
        if self.__combustible >= litros_usados:
            self.__combustible -= litros_usados
            print(f"Has conducido {km} km. Combustible restante: {self.__combustible} litros.")
        else:
            print("No hay suficiente combustible para conducir esa distancia.")

    def repostar(self, litros):
        if self.__combustible + litros > 100:
            self.__combustible = 100  # Máximo 100 litros
            print("Tanque lleno.")
        else:
            self.__combustible += litros
            print(f"Has añadido {litros} litros. Combustible.actual: {self.__combustible} litros.")

    def estado(self):
        print(f"Combustible restante: {self.__combustible} litros.")

   
    def obtener_marca(self):
        return self.__marca

    def obtener_modelo(self):
        return self.__modelo

# Funcion del menu
def menu():
    print("Bienvenido usuario")
    
    
    marca = input("Ingrese la marca del coche: ")
    modelo = input("Ingrese el modelo del coche: ")
    while marca == "" or modelo == "":
        print("La marca y el modelo no pueden estar vacíos. Intente nuevamente.")
        marca = input("Ingrese la marca del coche: ")
        modelo = input("Ingrese el modelo del coche: ")

    
    mi_coche = Coche(marca, modelo)#Donde viviran los datos del usuario ingresados

    while True:
        print("\n Menu de interaccion")
        print(f"Coche: {mi_coche.obtener_marca()} {mi_coche.obtener_modelo()}")
        print("1. Conducir")
        print("2. Repostar combustible")
        print("3. Mostrar estado del coche")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            km = input("Ingrese la cantidad de kilometros a conducir: ")
            if km.isdigit():
                mi_coche.conducir(float(km))
            else:
                print("Por favor, ingrese un número valido.")
        elif opcion == "2":
            litros = input("Ingrese la cantidad de litros a repostar: ")
            if litros.isdigit():
                mi_coche.repostar(float(litros))
            else:
                print("Por favor, ingrese un numero valido.")
        elif opcion == "3":
            mi_coche.estado()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, intente de nuevo.")
menu()