class CuentaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0  

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se han depositado {cantidad} unidades. Saldo actual: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a 0.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if self.__saldo >= cantidad:
                self.__saldo -= cantidad
                print(f"Has retiradoo {cantidad} unidades. Saldo actual: {self.__saldo}")
            else:
                print("Saldo insuficiente para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser mayorw a 0.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")

    def obtener_titular(self):
        return self.__titular

def menu():
    print("Bienvenido al sistema bancario.")

    titular = input("Ingrese el nombre del titular de la cuenta: ").strip()
    while not titular:
        print("El titular no puede estar vacio. Intente nuevamente.")
        titular = input("Ingrese el nombre del titular de la cuenta: ").strip()

    cuenta = CuentaBancaria(titular)

    while True:
        print("\nMenu")
        print(f"Cuenta de: {cuenta.obtener_titular()}")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar saldo")
        print("4. Salir")
        
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            cantidad = input("Ingrese la cantidad a depositar: ")
            if cantidad.isdigit():
                cuenta.depositar(float(cantidad))
            else:
                print("Por favor, ingrese un número valido.")
        elif opcion == "2":
            cantidad = input("Ingrese la cantidad a retirar: ")
            if cantidad.isdigit():
                cuenta.retirar(float(cantidad))
            else:
                print("Por favor, ingrese un número valido.")
        elif opcion == "3":
            cuenta.mostrar_saldo()
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opcioon no valida: Profavor intente de nuevo.")


menu()