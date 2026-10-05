from tkinter import END, Tk
from tkinter import messagebox

from Conexion import conectar
from DoctoresV import VentanaDoctores


class Doctores(VentanaDoctores):

    def __init__(self, ventana, al_cerrar=None):

        super().__init__(ventana, al_cerrar)

        self.btnNuevo.config(command=self.nuevo)

        self.btnGuardar.config(command=self.guardar)

        self.btnModificar.config(command=self.modificar)

        self.btnEliminar.config(command=self.eliminar)

        self.btnSalir.config(command=self.salir)

        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        self.cargar_especialidades()
        self.cargar()

    def nuevo(self):

        self.txtCi.delete(0, END)
        self.ci_original = None

        self.txtNombres.delete(0, END)
        self.txtTelefono.delete(0, END)

        self.cmbEspecialidad.set("")

        self.txtCi.focus()

    def validar(self, requiere_clave=True):
        ci = self.txtCi.get().strip()
        nombres = self.txtNombres.get().strip()
        telefono = self.txtTelefono.get().strip()
        espe = self.cmbEspecialidad.get().strip()

        if not ci:
            messagebox.showwarning("Validación", "No deje espacio en blanco en el campo CI.")
            return False

        if not nombres:
            messagebox.showwarning("Validación", "No deje espacio en blanco en el campo Nombres.")
            return False
        if not espe:
            messagebox.showwarning(
                "Validación", "No deje espacio en blanco en el campo Especialidad."
            )
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
            cursor.execute("SELECT ci FROM doctores WHERE ci = %s", (ci,))
            registro = cursor.fetchone()

            if registro is not None:
                messagebox.showerror("Error", "Ese CI ya está registrado.")
                return False

        finally:
            if "cursor" in locals():
                cursor.close()
            conexion.close()

        return True

    def cargar_especialidades(self):

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        try:

            cursor.execute("SELECT especialidad FROM especialidades")

            registros = cursor.fetchall()

            lista = []

            for fila in registros:
                lista.append(fila[0])

            self.cmbEspecialidad["values"] = lista

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def guardar(self):
        if not self.validar(requiere_clave=True):
            return
        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        INSERT INTO doctores
        (
            ci,
            nombres,
            telefono,
            especialidad
        )
        VALUES
        (%s,%s,%s,%s)
        """

        datos = (
            self.txtCi.get(),
            self.txtNombres.get(),
            self.txtTelefono.get(),
            self.cmbEspecialidad.get(),
        )

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Doctor registrado correctamente.")

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

            cursor.execute("SELECT * FROM doctores")

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

        self.nuevo()

        self.txtCi.insert(0, datos[0])
        self.ci_original = str(datos[0]).strip()
        self.txtNombres.insert(0, datos[1])

        self.txtTelefono.insert(0, datos[2])

        self.cmbEspecialidad.set(datos[3])

    def modificar(self):
        if not self.validar(requiere_clave=False):
            return

        if self.txtCi.get().strip() != self.ci_original:
            messagebox.showerror("Error", "No se puede cambiar el CI.")
            return

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        UPDATE doctores
        SET
            nombres=%s,
            telefono=%s,
            especialidad=%s
        WHERE ci=%s
        """

        datos = (
            self.txtNombres.get(),
            self.txtTelefono.get(),
            self.cmbEspecialidad.get(),
            self.txtCi.get(),
        )

        try:

            cursor.execute(sql, datos)

            conexion.commit()
            messagebox.showinfo("Hospital", "Doctor modificado correctamente.")
            self.cargar()
            self.nuevo()

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def eliminar(self):

        if self.txtCi.get() == "":

            messagebox.showwarning("Hospital", "Seleccione un doctor.")

            return

        respuesta = messagebox.askyesno("Hospital", "¿Desea eliminar este doctor?")

        if respuesta == False:
            return

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        try:

            cursor.execute("DELETE FROM doctores WHERE ci=%s", (self.txtCi.get(),))

            conexion.commit()

            messagebox.showinfo("Hospital", "Doctor eliminado correctamente.")

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

    app = Doctores(raiz)

    raiz.mainloop()
