from tkinter import *
from tkinter import ttk, messagebox
from Conexion import conectar

COLOR_FONDO = "#F4F8FC"
COLOR_AZUL_OSCURO = "#174EA6"
COLOR_AZUL = "#2563EB"
COLOR_AZUL_CLARO = "#EAF3FF"
COLOR_AZUL_HOVER = "#DCEBFF"
COLOR_BLANCO = "#FFFFFF"
COLOR_TEXTO = "#172B4D"
COLOR_SECUNDARIO = "#718096"
COLOR_BORDE = "#DCE6F2"
COLOR_ROJO = "#DC2626"


FUENTE_TITULO = ("Segoe UI", 22, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 10)
FUENTE_LABEL = ("Segoe UI", 10, "bold")
FUENTE_BOTON = ("Segoe UI", 10, "bold")


class Busquedas:

    def __init__(self, ventana, al_cerrar=None):

        self.ventana = ventana
        self.al_cerrar = al_cerrar
        self.ventana.title("Sistema Hospitalario - Búsquedas")

        self.ventana.resizable(False, False)

        ancho = 1150
        alto = 680

        pantalla_ancho = self.ventana.winfo_screenwidth()
        pantalla_alto = self.ventana.winfo_screenheight()

        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)

        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

        self.ventana.configure(bg=COLOR_FONDO)

        self.crear_interfaz()

    def crear_interfaz(self):

        franja = Frame(self.ventana, bg=COLOR_AZUL, height=5)

        franja.pack(fill="x")

        barra = Frame(self.ventana, bg=COLOR_BLANCO, height=70)

        barra.pack(fill="x")

        barra.pack_propagate(False)

        logo = Frame(barra, bg=COLOR_BLANCO)

        logo.pack(side=LEFT, padx=35)

        Label(logo, text="⌕", bg=COLOR_BLANCO, fg=COLOR_AZUL, font=("Segoe UI", 27, "bold")).pack(
            side=LEFT, padx=(0, 10)
        )

        texto_logo = Frame(logo, bg=COLOR_BLANCO)

        texto_logo.pack(side=LEFT)

        Label(
            texto_logo,
            text="Hospital Privado",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=("Segoe UI", 17, "bold"),
        ).pack(anchor="w")

        Label(
            texto_logo,
            text="Sistema de gestión hospitalaria",
            bg=COLOR_BLANCO,
            fg=COLOR_SECUNDARIO,
            font=("Segoe UI", 8),
        ).pack(anchor="w")

        contenido = Frame(self.ventana, bg=COLOR_FONDO)

        contenido.pack(fill=BOTH, expand=True, padx=40, pady=25)

        Label(contenido, text="Búsquedas", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TITULO).pack(
            anchor="w"
        )

        Label(
            contenido,
            text="Consulta rápidamente la información registrada en el sistema.",
            bg=COLOR_FONDO,
            fg=COLOR_SECUNDARIO,
            font=FUENTE_SUBTITULO,
        ).pack(anchor="w", pady=(3, 18))

        panel_busqueda = Frame(
            contenido, bg=COLOR_BLANCO, highlightbackground=COLOR_BORDE, highlightthickness=1
        )

        panel_busqueda.pack(fill="x")

        panel_busqueda.columnconfigure(1, weight=1)

        Label(
            panel_busqueda, text="Buscar en", bg=COLOR_BLANCO, fg=COLOR_TEXTO, font=FUENTE_LABEL
        ).grid(row=0, column=0, padx=(22, 10), pady=20)

        estilo = ttk.Style()

        estilo.theme_use("clam")

        estilo.configure(
            "Busqueda.TCombobox",
            fieldbackground=COLOR_BLANCO,
            background=COLOR_BLANCO,
            foreground=COLOR_TEXTO,
            bordercolor=COLOR_BORDE,
            arrowcolor=COLOR_AZUL,
            padding=7,
        )

        self.cmbTabla = ttk.Combobox(
            panel_busqueda,
            state="readonly",
            width=20,
            style="Busqueda.TCombobox",
            values=["Pacientes", "Doctores", "Reservas", "Atenciones", "Cirugias", "Kardex"],
        )

        self.cmbTabla.grid(row=0, column=1, padx=5, pady=20, sticky="ew")

        Label(panel_busqueda, text="Dato", bg=COLOR_BLANCO, fg=COLOR_TEXTO, font=FUENTE_LABEL).grid(
            row=0, column=2, padx=(20, 10), pady=20
        )

        self.txtBuscar = Entry(
            panel_busqueda,
            width=30,
            bg="#F8FAFC",
            fg=COLOR_TEXTO,
            insertbackground=COLOR_AZUL,
            relief="solid",
            bd=1,
            font=("Segoe UI", 10),
        )

        self.txtBuscar.grid(row=0, column=3, padx=5, pady=20)

        self.btnBuscar = Button(
            panel_busqueda,
            text="🔎  Buscar",
            width=14,
            bg=COLOR_AZUL,
            fg=COLOR_BLANCO,
            activebackground=COLOR_AZUL_OSCURO,
            activeforeground=COLOR_BLANCO,
            relief="flat",
            bd=0,
            cursor="hand2",
            font=FUENTE_BOTON,
            command=self.buscar,
        )

        self.btnBuscar.grid(row=0, column=4, padx=(15, 22), pady=20)

        resultado = Frame(
            contenido, bg=COLOR_BLANCO, highlightbackground=COLOR_BORDE, highlightthickness=1
        )

        resultado.pack(fill=BOTH, expand=True, pady=(20, 0))

        encabezado = Frame(resultado, bg=COLOR_BLANCO, height=48)

        encabezado.pack(fill="x")

        encabezado.pack_propagate(False)

        Label(
            encabezado,
            text="Resultados de búsqueda",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=("Segoe UI", 11, "bold"),
        ).pack(side=LEFT, padx=20)

        estilo.configure(
            "Busqueda.Treeview",
            background=COLOR_BLANCO,
            foreground=COLOR_TEXTO,
            fieldbackground=COLOR_BLANCO,
            rowheight=34,
            borderwidth=0,
            font=("Segoe UI", 9),
        )

        estilo.configure(
            "Busqueda.Treeview.Heading",
            background=COLOR_AZUL_OSCURO,
            foreground=COLOR_BLANCO,
            relief="flat",
            font=("Segoe UI", 9, "bold"),
        )

        estilo.map(
            "Busqueda.Treeview",
            background=[("selected", COLOR_AZUL_CLARO)],
            foreground=[("selected", COLOR_AZUL_OSCURO)],
        )

        tabla_contenedor = Frame(resultado, bg=COLOR_BLANCO)

        tabla_contenedor.pack(fill=BOTH, expand=True, padx=15, pady=(0, 15))

        self.tabla = ttk.Treeview(tabla_contenedor, show="headings", style="Busqueda.Treeview")

        scrollbar_vertical = ttk.Scrollbar(
            tabla_contenedor, orient="vertical", command=self.tabla.yview
        )

        scrollbar_horizontal = ttk.Scrollbar(
            tabla_contenedor, orient="horizontal", command=self.tabla.xview
        )

        self.tabla.configure(
            yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set
        )

        self.tabla.grid(row=0, column=0, sticky="nsew")

        scrollbar_vertical.grid(row=0, column=1, sticky="ns")

        scrollbar_horizontal.grid(row=1, column=0, sticky="ew")

        tabla_contenedor.rowconfigure(0, weight=1)

        tabla_contenedor.columnconfigure(0, weight=1)

        Button(
            contenido,
            text="←  Salir",
            width=12,
            bg=COLOR_BLANCO,
            fg=COLOR_SECUNDARIO,
            activebackground="#E2E8F0",
            activeforeground=COLOR_TEXTO,
            relief="solid",
            bd=1,
            cursor="hand2",
            font=FUENTE_BOTON,
            command=self.cerrar,
        ).pack(anchor="e", pady=(15, 0))

    def limpiar_tabla(self):

        self.tabla.delete(*self.tabla.get_children())

        self.tabla["columns"] = ()

    def mostrar_columnas(self, columnas):

        self.tabla["columns"] = columnas

        for col in columnas:

            self.tabla.heading(col, text=col.upper())

            self.tabla.column(col, width=140, anchor="center")

    def buscar(self):

        opcion = self.cmbTabla.get()

        dato = self.txtBuscar.get()

        if opcion == "":

            messagebox.showwarning("Aviso", "Seleccione una búsqueda.")

            return

        if dato == "":

            messagebox.showwarning("Aviso", "Ingrese un dato para buscar.")

            return

        conexion = conectar()

        cursor = conexion.cursor()

        try:

            self.limpiar_tabla()

            if opcion == "Pacientes":

                columnas = ("ci", "nombres", "apellidos", "telefono", "genero", "sangre")

                sql = """
                SELECT
                ci,
                nombres,
                apellidos,
                telefono,
                genero,
                sangre
                FROM pacientes
                WHERE ci LIKE %s
                OR nombres LIKE %s
                OR apellidos LIKE %s
                """

                valores = ("%" + dato + "%", "%" + dato + "%", "%" + dato + "%")

            elif opcion == "Doctores":

                columnas = ("ci", "nombres", "telefono", "especialidad")

                sql = """
                SELECT *
                FROM doctores
                WHERE ci LIKE %s
                OR nombres LIKE %s
                """

                valores = ("%" + dato + "%", "%" + dato + "%")

            elif opcion == "Reservas":

                columnas = ("id", "paciente", "doctor", "consultorio", "fecha", "estado")

                sql = """
                SELECT
                id,
                ci_paciente,
                ci_doctor,
                nro_consultorio,
                fecha,
                estado
                FROM reservas
                WHERE id LIKE %s
                OR ci_paciente LIKE %s
                """

                valores = ("%" + dato + "%", "%" + dato + "%")

            elif opcion == "Atenciones":

                columnas = ("id", "reserva", "fecha", "motivo")

                sql = """
                SELECT
                id,
                id_reserva,
                fecha,
                motivo
                FROM atenciones
                WHERE id LIKE %s
                OR id_reserva LIKE %s
                """

                valores = ("%" + dato + "%", "%" + dato + "%")

            elif opcion == "Cirugias":

                columnas = ("id", "paciente", "doctor", "fecha", "tipo", "estado")

                sql = """
                SELECT
                id,
                ci_paciente,
                ci_doctor,
                fecha,
                tipo,
                estado
                FROM cirugias
                WHERE id LIKE %s
                OR ci_paciente LIKE %s
                """

                valores = ("%" + dato + "%", "%" + dato + "%")

            elif opcion == "Kardex":

                columnas = ("nro", "paciente", "fecha", "descripcion")

                sql = """
                SELECT *
                FROM kardex
                WHERE nro LIKE %s
                OR ci_paciente LIKE %s
                """

                valores = ("%" + dato + "%", "%" + dato + "%")

            else:

                return

            self.mostrar_columnas(columnas)

            cursor.execute(sql, valores)

            registros = cursor.fetchall()

            for fila in registros:

                self.tabla.insert("", END, values=fila)

            if len(registros) == 0:

                messagebox.showinfo("Resultado", "No se encontraron registros.")

        except Exception as e:

            messagebox.showerror("Error", str(e))

        finally:

            cursor.close()
            conexion.close()

    def cerrar(self):
        if self.al_cerrar:
            self.al_cerrar()
        else:
            self.ventana.destroy()


def menu_busquedas(ventana, al_cerrar=None):
    return Busquedas(ventana, al_cerrar)


if __name__ == "__main__":

    raiz = Tk()
    app = Busquedas(raiz)
    raiz.mainloop()
