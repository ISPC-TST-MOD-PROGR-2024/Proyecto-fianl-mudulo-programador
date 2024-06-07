from database import Database

class Menu:
    def __init__(self, db):
        self.db = db

# ------------------------------------------------------------------------------------------------------------------
# Metodo que muestra el menu en consola y espera el ingreso de un valor del menu para llamar al metodo correspondiente.
# En caso de no haber coincidencia con ninguno, imprime un mensaje de error.
# ------------------------------------------------------------------------------------------------------------------ 
    def ejecutar(self):
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
# ------------------------------------------------------------------------------------------------------------------
# Despliega el menu de opciones
# ------------------------------------------------------------------------------------------------------------------  
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
        # ------------------------------------------------------------------------------------------------------------------
        # Despliega el submenu de altas
        # ------------------------------------------------------------------------------------------------------------------ 
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

# ------------------------------------------------------------------------------------------------------------------
# Despliega el submenu de bajas
# ------------------------------------------------------------------------------------------------------------------ 
    def mostrar_bajas(self):
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
# Esta opción permitirá al usuario programar una actividad para una maquina.      
# ------------------------------------------------------------------------------------------------------------------ 
    def programar_actividad(self): 
        print("Esta opción permitirá al usuario ingresar los detalles de un nuevo trabajo de impresión 3D.")

# ------------------------------------------------------------------------------------------------------------------
# Aquí el usuario podrá consultar las actividades realizadas por y sobre la maquina
# ------------------------------------------------------------------------------------------------------------------ 

    def historial_maquina(self):
        print("Aquí el usuario podrá consultar el presupuesto basado en la lista de materiales")
        print("y el tiempo estimado de impresión.")

# ------------------------------------------------------------------------------------------------------------------
# Aquí el usuario podrá consultar las actividades realizadas por un usuario determinado
# ------------------------------------------------------------------------------------------------------------------ 
    def historial_operario(self):
        print("Muestra el estado actual del stock de materiales como filamentos, tuercas, tornillos, etc.")

# ------------------------------------------------------------------------------------------------------------------
# Permite ver el stock del almacen y las cantidades discriminadas
# en cantidad actual y cantidad critica      
# ------------------------------------------------------------------------------------------------------------------ 
    def informe_almacen(self):
        print("Permite ver el historial de trabajos realizados para un cliente específico y")
        print("aplicar descuentos si es un cliente frecuente.")

# ------------------------------------------------------------------------------------------------------------------
# Esta opción permite al usuario cargar la cantidad de horas trabajadas por una maquina al finalizar
# la jornada de trabajo.
# ------------------------------------------------------------------------------------------------------------------ 
    def carga_horas_diarias(self):  
        print("Esta opción permite ingresar o actualizar la cantidad de stock de un ")
        print("material específico.")


# ------------------------------------------------------------------------------------------------------------------
# Imprime las estadísticas generales de la flota
# ------------------------------------------------------------------------------------------------------------------ 
    def ver_estadisticas_uso(self): 
        print("Estadísticas de uso de materiales:")
        print("Devuelve las cantidades usadas de cada material")
        print("tomando como referencia los trabajos finalizados")


# ------------------------------------------------------------------------------------------------------------------
# Imprime una alerta de mantenimiento para una maquina determinada. Se evalua al ingreso de las horas trabajadas.
# ------------------------------------------------------------------------------------------------------------------ 
    def alerta_mantenimiento(self): 
        print("Estadísticas de uso de materiales:")


# ------------------------------------------------------------------------------------------------------------------
# Imprime una alerta de de cantidad critica de insumos, se evalua cada vez que cambia el stock de almacen
# ------------------------------------------------------------------------------------------------------------------ 
    def alerta_almacen(self): 
        print("Estadísticas de uso de materiales:")

# ------------------------------------------------------------------------------------------------------------------
# Imprime Reporte semanal de compras para reponer almacen en estado critico.
# ------------------------------------------------------------------------------------------------------------------ 
    def compra_semanal(self): 
        print("Estadísticas de uso de materiales:")


# ------------------------------------------------------------------------------------------------------------------
#Finaliza la ejecución del programa.
# ------------------------------------------------------------------------------------------------------------------ 

    def salir(self): 
        print("Saliendo del programa...")



#gestion_impresion = Menu() #creo una instacia de la clase 
#gestion_impresion.ejecutar() #llamo al metodo ejecutar para mostrar el menu de opciones