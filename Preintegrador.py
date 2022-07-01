
from prettytable import PrettyTable
#id nombre apellido edad comision
#1  rodol  giaco    25    1
#lista -> [persona1,persona2,persona3]
#persona = {"id":1,"Nombre":Rodol......}
#menu -> agregar, ver, eliminar salir

def comprobar(elemento):
        personas_aux= personas.copy() 
        elemento_aux = elemento.copy()

        for i in personas_aux:
            i["id"] = 1
        elemento_aux["id"] = 1
        if elemento_aux in personas_aux:
            print("Esta persona ya existe!")
        else:
            personas.append(elemento)
             

def agregar():
    print("Usted selecciono agregar personas")
    diccionario = dict.fromkeys(encabezados,"")
    for claves in diccionario:
        if claves == "id":
           diccionario[claves] = len(personas)+1 
        elif claves == "edad" or claves == "comision":
            diccionario[claves] = int(input(f"Ingresar {claves}:")) 
        else:
            dato = input(f"ingrese {claves}:")
            diccionario[claves] = dato
    if len(personas) > 0:
        comprobar(diccionario)
    else:
        personas.append(diccionario)
    

def ver():
    print("Usted selecciono ver personas")
    if len(personas) > 0:
        tabla = PrettyTable()
        tabla.field_names = encabezados
        for diccionarios in personas:
            tabla.add_row(diccionarios.values())
        print(tabla)
    else:
        print("Lista vacia!!!!!")

personas = []
encabezados = ["id", "nombre", "apellido", "edad", "comision"]



while True:
    print("BIENVENIDOS AL REGISTRO DE PERSONAS")
    opcion = int(input("""Seleccionar opcion
1)_Agregar
2)_Ver
3)_Salir"""))

    if opcion == 1:
        agregar()
    elif opcion == 2:
        ver()
    elif opcion == 3:
        print("Adios!!")
        break
    else:
        print("Opcion Invalida!!")

    