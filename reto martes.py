def validacion (variable, min:int, max:int, id:str):
    while (len(variable) < min) or (len(variable) > max):
        tipo_variable = type(variable)
        if id == "apellidos":
            print(f"Sus {id} deben tener entre {min} y {max} caracteres")
            variable = tipo_variable(input(f"Introduzca de nuevo sus {id}: "))
        elif id == "telefono":
            print(f"Su {id} debe tener {max} dígitos")
            variable = tipo_variable(input(f"Introduzca de nuevo su {id}: "))
        else:
            print(f"Su {id} debe tener entre {min} y {max} caracteres")
            variable = tipo_variable(input(f"Introduzca de nuevo su {id}: "))
    return variable

n = int(input("Introduzca cuantos usuarios desea crear: "))
contador = 1

while contador <= n:
    print(f"----------Usuario {contador}----------")
    nombre = str(input("Ingrese su nombre: "))
    mi_nombre = validacion(variable = nombre, min = 5, max = 50, id = "nombre")
    apellidos = str(input("Ingrese sus apellidos: "))
    mis_apellidos = validacion(variable = apellidos, min = 5, max = 50, id = "apellidos")
    telefono = str(input("Ingrese su número de teléfono: "))
    mi_telefono = validacion(variable = telefono, min = 10, max = 10, id = "telefono")
    correo = str(input("Ingrese su correo electrónico: "))
    mi_correo = validacion(variable = correo, min = 5, max = 50, id = "correo")
    contador += 1