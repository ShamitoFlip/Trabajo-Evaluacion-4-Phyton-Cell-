from cliente import Cliente
import funcion as f
cl  = Cliente()

while True:
    if f.menu() == 1:
        if cl.verificarConexion() == True:
            while True:
                opcion= f.submenu()
                match opcion:
                    case 1:
                        cl.insertData()
                    case 2:
                        cl.ModificarDatos()
                    case 3:
                        cl.leerTodo()
                    case 4:
                        cl.buscarLlamada()
                    case 5:
                        cl.eliminarCliente()
                    case 6:
                        pass #Menu de consultas
                    case 7:
                        cl.leerPais()
                    case 8:
                        cl.cerrarConexion()
                        break
                        
    else:
        f.fin()
        break