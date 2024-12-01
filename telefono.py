from conexion import Conexion
from mysql.connector import Error

class Telefono(Conexion):
    def __init__(self):
         super().__init__()
    
    def insertData(self,listaTelefono):
        try:
            if  self.conexion.is_connected():
                cursor = self.conexion.cursor()
                query  = "INSERT INTO telefono (numero,duracion,fecha,id_cliente) VALUES (%s,%s,%s,%s)"
                cursor.execute(query, listaTelefono)
               
            
            
                print("Se inserto correctamente")
        except Error as ex:
                print("Error de conexión: {0} ".format(ex))