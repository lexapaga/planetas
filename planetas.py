# Pedir al usuario su peso en la Tierra
weight_on_earth = float(input("Ingrese su peso en la Tierra (en kg): "))

# Crear un diccionario con la relación peso/gravedad en cada planeta
planet_gravity = {
    "Mercurio": 0.37,
    "Venus": 0.88,
    "Tierra": 1.0,
    "Marte": 0.38,
    "Jupiter": 2.64,
    "Saturno": 1.15,
    "Urano": 0.92,
    "Neptuno": 1.19
}

# Imprimir el peso del usuario en cada planeta
for planet, gravity in planet_gravity.items():
    weight_on_planet = weight_on_earth * gravity
    print(f"Su peso en {planet} es {weight_on_planet:.2f} kg")