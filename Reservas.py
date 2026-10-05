from tkinter import BOTH, END, Tk
from tkinter import messagebox
from Conexion import conectar
from ReservasV import VentanaReservas
from datetime import datetime


class Reservas(VentanaReservas):

    def __init__(self, ventana, al_cerrar=None):

        super().__init__(ventana, al_cerrar)

        # Eventos de los botones
        self.btnNuevo.config(command=self.nuevo)
        self.btnGuardar.config(command=self.guardar)
        self.btnModificar.config(command=self.modificar)
        self.btnEliminar.config(command=self.eliminar)
        self.btnSalir.config(command=self.salir)

        self.tabla.bind("<ButtonRelease-1>", self.seleccionar)

        self.cargar_comboboxes()
        self.mostrar()
        self.colocar_fecha_hora()

    def _existe_registro(self, tabla, campo, valor):

        conexion = conectar()

        if conexion is None:
            return False

        cursor = conexion.cursor()

        try:
            cursor.execute(f"SELECT 1 FROM {tabla} WHERE {campo} = %s", (valor,))
            return cursor.fetchone() is not None
        finally:
            cursor.close()
            conexion.close()

    def cargar_comboboxes(self):

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        try:
            cursor.execute("SELECT ci FROM pacientes ORDER BY ci")
            pacientes = [str(fila[0]) for fila in cursor.fetchall()]
            self.cmbPaciente["values"] = pacientes

            cursor.execute("SELECT ci FROM doctores ORDER BY ci")
            doctores = [str(fila[0]) for fila in cursor.fetchall()]
            self.cmbDoctor["values"] = doctores

            cursor.execute("SELECT nro FROM consultorios ORDER BY nro")
            consultorios = [str(fila[0]) for fila in cursor.fetchall()]
            self.cmbConsultorio["values"] = consultorios
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conexion.close()

    def validar(self):

        ci_paciente = self.cmbPaciente.get().strip()
        ci_doctor = self.cmbDoctor.get().strip()
        nro_consultorio = self.cmbConsultorio.get().strip()
        estado = self.cmbEstado.get().strip()

        if not ci_paciente:
            messagebox.showwarning("Validación", "Ingrese el CI del paciente.")
            return False

        if not ci_doctor:
            messagebox.showwarning("Validación", "Ingrese el CI del doctor.")
            return False

        if not nro_consultorio:
            messagebox.showwarning("Validación", "Ingrese el número del consultorio.")
            return False

        if not estado:
            messagebox.showwarning("Validación", "Seleccione un estado para la reserva.")
            return False

        if not self._existe_registro("pacientes", "ci", ci_paciente):
            messagebox.showerror("Error", "El CI del paciente no está registrado.")
            return False

        if not self._existe_registro("doctores", "ci", ci_doctor):
            messagebox.showerror("Error", "El CI del doctor no está registrado.")
            return False

        if not self._existe_registro("consultorios", "nro", nro_consultorio):
            messagebox.showerror("Error", "El número de consultorio no está registrado.")
            return False

        return True

    def guardar(self):

        if not self.validar():
            return

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        INSERT INTO reservas
        (ci_paciente, ci_doctor, nro_consultorio,
        fecha, hora, estado)
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        datos = (
            self.cmbPaciente.get(),
            self.cmbDoctor.get(),
            self.cmbConsultorio.get(),
            self.txtFecha.get(),
            self.txtHora.get(),
            self.cmbEstado.get(),
        )

        try:

            cursor.execute(sql, datos)
            conexion.commit()

            messagebox.showinfo("Sistema", "Reserva registrada correctamente.")

            self.mostrar()
            self.nuevo()

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def mostrar(self):

        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        self.tabla.delete(*self.tabla.get_children())

        sql = "SELECT * FROM reservas"

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

    def modificar(self):
        if not self.validar():
            return
        conexion = conectar()

        if conexion is None:
            return

        cursor = conexion.cursor()

        sql = """
        UPDATE reservas
        SET ci_paciente=%s,
            ci_doctor=%s,
            nro_consultorio=%s,
            fecha=%s,
            hora=%s,
            estado=%s
        WHERE id=%s
        """

        datos = (
            self.cmbPaciente.get(),
            self.cmbDoctor.get(),
            self.cmbConsultorio.get(),
            self.txtFecha.get(),
            self.txtHora.get(),
            self.cmbEstado.get(),
            self.id_seleccionado,
        )

        try:
            cursor.execute(sql, datos)

            if cursor.rowcount == 0:
                messagebox.showwarning("Sistema", "No existe la reserva.")

            else:

                conexion.commit()
                messagebox.showinfo("Sistema", "Reserva modificada correctamente.")

            self.mostrar()
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

        cursor = conexion.cursor()

        sql = "DELETE FROM reservas WHERE id=%s"

        try:

            cursor.execute(sql, (self.id_seleccionado,))

            if cursor.rowcount == 0:
                messagebox.showwarning("Sistema", "No existe la reserva.")
            else:
                conexion.commit()
                messagebox.showinfo("Sistema", "Reserva eliminada correctamente.")

            self.mostrar()
            self.nuevo()

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def seleccionar(self, event):

        fila = self.tabla.focus()

        if fila:

            datos = self.tabla.item(fila)["values"]

            self.id_seleccionado = datos[0]

            self.txtFecha.delete(0, END)
            self.txtHora.delete(0, END)
            self.cmbEstado.set("")

            self.cmbPaciente.set(datos[1])
            self.cmbDoctor.set(datos[2])
            self.cmbConsultorio.set(datos[3])
            self.txtFecha.insert(0, datos[4])
            self.txtHora.insert(0, datos[5])
            self.cmbEstado.set(datos[6])

    def colocar_fecha_hora(self):

        self.txtFecha.delete(0, END)
        self.txtHora.delete(0, END)

        ahora = datetime.now()

        self.txtFecha.insert(0, ahora.strftime("%Y-%m-%d"))

        self.txtHora.insert(0, ahora.strftime("%H:%M:%S"))

    def nuevo(self):

        self.cmbPaciente.set("")
        self.cmbDoctor.set("")
        self.cmbConsultorio.set("")
        self.txtFecha.delete(0, END)
        self.txtHora.delete(0, END)

        self.cmbEstado.set("")
        self.id_seleccionado = None

        self.colocar_fecha_hora()

        self.cmbPaciente.focus()


if __name__ == "__main__":

    raiz = Tk()

    app = Reservas(raiz)

    raiz.mainloop()
