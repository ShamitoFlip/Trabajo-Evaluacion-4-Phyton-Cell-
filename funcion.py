#FUNCIONES DE MENU
def menu():
    while True:    
        try: 
            opc = int(input("********** MENU **********\n"
                "1. Inicializar Base de datos\n"
                "2. Cerrar programa\n"
                "opcion: "))     
            if opc >=1 and opc <= 2:
                return opc
            else:
                print("Ingrese '1' para inciar la base de datos o '2' para cerrar el programa")
        except:
            print("\nIngrese valores numericos\n")

def submenu():
    while True:
        try:   
            opc = int(input("\n************** PHYTONCELL **************\n"
                    "1. Agregar cliente o registro de llamada\n"
                    "2. Eliminar cliente o registro de llamada\n"
                    "3. Actualizar Datos\n"
                    "4. Mostrar todos los datos de la base de datos\n"
                    "5. Mostrar los datos filtrados por rut\n"
                    "6. Consultas BD\n"  
                    "7. Cerrar conexion a la base de datos\n"
                    "opcion: "))
            if opc >=1 and opc <= 7:
                return opc
            else:
                print("Ingrese del '1' al '7' para manejar el menu")
        except:
            print("\nIngrese valores numericos\n")

def subMenu1():
    while True:
        try:
            opc = int(input("\n***** ELEGIR UNA OPCION *****\n"
                "1. Cliente \n"
                "2. Registro de llamadas\n"
                "3. Devolver\n"
                "opcion: "))
            if opc >=1 and opc <= 3:
                return opc
            else:
                print("Ingrese del '1' al '3' para manejar el menu")
        except:
            print("\nIngrese valores numericos\n")

def subMenu2():
    while True:
        try:
            opc = int(input("\n***** ELEGIR UNA OPCION *****\n"
                "1. Cliente \n"
                "2. Registro de llamadas\n"
                "3. Mostrar ambos\n"
                "4. Devolver\n"
                "opcion: "))

            if opc >=1 and opc <= 7:
                return opc
            else:
                print("Ingrese del '1' al '4' para manejar el menu")
        except:
            print("\nIngrese valores numericos\n")

def subMenu3(opc):
    if opc == 1:
        while True:
            try:   
                opc1 = int(input("\n***** ACTUALIZAR *****\n"
                    "1. Modificar Nombre\n"
                    "2. Modificar Pais\n"
                    "3. devolver\n"
                    "opcion: "))
                if opc1 >=1 and opc1 <= 3:
                    return opc1
                else:
                    print("Ingrese del '1' al '3' para manejar el menu")
            except:
                print("\nIngrese valores numericos\n")
    elif opc == 2:
        while True:
            try:   
                opc1 = int(input("\n***** ACTUALIZAR *****\n"
                "1. Modificar Numero de telefono\n"
                "2. Modificar Duracion\n"
                "3. Modificar Fecha\n"
                "4. devolver\n"
                "opcion: "))
                if opc1 >=1 and opc1 <= 4:
                    return opc1
                else:
                    print("Ingrese del '1' al '4' para manejar el menu")
            except:
                print("\nIngrese valores numericos\n")

def menuConsulta():
    while True:
        try:
            opc = int(input("\n***** ELEGIR CONSULTA *****\n"
                "1. Buscar llamada por rut del cliente\n"
                "2. Listado de paises de los clientes registrados\n"
                "3. Total de minutos de llamada por cliente\n"
                "4. Telefonos utilizados por clientes de un pais especifico\n"
                "5. Devolver\n"
                "opcion: "))
            if opc >=1 and opc <= 5:
                return opc
            else:
                print("Ingrese del '1' al '5' para manejar el menu")
        except:
            print("\nIngrese valores numericos\n")

#FUNCIONES PARA EL CRUD Y CONSULTAS
def datosCliente():
    while True:
        nombre = input("Ingrese Nombre del cliente: ").upper().strip()
        if nombre:
            break
    while True:
            apellido = input("Ingrese Apellido del cliente: ").upper().strip()
            if apellido:
                break
    nombreCompleto = nombre + " " + apellido
        
    while True:
        pais = input("Ingrese Pais para el nuevo cliente: ").upper().strip()
        if pais:
                break
    return([nombreCompleto ,pais])

def datosRegistro(cliente_id):
    while True:
        try:
            duracion    = int(input("REGISTRAR DURACION DE LA LLAMADA (MIN): "))
            if duracion >= 0:
                break
            else:
                print("\n-----------------------------------------------------------------------------")
                print("El numero ingresado no puede ser -1 o inferior\n")
                print("-----------------------------------------------------------------------------\n")
            break
        except:
            print("\n-----------------------------------------------------------------------------")
            print("Caracter ingresado invalido")
            print("-----------------------------------------------------------------------------\n")

    print("\n-----------------------------------------------------------------------------")
    print("************************ INGRESAR FECHA (dd/mm/yyyy) ************************")
    print("-----------------------------------------------------------------------------")
    while True:
        try:
            dd = int(input("INGRESAR DIA (dd): "))   
            if dd <= 31 and dd > 0:
                break
            else:
                print("\n-----------------------------------------------------------------------------")
                print("Ingresar valor dentro del rango(1-31)\n")
                print("-----------------------------------------------------------------------------\n") 
        except:
            print("\n-----------------------------------------------------------------------------")
            print("Volver a intentar caracter invalido")
            print("-----------------------------------------------------------------------------\n")     
    while True:
        try: 
            mm = int(input("INGRESAR MES (mm): ")) 
            if mm <= 12 and mm > 0: 
                break
            else:
                print("\n-----------------------------------------------------------------------------")
                print("Ingresar valor dentro del rango(1-12)\n")
                print("-----------------------------------------------------------------------------\n")
        except:
            print("\n-----------------------------------------------------------------------------")
            print("Volver a intentar caracter invalido")
            print("-----------------------------------------------------------------------------\n") 
    while True:
        try:
            yyyy = int(input("INGRESAR AÑO (yyyy): ")) 
            if yyyy < 2025 and yyyy > 1990: 
                break
            else:
                print("\n-----------------------------------------------------------------------------")
                print("Fuera del limite (Registros desde la fecha 1990 al año actual 2024)")
                print("-----------------------------------------------------------------------------\n")
        except:
            print("\n-----------------------------------------------------------------------------")
            print("Volver a intentar caracter invalido")
            print("-----------------------------------------------------------------------------\n") 

    fecha = f"{dd}/{mm}/{yyyy}"
    return([duracion,fecha,cliente_id])

def fecha():
    print("\n-----------------------------------------------------------------------------")
    print("****************** FECHA QUE SE DESEA BUSCAR (dd/mm/yyyy) *********************")
    print("-----------------------------------------------------------------------------")
    while True:
        try:
            dd = int(input("INGRESAR DIA (dd): "))   
            if dd <= 31 and dd > 0:
                break
            else:
                print("\n-----------------------------------------------------------------------------")
                print("Ingresar valor dentro del rango(1-31)\n")
                print("-----------------------------------------------------------------------------\n") 
        except:
            print("\n-----------------------------------------------------------------------------")
            print("Volver a intentar caracter invalido")
            print("-----------------------------------------------------------------------------\n")     
    while True:
        try: 
            mm = int(input("INGRESAR MES (mm): ")) 
            if mm <= 12 and mm > 0: 
                break
            else:
                print("\n-----------------------------------------------------------------------------")
                print("Ingresar valor dentro del rango(1-12)\n")
                print("-----------------------------------------------------------------------------\n")
        except:
            print("\n-----------------------------------------------------------------------------")
            print("Volver a intentar caracter invalido")
            print("-----------------------------------------------------------------------------\n") 
    while True:
        try:
            yyyy = int(input("INGRESAR AÑO (yyyy): ")) 
            if yyyy < 2025 and yyyy > 1990: 
                break
            else:
                print("\n-----------------------------------------------------------------------------")
                print("Fuera del limite (Registros desde la fecha 1990 al año actual 2024)")
                print("-----------------------------------------------------------------------------\n")
        except:
            print("\n-----------------------------------------------------------------------------")
            print("Volver a intentar caracter invalido")
            print("-----------------------------------------------------------------------------\n") 
    fecha = f"{dd}/{mm}/{yyyy}"
    return([
        fecha])

def leerNumero():
    print("\n----------------------------------------------------------------------------")
    print("***************************** REGISTRAR LLAMADA *****************************")
    print("-----------------------------------------------------------------------------")
    while True:
        numero = input("REGISTRAR NUMERO CELULAR(+569XXXXXXXX): ").strip()

        if numero:
            if len(numero)<=7:
                print("\n-----------------------------------------------------------------------------")
                print("El numero ingresado como minimo debe ser mayor a 7 digitos")
                print("-----------------------------------------------------------------------------\n")
            elif len(numero)>=16:
                print("\n-----------------------------------------------------------------------------")
                print("El numero excede el limite de largo, debe ser menor a 17 digitos")
                print("-----------------------------------------------------------------------------\n")
            else:
                break
    return numero

def leerTexto(mensaje):
    while True:
        texto = input(f"{mensaje}: ").strip()
        if texto:
            return texto.upper()
        else:
            print("No puede quedar vacio el campo, intente de nuevo. ")

def nuevoDato(mod,opc):
    if opc == 1:
        match mod:
            case 1:
                while True:
                    nombre = input("Ingrese Nombre del cliente: ").upper().strip()
                    if nombre:
                        break
                while True:
                    apellido = input("Ingrese Apellido del cliente: ").upper().strip()
                    if apellido:
                        break
                nombreCompleto = nombre + " " + apellido
                return nombreCompleto
            case 2:
                while True:
                    pais = input("Ingrese Pais para el nuevo cliente: ").upper().strip()
                    if pais:
                        break   
                return pais
    elif opc == 2:
        match mod:
            case 1:
                while True:
                    numero = input("REGISTRAR NUEVO NUMERO CELULAR(+569XXXXXXXX): ").upper().strip()
                    if len(numero)<=7:
                        print("\n-----------------------------------------------------------------------------")
                        print("El numero ingresado como minimo debe ser mayor a 7 digitos")
                        print("-----------------------------------------------------------------------------\n")
                    elif len(numero)>=16:
                        print("\n-----------------------------------------------------------------------------")
                        print("El numero excede el limite de largo, debe ser menor a 17 digitos")
                        print("-----------------------------------------------------------------------------\n")
                    else:
                        break
                return numero
            case 2:
                try:
                    while True:
                        duracion    = int(input("NUEVA DURACION DE LA LLAMADA(MIN): "))
                        if duracion >= 0:
                            break
                        else:
                            print("\n-----------------------------------------------------------------------------")
                            print("El numero ingresado no puede ser -1 o inferior\n")
                            print("-----------------------------------------------------------------------------\n")
                            break
                except:
                    print("\n-----------------------------------------------------------------------------")
                    print("Caracter ingresado invalido")
                    print("-----------------------------------------------------------------------------\n")
                return duracion
            case 3:
                while True:
                    try:
                        dd = int(input("INGRESAR DIA (dd): "))   
                        if dd <= 31 and dd > 0:
                            break
                        else:
                            print("\n-----------------------------------------------------------------------------")
                            print("Ingresar valor dentro del rango(1-31)\n")
                            print("-----------------------------------------------------------------------------\n") 
                    except:
                        print("\n-----------------------------------------------------------------------------")
                        print("Volver a intentar caracter invalido")
                        print("-----------------------------------------------------------------------------\n")     
                while True:
                    try: 
                        mm = int(input("INGRESAR MES (mm): ")) 
                        if mm <= 12 and mm > 0: 
                            break
                        else:
                            print("\n-----------------------------------------------------------------------------")
                            print("Ingresar valor dentro del rango(1-12)\n")
                            print("-----------------------------------------------------------------------------\n")
                    except:
                        print("\n-----------------------------------------------------------------------------")
                        print("Volver a intentar caracter invalido")
                        print("-----------------------------------------------------------------------------\n") 
                while True:
                    try:
                        yyyy = int(input("INGRESAR AÑO (yyyy): ")) 
                        if yyyy < 2025: 
                            break
                        else:
                            print("\n-----------------------------------------------------------------------------")
                            print("Fuera del limite (menor o igual a 2024)\n")
                            print("-----------------------------------------------------------------------------\n")
                    except:
                        print("\n-----------------------------------------------------------------------------")
                        print("Volver a intentar caracter invalido")
                        print("-----------------------------------------------------------------------------\n") 

                fecha= f"{dd}/{mm}/{yyyy}"
                return fecha              
            
            case 4:
                return input("Ingresa el nuevo Id Foraneo")

def leerRut():
    while True:
        rut = input("Ingrese RUT(XXXXXXXX-X): ").upper().strip()
        if rut:
            validar = validacionRut(rut)
            if  validar != None:
                break
    return rut

def validacionRut(rut):
    lista = ['1','2','3','4','5','6','7','8','9','0','K','-']
    list_InvCharacter=[]
    listaRut=[]
    #Validar contenido
    for item in rut:
        if item in lista:
            listaRut.append(item)
            estado = True
        else:
            for item in rut:
                if item not in lista:
                    list_InvCharacter.append(item)
                    estado = False
            break
    if estado == True:
        if  len(rut) == 10 : #Validar el largo del rut
            if rut.find("-") == 8: #Validadr posicion del guion 
                if rut.find("K") == 9:
                    if digitoVerificadorRut(listaRut):
                        return rut
                    else:
                        print("RUT INCORRECTO")
                elif rut.find("K") == -1:
                    if digitoVerificadorRut(listaRut):
                        return rut
                    else:
                        print("RUT INCORRECTO")
                else:
                    print("Ingreso la letra K en la posicion incorrecta")
            else:
                print("Falta el guion o no se encuentra en la posicion correcta")

        elif len(rut) == 9:
            if rut.find("-") == 7:
                if rut.find("K") == 8:
                    if digitoVerificadorRut(listaRut):
                        return rut
                    else:
                        print("RUT INCORRECTO")
                elif rut.find("K") == -1:
                    if digitoVerificadorRut(listaRut):
                        return rut
                    else:
                        print("RUT INCORRECTO")
                else:
                    print("Ingreso la letra K en la posicion incorrecta")
            else:
                print("Falta el guion o no se encuentra en la posicion correcta")

        elif  len(rut) < 9:
            print("El rut es muy corto")
        else:
            print("El rut es muy largo")
    else:
        print(f"Error! Caracteres invalidos {list_InvCharacter}")

def digitoVerificadorRut(rut):
    listaMulDv1= [3,2,7,6,5,4,3,2]
    listaMulDv2= [2,7,6,5,4,3,2]
    listaVerificadora=[]
    n= sumaTotal = salir = 0
    if len(rut) == 10 :
        for item in rut:
            salir+=1
            listaVerificadora.append(int(item))
            if salir == 8:
                break
        for item in listaVerificadora:
            mult=listaMulDv1[n]*listaVerificadora[n]
            sumaTotal+=mult
            n+=1
        dv = 11-(sumaTotal%11)
        if str(dv) == rut[9]:
            return True
        elif dv == 10 and rut[9] == 'K' :
            return True
        elif dv == 11 and rut[9] == '0' :
            return True
    else:
        for item in rut:
            salir+=1
            listaVerificadora.append(int(item))
            if salir == 7:
                break
        for item in listaVerificadora:
            mult=listaMulDv2[n]*listaVerificadora[n]
            sumaTotal+=mult
            n+=1
        dv = 11-(sumaTotal%11)
        if str(dv) == rut[8] or dv == 1:
            return True
        elif dv == 10 and rut[8] == 'K' :
            return True
        elif dv == 11 and rut[8] == '0' :
            return True

def switchClient(num):
    if num == 1:
        return "Cliente "
    else:
        return "Clientes"

#ART ASCII
def fin():
    print(".-----------------.      ------.       .--------             .-----:")     
    print("+@@@@@@@@@@@@@@@@@-      @@@@@@=       +@@@@@@@@%.           =@@@@@*")    
    print("+@@@@@@@@@@@@@@@@@-      @@@@@@=       +@@@@@@@@@%           =@@@@@*")     
    print("+@@@@@@+==========.      @@@@@@=       +@@@@@@@@@@%.         =@@@@@*")    
    print("+@@@@@%                  @@@@@@=       +@@@@@%@@@@@@:        =@@@@@*")     
    print("+@@@@@%                  @@@@@@=       +@@@@@:+@@@@@@=       =@@@@@*")     
    print("+@@@@@%                  @@@@@@=       +@@@@@- -@@@@@@*      =@@@@@*")     
    print("+@@@@@@+=========:       @@@@@@=       +@@@@@=  :@@@@@@#     =@@@@@*")     
    print("+@@@@@@@@@@@@@@@@+       @@@@@@=       +@@@@@+   :@@@@@@%.   =@@@@@*")     
    print("+@@@@@@@@@@@@@@@@+       @@@@@@=       +@@@@@+    :@@@@@@@:  -@@@@@*")     
    print("+@@@@@%----------.       @@@@@@=       +@@@@@+     .%@@@@@@- -@@@@@*")     
    print("+@@@@@%                  @@@@@@=       +@@@@@+       #@@@@@@+:@@@@@*")     
    print("+@@@@@%                  @@@@@@=       +@@@@@+        +@@@@@@%@@@@@*")     
    print("+@@@@@%                  @@@@@@=       +@@@@@+         =@@@@@@@@@@@*")   
    print("+@@@@@%                  @@@@@@=       +@@@@@+          -@@@@@@@@@@*")     
    print("+@@@@@%                  @@@@@@=       +@@@@@+           :@@@@@@@@@*")     
    print("-*****+                  ******:       -*****-            .********=")    

pritn("")