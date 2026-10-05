from tkinter import END, Tk
from tkinter import messagebox
from datetime import datetime

from Conexion import conectar
from CirugiasV import VentanaCirugias


class Cirugias(VentanaCirugias):

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

        self.txtId.delete(0, END)
        self.txtPaciente.delete(0, END)
        self.txtDoctor.delete(0, END)
        self.txtQuirofano.delete(0, END)
        self.txtEnfermera.delete(0, END)
        self.txtFecha.delete(0, END)
        self.txtTipo.delete(0, END)
        self.txtDescripcion.delete(0, END)

        self.cmbEstado.set("")

        self.txtFecha.insert(0, datetime.now().strftime("%Y-%m-%d"))

        self.txtPaciente.focus()

    def guardar(self):

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        INSERT INTO cirugias
        (
        ci_paciente,
        ci_doctor,
        nro_quirofano,
        ci_enfermera,
        fecha,
        tipo,
        descripcion,
        estado
        )
        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        datos = (
            self.txtPaciente.get(),
            self.txtDoctor.get(),
            self.txtQuirofano.get(),
            self.txtEnfermera.get(),
            self.txtFecha.get(),
            self.txtTipo.get(),
            self.txtDescripcion.get(),
            self.cmbEstado.get(),
        )

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Cirugía registrada correctamente.")

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
        SELECT
        id,
        ci_paciente,
        ci_doctor,
        nro_quirofano,
        ci_enfermera,
        fecha,
        tipo,
        descripcion,
        estado
        FROM cirugias
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

        self.nuevo()

        self.txtId.insert(0, datos[0])

        self.txtPaciente.insert(0, datos[1])

        self.txtDoctor.insert(0, datos[2])

        self.txtQuirofano.insert(0, datos[3])

        self.txtEnfermera.insert(0, datos[4])

        self.txtFecha.insert(0, datos[5])

        self.txtTipo.insert(0, datos[6])

        self.txtDescripcion.insert(0, datos[7])

        self.cmbEstado.set(datos[8])

    def modificar(self):

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        UPDATE cirugias
        SET
        ci_paciente=%s,
        ci_doctor=%s,
        nro_quirofano=%s,
        ci_enfermera=%s,
        fecha=%s,
        tipo=%s,
        descripcion=%s,
        estado=%s
        WHERE id=%s
        """

        datos = (
            self.txtPaciente.get(),
            self.txtDoctor.get(),
            self.txtQuirofano.get(),
            self.txtEnfermera.get(),
            self.txtFecha.get(),
            self.txtTipo.get(),
            self.txtDescripcion.get(),
            self.cmbEstado.get(),
            self.txtId.get(),
        )

        try:

            cursor.execute(sql, datos)

            conexion.commit()

            messagebox.showinfo("Hospital", "Cirugía modificada correctamente.")

            self.cargar()
            self.nuevo()

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def eliminar(self):

        if self.txtId.get() == "":

            messagebox.showwarning("Hospital", "Seleccione una cirugía.")

            return

        respuesta = messagebox.askyesno("Eliminar", "¿Desea eliminar esta cirugía?")

        if respuesta == False:
            return

        conexion = conectar()

        cursor = conexion.cursor()

        sql = """
        DELETE FROM cirugias
        WHERE id=%s
        """

        try:

            cursor.execute(sql, (self.txtId.get(),))

            conexion.commit()

            messagebox.showinfo("Hospital", "Cirugía eliminada correctamente.")

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

    app = Cirugias(raiz)

    raiz.mainloop()
