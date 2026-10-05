from tkinter import END, Tk
from tkinter import messagebox
import hashlib

from Conexion import conectar
from UsuariosV import VentanaUsuarios


class Usuarios(VentanaUsuarios):

    def __init__(self, ventana, al_cerrar=None):

        super().__init__(ventana, al_cerrar)

        self.btnNuevo.config(command=self.nuevo)

        self.btnGuardar.config(command=self.guardar)

        self.btnModificar.config(command=self.modificar)

        self.btnEliminar.config(command=self.eliminar)

        self.btnSalir.config(command=self.salir)

        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        self.cargar()

    def encriptar(self, clave):

        return hashlib.md5(clave.encode("utf-8")).hexdigest()

    def nuevo(self):

        self.txtNombres.delete(0, END)

        self.txtUsuario.delete(0, END)

        self.txtClave.delete(0, END)

        self.cmbNivel.set("")

        self.cmbEstado.set("")

        self.txtNombres.focus()

    def guardar(self):

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        INSERT INTO usuarios
        (
            nombres,
            usuario,
            clave,
            nivel,
            estado
        )
        VALUES
        (%s,%s,%s,%s,%s)
        """

        datos = (
            self.txtNombres.get(),
            self.txtUsuario.get(),
            self.encriptar(self.txtClave.get()),
            self.cmbNivel.get(),
            1 if self.cmbEstado.get() == "Activo" else 0,
        )

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Usuario registrado correctamente.")

            self.cargar()
            self.nuevo()

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def cargar(self):

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        self.tabla.delete(*self.tabla.get_children())

        try:

            cursor.execute("""
                SELECT 
                id,
                nombres,
                usuario,
                nivel,
                estado
                FROM usuarios
                """)

            registros = cursor.fetchall()

            for fila in registros:

                estado = "Activo" if fila[4] == 1 else "Inactivo"

                self.tabla.insert("", END, values=(fila[0], fila[1], fila[2], fila[3], estado))

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def seleccionar(self, event):

        fila = self.tabla.focus()

        if fila == "":
            return

        datos = self.tabla.item(fila, "values")

        self.nuevo()

        self.txtNombres.insert(0, datos[1])

        self.txtUsuario.insert(0, datos[2])

        self.cmbNivel.set(datos[3])

        self.cmbEstado.set(datos[4])

    def modificar(self):

        fila = self.tabla.focus()

        if fila == "":

            messagebox.showwarning("Hospital", "Seleccione un usuario.")

            return

        datos_tabla = self.tabla.item(fila, "values")

        id_usuario = datos_tabla[0]

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        if self.txtClave.get() != "":

            sql = """
            UPDATE usuarios
            SET
                nombres=%s,
                usuario=%s,
                clave=%s,
                nivel=%s,
                estado=%s
            WHERE id=%s
            """

            datos = (
                self.txtNombres.get(),
                self.txtUsuario.get(),
                self.encriptar(self.txtClave.get()),
                self.cmbNivel.get(),
                1 if self.cmbEstado.get() == "Activo" else 0,
                id_usuario,
            )

        else:

            sql = """
            UPDATE usuarios
            SET
                nombres=%s,
                usuario=%s,
                nivel=%s,
                estado=%s
            WHERE id=%s
            """

            datos = (
                self.txtNombres.get(),
                self.txtUsuario.get(),
                self.cmbNivel.get(),
                1 if self.cmbEstado.get() == "Activo" else 0,
                id_usuario,
            )

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Usuario modificado correctamente.")

            self.cargar()
            self.nuevo()

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def eliminar(self):

        fila = self.tabla.focus()

        if fila == "":

            messagebox.showwarning("Hospital", "Seleccione un usuario.")

            return

        datos = self.tabla.item(fila, "values")

        respuesta = messagebox.askyesno("Hospital", "¿Desea eliminar este usuario?")

        if respuesta == False:
            return

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        try:

            cursor.execute(
                """
                DELETE FROM usuarios
                WHERE id=%s
                """,
                (datos[0],),
            )

            conexion.commit()

            messagebox.showinfo("Hospital", "Usuario eliminado correctamente.")

            self.cargar()
            self.nuevo()

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def salir(self):
        if self.al_cerrar:
            self.al_cerrar()
        else:
            self.ventana.destroy()


if __name__ == "__main__":

    raiz = Tk()
    app = Usuarios(raiz)
    raiz.mainloop()
