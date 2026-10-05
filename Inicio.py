from tkinter import messagebox
from Conexion import conectar
import hashlib


def ocultar(cadena):
    return hashlib.md5(cadena.encode("utf-8")).hexdigest()


class Inicio:

    def __init__(self, vista):
        self.vista = vista

    def iniciar_sesion(self):

        usuario = self.vista.txtUsuario.get().strip()
        clave = self.vista.txtClave.get().strip()

        if usuario == "" or clave == "":

            messagebox.showwarning("Datos incompletos", "Ingrese usuario y contraseña.")

            return

        conexion = conectar()

        if conexion is None:

            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")

            return

        cursor = conexion.cursor()

        try:

            sql = """
            SELECT
                id,
                nombres,
                usuario,
                clave,
                nivel,
                estado
            FROM usuarios
            WHERE usuario=%s
            """

            cursor.execute(sql, (usuario,))

            fila = cursor.fetchone()

            if fila is None:

                messagebox.showerror("Acceso denegado", "Usuario inexistente.")

                return

            clave_hash = ocultar(clave)

            if fila[3] != clave_hash:

                messagebox.showerror("Acceso denegado", "Contraseña incorrecta.")

                return

            if int(fila[5]) != 1:

                messagebox.showwarning("Usuario inactivo", "El usuario está deshabilitado.")

                return

            datos_usuario = {
                "id": fila[0],
                "nombres": fila[1],
                "usuario": fila[2],
                "nivel": fila[4],
                "estado": fila[5],
            }

            messagebox.showinfo("Bienvenido", f"Bienvenido/a {fila[1]}")

            self.abrir_menu(datos_usuario)

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def abrir_menu(self, datos_usuario):

        from MenuPrincipalV import MenuPrincipalV

        self.vista.ventana.destroy()

        from tkinter import Tk

        nueva_ventana = Tk()

        MenuPrincipalV(nueva_ventana, datos_usuario)

        nueva_ventana.state("zoomed")

        nueva_ventana.mainloop()

    if __name__ == "__main__":

        from tkinter import Tk
        from InicioV import InicioV

        ventana = Tk()
        app = InicioV(ventana)
        ventana.mainloop()
