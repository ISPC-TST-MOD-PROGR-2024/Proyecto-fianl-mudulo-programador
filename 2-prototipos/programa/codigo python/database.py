import mysql.connector

class Database:
    """
    Clase Database para manejar la conexión y operaciones con una base de datos MySQL.
    Atributos:
    -----------
    midb : mysql.connector.connection.MySQLConnection
    La conexión a la base de datos MySQL.
    cursor : mysql.connector.cursor.MySQLCursor
    El cursor para ejecutar consultas en la base de datos MySQL. 
    Métodos:
    --------
    __init__(self, host, user, password, database):
    Inicializa la conexión a la base de datos MySQL.

    ejecutar_consulta(self, consulta, valores=None):
    Ejecuta una consulta SQL (INSERT, UPDATE, DELETE) en la base de datos. 

    obtener_resultados(self, consulta, valores=None):
    Ejecuta una consulta SQL (SELECT) y retorna los resultados.

    cerrar_conexion(self):
    Cierra la conexión a la base de datos y el cursor.
    """
    def __init__(host, user, password, database):
        """
        Inicializa la conexión a la base de datos MySQL.
        Parámetros:
        -----------
        host : str
        La dirección del host donde se encuentra la base de datos MySQL.
        user : str
        El nombre de usuario para la conexión a la base de datos. 
        password : str
        La contraseña para la conexión a la base de datos.
        database : str
        El nombre de la base de datos a la que se va a conectar. 
        Excepciones:
        ------------
        Exception
        Si la conexión a la base de datos falla, se imprime un mensaje de error. """
    try:
        midb = mysql.connector.connect(
            host='localhost',
            database='mydb',
            user='root',
            password='root'
            )
        cursor = midb.cursor()
        print("Conexión establecida exitosamente")
    except:
        print("Error: ", mysql.connector.Error)
        midb = None
        cursor = None


    #Metodos para obtener, insertar, actualizar y eliminar datos
    def obtener_resultados(self, consulta, valores=None):
        """
        Ejecuta una consulta SQL (INSERT, UPDATE, DELETE) en la base de datos. Parámetros:
        -----------
        consulta : str
        La consulta SQL a ejecutar.
        valores : tuple, opcional
        Los valores que se deben insertar en la consulta SQL (por defecto None). """
        self.cursor.execute(consulta, valores)
        return self.cursor.fetchall()

    def ejecutar_consulta(self, consulta, valores=None):
        """
        Ejecuta una consulta SQL (SELECT) y retorna los resultados.
        Parámetros:
        -----------
        consulta : str
        La consulta SQL a ejecutar.
        valores : tuple, opcional
        Los valores que se deben insertar en la consulta SQL (por defecto None). Retorna:
        --------
        list
        Una lista de tuplas con los resultados de la consulta.
        """
        self.cursor.execute(consulta, valores)
        self.midb.commit()

    def cerrar_conexion(self):  #Metodo para cerrar conexion

        self.cursor.close()
        self.midb.close()

#Lineas para probar la conexion con el motor SQL. Dejar comentadas cuando se arma el programa complet
FLota = Database('mydb','root','root')
print(FLota)
print("iiiuupiiii")