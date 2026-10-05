from tkinter import END, Tk
from tkinter import messagebox
from Conexion import conectar
from EnfermerasV import VentanaEnfermeras


class Enfermeras(VentanaEnfermeras):

    def __init__(self, ventana, al_cerrar=None):
        print("VERSION NUEVA CARGADA")
        super().__init__(ventana, al_cerrar)

        self.btnNuevo.config(command=self.nuevo)

        self.btnGuardar.config(command=self.guardar)

        self.btnModificar.config(command=self.modificar)

        self.btnEliminar.config(command=self.eliminar)

        self.btnSalir.config(command=self.salir)

        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        self.cargar()

    def nuevo(self):

        self.txtCi.delete(0, END)
        self.ci_original = None
        self.txtNombres.delete(0, END)

        self.txtTelefono.delete(0, END)

        self.txtCi.focus()

    def validar(self, requiere_clave=True):
        ci = self.txtCi.get().strip()
        nombres = self.txtNombres.get().strip()
        telefono = self.txtTelefono.get().strip()

        if not ci:
            messagebox.showwarning("Validación", "No deje espacio en blanco en el campo CI.")
            return False

        if not nombres:
            messagebox.showwarning("Validación", "No deje espacio en blanco en el campo Nombres.")
            return False

        if not telefono.isdigit():
            messagebox.showerror("Error", "El teléfono debe contener solo números.")
            return False

        if not ci.isdigit():
            messagebox.showerror("Error", "El CI debe contener solo números.")
            return False

        ci_original = str(getattr(self, "ci_original", "") or "").strip()

        if not requiere_clave and ci_original == ci:
            return True

        conexion = conectar()

        if conexion is None:
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT ci FROM enfermeras WHERE ci = %s", (ci,))
            registro = cursor.fetchone()

            if registro is not None:
                messagebox.showerror("Error", "Ese CI ya está registrado.")
                return False

        finally:
            if "cursor" in locals():
                cursor.close()
            conexion.close()

        return True

    def guardar(self):
        if not self.validar(requiere_clave=True):
            return
        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        INSERT INTO enfermeras
        (ci,nombres,telefono)
        VALUES(%s,%s,%s)
        """

        datos = (self.txtCi.get(), self.txtNombres.get(), self.txtTelefono.get())

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Enfermera registrada correctamente.")

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

        cursor.execute("SELECT * FROM enfermeras")

        registros = cursor.fetchall()

        for fila in registros:

            self.tabla.insert("", END, values=fila)

        cursor.close()
        conexion.close()

    def seleccionar(self, event):

        fila = self.tabla.focus()

        if fila == "":
            return

        datos = self.tabla.item(fila, "values")

        self.nuevo()

        self.txtCi.insert(0, datos[0])
        self.ci_original = str(datos[0]).strip()

        self.txtNombres.insert(0, datos[1])

        self.txtTelefono.insert(0, datos[2])

    def modificar(self):
        if not self.validar(requiere_clave=False):
            return

        if self.txtCi.get().strip() != self.ci_original:
            messagebox.showerror("Error", "No se puede cambiar el CI .")
            return

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        UPDATE enfermeras
        SET nombres=%s,
            telefono=%s
        WHERE ci=%s
        """

        datos = (self.txtNombres.get(), self.txtTelefono.get(), self.txtCi.get())

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Enfermera modificada correctamente.")

            self.cargar()
            self.nuevo()

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def eliminar(self):

        if self.txtCi.get() == "":

            messagebox.showwarning("Hospital", "Seleccione una enfermera.")

            return

        respuesta = messagebox.askyesno("Hospital", "¿Desea eliminar esta enfermera?")

        if respuesta == False:
            return

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        DELETE FROM enfermeras
        WHERE ci=%s
        """

        try:

            cursor.execute(sql, (self.txtCi.get(),))

            conexion.commit()

            messagebox.showinfo("Hospital", "Enfermera eliminada correctamente.")

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

    app = Enfermeras(raiz)

    raiz.mainloop()
