
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

# Función del menú principal
def menu():
    print("Seleccione la conversión que desea realizar:")
    print("1. Fahrenheit a Celsius")
    print("2. Celsius a Fahrenheit")
    print("3. Celsius a Kelvin")
    print("4. Kelvin a Celsius")
    
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        fahrenheit = float(input("Ingrese los grados Fahrenheit: "))
        resultado = fahrenheit_a_celsius(fahrenheit)
        print(f"{fahrenheit}°F equivalen a {resultado:.2f}°C")
    
    elif opcion == "2":
        celsius = float(input("Ingrese los grados Celsius: "))
        resultado = celsius_a_fahrenheit(celsius)
        print(f"{celsius}°C equivalen a {resultado:.2f}°F")

    elif opcion == "3":
        celsius = float(input("Ingrese los grados Celsius: "))
        resultado = celsius_a_kelvin(celsius)
        print(f"{celsius}°C equivalen a {resultado:.2f}K")

    elif opcion == "4":
        kelvin = float(input("Ingrese los grados Kelvin: "))
        resultado = kelvin_a_celsius(kelvin)
        print(f"{kelvin}K equivalen a {resultado:.2f}°C")

    else:
        print("Opcion no valida")

menu()