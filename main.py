from cliente import Cliente
import funcion as f
cl  = Cliente()

while True:
    if f.menu() == 1:
        if cl.verificarConexion() == True:
            while True:
                match f.submenu():
                    case 1:
                        cl.insertData()
                    case 2:
                        cl.eliminarCliente()
                    case 3:
                        cl.modificarDatos()
                    case 4:
                        cl.leerTodo()
                    case 5:
                        cl.leerUno()
                    case 6:
                        while True:
                            match f.menuConsulta():
                                case 1:
                                    cl.buscarLlamadas()
                                case 2:
                                    cl.leerPais()                                
                                case 3:
                                    pass
                                case 4:
                                    break
                    case 8:
                        cl.cerrarConexion()
                        break
                        
    else:
        f.fin()
        break