from tkinter import END, Tk
from tkinter import messagebox
from Conexion import conectar
from KardexV import VentanaKardex
from datetime import datetime


class Kardex(VentanaKardex):

    def __init__(self, ventana, al_cerrar=None):

        super().__init__(ventana, al_cerrar)

        self.btnNuevo.config(command=self.nuevo)

        self.btnGuardar.config(command=self.guardar)

        self.btnSalir.config(command=self.salir)

        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        self.cargar()

    def nuevo(self):

        self.txtNro.delete(0, END)
        self.txtPaciente.delete(0, END)
        self.txtFecha.delete(0, END)
        self.txtDescripcion.delete(0, END)

        self.txtFecha.insert(0, datetime.now().strftime("%Y-%m-%d"))

        self.txtPaciente.focus()

    def guardar(self):

        if self.txtPaciente.get() == "":

            messagebox.showwarning("Hospital", "Ingrese el CI del paciente.")

            self.txtPaciente.focus()
            return

        if self.txtDescripcion.get() == "":

            messagebox.showwarning("Hospital", "Ingrese la descripción médica.")

            self.txtDescripcion.focus()
            return

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        INSERT INTO kardex
        (ci_paciente, fecha, descripcion)
        VALUES(%s,%s,%s)
        """

        datos = (self.txtPaciente.get(), self.txtFecha.get(), self.txtDescripcion.get())

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Registro de kardex guardado correctamente.")

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

        sql = """
        SELECT nro, ci_paciente, fecha, descripcion
        FROM kardex
        ORDER BY fecha DESC
        """

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

        fila = self.tabla.focus()

        if fila == "":
            return

        datos = self.tabla.item(fila)["values"]

        self.txtNro.delete(0, END)

        self.txtPaciente.delete(0, END)

        self.txtFecha.delete(0, END)

        self.txtDescripcion.delete(0, END)

        self.txtNro.insert(0, datos[0])

        self.txtPaciente.insert(0, datos[1])

        self.txtFecha.insert(0, datos[2])

        self.txtDescripcion.insert(0, datos[3])

    def salir(self):

        if self.al_cerrar:
            self.al_cerrar()
        else:
            self.ventana.destroy()


if __name__ == "__main__":

    raiz = Tk()

    app = Kardex(raiz)

    raiz.mainloop()
