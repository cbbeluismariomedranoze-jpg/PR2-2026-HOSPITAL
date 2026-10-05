from tkinter import *
from tkinter import ttk

COLOR_FONDO = "#F4F8FC"
COLOR_AZUL_OSCURO = "#174EA6"
COLOR_AZUL = "#2563EB"
COLOR_AZUL_CLARO = "#EAF3FF"
COLOR_AZUL_HOVER = "#DCEBFF"
COLOR_BLANCO = "#FFFFFF"
COLOR_TEXTO = "#172B4D"
COLOR_SECUNDARIO = "#718096"
COLOR_BORDE = "#DCE6F2"


FUENTE_TITULO = ("Segoe UI", 22, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 10)
FUENTE_LABEL = ("Segoe UI", 10, "bold")
FUENTE_ENTRY = ("Segoe UI", 10)
FUENTE_BOTON = ("Segoe UI", 10, "bold")


class VentanaReservas:

    def __init__(self, ventana, al_cerrar=None):

        self.ventana = ventana
        self.al_cerrar = al_cerrar

        self.ventana.title("Sistema Hospitalario - Reservas")

        self.ventana.resizable(True, True)

        ancho = 1000
        alto = 650

        pantalla_ancho = self.ventana.winfo_screenwidth()
        pantalla_alto = self.ventana.winfo_screenheight()

        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)

        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

        self.ventana.minsize(900, 600)

        self.ventana.configure(bg=COLOR_FONDO)

        self.crear_interfaz()

    def crear_interfaz(self):

        Frame(self.ventana, bg=COLOR_AZUL, height=5).pack(fill=X)

        barra = Frame(self.ventana, bg=COLOR_BLANCO, height=70)

        barra.pack(fill=X)

        barra.pack_propagate(False)

        logo = Frame(barra, bg=COLOR_BLANCO)

        logo.pack(side=LEFT, padx=35)

        Label(logo, text="✚", bg=COLOR_BLANCO, fg=COLOR_AZUL, font=("Segoe UI", 25, "bold")).pack(
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

        Label(
            contenido,
            text="Registro de reservas",
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            font=FUENTE_TITULO,
        ).pack(anchor="w")

        Label(
            contenido,
            text="Administra las reservas y citas médicas del hospital.",
            bg=COLOR_FONDO,
            fg=COLOR_SECUNDARIO,
            font=FUENTE_SUBTITULO,
        ).pack(anchor="w", pady=(5, 20))

        datos = Frame(
            contenido, bg=COLOR_BLANCO, highlightbackground=COLOR_BORDE, highlightthickness=1
        )

        datos.pack(fill=X)

        formulario = Frame(datos, bg=COLOR_BLANCO)

        formulario.pack(padx=25, pady=20)

        Label(formulario, text="Fecha", bg=COLOR_BLANCO, fg=COLOR_TEXTO, font=FUENTE_LABEL).grid(
            row=0, column=2, sticky=W, pady=5
        )

        self.txtFecha = Entry(formulario, width=25, font=FUENTE_ENTRY)

        self.txtFecha.grid(row=0, column=3, pady=5, padx=20)

        Label(
            formulario, text="CI Paciente", bg=COLOR_BLANCO, fg=COLOR_TEXTO, font=FUENTE_LABEL
        ).grid(row=0, column=0, sticky=W, pady=5)

        self.cmbPaciente = ttk.Combobox(formulario, width=29, state="FUENTE_ENTRY")

        self.cmbPaciente.grid(row=0, column=1, pady=5, padx=(20, 40))

        Label(formulario, text="Hora", bg=COLOR_BLANCO, fg=COLOR_TEXTO, font=FUENTE_LABEL).grid(
            row=1, column=2, sticky=W, pady=5
        )

        self.txtHora = Entry(formulario, width=25, font=FUENTE_ENTRY)

        self.txtHora.grid(row=1, column=3, pady=5, padx=20)

        Label(
            formulario, text="CI Doctor", bg=COLOR_BLANCO, fg=COLOR_TEXTO, font=FUENTE_LABEL
        ).grid(row=1, column=0, sticky=W, pady=5)

        self.cmbDoctor = ttk.Combobox(formulario, width=25, font=FUENTE_ENTRY)

        self.cmbDoctor.grid(row=1, column=1, pady=5, padx=(20, 40))

        Label(formulario, text="Estado", bg=COLOR_BLANCO, fg=COLOR_TEXTO, font=FUENTE_LABEL).grid(
            row=2, column=2, sticky=W, pady=5
        )

        self.cmbEstado = ttk.Combobox(
            formulario, width=22, state="readonly", values=["Pendiente", "Atendido", "Cancelado"]
        )

        self.cmbEstado.grid(row=2, column=3, pady=5, padx=20)

        Label(
            formulario, text="N° Consultorio", bg=COLOR_BLANCO, fg=COLOR_TEXTO, font=FUENTE_LABEL
        ).grid(row=2, column=0, sticky=W, pady=5)

        self.cmbConsultorio = ttk.Combobox(formulario, width=25, font=FUENTE_ENTRY)

        self.cmbConsultorio.grid(row=2, column=1, pady=5, padx=(20, 40))

        botones = Frame(contenido, bg=COLOR_FONDO)

        botones.pack(pady=15)

        botones_datos = [
            ("btnNuevo", "Nuevo", COLOR_AZUL_CLARO, COLOR_AZUL_OSCURO),
            ("btnGuardar", "Guardar", COLOR_AZUL, COLOR_BLANCO),
            ("btnModificar", "Modificar", COLOR_AZUL_CLARO, COLOR_AZUL_OSCURO),
            ("btnEliminar", "Eliminar", COLOR_AZUL_CLARO, COLOR_AZUL_OSCURO),
            ("btnSalir", "Salir", COLOR_BLANCO, COLOR_AZUL_OSCURO),
        ]

        for columna, (nombre, texto, fondo, fg) in enumerate(botones_datos):

            boton = Button(
                botones,
                text=texto,
                width=12,
                bg=fondo,
                fg=fg,
                activebackground=COLOR_AZUL_HOVER,
                relief=FLAT if fondo != COLOR_BLANCO else "solid",
                bd=1,
                cursor="hand2",
                font=FUENTE_BOTON,
            )

            boton.grid(row=0, column=columna, padx=5)

            setattr(self, nombre, boton)

        tabla_frame = Frame(
            contenido, bg=COLOR_BLANCO, highlightbackground=COLOR_BORDE, highlightthickness=1
        )

        tabla_frame.pack(fill=BOTH, expand=True)

        contenedor_tabla = Frame(tabla_frame, bg=COLOR_BLANCO)

        contenedor_tabla.pack(fill=BOTH, expand=True, padx=10, pady=10)

        estilo = ttk.Style()

        estilo.configure("Treeview", font=("Segoe UI", 9), rowheight=28)

        estilo.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

        self.tabla = ttk.Treeview(
            contenedor_tabla,
            columns=("id", "paciente", "doctor", "consultorio", "fecha", "hora", "estado"),
            show="headings",
        )

        columnas = [
            ("id", "ID", 70),
            ("paciente", "CI Paciente", 120),
            ("doctor", "CI Doctor", 120),
            ("consultorio", "Consultorio", 120),
            ("fecha", "Fecha", 120),
            ("hora", "Hora", 100),
            ("estado", "Estado", 130),
        ]

        for col, texto, ancho in columnas:

            self.tabla.heading(col, text=texto)

            self.tabla.column(col, width=ancho)

        scroll_y = ttk.Scrollbar(contenedor_tabla, orient=VERTICAL, command=self.tabla.yview)

        scroll_x = ttk.Scrollbar(contenedor_tabla, orient=HORIZONTAL, command=self.tabla.xview)

        self.tabla.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        self.tabla.grid(row=0, column=0, sticky="nsew")

        scroll_y.grid(row=0, column=1, sticky="ns")

        scroll_x.grid(row=1, column=0, sticky="ew")

        contenedor_tabla.grid_rowconfigure(0, weight=1)

        contenedor_tabla.grid_columnconfigure(0, weight=1)

    def nuevo(self):

        self.cmbPaciente.set("")
        self.cmbDoctor.set("")
        self.cmbConsultorio.set("")
        self.txtFecha.delete(0, "end")
        self.txtHora.delete(0, "end")
        self.cmbEstado.set("")

        self.cmbPaciente.focus()

    def salir(self):
        if self.al_cerrar:
            self.al_cerrar()
        else:
            self.ventana.destroy()


if __name__ == "__main__":

    raiz = Tk()

    VentanaReservas(raiz)

    raiz.mainloop()
