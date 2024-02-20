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

def menu(diccionario:dict, num_usuarios:int):
    # En el reto del viernes este código estará mejor ordenado con sus correspondientes funciones
    print(f"----------MENÚ----------")
    print("A. - Registrar nuevos usuarios")
    print("B. - Listar los usuarios")
    print("C. - Editar usuarios")
    opcion = str(input("\nElija una opcion: "))
    if opcion == "A" or opcion == "a":
            nombre = str(input("Ingrese su nombre: "))
            mi_nombre = validacion(variable=nombre, min=5, max=50, id="nombre")
            apellidos = str(input("Ingrese sus apellidos: "))
            mis_apellidos = validacion(variable=apellidos, min=5, max=50, id="apellidos")
            telefono = str(input("Ingrese su número de teléfono: "))
            mi_telefono = validacion(variable=telefono, min=10, max=10, id="telefono")
            correo = str(input("Ingrese su correo electrónico: "))
            mi_correo = validacion(variable=correo, min=5, max=50, id="correo")

            num_usuarios += 1
            diccionario[num_usuarios] = {"nombre": mi_nombre, "apellidos": mis_apellidos, "telefono": mi_telefono,
                                     "correo": mi_correo}

    elif opcion == "B" or opcion == "b":
        print("A. - Listar IDs de los usuarios")
        print("B. - Listar datos de un usuario concreto")
        opcion = str(input("\nElija una opcion: "))
        if opcion == "A" or opcion == "a":
            print(sorted(diccionario.keys()))
        else:
            print(f"\nIDs de usuarios: {sorted(diccionario.keys())} ")
            id = int(input("Introduzca el ID a filtrar: "))
            print(f"\nNombre: {diccionario[id]['nombre']}\nApellidos: {diccionario[id]['apellidos']}\n"
                  f"Telefono: {diccionario[id]['telefono']}\nCorreo: {diccionario[id]['correo']}")

    else:
        print(f"\nIDs de usuarios: {sorted(diccionario.keys())} ")
        id = int(input("Introduzca el ID del usuario a editar: "))
        del diccionario[id]
        nombre = str(input("Ingrese su nombre: "))
        mi_nombre = validacion(variable=nombre, min=5, max=50, id="nombre")
        apellidos = str(input("Ingrese sus apellidos: "))
        mis_apellidos = validacion(variable=apellidos, min=5, max=50, id="apellidos")
        telefono = str(input("Ingrese su número de teléfono: "))
        mi_telefono = validacion(variable=telefono, min=10, max=10, id="telefono")
        correo = str(input("Ingrese su correo electrónico: "))
        mi_correo = validacion(variable=correo, min=5, max=50, id="correo")

        diccionario[id] = {"nombre": mi_nombre, "apellidos": mis_apellidos, "telefono": mi_telefono,
                                 "correo": mi_correo}

    print("\n¿ Desea salir del programa ?")
    opcion2 = input("1. - SÍ\n2. - NO\n")
    if opcion2 in ["1", "si", "sí", "SI", "SÍ"]:
        exit()
    else:
        menu(diccionario, num_usuarios)

if __name__ == "__main__":
    usuarios = {}
    menu(usuarios, 0)