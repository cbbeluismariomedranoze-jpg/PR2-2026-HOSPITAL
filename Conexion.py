import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="bdhospital_privado"
        )

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")

        return conexion

    except mysql.connector.Error as error:
        print("Error al conectar a MySQL:", error)
        return None