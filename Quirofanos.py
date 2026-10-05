from tkinter import END, Tk
from tkinter import messagebox

from Conexion import conectar
from QuirofanosV import VentanaQuirofanos


class Quirofanos(VentanaQuirofanos):

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

        self.txtNumero.delete(0, END)

        self.txtDetalle.delete(0, END)

        self.cmbUbicacion.set("")

        self.txtNumero.focus()

    def guardar(self):

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        INSERT INTO quirofanos
        (nro, detalle, ubicacion)
        VALUES (%s,%s,%s)
        """

        datos = (self.txtNumero.get(), self.txtDetalle.get(), self.cmbUbicacion.get())

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Quirófano registrado correctamente.")

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

        cursor.execute("SELECT * FROM quirofanos")

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

        self.txtNumero.delete(0, END)

        self.txtDetalle.delete(0, END)

        self.cmbUbicacion.set("")

        self.txtNumero.insert(0, datos[0])

        self.txtDetalle.insert(0, datos[1])

        self.cmbUbicacion.set(datos[2])

    def modificar(self):

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        UPDATE quirofanos
        SET detalle=%s,
            ubicacion=%s
        WHERE nro=%s
        """

        datos = (self.txtDetalle.get(), self.cmbUbicacion.get(), self.txtNumero.get())

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Quirófano modificado correctamente.")

            self.cargar()
            self.nuevo()

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def eliminar(self):

        if self.txtNumero.get() == "":

            messagebox.showwarning("Hospital", "Seleccione un quirófano.")

            return

        respuesta = messagebox.askyesno("Eliminar", "¿Desea eliminar este quirófano?")

        if respuesta == False:
            return

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        DELETE FROM quirofanos
        WHERE nro=%s
        """

        try:

            cursor.execute(sql, (self.txtNumero.get(),))

            conexion.commit()

            messagebox.showinfo("Hospital", "Quirófano eliminado correctamente.")

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

    app = Quirofanos(raiz)

    raiz.mainloop()
