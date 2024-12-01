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
                rut = fun.leerRut()
                buscarCliente = self.buscarCliente(rut) #(1,rut,nombre,pais))
                if  buscarCliente is not None: #reparar unreal data
                    print("RUT YA REGISTRADO!!!")
                    
                elif buscarCliente == None:
                    print("\n----------------------------------------------------------------------------")
                    print("************ El RUT DEL CLIENTE ES NUEVO REGISTRE NOMBRE Y PAIS ************")
                    print("----------------------------------------------------------------------------")
                    listaCliente = fun.agregarCliente()
                    listaCliente.insert(0,rut)

                    query  = "INSERT INTO cliente (rut,nombre,pais) VALUES (%s,%s,%s)"
                    cursor.execute(query, listaCliente)
                    buscarCliente = [cursor.lastrowid]
                    print("----------------------------------------------------------------------------")
                    print("CLIENTE REGISTRADO CON EXITO")
                    print("----------------------------------------------------------------------------")
                
                query  = "INSERT INTO telefono (numero,duracion,fecha,id_cliente) VALUES (%s,%s,%s,%s)"
                cursor.execute(query, fun.agregarTelefono(buscarCliente[0]))
                self.conexion.commit()
                cursor.close()
                
                

                
        except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def eliminarCliente(self): #Aun faltan condiciones
            if self.conexion.is_connected():
                try:
                    opc = fun.subMenu2()
                    cursor = self.conexion.cursor()
                    match opc:
                        case 1:
                            rut = fun.leerRut()
                            idCliente=[self.buscarCliente(rut)[0]]
                            cursor.execute("DELETE FROM telefono WHERE id_cliente = %s", idCliente)
                            cursor.execute("DELETE FROM cliente WHERE id = %s", idCliente)
                            self.conexion.commit()
                            print("Cliente eliminado exitosamente")
                        case 2:
                            id=int(input("Ingresar ID que desea eliminar: "))
                            cursor.execute("DELETE FROM telefono WHERE id_cliente = %s", [])

                except Error as ex:
                    print("Error de conexión: {0} ".format(ex))
                    
    def ModificarDatos(self): #AUN NO SE AVANZA
        pass
        #El usuario debe poder seleccionar el atributo a modifcar ya sea de la tabla cliente o de la tabla telefono
        #Se puede crear un menu para seleccionar que tabla modificar 
        #y un submenu que con los atributos a modificar (cliente(rut,nombre y pais) y en telefono(numero, duracion y fecha))
        #Opcional para mejorar el nivel de detalle mostrar los datos antiguos y los nuevos que se modificaron o cambiaron

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
        
    def leerUno(self): #Error UNREAD RESULT FOUND
        if self.conexion.is_connected():
            try:
                while True:
                    cursor=self.conexion.cursor()
                    rut = fun.leerRut()
                    buscarCliente = self.buscarCliente(rut)
                    idCliente = [buscarCliente[0]]
                    if  buscarCliente is not None: #reparar unread data
                        print("Cliente encontrado")  

                        cursor.execute("SELECT tf.id, tf.numero,tf.duracion,tf.fecha,tf.id_cliente FROM telefono AS tf INNER JOIN cliente AS cl ON tf.id_cliente = cl.id WHERE tf.id_cliente = %s  ORDER BY tf.id",idCliente)
                        resultado = cursor.fetchall()
                        c=1
                        print("--------------------------------------------")
                        print("**** EL RESULTADO DE LA BUSQUEDA ES: ****")
                        print("--------------------------------------------")
                        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
                        
                        print(f"{c}.","ID:",buscarCliente[0],"|RUT:", buscarCliente[1],"|NOMBRE:",buscarCliente[2],"|PAIS:",buscarCliente[3])
                        for fila in resultado:
                            print(f"\t-.","ID:",fila[0],"|NUMERO CELULAR:", fila[1],"|DURACION:",fila[2],"MIN |FECHA:",fila[3],"MIN |ID_CLIENTE:",fila[4])
                        
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
    
    def verificarConexion(self):
        self.conectarBaseDatos()
        if self.conexion.is_connected():
            print("\nConexion a la base de datos EXITOSA!...")
            return True

#CONSULTAS
    def buscarLlamadas(self): #Error UNREAD RESULT FOUND
        if self.conexion.is_connected():
            try:
                while True:
                    cursor=self.conexion.cursor()
                    rut = fun.leerRut()
                    buscarCliente = self.buscarCliente(rut)
                    idCliente = [buscarCliente[0]]
                    if  buscarCliente is not None: #reparar unread data
                        print("Cliente encontrado")  

                        cursor.execute("SELECT tf.id, tf.numero,tf.duracion,tf.fecha,tf.id_cliente FROM telefono AS tf INNER JOIN cliente AS cl ON tf.id_cliente = cl.id WHERE tf.id_cliente = %s  ORDER BY tf.id",idCliente)
                        resultado = cursor.fetchall()
                        c=1
                        print("--------------------------------------------")
                        print("**** EL RESULTADO DE LA BUSQUEDA ES: ****")
                        print("--------------------------------------------")
                        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
                        
                        print(f"{c}.","ID:",buscarCliente[0],"|RUT:", buscarCliente[1],"|NOMBRE:",buscarCliente[2],"|PAIS:",buscarCliente[3])
                        for fila in resultado:
                            print(f"\t-.","ID:",fila[0],"|NUMERO CELULAR:", fila[1],"|DURACION:",fila[2],"MIN |FECHA:",fila[3],"MIN |ID_CLIENTE:",fila[4])
                        
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