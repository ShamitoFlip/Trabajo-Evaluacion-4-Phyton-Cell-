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
                buscarCliente = self.buscarCliente(rut) #(1,rut,nombre,pais) 
                if  buscarCliente is not None: #reparar unread found
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
    
    def eliminarCliente(self): 
        listCli= self.buscarCliente(fun.leerRut())
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("DELETE FROM telefono WHERE id_cliente = %s",[listCli[0]]) 
                cursor.execute("DELETE FROM cliente WHERE rut = %s",[listCli[1]])
                self.conexion.commit()

                cursor.close()
                print("Cliente borrado con exito")
            
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def ModificarDatos(self): 
            if self.conexion.is_connected():
                try: 
                    opc = fun.subMenu1()
                    cursor = self.conexion.cursor()
                    match opc:
                        case 1:
                            idCliente = self.buscarCliente(fun.leerRut())
                            mod = fun.subMenu3(opc)
                            match mod:  
                                case 1: 
                                    listaNom = [fun.nuevoDato(mod,opc),idCliente[0]]
                                    cursor.execute("UPDATE cliente SET nombre = %s WHERE id= %s", listaNom)
                                case 2:
                                    listaPai = [fun.nuevoDato(mod,opc),idCliente[0]]
                                    cursor.execute("UPDATE cliente SET pais = %s WHERE id= %s", listaPai)
                        case 2:
                            idCliente = self.buscarCliente(fun.leerRut())
                            mod = fun.subMenu3(opc)
                            match mod:
                                case 1:
                                    listNum = [fun.nuevoDato(mod,opc),idCliente[0]]
                                    cursor.execute("UPDATE telefono SET numero = %s where id = %s", listNum)
                                case 2:
                                    listaDur = [fun.nuevoDato(mod,opc),idCliente[0]]
                                    cursor.execute("UPDATE telefono SET duracion = %s where id = %s", listaDur)
                                case 3:
                                    listaFech = [fun.nuevoDato(mod,opc),idCliente[0]]
                                    cursor.execute("UPDATE telefono SET fecha = %s where id = %s", listaFech)
                                case 4:
                                    listaIdFk = [fun.nuevoDato(mod,opc),idCliente[0]]
                                    cursor.execute("UPDATE telefono SET id_cliente = %s where id = %s", listaIdFk)



                    self.conexion.commit()
                    print("Los datos del cliente se han actualizado correctamente")
                    

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


#CONSULTASBD
    def leerPais(self):#Consulta 2 
        
        try:
            if self.conexion.is_connected():
                cursor = self.conexion.cursor()
                cursor.execute("SELECT pais FROM cliente ORDER BY pais")
                resultado=cursor.fetchall()
                print(resultado)
                print("-------------------------------------------------------------")
                print("LOS CLIENTE DE LA BASE DE DATOS SON DE LOS SIGUIENTES PAISES:")
                print("-------------------------------------------------------------")
                #print(resultado)
                listaPaises = []
                for fila in resultado:
                    if fila not in listaPaises:
                        listaPaises.append(fila) 
                c=1
                for fila in listaPaises:
                    print("-----------------")
                    print(f"{c}.","-",fila[0])
                    print("-----------------")
                    c+=1
                print("------------------------------------------------------------")
                
                """
                c=1
                for fila in resultado:
                    print(f"{c}.","ID:",fila[0],"|RUT:", fila[1],"|NOMBRE:",fila[2],"|PAIS:",fila[3])
                    c+=1
                print("-----------------------------------------------------------------")
                def leerPais(self):
                    try:
                        if self.conexion.is_connected():
                            cursor = self.conexion.cursor()
                            cursor.execute("SELECT pais, COUNT(*) AS cantidad FROM cliente GROUP BY pais ORDER BY pais")
                            resultado = cursor.fetchall()
                            print("-------------------------------------------------------------")
                            print("LOS CLIENTES DE LA BASE DE DATOS SON DE LOS SIGUIENTES PAISES:")
                            print("-------------------------------------------------------------")
                            
                            listaPaises = []
                            for fila in resultado:
                                listaPaises.append((fila[0], fila[1])) 
                            
                            c = 1
                            for pais, cantidad in listaPaises:
                                print("-----------------")
                                print(f"{c}.", "-", pais, "con", cantidad, "clientes")
                                print("-----------------")
                                c += 1
                                
                            print("------------------------------------------------------------")
                    except Error as ex:
                        print("Error de conexión: {0} ".format(ex))

                """
    
        except Error as ex:
                print("Error de conexión: {0} ".format(ex))
    
    def sumaMinutos(self):#Consulta 3
        pass


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
