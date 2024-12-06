import funcion as fun
from conexion import Conexion
from mysql.connector import Error

class Cliente(Conexion): 
    def __init__(self):
        super().__init__()      

#CRUD
    def insertData(self):#Se debe verificar el telefono que no se repita con otro cliente:D.
        try:
            if  self.conexion.is_connected():
                cursor = self.conexion.cursor()
                print("")
                rut = fun.leerRut() 
                buscarCliente = self.buscarCliente(rut) #(1,rut,nombre,pais) 
                if  buscarCliente is not None: #reparar unread found
                    print("RUT YA REGISTRADO!!!")
                    
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
                
                numero = fun.leerNumero()
                listaTelf = fun.datosRegistro(buscarCliente[0])
                listaTelf.insert(0,numero)
                query  = "INSERT INTO telefono (numero,duracion,fecha,id_cliente) VALUES (%s,%s,%s,%s)"
                cursor.execute(query, listaTelf)
                self.conexion.commit()
                cursor.close()


                
        except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def eliminarCliente(self): #Aun faltan condiciones
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
                                    cursor.execute("DELETE FROM telefono WHERE id_cliente = %s", [encontrarRUT[0]]) 
                                    cursor.execute("DELETE FROM cliente WHERE id = %s", [encontrarRUT[0]])
                                    self.conexion.commit()
                                    print("Cliente eliminado exitosamente")
                                else:
                                    print("Cliente no existe en la base de datos")
                                    
                            case 2:
                                print("")
                                idTelf = input("Ingrese el ID: ")
                                encontrarID = self.buscarID(idTelf)
                                if encontrarID is not None:
                                    cursor.execute("DELETE FROM telefono WHERE id = %s", [idTelf])
                                    self.conexion.commit()
                                    print("Numero eliminado correctamente")
                                else:
                                    print("No se encuentra ese id en la base de datos")
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
                                                print("Los datos del cliente se han actualizado correctamente")
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
                                                print("Los datos del cliente se han actualizado correctamente")
                                            else:
                                                print("EL CLIENTE NO SE ENCUENTRA REGISTRADO")
                                        case 3:
                                            break
                            case 2:
                                while True:
                                    mod = fun.subMenu3(opc)
                                    match mod:
                                        case 1:
                                            print("\nINGRESAR RUT AL QUE DESEA MODIFICAR LOS DATOS")
                                            cliente = self.buscarCliente(fun.leerRut())
                                            print("-------------------------------------------------------")
                                            if cliente:
                                                listNum = [fun.nuevoDato(mod,opc),cliente[0]]
                                                cursor.execute("UPDATE telefono SET numero = %s where id = %s", listNum)
                                                self.conexion.commit()
                                                print("Los datos del cliente se han actualizado correctamente")
                                            else:
                                                print("EL CLIENTE NO SE ENCUENTRA REGISTRADO")
                                        case 2:
                                            print("\nINGRESAR RUT AL QUE DESEA MODIFICAR LOS DATOS")
                                            cliente = self.buscarCliente(fun.leerRut())
                                            print("-------------------------------------------------------")
                                            if cliente:
                                                listaDur = [fun.nuevoDato(mod,opc),cliente[0]]
                                                cursor.execute("UPDATE telefono SET duracion = %s where id = %s", listaDur)
                                                self.conexion.commit()
                                                print("Los datos del cliente se han actualizado correctamente")
                                            else:
                                                print("EL CLIENTE NO SE ENCUENTRA REGISTRADO")
                                        case 3:
                                            print("\nINGRESAR RUT AL QUE DESEA MODIFICAR LOS DATOS")
                                            cliente = self.buscarCliente(fun.leerRut())
                                            print("-------------------------------------------------------")
                                            if cliente:
                                                listaFech = [fun.nuevoDato(mod,opc),cliente[0]]
                                                cursor.execute("UPDATE telefono SET fecha = %s where id = %s", listaFech)
                                                self.conexion.commit()
                                                print("Los datos del cliente se han actualizado correctamente")
                                            else:
                                                print("EL CLIENTE NO SE ENCUENTRA REGISTRADO")
                                        case 4:
                                            break
                            case 3:
                                break
                    
                    

                except Error as ex:
                    print("Error al actualizar datos: {0} ".format(ex))
    
    def leerTodo(self): #Listoco
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

#FUNCIONES EXTRA
    def buscarCliente(self,rut):
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
    
    def buscarRegistro(self,numTelefono):
        listaTelefono=[numTelefono]
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = ("SELECT * FROM telefono WHERE numero = %s")
                cursor.execute(query,listaTelefono)
                resultado = cursor.fetchall()
                cursor.close()
                for item in resultado:
                    datos = [item[1],item[4]]
                return datos
                
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))
    
    def buscarID(self,id):
        listRut=[id]
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = ("SELECT * FROM telefono WHERE id = %s")
                cursor.execute(query,listRut )
                resultado = cursor.fetchone()
                cursor.close()
                return resultado
                
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def verificarConexion(self):
        self.conectarBaseDatos()
        if self.conexion.is_connected():
            print("\nConexion a la base de datos EXITOSA!...")
            return True

#CONSULTAS
    def buscarLlamadas(self): #Consulta 1
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
                        print("Total registros de llamada leídos:",cursor.rowcount)
                        print(f"Suma total de minutos de llamada: {suma} min")
                        print("-----------------------------------------------------------------------------------------------------------------------------")
                        cursor.close()      

                            


                else:
                    print("\nNo existe registro con la fecha seleccionada")
        except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def consultaExtra(self): #Consulta 4
        pass