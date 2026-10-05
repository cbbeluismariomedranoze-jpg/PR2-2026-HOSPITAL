from tkinter import END, Tk
from tkinter import messagebox

from Conexion import conectar
from ConsultoriosV import VentanaConsultorios


class Consultorios(VentanaConsultorios):

    def __init__(self, formulario, al_cerrar=None):

        super().__init__(formulario, al_cerrar)

        self.btnNuevo.config(command=self.nuevo)
        self.btnGuardar.config(command=self.registrar)
        self.btnModificar.config(command=self.modificar)
        self.btnEliminar.config(command=self.eliminar)
        self.btnSalir.config(command=self.salir)

        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        # Mostrar registros
        self.cargar()

    def nuevo(self):

        self.txtNumero.delete(0, END)
        self.txtDetalle.delete(0, END)
        self.cmbUbicacion.set("")

        self.txtNumero.focus()

    def registrar(self):

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        INSERT INTO consultorios
        (nro, detalle, ubicacion)
        VALUES (%s, %s, %s)
        """

        datos = (self.txtNumero.get(), self.txtDetalle.get(), self.cmbUbicacion.get())

        try:

            cursor.execute(sql, datos)
            conexion.commit()

            messagebox.showinfo("Hospital", "Consultorio registrado correctamente.")

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

        sql = "SELECT * FROM consultorios"

        try:

            cursor.execute(sql)

            registros = cursor.fetchall()

            for fila in registros:

                self.tabla.insert("", END, values=fila)

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def seleccionar(self, event):

        registro = self.tabla.focus()

        if registro == "":
            return

        datos = self.tabla.item(registro, "values")

        self.nuevo()

        self.txtNumero.insert(0, datos[0])
        self.txtDetalle.insert(0, datos[1])
        self.cmbUbicacion.set(datos[2])

    def modificar(self):

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        UPDATE consultorios
        SET detalle=%s,
            ubicacion=%s
        WHERE nro=%s
        """

        datos = (self.txtDetalle.get(), self.cmbUbicacion.get(), self.txtNumero.get())

        try:

            cursor.execute(sql, datos)
            conexion.commit()

            messagebox.showinfo("Hospital", "Consultorio modificado correctamente.")

            self.cargar()
            self.nuevo()

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def eliminar(self):

        conexion = conectar()

        if conexion is None:
            return

        if not messagebox.askyesno("Hospital", "¿Desea eliminar este consultorio?"):
            return

        cursor = conexion.cursor()

        sql = "DELETE FROM consultorios WHERE nro=%s"

        try:

            cursor.execute(sql, (self.txtNumero.get(),))
            conexion.commit()

            messagebox.showinfo("Hospital", "Consultorio eliminado correctamente.")

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

    app = Consultorios(raiz)

    raiz.mainloop()
