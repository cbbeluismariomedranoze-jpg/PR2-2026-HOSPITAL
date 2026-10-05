from tkinter import END, Tk
from tkinter import messagebox

from Conexion import conectar
from DiagnosticosV import VentanaDiagnosticos


class Diagnosticos(VentanaDiagnosticos):

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

        self.txtAtencion.delete(0, END)

        self.txtDetalle.delete(0, END)

        self.txtAtencion.focus()

    def guardar(self):

        if self.txtAtencion.get() == "":

            messagebox.showwarning("Hospital", "Los campos estan en blanco.")

            return

        conexion = conectar()

        cursor = conexion.cursor()

        sql = """

        INSERT INTO diagnosticos
        (id_atencion,detalle)

        VALUES(%s,%s)

        """

        datos = (self.txtAtencion.get(), self.txtDetalle.get())

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Diagnóstico registrado correctamente.")

            self.cargar()
            self.nuevo()

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def cargar(self):

        conexion = conectar()

        cursor = conexion.cursor()

        self.tabla.delete(*self.tabla.get_children())

        cursor.execute("SELECT * FROM diagnosticos")

        registros = cursor.fetchall()

        for fila in registros:

            self.tabla.insert("", END, values=fila)

        conexion.close()

    def seleccionar(self, event):

        fila = self.tabla.focus()

        if fila == "":

            return

        datos = self.tabla.item(fila)["values"]

        self.txtAtencion.delete(0, END)

        self.txtDetalle.delete(0, END)

        self.txtAtencion.insert(0, datos[1])

        self.txtDetalle.insert(0, datos[2])

    def modificar(self):

        conexion = conectar()

        cursor = conexion.cursor()

        sql = """

        UPDATE diagnosticos

        SET detalle=%s

        WHERE id_atencion=%s

        """

        datos = (self.txtDetalle.get(), self.txtAtencion.get())

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Diagnóstico modificado correctamente.")

            self.cargar()
            self.nuevo()

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def eliminar(self):

        conexion = conectar()

        cursor = conexion.cursor()

        sql = """

        DELETE FROM diagnosticos

        WHERE id_atencion=%s

        """

        try:

            cursor.execute(sql, (self.txtAtencion.get(),))

            conexion.commit()

            messagebox.showinfo("Hospital", "Diagnóstico eliminado correctamente.")

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

    app = Diagnosticos(raiz)

    raiz.mainloop()
