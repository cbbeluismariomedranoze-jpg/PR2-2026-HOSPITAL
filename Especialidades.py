from tkinter import END, Tk
from tkinter import messagebox

from Conexion import conectar
from EspecialidadesV import VentanaEspecialidades


class Especialidades(VentanaEspecialidades):

    def __init__(self, ventana, al_cerrar=None):

        super().__init__(ventana, al_cerrar)

        self.btnNuevo.config(command=self.nuevo)

        self.btnGuardar.config(command=self.guardar)

        self.btnModificar.config(command=self.modificar)

        self.btnEliminar.config(command=self.eliminar)

        self.btnSalir.config(command=self.salir)

        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        self.cargar()

    def nuevo(self):

        self.txtEspecialidad.delete(0, END)
        self.ci_original = None
        self.txtEspecialidad.focus()

    def validar(self, requiere_clave=True):

        especialidad = self.txtEspecialidad.get().strip()
        if not especialidad:
            messagebox.showerror("Error", "El campo especialidad no puede estar vacío.")
            return False

        if not especialidad.isalpha():
            messagebox.showerror("Error", "El campo especialidad no puede contener números.")
            return False

        especialidad_original = str(getattr(self, "especialidad_anterior", "") or "").strip()

        if not requiere_clave and especialidad_original == especialidad:
            return True

        conexion = conectar()

        if conexion is None:
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT COUNT(*) FROM especialidades WHERE especialidad=%s", (especialidad,)
            )
            registro = cursor.fetchone()

            if registro is not None:
                messagebox.showerror("Error", "Esa especialidad ya existe.")
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
        INSERT INTO especialidades
        (especialidad)
        VALUES(%s)
        """

        try:

            cursor.execute(sql, (self.txtEspecialidad.get(),))

            conexion.commit()

            messagebox.showinfo("Hospital", "Especialidad registrada correctamente.")

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

            cursor.execute("SELECT * FROM especialidades")

            registros = cursor.fetchall()

            for fila in registros:

                self.tabla.insert("", END, values=fila)

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

        self.especialidad_anterior = datos[0]
        self.nuevo()
        self.txtEspecialidad.insert(0, datos[0])
        self.ci_original = str(datos[0]).strip()

    def modificar(self):
        if not self.validar(requiere_clave=False):
            return

        if self.txtEspecialidad.get().strip() != self.ci_original:
            messagebox.showerror("Error", "No se puede cambiar el CI del paciente.")
            return

        if not hasattr(self, "especialidad_anterior"):

            messagebox.showwarning("Hospital", "Seleccione una especialidad para modificar.")
            return

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        UPDATE especialidades
        SET especialidad=%s
        WHERE especialidad=%s
        """

        datos = (self.txtEspecialidad.get(), self.especialidad_anterior)

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Especialidad modificada correctamente.")

            self.cargar()
            self.nuevo()

        except Exception as e:
            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def eliminar(self):

        if self.txtEspecialidad.get() == "":
            return

        respuesta = messagebox.askyesno("Hospital", "¿Desea eliminar esta especialidad?")

        if respuesta == False:
            return

        conexion = conectar()

        cursor = conexion.cursor()

        try:

            cursor.execute(
                "DELETE FROM especialidades WHERE especialidad=%s", (self.txtEspecialidad.get(),)
            )

            conexion.commit()

            messagebox.showinfo("Hospital", "Especialidad eliminada correctamente.")

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

    app = Especialidades(raiz)

    raiz.mainloop()
