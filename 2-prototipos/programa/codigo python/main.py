from menu import Menu
from database import Database
# Programa para gestionar un BD MySQL
# Modelo de Proyecto Integrador
# Modulo Programador 2024
# ISPC - Prof. Lisandro Lanfranco
def main():
    print("##################* SILVER AGRO *##################\n\n#################* FLOTA CONTROL *################\n\n")
        # Crear una instancia de la base de datos
    db = Database('localhost', 'root', 'root', 'mydb')
    
    if db.midb and db.cursor:
            #print("Conexión establecida exitosamente ")
            menu = Menu(db)
            menu.ejecutar()
            db.cerrar_conexion()
    else:
        print("No se pudo establecer la conexión a la base de datos")
        #asegura que el archivo main.py se est ejecutando como programa principal
if __name__ == "__main__":
        main()