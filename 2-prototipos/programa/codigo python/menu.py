from database import Database

class Menu:
    def __init__(self, db):
        self.db = db


    def ejecutar(self):
        """
# ----------------------------------------------------------------
# Metodo que muestra el menu en consola y espera el ingreso de 
# un valor del menu para # llamar al metodo correspondiente.
# En caso de no haber coincidencia con ninguno, 
# imprime un mensaje de error y aguarda nuevo ingreso.
# ----------------------------------------------------------------
        """        
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.mostrar_altas()
            elif opcion == '2':
                self.mostrar_bajas()
            elif opcion == '3':
                self.programar_actividad()
            elif opcion == '4':
                self.historial_maquina()
            elif opcion == '5':
                self.historial_operario()
            elif opcion == '6':
                self.informe_almacen()
            elif opcion == '7':
                self.carga_horas_diarias()
            elif opcion == '8':
                self.ver_estadisticas_uso()
            elif opcion == '9':
                self.salir()
                break
            else:
                print("Opción no válida. Por favor, seleccione nuevamente.")


    def mostrar_menu(self):
        """
# -----------------------------------
# Despliega el menu de opciones
# -----------------------------------
        """       
        print("\nMenú de opciones:")
        print("1. Ingresar Submenu Altas")
        print("2. Ingresar Submenu Bajas")
        print("3. Programar Actividad")
        print("4. Historial Maquina")
        print("5. Historial Operario")
        print("6. Informe Almacen")
        print("7. Carga Diaria Horas")
        print("8. Estadisticas Generales")
        print("9. Salir")


    def mostrar_altas(self):
        """
        # -----------------------------------------------------------------------------
        # Despliega el submenu de altas, y aguarda el a eleccion de una opcion, 
        # llamando al metodo correspondiente.
        # En caso de opcion incorrecta imprime mensaje de error y regresa al menu principal. 
        # -----------------------------------------------------------------------------
        """
        print("\nSubMenú de Altas:")
        print("1. Alta Maquina")
        print("2. Alta Actividad")
        print("3. Alta Operario")
        print("4. Alta Repuesto")
        print("5. Alta Consumible")
        print("6. Alta Proveedor")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            self.alta_maquina()
        elif opcion == '2':
            self.alta_actividad()
        elif opcion == '3':
            self.alta_operario()
        elif opcion == '4':
            self.alta_repuesto()
        elif opcion == '5':
            self.alta_consumible()
        elif opcion == '6':
            self.alta_proveedor()
        elif opcion == '9':
            self.ejecutar()
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")


    def mostrar_bajas(self):
        """
        # -----------------------------------------------------------------------------
        # Despliega el submenu de bajas, y aguarda el a eleccion de una opcion, 
        # llamando al metodo correspondiente.
        # En caso de opcion incorrecta imprime mensaje de error y regresa al menu principal. 
        # -----------------------------------------------------------------------------
        """        
        print("\nSubMenú de Altas:")
        print("1. Baja Maquina")
        print("2. Baja Actividad")
        print("3. Baja Operario")
        print("4. Baja Repuesto")
        print("5. Baja Consumible")
        print("6. Baja Proveedor")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            self.baja_maquina()
        elif opcion == '2':
            self.baja_actividad()
        elif opcion == '3':
            self.baja_operario()
        elif opcion == '4':
            self.baja_repuesto()
        elif opcion == '5':
            self.baja_consumible()
        elif opcion == '6':
            self.baja_proveedor()
        elif opcion == '9':
            self.ejecutar()
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")


# ------------------------------------------------------------------------------------------------------------------
# Aqui comienza el codigo con los metodos para hacer las consultas sobre y hacia la base de datos:
# alta_maquina()
# alta_actividad()
# alta_operario()
# alta_repuesto()
# alta_consumible()
# alta_proveedor()
# baja_maquina()
# baja_actividad()
# baja_operario()
# baja_repuesto()
# baja_consumible()
# baja_proveedor()  
# programar_actividad()
# historial_maquina()
# historial_operario()
# informe_almacen()
# carga_horas_diarias()
# ver_estadisticas_uso()
# salir()    
# ------------------------------------------------------------------------------------------------------------------ 
    def alta_maquina(self):
        print("Para continuar debe seleccionar tipo de maquina:")
        print("1. COSECHADORA")
        print("2. TRACTOR")
        print("3. CAMION")

        seleccion = input("Ingrese seleccion: ")
        if seleccion == '1':
            tipo_maquina = 'COSECHADORA'
        elif seleccion == '2':
            tipo_maquina = 'TRACTOR'
        elif seleccion == '3':
            tipo_maquina = 'CAMION'

        nombre = input("Ingrese nombre de la maquina: ")
        chasis = input("Ingrese codigo de chasis: ")
        motor = input("Ingrese codigo de motor: ")
        modelo = input("Ingrese modelo año: ")
        horas = input("Ingrese cantidad de horas de trabajo: ")

        consulta = "insert into maquina (Tipo_maquina, Nombre, Chasis, Motor, Modelo, Horas_de_Trabajo) values(%s, %s, %s, %s, %s, %s)"
        valores = (tipo_maquina, nombre, chasis, motor, modelo, horas)
        self.db.ejecutar_consulta(consulta, valores)
        print("Maquina ingresada correctamente.")
        

    def alta_actividad(self):
        print("Seleccione tipo de actividad: ")
        print("1. TRABAJO")
        print("2. MANTENIMIENTO")

        seleccion = input("Ingrese seleccion: ")
        if seleccion == '1':
            Tipo = 'TRABAJO'
        elif seleccion == '2':
            Tipo = 'MANTENIMIENTO'

        descripcion = input("Ingrese la descripción de la actividad: ")
        lugar = input("Ingrese el lugar de la actividad: ")
        limite_horas = input("Si la actividad es 'mantenimiento', ingrese limite de horas: ")
        id_maquina = input("Ingrese la maquina afectada a la actividad: ")
        id_operario = input("Ingrese el operario afectado a la actividad: ")

        consulta = "insert into actividad  (Tipo, Descripcion, Lugar, Limite_horas, Maquina_id_Maquina, Operario_idOperario) values(%s, %s, %s, %s, %s, %s)"
        valores = (Tipo, descripcion, lugar, limite_horas, id_maquina, id_operario)
        self.db.ejecutar_consulta(consulta, valores)
        print("Actividad ingresada correctamente.")


    def alta_operario(self):
        print("Seleccione categoria operario: ")
        print("1. CHOFER")
        print("2. MECANICO")

        seleccion = input("Ingrese seleccion: ")
        if seleccion == '1':
            categoria = 'CHOFER'
        elif seleccion == '2':
            categoria = 'MECANICO'

        nombre = input("Ingrese nombre de operario: ")
        apellido = input("Ingrese apellido del operario: ")
        esExterno = input("Si el operario no pertenece a la firma ingrese 'si' de lo contrario ingrese 'no' ")
        
        consulta = "insert into Operario  (nombre, apellido, categoria, esExterno) values(%s, %s, %s, %s)"
        valores = (nombre, apellido, categoria, esExterno)
        self.db.ejecutar_consulta(consulta, valores)
        print("Actividad ingresada correctamente.")
        

    def alta_repuesto(self):
        
        Descripcion = input("Ingrese descripción del repuesto: ")
        Marca = input("Ingrese la marca del repuesto original: ")
        Alternativo = input("Ingrese la marca del repuesto alternativo: ")
        id_activad = input("Ingrese la actividad a realizar: ")
        id_proveedor = input("Ingrese el proveedor del repuesto: ")
        id_almacen = input("Ingrese el codigo interno del almacen: ")
        
        consulta = "insert into Repuesto  (Descripcion, Marca, Alternativo, Actividad_id_Actividad, Proveedor_id_Proveedor, Almacen_id_Almacen) values(%s, %s, %s, %s,%s,%s)"
        valores = (Descripcion, Marca, Alternativo, id_activad,id_proveedor,id_almacen)
        self.db.ejecutar_consulta(consulta, valores)
        print("Repuesto agregado exitosamente...")

    def alta_consumible(self):
        Descripcion = input("Ingrese descripción del consumible: ")
        Marca = input("Ingrese la marca del consumible original: ")
        Alternativo = input("Ingrese la marca del consumible alternativo: ")
        id_activad = input("Ingrese la actividad a realizar: ")
        id_proveedor = input("Ingrese el proveedor del consumible: ")
        id_almacen = input("Ingrese el codigo interno del almacen: ")
        
        consulta = "insert into Consumible (Descripcion, Marca, Alternativo, Actividad_id_Actividad, Proveedor_id_Proveedor, Almacen_id_Almacen) values(%s, %s, %s, %s,%s,%s)"
        valores = (Descripcion, Marca, Alternativo, id_activad,id_proveedor,id_almacen)
        self.db.ejecutar_consulta(consulta, valores)
        print("Consumible agregado exitosamente...")
        
    def alta_proveedor(self):
        Nombre = input("Ingrese el nombre del proveedor: ")
        Direccion = input("Ingrese la dirección del proveedor: ")
        Despacho = input("Ingrese el lugar despacho: ")
        Pago = input("Ingrese el pago realizado: ")
                
        consulta = "insert into Proveedor (Nombre, Direccion, Despacho, Pago) values(%s, %s, %s, %s)"
        valores = (Nombre, Direccion, Despacho, Pago)
        self.db.ejecutar_consulta(consulta, valores)
        print("Proveedor ingresado exitosamente...")

    def baja_maquina(self):
        print("Para continuar debe seleccionar tipo de maquina a eliminar: ")
        print("1. COSECHADORA")
        print("2. TRACTOR")
        print("3. CAMION")

        seleccion = input("Ingrese seleccion: ")
        if seleccion == '1':
            tipo_maquina = 'COSECHADORA'
        elif seleccion == '2':
            tipo_maquina = 'TRACTOR'
        elif seleccion == '3':
            tipo_maquina = 'CAMION'
        else:
            print("Selección inválida.")
            return

        chasis = input("Ingrese codigo de chasis de la maquina a eliminar: ")

        # A continuación confirma que la maquinaria existe antes de intentar eliminarla para evitar errores y visualizar
        consulta_verificacion = "SELECT * FROM maquina WHERE Tipo_maquina = %s AND Chasis = %s"
        valores_verificacion = (tipo_maquina, chasis)
        resultado = self.db.obtener_resultados(consulta_verificacion, valores_verificacion)

        if resultado:
            confirmacion = input(f"¿Está seguro de que desea eliminar la maquinaria {tipo_maquina} con chasis {chasis}? `s` para CONFIRMAR, `n` CANCELAR: ")
            if confirmacion.lower() == 's':
                consulta_eliminacion = "DELETE FROM maquina WHERE Tipo_maquina = %s AND Chasis = %s"
                valores_eliminacion = (tipo_maquina, chasis)
                self.db.obtener_resultados(consulta_eliminacion, valores_eliminacion)
                print("Maquinaria eliminada correctamente.")
            else:
                print("Operación cancelada.")
        else:
            print("No se encontró una maquinaria con el tipo y chasis proporcionados.")
    

    def baja_actividad(self):
        print("Para continuar debe seleccionar tipo de actividad a eliminar: ")
        print("1. TRABAJO")
        print("2. MANTENIMIENTO")

        seleccion = input("Ingrese seleccion: ")
        if seleccion == '1':
            tipo_actividad = 'TRABAJO'
        elif seleccion == '2':
            tipo_actividad = 'MANTENIMIENTO'
        else:
            print("Selección inválida.")
            return
        descripcion_actividad = input("Ingrese la descripción de la actividad a eliminar: ")

    # A continuación, confirma que la actividad existe antes de intentar eliminar para evitar errores y visualizar
        consulta_verificacion = "SELECT * FROM actividad WHERE Tipo = %s AND Descripcion = %s"
        valores_verificacion = (tipo_actividad, descripcion_actividad)
        resultado = self.db.obtener_resultados(consulta_verificacion, valores_verificacion)

        if resultado:
            confirmacion = input(f"¿Está seguro de que desea eliminar la actividad {tipo_actividad} con descripción '{descripcion_actividad}'? `s` para CONFIRMAR, `n` para CANCELAR: ")
            if confirmacion.lower() == 's':
                consulta_eliminacion = "DELETE FROM actividad WHERE Tipo = %s AND Descripcion = %s"
                valores_eliminacion = (tipo_actividad, descripcion_actividad)
                self.db.obtener_resultados(consulta_eliminacion, valores_eliminacion)
                print("Actividad eliminada correctamente.")
            else:
               print("Operación cancelada.")
        else:
            print("No se encontró una actividad con el tipo y descripción proporcionados.")
            
    def baja_operario(self):
        print("Para continuar debe seleccionar tipo de operario: ")
        print("1. CHOFER")
        print("2. MECANICO")

        seleccion = input("Ingrese seleccion: ")
        if seleccion == '1':
            categoria = 'CHOFER'
        elif seleccion == '2':
            categoria = 'MECANICO'

        nombre = input("Ingrese nombre de operario: ")
        apellido = input("Ingrese apellido del operario: ")
        
        # A continuación, confirma que el operario existe antes de intentar eliminar para evitar errores y visualizar
        consulta_verificacion = "SELECT * FROM Operario WHERE nombre = %s AND apellido = %s"
        valores_verificacion = (categoria, nombre, apellido)
        resultado = self.db.obtener_resultados(consulta_verificacion, valores_verificacion)
        if resultado:
            confirmacion = input(f"¿Está seguro de que desea eliminar al operario {nombre} con descripción '{apellido}'? `s` para CONFIRMAR, `n` para CANCELAR: ")
            if confirmacion.lower() == 's':
                consulta_eliminacion = "DELETE FROM actividad WHERE Tipo = %s AND Descripcion = %s"
                valores_eliminacion = (nombre, apellido)
                self.db.obtener_resultados(consulta_eliminacion, valores_eliminacion)
                print("Operario eliminado correctamente.")
            else:
               print("Operación cancelada.")
        else:
            print("No se encontró un operario con el nómbre y apellido proporcionados.")
        

    def baja_repuesto(self):
        print("poner consulta para borrar repuesto")

    def baja_consumible(self):
        print("poner consulta para borrar consumible")

    def baja_proveedor(self):
        print("poner consulta para borrar proveedor")

    def programar_actividad(self):
        """
# ---------------------------------------------------------------------------------
# Aquí el usuario podrá agregar actividades a la tabla Actividad
# ---------------------------------------------------------------------------------         
        """ 
        print("poner consulta para agregar actividades a la tabla Actividad")



    def historial_maquina(self):
        """
# ---------------------------------------------------------------------------------
# Aquí el usuario podrá consultar las actividades realizadas por y sobre la maquina
# ---------------------------------------------------------------------------------         
        """
        print("generar consulta que traiga las actividades donde estuvo afectada la maquina")
        


    def historial_operario(self):
        """
# ---------------------------------------------------------------------------------
# Aquí el usuario podrá consultar las actividades realizadas por un operario 
# ---------------------------------------------------------------------------------         
        """        
        print("generar consulta que traiga las actividades realizadas por el operario")


    def informe_almacen(self):
        """
# ---------------------------------------------------------------------------------
# Aquí el usuario podrá consultar el stock del almacen discriminado en cantidad actual y
# cantidad critica.
# ---------------------------------------------------------------------------------         
        """        
        print("Generar consulta que muestre el stock de almacen y las cantidades limite")
        


    def carga_horas_diarias(self):
        """
# ---------------------------------------------------------------------------------
# Aquí el usuario cargara la cantidad de horas trabajadas por una maquina al finalizar
# la jornada de trabajo. 
# Este metodo arroja una alarma de actividad pendiente si se alcanza el limite de horas 
# para dicha actividad.
# ---------------------------------------------------------------------------------         
        """          
        print("Generar consulta para actualizar el contador de horas a una maquina determinada")
        print("llamar al metodo alerta de mantenimiento")



    def ver_estadisticas_uso(self):
        """
# ---------------------------------------------------------------------------------
# Esta consulta imprime estadisticas generales de la Flota
# ---------------------------------------------------------------------------------         
        """ 
        print("generar una consulta para tirar estadisticas ")
        


 
    def alerta_mantenimiento(self): 
        """
# -----------------------------------------------------------------
# Imprime una alerta de mantenimiento para una maquina determinada. Se evalua al ingreso de las horas trabajadas.
# -----------------------------------------------------------------        
        """
        print("consulta para generar una alerta de mantenimiento y/o actividad")



    def alerta_almacen(self):
        """
# -----------------------------------------------------------------
# Imprime una alerta de cantidad critica de insumos, se evalua cada vez que cambia el stock de almacen
# -----------------------------------------------------------------     
        """ 
        print("Generar consulta para tirar alarma en caso de que stock < cantidad critica")

 
    def compra_semanal(self): 
        """
# -----------------------------------------------------------------
# Imprime un reporte semanal de compras para reponer stock de almacen en estado critico.
# -----------------------------------------------------------------     
        """ 
        print("Generar consulta que devuelva lista de compra para reponer stock")




    def salir(self): 
        """
# -----------------------------------------------------------------
# Imprime mensaje de despedida antes de salir del programa.
# -----------------------------------------------------------------     
        """ 
        print("Saliendo del programa...")

