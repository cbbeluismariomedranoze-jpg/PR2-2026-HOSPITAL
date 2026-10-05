from tkinter import END, Tk
from tkinter import messagebox
from Conexion import conectar
from LaboratoriosV import VentanaLaboratorios
from datetime import datetime


class Laboratorios(VentanaLaboratorios):

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
        self.txtFecha.delete(0, END)
        self.txtResultado.delete(0, END)

        self.cmbEstado.set("")

        self.txtFecha.insert(0, datetime.now().strftime("%Y-%m-%d"))

        self.txtAtencion.focus()

    def guardar(self):

        conexion = conectar()

        cursor = conexion.cursor()

        sql = """

        INSERT INTO laboratorios
        (id_atencion,fecha,resultado,estado)

        VALUES(%s,%s,%s,%s)

        """

        datos = (
            self.txtAtencion.get(),
            self.txtFecha.get(),
            self.txtResultado.get(),
            self.cmbEstado.get(),
        )

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Laboratorio registrado correctamente.")

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

        cursor.execute("SELECT * FROM laboratorios")

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
        self.txtFecha.delete(0, END)
        self.txtResultado.delete(0, END)

        self.txtAtencion.insert(0, datos[1])
        self.txtFecha.insert(0, datos[2])
        self.txtResultado.insert(0, datos[3])
        self.cmbEstado.set(datos[4])

    def modificar(self):

        conexion = conectar()

        cursor = conexion.cursor()

        sql = """

        UPDATE laboratorios

        SET fecha=%s,
            resultado=%s,
            estado=%s

        WHERE id_atencion=%s

        """

        datos = (
            self.txtFecha.get(),
            self.txtResultado.get(),
            self.cmbEstado.get(),
            self.txtAtencion.get(),
        )

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Laboratorio modificado correctamente.")

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

        DELETE FROM laboratorios

        WHERE id_atencion=%s

        """

        try:

            cursor.execute(sql, (self.txtAtencion.get(),))

            conexion.commit()

            messagebox.showinfo("Hospital", "Laboratorio eliminado correctamente.")

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

    app = Laboratorios(raiz)

    raiz.mainloop()
