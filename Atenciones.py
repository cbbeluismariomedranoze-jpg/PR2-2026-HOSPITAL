from tkinter import END, Tk
from tkinter import messagebox
from Conexion import conectar
from AtencionesV import VentanaAtenciones
from datetime import datetime


class Atenciones(VentanaAtenciones):

    def __init__(self, ventana, al_cerrar=None):

        super().__init__(ventana, al_cerrar)

        self.btnNuevo.config(command=self.nuevo)
        self.btnGuardar.config(command=self.guardar)
        self.btnModificar.config(command=self.modificar)
        self.btnEliminar.config(command=self.eliminar)
        self.btnSalir.config(command=self.salir)

        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)
        self.cargar_reserva()
        self.nuevo()
        self.cargar()

    def cargar_reserva(self):

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        try:
            cursor.execute("SELECT id FROM reservas ORDER BY id")
            reservas = [str(fila[0]) for fila in cursor.fetchall()]
            self.cmbReserva["values"] = reservas
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conexion.close()

    def nuevo(self):

        self.cmbReserva.set("")
        self.txtFecha.delete(0, END)
        self.txtPeso.delete(0, END)
        self.txtTalla.delete(0, END)
        self.txtTemperatura.delete(0, END)
        self.txtPresion.delete(0, END)
        self.txtMotivo.delete(0, END)
        self.txtDiagnostico.delete(0, END)
        self.txtTratamiento.delete(0, END)
        self.txtObservaciones.delete(0, END)

        self.txtFecha.insert(0, datetime.now().strftime("%Y-%m-%d"))

        self.id_seleccionado = None
        self.cmbReserva.focus()

    def validar(self):

        campos = {
            "ID Reserva": self.cmbReserva.get().strip(),
            "Fecha": self.txtFecha.get().strip(),
            "Peso": self.txtPeso.get().strip(),
            "Talla": self.txtTalla.get().strip(),
            "Temperatura": self.txtTemperatura.get().strip(),
            "Presión": self.txtPresion.get().strip(),
            "Motivo": self.txtMotivo.get().strip(),
            "Diagnóstico": self.txtDiagnostico.get().strip(),
            "Tratamiento": self.txtTratamiento.get().strip(),
            "Observaciones": self.txtObservaciones.get().strip(),
        }

        for nombre, valor in campos.items():
            if not valor:
                messagebox.showwarning("Validación", f"No deje el campo {nombre} en blanco.")
                return False

        numericos = {
            "Peso": campos["Peso"],
            "Talla": campos["Talla"],
            "Temperatura": campos["Temperatura"],
            "Presión": campos["Presión"],
        }

        for nombre, valor in numericos.items():
            try:
                float(valor)
            except ValueError:
                messagebox.showwarning("Validación", f"El campo {nombre} solo acepta números.")
                return False

        if not self._existe_reserva(campos["ID Reserva"]):
            messagebox.showerror("Error", "La reserva seleccionada no está registrada.")
            return False

        return True

    def _existe_reserva(self, id_reserva):

        conexion = conectar()

        if conexion is None:
            return False

        cursor = conexion.cursor()

        try:
            cursor.execute("SELECT 1 FROM reservas WHERE id = %s", (id_reserva,))
            return cursor.fetchone() is not None
        finally:
            cursor.close()
            conexion.close()

    def guardar(self):
        if not self.validar():
            return

        conexion = conectar()
        if conexion is None:
            return
        cursor = conexion.cursor()

        sql = """
        INSERT INTO atenciones
        (id_reserva,fecha,peso,talla,temperatura,presion,motivo,diagnostico,tratamiento,observaciones)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        datos = (
            self.cmbReserva.get(),
            self.txtFecha.get(),
            self.txtPeso.get(),
            self.txtTalla.get(),
            self.txtTemperatura.get(),
            self.txtPresion.get(),
            self.txtMotivo.get(),
            self.txtDiagnostico.get(),
            self.txtTratamiento.get(),
            self.txtObservaciones.get(),
        )

        try:
            cursor.execute(sql, datos)
            conexion.commit()

            messagebox.showinfo("Hospital", "Atención registrada correctamente.")

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

        cursor.execute("SELECT id,id_reserva,fecha,peso,temperatura FROM atenciones")

        registros = cursor.fetchall()

        for fila in registros:

            self.tabla.insert("", END, values=fila)

        conexion.close()

    def seleccionar(self, event):

        fila = self.tabla.focus()

        if fila == "":
            return

        datos = self.tabla.item(fila)["values"]

        id_atencion = datos[0]

        conexion = conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT id_reserva, fecha, peso, talla,
        temperatura, presion, motivo,
        diagnostico, tratamiento, observaciones
        FROM atenciones
        WHERE id=%s
        """

        cursor.execute(sql, (id_atencion,))
        registro = cursor.fetchone()

        conexion.close()

        if registro:

            self.txtFecha.delete(0, END)
            self.txtPeso.delete(0, END)
            self.txtTalla.delete(0, END)
            self.txtTemperatura.delete(0, END)
            self.txtPresion.delete(0, END)
            self.txtMotivo.delete(0, END)
            self.txtDiagnostico.delete(0, END)
            self.txtTratamiento.delete(0, END)
            self.txtObservaciones.delete(0, END)

            self.cmbReserva.set(registro[0])
            self.id_seleccionado = id_atencion
            self.txtFecha.insert(0, registro[1])
            self.txtPeso.insert(0, registro[2])
            self.txtTalla.insert(0, registro[3])
            self.txtTemperatura.insert(0, registro[4])
            self.txtPresion.insert(0, registro[5])
            self.txtMotivo.insert(0, registro[6])
            self.txtDiagnostico.insert(0, registro[7])
            self.txtTratamiento.insert(0, registro[8])
            self.txtObservaciones.insert(0, registro[9])

    def modificar(self):
        if not self.validar():
            return
        if self.id_seleccionado is None:
            messagebox.showwarning("Hospital", "Seleccione una atención.")
            return
        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        UPDATE atenciones
        SET 
            id_reserva=%s,
            fecha=%s,
            peso=%s,
            talla=%s,
            temperatura=%s,
            presion=%s,
            motivo=%s,
            diagnostico=%s,
            tratamiento=%s,
            observaciones=%s
        WHERE id=%s
        """

        datos = (
            self.cmbReserva.get(),
            self.txtFecha.get(),
            self.txtPeso.get(),
            self.txtTalla.get(),
            self.txtTemperatura.get(),
            self.txtPresion.get(),
            self.txtMotivo.get(),
            self.txtDiagnostico.get(),
            self.txtTratamiento.get(),
            self.txtObservaciones.get(),
            self.id_seleccionado,
        )

        try:

            cursor.execute(sql, datos)

            if cursor.rowcount == 0:
                messagebox.showwarning("Hospital", "No existe la atención o no hubo cambios.")

            else:

                conexion.commit()

                messagebox.showinfo("Hospital", "Atención modificada correctamente.")

                self.cargar()
                self.nuevo()

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def eliminar(self):

        if self.id_seleccionado is None:
            messagebox.showwarning("Hospital", "Seleccione una atención.")

            return

        respuesta = messagebox.askyesno("Hospital", "¿Desea eliminar esta atención?")

        if respuesta == False:
            return

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        DELETE FROM atenciones
        WHERE id=%s
        """

        try:

            cursor.execute(sql, (self.id_seleccionado,))

            if cursor.rowcount == 0:

                messagebox.showwarning("Hospital", "No existe la atención.")

            else:
                conexion.commit()
                messagebox.showinfo("Hospital", "Atención eliminada correctamente.")
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

    app = Atenciones(raiz)

    raiz.mainloop()
