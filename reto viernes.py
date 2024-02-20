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

def new_user(diccionario:dict, posicion:int = 0):
    nombre = str(input("Ingrese su nombre: "))
    mi_nombre = validacion(variable=nombre, min=5, max=50, id="nombre")
    apellidos = str(input("Ingrese sus apellidos: "))
    mis_apellidos = validacion(variable=apellidos, min=5, max=50, id="apellidos")
    telefono = str(input("Ingrese su número de teléfono: "))
    mi_telefono = validacion(variable=telefono, min=10, max=10, id="telefono")
    correo = str(input("Ingrese su correo electrónico: "))
    mi_correo = validacion(variable=correo, min=5, max=50, id="correo")
    if posicion != 0:
        diccionario[posicion] = {"nombre": mi_nombre, "apellidos": mis_apellidos, "telefono": mi_telefono,
                                 "correo": mi_correo}
    else:
        diccionario[len(diccionario) + 1] = {"nombre": mi_nombre, "apellidos": mis_apellidos, "telefono": mi_telefono,
                                         "correo": mi_correo}
    return f"\nSe ha registrado el usuario {mi_nombre} {mis_apellidos} correctamente"

def show_user(ID:int, diccionario:dict):
    return(f"\nNombre: {diccionario[ID]['nombre']}\nApellidos: {diccionario[ID]['apellidos']}\n"
          f"Telefono: {diccionario[ID]['telefono']}\nCorreo: {diccionario[ID]['correo']}")

def list_user(diccionario:dict):
    usuarios = ""
    for valor in diccionario.values():
        usuarios += (f"\nNombre: {valor['nombre']}\nApellidos: {valor['apellidos']}\n"
          f"Telefono: {valor['telefono']}\nCorreo: {valor['correo']}\n")
    return usuarios

def delete_user(ID:int, diccionario:dict):
    del diccionario[ID]
    return f"\nSe ha eliminado el usuario {ID} correctamente"

def edit_user(ID:int, diccionario:dict):
    delete_user(ID, diccionario)
    new_user(diccionario, posicion = ID)
    return f"\nSe ha editado el usuario {ID} correctamente"

def menu(diccionario:dict):
    print(f"----------MENÚ----------")
    print("A. - Registrar nuevo usuarios")
    print("B. - Listar todos los usuarios")
    print("C. - Mostrar los datos de un usuario concreto")
    print("D. - Editar usuario")
    print("E. - Eliminar usuario")
    print("F. - Salir")

    opcion = str(input("\nElija una opcion: "))
    if opcion == "A" or opcion == "a":
        print(new_user(diccionario))

    elif opcion == "B" or opcion == "b":
        print(list_user(diccionario))

    elif opcion == "C" or opcion == "c":
        print(f"\nIDs de usuarios: {diccionario.keys()} ")
        id = int(input("Introduzca el ID a filtrar: "))
        print(show_user(id, diccionario))

    elif opcion == "D" or opcion == "d":
        print(f"\nIDs de usuarios: {diccionario.keys()} ")
        id = int(input("Introduzca el ID del usuario a editar: "))
        print(edit_user(id, diccionario))

    elif opcion == "E" or opcion == "e":
        if len(diccionario) != 0:
            print(f"\nIDs de usuarios: {diccionario.keys()} ")
            id = int(input("Introduzca el ID del usuario a editar: "))
            print(delete_user(id, diccionario))
        else:
            print(f"\nNo hay usuarios que eliminar")
    else:
        exit()

    print("\n¿ Desea salir del programa ?")
    opcion2 = input("1. - SÍ\n2. - NO\n")
    if opcion2 in ["1", "si", "sí", "SI", "SÍ"]:
        exit()
    else:
        menu(diccionario)

if __name__ == "__main__":
    usuarios = {}
    menu(usuarios)