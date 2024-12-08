import funcion as fun
from conexion import Conexion
from mysql.connector import Error

class Cliente(Conexion): #CLASE HIJA CON HERENCIA DESDE LA TABLA CONEXION(CLASE PADRE)
    def __init__(self):
        super().__init__()      

#CRUD PARA AMBAS TABLAS CLIENTE Y TELEFONO
    def insertData(self):
        try:
            if  self.conexion.is_connected():
                cursor = self.conexion.cursor()
                print("")
                rut = fun.leerRut() 
                buscarCliente = self.buscarCliente(rut) #(1,rut,nombre,pais) 
                if  buscarCliente is not None: 
                    print("RUT YA REGISTRADO!!!")
                    while True:
                        numero = fun.leerNumero()
                        encontrarNumero= self.buscarRegistro(numero)
                        if encontrarNumero  is not None:
                            if encontrarNumero[0] == numero and encontrarNumero[1] == buscarCliente[0]:
                                listaTelf = fun.datosRegistro(buscarCliente[0])
                                listaTelf.insert(0,numero)
                                query  = "INSERT INTO telefono (numero,duracion,fecha,id_cliente) VALUES (%s,%s,%s,%s)"
                                cursor.execute(query, listaTelf)
                                self.conexion.commit()
                                cursor.close()
                                print("\nREGISTRO COMPLETADO CON EXITO\n")
                                break
                            else:
                                print("EL NUMERO INGRESADO YA SE ENCUENTRA VINCULADO A UN CLIENTE DIFERENTE\n")
                        else:
                            listaTelf = fun.datosRegistro(buscarCliente[0])
                            listaTelf.insert(0,numero)
                            query  = "INSERT INTO telefono (numero,duracion,fecha,id_cliente) VALUES (%s,%s,%s,%s)"
                            cursor.execute(query, listaTelf)
                            self.conexion.commit()
                            cursor.close()
                            print("\nREGISTRO COMPLETADO CON EXITO\n")
                            break
                    
                elif buscarCliente == None:
                    print("\n----------------------------------------------------------------------------")
                    print("************ El RUT DEL CLIENTE ES NUEVO REGISTRE NOMBRE Y PAIS ************")
                    print("----------------------------------------------------------------------------")
                    listaCliente = fun.datosCliente()
                    listaCliente.insert(0,rut)

                    query  = "INSERT INTO cliente (rut,nombre,pais) VALUES (%s,%s,%s)"
                    cursor.execute(query, listaCliente)
                    buscarCliente = [cursor.lastrowid]
                    print("----------------------------------------------------------------------------")
                    print("CLIENTE REGISTRADO CON EXITO")
                    print("----------------------------------------------------------------------------")
                    while True:
                        numero = fun.leerNumero()
                        encontrarNumero= self.buscarRegistro(numero)
                        if encontrarNumero  == None:
                            listaTelf = fun.datosRegistro(buscarCliente[0])
                            listaTelf.insert(0,numero)
                            query  = "INSERT INTO telefono (numero,duracion,fecha,id_cliente) VALUES (%s,%s,%s,%s)"
                            cursor.execute(query, listaTelf)
                            self.conexion.commit()
                            cursor.close()
                            print("\nREGISTRO COMPLETADO CON EXITO\n")
                            break
                        else:
                            print("EL NUMERO INGRESADO YA SE ENCUENTRA VINCULADO A UN CLIENTE DIFERENTE\n")


                
        except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def eliminarCliente(self): 
            if self.conexion.is_connected():
                try:
                    while True:
                        opc = fun.subMenu1()
                        cursor = self.conexion.cursor() 
                        match opc:
                            case 1:
                                print("")
                                rut=fun.leerRut()
                                encontrarRUT = self.buscarCliente(rut)
                                if encontrarRUT is not None:
                                    while True:
                                        resp=input(f"\nEsta seguro que desea eliminar cliente '{encontrarRUT[2]}'?(Si o No)\nINGRESE RESPUESTA:").strip().title()
                                        if resp:
                                            if resp == 'Si':
                                                cursor.execute("DELETE FROM telefono WHERE id_cliente = %s", [encontrarRUT[0]]) 
                                                cursor.execute("DELETE FROM cliente WHERE id = %s", [encontrarRUT[0]])
                                                self.conexion.commit()
                                                print(f"\nEL CLIENTE {encontrarRUT[2]} A SIDO ELIMINADO DE LA BASE DE DATOS AL IGUAL QUE SUS REGISTROS VINCULADOS CON EXITO")
                                                break
                                            elif resp == 'No':
                                                print(f"\nSE CANCELO LA ELIMINACION DEL CLIENTE")
                                                break
                                            else:
                                                print("\nINGRESAR Si o No!.")
                                    
                                    
                                else:
                                    print("Cliente no existe en la base de datos")
                                    
                            case 2:
                                while True: 
                                    print("\n¿QUE REGISTRO DESEA ELIMINAR?")
                                    print("------------------------------")
                                    self.mostrarTelefono()
                                    try:   
                                        idTelf = int(input("Ingrese el ID: "))
                                        encontrarID = self.buscarID(idTelf)
                                        if encontrarID is not None:
                                            while True:
                                                resp=input(f"\nEsta seguro que desea eliminar el registro vinculado al ID '{idTelf}'?(Si o No)\nINGRESE RESPUESTA:").strip().title()
                                                if resp:
                                                    if resp == 'Si':
                                                        cursor.execute("DELETE FROM telefono WHERE id = %s", [idTelf])
                                                        self.conexion.commit()
                                                        print(f"DATOS DEL REGISTRO DE LLAMADA ELIMINADOS CON EXITO VINCULADO AL ID {idTelf}")
                                                        break
                                                    elif resp == 'No':
                                                        print(f"\nELIMINACION CANCELADA")
                                                        break
                                                    else:
                                                        print("\nINGRESAR Si o No!.")
                                            break
                                        else:
                                            print("EL REGISTRO NO SE ENCUENTRA EN LA BD, PORFAVOR INGRESAR UN ID QUE APAREZCA EN LA LISTA")
                                    except:
                                        print("\nINGRESE UN VALOR NUMERICO")
                            case 3:
                                break

                except Error as ex:
                    print("Error de conexión: {0} ".format(ex))

    def modificarDatos(self): 
            if self.conexion.is_connected():
                try: 
                    cursor = self.conexion.cursor()
                    while True:
                        opc = fun.subMenu1()
                        match opc:
                            case 1:
                                while True:
                                    mod = fun.subMenu3(opc)
                                    match mod:
                                        case 1:
                                            print("\nINGRESAR RUT AL QUE DESEA MODIFICAR LOS DATOS")
                                            cliente = self.buscarCliente(fun.leerRut())
                                            print("-------------------------------------------------------")
                                            if cliente:
                                                listaNom = [fun.nuevoDato(mod,opc),cliente[0]]
                                                cursor.execute("UPDATE cliente SET nombre = %s WHERE id= %s", listaNom)
                                                self.conexion.commit()
                                                print("\nEL NOMBRE DEL CLIENTE SE ACTUALIZO CON EXITO")
                                            else:
                                                print("EL CLIENTE NO SE ENCUENTRA REGISTRADO")
                                        case 2:
                                            print("\nINGRESAR RUT AL QUE DESEA MODIFICAR LOS DATOS")
                                            cliente = self.buscarCliente(fun.leerRut())
                                            print("-------------------------------------------------------")
                                            if cliente:
                                                listaPai = [fun.nuevoDato(mod,opc),cliente[0]]
                                                cursor.execute("UPDATE cliente SET pais = %s WHERE id= %s", listaPai)
                                                self.conexion.commit()
                                                print("\nEL PAIS DEL CLIENTE SE ACTUALIZO CON EXITO")
                                            else:
                                                print("EL CLIENTE NO SE ENCUENTRA REGISTRADO")
                                        case 3:
                                            break
                            case 2:
                                while True:
                                    mod = fun.subMenu3(opc)
                                    match mod:
                                        case 1: #TAREA: REALIZAR LO MISMO QUE EN INSERT EVITAR DUPLICACION DE NUMERO CELULAR AL ACTUALIZARLO
                                            listaID=[]
                                            print("\nINGRESAR RUT AL QUE DESEA MODIFICAR LOS DATOS")
                                            cliente = self.buscarCliente(fun.leerRut())
                                            if cliente:
                                                buscar = self.buscarTelefono(cliente[0])
                                                if buscar is not None:
                                                    print("\nREGISTRO DE LLAMADAS DEL CLIENTE SELECCIONADO")
                                                    for item in buscar:
                                                        print(f"ID:{item[0]}, NUMERO:{item[1]}, DURACION DE LLAMADA:{item[2]}, FECHA:{item[3]}")
                                                        listaID.append(item[0])
                                                    while True:
                                                        try:
                                                            idTf=int(input("\nIngrese el ID del registro al que desea modificar el numero:"))
                                                        except:
                                                            print("\nIngrese solo numeros enteros")
                                                        
                                                        if idTf not in listaID:        
                                                            print("\nPorfavor revise la lista y ingrese el ID valido para el cliente seleccionado")
                                                        else:
                                                            print("-------------------------------------------------------")
                                                            while True:
                                                                listNum = [fun.nuevoDato(mod,opc),idTf]
                                                                encontrarNumero= self.buscarRegistro(listNum[0])
                                                                if encontrarNumero is not None:
                                                                    if encontrarNumero[0] == listNum[0] and encontrarNumero[1] == cliente[0]:
                                                                        cursor.execute("UPDATE telefono SET numero = %s where id = %s", listNum)
                                                                        self.conexion.commit()
                                                                        print("NUMERO DE CELULAR ACTUALIZADO")
                                                                        break
                                                                    else:
                                                                        print("EL NUMERO INGRESADO YA SE ENCUENTRA VINCULADO A UN CLIENTE DIFERENTE\n")
                                                                else:
                                                                    cursor.execute("UPDATE telefono SET numero = %s where id = %s", listNum)
                                                                    self.conexion.commit()
                                                                    print("NUMERO DE CELULAR ACTUALIZADO")
                                                                    break
                                                            break
                                                else:
                                                    print("\nCLIENTE SIN REGISTROS PARA MODIFICAR.")
                                            else:
                                                print("EL CLIENTE NO SE ENCUENTRA REGISTRADO")
                                        case 2:
                                            listaID=[]
                                            print("\nINGRESAR RUT AL QUE DESEA MODIFICAR LOS DATOS")
                                            cliente = self.buscarCliente(fun.leerRut())
                                            if cliente:
                                                buscar = self.buscarTelefono(cliente[0])
                                                if buscar is not None:
                                                    print("\nREGISTRO DE LLAMADAS DEL CLIENTE SELECCIONADO")
                                                    for item in buscar:
                                                        print(f"ID:{item[0]}, NUMERO:{item[1]}, DURACION DE LLAMADA:{item[2]}, FECHA:{item[3]}")
                                                        listaID.append(item[0])

                                                    while True:
                                                        try:
                                                            idTf=int(input("\nIngrese el ID del registro al que desea modificar la duracion:"))
                                                        except:
                                                            print("\nIngrese solo numeros enteros")
                                                        
                                                        if idTf not in listaID:        
                                                            print("\nPorfavor revise la lista y ingrese el ID valido para el cliente seleccionado")
                                                        else:
                                                            print("-------------------------------------------------------")
                                                            listaDur = [fun.nuevoDato(mod,opc),idTf]
                                                            cursor.execute("UPDATE telefono SET duracion = %s where id = %s", listaDur)
                                                            self.conexion.commit()
                                                            print("\nDURACION DE LA LLAMADA ACTUALIZADA CON EXITO")
                                                            break
                                                else:
                                                    print("\nCLIENTE SIN REGISTROS PARA MODIFICAR.")
                                            else:
                                                print("EL CLIENTE NO SE ENCUENTRA REGISTRADO")
                                        case 3:
                                            listaID=[]
                                            print("\nINGRESAR RUT AL QUE DESEA MODIFICAR LOS DATOS")
                                            cliente = self.buscarCliente(fun.leerRut())
                                            if cliente:
                                                buscar = self.buscarTelefono(cliente[0])
                                                if buscar is not None:    
                                                    print("\nREGISTRO DE LLAMADAS DEL CLIENTE SELECCIONADO")
                                                    for item in buscar:
                                                        print(f"ID:{item[0]}, NUMERO:{item[1]}, DURACION DE LLAMADA:{item[2]}, FECHA:{item[3]}")
                                                        listaID.append(item[0])

                                                    while True:
                                                        try:
                                                            idTf=int(input("\nIngrese el ID del registro que desea modificar la fecha:"))
                                                        except:
                                                            print("\nIngrese solo numeros enteros")
                                                        
                                                        if idTf not in listaID:        
                                                            print("\nPorfavor revise la lista y ingrese el ID valido para el cliente seleccionado")
                                                        else:
                                                            print("-------------------------------------------------------")
                                                            listaFech = [fun.nuevoDato(mod,opc),idTf]
                                                            cursor.execute("UPDATE telefono SET fecha = %s where id = %s", listaFech)
                                                            self.conexion.commit()
                                                            print("\nFECHA ACTUALIZADA CON EXITO")
                                                            break
                                                else:
                                                    print("\nCLIENTE SIN REGISTROS PARA MODIFICAR.")
                                            else:
                                                print("EL CLIENTE NO SE ENCUENTRA REGISTRADO")
                                                    
                                        case 4:
                                            break
                            case 3:
                                break
                    
                    

                except Error as ex:
                    print("Error al actualizar datos: {0} ".format(ex))

    def leerTodo(self): 
        try:
            opc = fun.subMenu2()
            if  self.conexion.is_connected():
                cursor = self.conexion.cursor()
                match opc:
                    case 1:
                        cursor.execute("SELECT * FROM cliente ORDER BY id")
                        resultado=cursor.fetchall()
                        print("--------------------------------------------")
                        print("La tabla cliente tiene los siguientes datos:")
                        print("--------------------------------------------")
                        print("-----------------------------------------------------------------")
                        c=1
                        for fila in resultado:
                            print(f"{c}.","ID:",fila[0],"|RUT:", fila[1],"|NOMBRE:",fila[2],"|PAIS:",fila[3])
                            c+=1
                        print("-----------------------------------------------------------------")    
                        print("Total registros leídos:",cursor.rowcount)
                        print("-----------------------------------------------------------------")
                        cursor.close()

                    case 2:
                        cursor.execute("SELECT * FROM telefono ORDER BY id_cliente")
                        resultado=cursor.fetchall()
                        print("---------------------------------------------")
                        print("La tabla telefono tiene los siguientes datos:")
                        print("---------------------------------------------")
                        print("-----------------------------------------------------------------")
                        c=1
                        for fila in resultado:  
                            print(f"{c}.","ID:",fila[0],"|NUMERO:", fila[1],"|MINUTOS DE LA LLAMADA:",fila[2],"|FECHA:",fila[3])
                            c+=1
                        print("-----------------------------------------------------------------")  
                        print("\nTotal registros leídos:",cursor.rowcount)
                        print("-----------------------------------------------------------------")
                        print("")
                        cursor.close()
                    
                    case 3:
                        cursor.execute("SELECT * FROM cliente") 
                        resultado=cursor.fetchall()

                        cursor.execute("SELECT tf.id, tf.numero,tf.duracion,tf.fecha,tf.id_cliente FROM telefono AS tf INNER JOIN cliente AS cl ON tf.id_cliente = cl.id WHERE cl.id = tf.id_cliente  ORDER BY tf.id ")
                        resultado2 = cursor.fetchall()

                        print("\n----------------------------------------------------------------------------------------------------------------------------")
                        print("La tabla cliente tiene los siguientes datos:")
                        print("----------------------------------------------------------------------------------------------------------------------------")
                        c=1
                        for fila in resultado:
                            print(f"{c}.","ID:",fila[0],"|RUT:", fila[1],"|NOMBRE:",fila[2],"|PAIS:",fila[3])
                            for item in resultado2:
                                if fila[0] == item[4]:
                                    print("\t-","ID TELEFONO:",item[0],"|NUMERO:",item[1],"|MINUTOS DE LLAMADA:",item[2],"|FECHA:",item[3])
                            c+=1        
                            print("-----------------------------------------------------------------------------------------------------------------------------")
                        print("Total registros leídos:",cursor.rowcount)
                        print("-----------------------------------------------------------------------------------------------------------------------------")
                        cursor.close()
        except Error as ex:
                print("Error de conexión: {0} ".format(ex))   

    def leerUno(self):
        try:
            if self.conexion.is_connected():
                cursor = self.conexion.cursor()
                rut = fun.leerRut()
                cliente = self.buscarCliente(rut)
                if cliente:
                    print("----------------------------------------------------------------------------------------------")
                    print(f" ID: {cliente[0]} | RUT: {cliente[1]} | NOMBRE: {cliente[2]} | PAIS: {cliente[3]}")
                    print("----------------------------------------------------------------------------------------------")
                else:
                    print("\n No hay registro del cliente en la base de datos. Porfavor agregelo seleccionando el numero 1 en el menu ")
                    return
                query_llamadas = """
                    SELECT id, numero, duracion, fecha
                    FROM telefono
                    WHERE id_cliente = %s
                """
                cursor.execute(query_llamadas, (cliente[0],))
                llamadas = cursor.fetchall()
                if llamadas:
                    print("\n Llamadas asociadas: ")
                    for llamada in llamadas:
                        print(f" - ID: {llamada[0]} | NUMERO: {llamada[1]} | DURACION: {llamada[2]} MIN | FECHA: {llamada[3]}")
                else:
                    print("\n No hay registro de llamada en la base de datos ")

            else:
                print("No se pudo conectar a la base de datos. ")
        except Error as ex:
            print("Error de conexion: {0}".format(ex))

#FUNCIONES PARA MANIPULACION DE DATOS DE LA BD
    def buscarCliente(self,rut):            #GENERO UNA TUPLA DE DATOS DE LA TABLA CLIENTE (ID,RUT,NOMBRE,PAIS)
        listRut=[rut]
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = ("SELECT * FROM cliente WHERE rut = %s")
                cursor.execute(query,listRut )
                resultado = cursor.fetchone()
                cursor.close()
                return resultado
                
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def buscarRegistro(self,numTelefono):   #GENERO UNA LISTA DE DATOS DE LA TABLA CLIENTE [NUMERO, ID_CLIENTE]
        listaTelefono=[numTelefono]
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = ("SELECT * FROM telefono WHERE numero = %s")
                cursor.execute(query,listaTelefono)
                resultado = cursor.fetchall()
                cursor.close()
                if len(resultado)>0:
                    for item in resultado:
                        datos = [item[1],item[4]]
                    print()
                    return datos
                else:
                    return None
                
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def buscarTelefono(self,idClient):      #GENERO UNA LISTA DE TUPLAS DE LA TABLA TELEFONO [(ID,NUM,DURACION,FECHA),(ID,NUM,DURACION,FECHA),...ETC]
        listaIdClient=[idClient]
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = ("SELECT tf.id, tf.numero, tf.duracion, tf.fecha, tf.id_cliente FROM telefono AS tf INNER JOIN cliente AS cl ON cl.id=tf.id_cliente WHERE cl.id = %s")
                cursor.execute(query,listaIdClient)
                resultado = cursor.fetchall()
                cursor.close()
                if len(resultado)>0:
                    return resultado
                else:
                    return None
                
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def buscarID(self,id):                  #GENERO UNA TUPLA DE DATOS DE LA TABLA TELEFONO (ID,NUM,DURACION,FECHA,ID_CLIENTE )
        listID=[id]
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = ("SELECT * FROM telefono WHERE id = %s")
                cursor.execute(query,listID )
                resultado = cursor.fetchone()
                cursor.close()
                return resultado
                
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def mostrarTelefono(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM telefono")
                resultado = cursor.fetchall()
                cursor.close()
                for item in resultado:
                    print(f"ID:{item[0]} | NUMERO:{item[1]} | DURACION:{item[2]} | FECHA:{item[3]} | ID_CLIENTE:{item[4]}")
                print("")



            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def verificarConexion(self):            #Verifico de forma directa la conexion a la Base de datos
        self.conectarBaseDatos()
        if self.conexion.is_connected():
            print("\nConexion a la base de datos EXITOSA!...")
            return True

#CONSULTAS
    def buscarLlamadas(self):#Consulta 1
        if self.conexion.is_connected():
            try:
                while True:
                    cursor=self.conexion.cursor()
                    rut = fun.leerRut()
                    buscarCliente = self.buscarCliente(rut)
                    
                    if  buscarCliente is not None: #reparar unread data
                        print("")  
                        idCliente = [buscarCliente[0]]
                        cursor.execute("SELECT tf.id, tf.numero,tf.duracion,tf.fecha,tf.id_cliente FROM telefono AS tf INNER JOIN cliente AS cl ON tf.id_cliente = cl.id WHERE tf.id_cliente = %s  ORDER BY tf.id",idCliente)
                        resultado = cursor.fetchall()
                        count=0
                        print("--------------------------------------------")
                        print("       **** CLIENTE ENCONTRADO ****")
                        print("--------------------------------------------")
                        print("EL RESULTADO DE LA BUSQUEDA ES:")
                        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
                        
                        print("RUT: " + buscarCliente[1] + "\nCLIENTE: "+  buscarCliente[2] +  "\t  PAIS: " + buscarCliente[3])
                        print("--------------------------------------------------------------------------------------------------------------------------------------------------")

                        for fila in resultado:
                            count+=1
                            print(f"{count}. NUMERO CELULAR:", fila[1],"|DURACION:",fila[2],"MIN |FECHA:",fila[3])
                        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("Registro total de llamadas encontradas: ", count)
                        
                        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("")
                        break
                    else:
                        print("Rut no esta en BD")
                        resp = input("DESEA INTENTAR DE NUEVO [SI O NO]").title()
                        if resp == "No":
                            break
                        elif resp == "Si":
                            print("Ingresa nuevamenter el rut")
                        else:
                            print("Respuesta es SI o NO")
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def leerPais(self):#Consulta 2 
        try:
            if self.conexion.is_connected():
                cursor = self.conexion.cursor()
                
                cursor.execute("SELECT pais FROM cliente ORDER BY pais")
                resultado=cursor.fetchall()
                
                cursor.execute("SELECT count(rut) FROM cliente GROUP BY pais ORDER BY pais")
                countPais=cursor.fetchall()

                print("\n-------------------------------------------------------------")
                print("CANTIDAD DE CLIENTES POR PAIS REGISTRADOS:")
                print("-------------------------------------------------------------")
                
                num=num2=0
                listaNum = []; listaPaises = []
                for pais in countPais:
                    listaNum.append(pais[0])

                for fila in resultado:
                    if fila not in listaPaises:
                        listaPaises.append(fila) 
                for fila in listaPaises:
                    print(f" {listaNum[num2]} {fun.switchClient(listaNum[num2])}    | {fila[0]} ")
                    num2+=1;num+=1
                    
                print("------------------------------------------------------------")
                print(f"PAISES TOTALES REGISTRADOS: {num}")
                print("------------------------------------------------------------")
    
        except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def sumaMinutos(self):#Consulta 3
        listaNombres= []
        suma=0
        try:
            if self.conexion.is_connected():
                cursor = self.conexion.cursor()
                fecha = fun.fecha()

                cursor.execute("SELECT cl.id, cl.nombre FROM telefono as tf INNER JOIN cliente as cl ON cl.id = tf.id_cliente WHERE tf.fecha = %s",fecha)
                resultado=cursor.fetchall()

                cursor.execute("SELECT duracion, fecha, id_cliente FROM telefono WHERE fecha=%s",fecha) 
                resultado2=cursor.fetchall()

                if resultado:
                        print("\n----------------------------------------------------------------------------------------------------------------------------")
                        print("CLIENTE Y REGISTROS DE LLAMADA (SUMA DEL TOTAL DE MINUTOS LLAMADOS):")
                        print("----------------------------------------------------------------------------------------------------------------------------")
                        c=1
                        for fila in resultado:
                            if fila not in listaNombres:
                                listaNombres.append(fila)

                        for fila1 in resultado2:
                            suma+=fila1[0]
                        
                        
                        for fila2 in listaNombres:
                            print(f"{c}.","ID:",fila2[0]," |NOMBRE:",fila2[1])
                            suma2 = 0
                            for item in resultado2:
                                if fila2[0] == item[2]:
                                    print("\t-","|MINUTOS DE LLAMADA:",item[0],"min","|FECHA:",item[1])
                                    suma2+=item[0]
                            print("-----------------------------------------------------------------------------------------------------------------------------")
                            print(f"Total minutos llamados por el cliente {fila2[1]}: ",suma2, "min")
                            print("-----------------------------------------------------------------------------------------------------------------------------")

                            c+=1        
                        print("-----------------------------------------------------------------------------------------------------------------------------")
                        print("Total registros de llamada leídos:",cursor.rowcount, f"\nFecha: {fecha[0]}")
                        print(f"Suma total de minutos de llamada: {suma} min")
                        print("-----------------------------------------------------------------------------------------------------------------------------")
                        cursor.close()      

                            


                else:
                    print("\nNo existe registro con la fecha seleccionada")
        except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def telefonosPais(self): #Consulta 4
        try:
            if self.conexion.is_connected():
                cursor = self.conexion.cursor()
                pais = fun.leerTexto("Ingrese el país: ")
                consulta = """
                SELECT
                    tf.numero,
                    COUNT(tf.id) AS cantidadLlamadas
                FROM
                    cliente AS cl
                INNER JOIN
                    telefono AS tf
                ON
                    cl.id = tf.id_cliente
                WHERE
                    cl.pais = %s
                GROUP BY
                    tf.numero
                """
                cursor.execute(consulta, (pais,))
                resultados = cursor.fetchall()
                print("\n--------------------------------------------")
                print(f"Telefonos utilizados por clientes de {pais}: ")
                print("----------------------------------------------")
                for fila in resultados:
                    print(f"Numero: {fila[0]} | Cantidad de llamadas: {fila[1]}")
                print("----------------------------------------------")
            else:
                print("No se pudo conectar a la base de datos. ")
        except Error as ex:
            print("Error de conexión: {0} ".format(ex))