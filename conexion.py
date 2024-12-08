import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self):
        self.conexion=None
    
    def conectarBaseDatos(self):  
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',   # hosting
                port=3306,          # puerto mysql
                user='root',        # nombre del usuario
                password='',        # contraseña del usuario
                db='eva4'           # nombre de la base de datos
            )
        except Error as ex:
            print("Error de conexión:",ex)
    
    def cerrarConexion(self): 
        if self.conexion.is_connected():
                self.conexion.close()
                print("\nLa conexión ha sido cerrada\n")

        else: 
                print("\nBase de dato ya esta cerrada") 