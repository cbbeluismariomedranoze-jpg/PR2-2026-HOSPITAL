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


class VentanaKardex:

    def __init__(self, ventana, al_cerrar=None):

        self.ventana = ventana
        self.al_cerrar = al_cerrar
        self.ventana.title("Sistema Hospitalario - Kardex")

        self.ventana.resizable(True, True)

        ancho = 950
        alto = 600

        pantalla_ancho = self.ventana.winfo_screenwidth()
        pantalla_alto = self.ventana.winfo_screenheight()

        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)

        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

        self.ventana.minsize(950, 600)

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
            text="Historial Kardex del paciente",
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            font=("Segoe UI", 22, "bold"),
        ).pack(anchor="w")

        Label(
            contenido,
            text="Registro de evolución y seguimiento médico.",
            bg=COLOR_FONDO,
            fg=COLOR_SECUNDARIO,
            font=("Segoe UI", 10),
        ).pack(anchor="w", pady=(5, 20))

        formulario_frame = Frame(
            contenido, bg=COLOR_BLANCO, highlightbackground=COLOR_BORDE, highlightthickness=1
        )

        formulario_frame.pack(fill=X)

        formulario = Frame(formulario_frame, bg=COLOR_BLANCO)

        formulario.pack(padx=25, pady=15)

        campos = [
            ("N° Kardex", "txtNro"),
            ("CI Paciente", "txtPaciente"),
            ("Fecha", "txtFecha"),
            ("Descripción médica", "txtDescripcion"),
        ]

        for fila, (texto, nombre) in enumerate(campos):

            Label(
                formulario,
                text=texto,
                bg=COLOR_BLANCO,
                fg=COLOR_TEXTO,
                font=("Segoe UI", 10, "bold"),
            ).grid(row=fila, column=0, sticky="w", pady=6)

            entrada = Entry(formulario, width=65, font=("Segoe UI", 10), relief="solid", bd=1)

            entrada.grid(row=fila, column=1, padx=30, pady=6)

            setattr(self, nombre, entrada)

        botones = Frame(contenido, bg=COLOR_FONDO)

        botones.pack(pady=15)

        self.btnNuevo = Button(
            botones,
            text="Nuevo",
            bg=COLOR_AZUL_CLARO,
            fg=COLOR_AZUL_OSCURO,
            activebackground=COLOR_AZUL_HOVER,
            relief=FLAT,
            bd=0,
            width=12,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
        )

        self.btnNuevo.grid(row=0, column=0, padx=8)

        self.btnGuardar = Button(
            botones,
            text="Guardar",
            bg=COLOR_AZUL,
            fg=COLOR_BLANCO,
            activebackground=COLOR_AZUL_OSCURO,
            relief=FLAT,
            bd=0,
            width=12,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
        )

        self.btnGuardar.grid(row=0, column=1, padx=8)

        self.btnSalir = Button(
            botones,
            text="Salir",
            bg=COLOR_BLANCO,
            fg=COLOR_AZUL_OSCURO,
            activebackground=COLOR_AZUL_HOVER,
            relief="solid",
            bd=1,
            width=12,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
        )

        self.btnSalir.grid(row=0, column=2, padx=8)

        # TABLA CON SCROLL

        tabla_frame = Frame(
            contenido, bg=COLOR_BLANCO, highlightbackground=COLOR_BORDE, highlightthickness=1
        )

        tabla_frame.pack(fill=BOTH, expand=True)

        tabla_contenedor = Frame(tabla_frame, bg=COLOR_BLANCO)

        tabla_contenedor.pack(fill=BOTH, expand=True, padx=10, pady=10)

        estilo = ttk.Style()

        estilo.configure("Treeview", font=("Segoe UI", 9), rowheight=28)

        estilo.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

        self.tabla = ttk.Treeview(
            tabla_contenedor, columns=("nro", "paciente", "fecha", "descripcion"), show="headings"
        )

        columnas = [
            ("nro", "N°", 80),
            ("paciente", "CI Paciente", 150),
            ("fecha", "Fecha", 120),
            ("descripcion", "Descripción", 450),
        ]

        for clave, texto, ancho in columnas:

            self.tabla.heading(clave, text=texto)

            self.tabla.column(clave, width=ancho)

        scroll_y = ttk.Scrollbar(tabla_contenedor, orient=VERTICAL, command=self.tabla.yview)

        scroll_x = ttk.Scrollbar(tabla_contenedor, orient=HORIZONTAL, command=self.tabla.xview)

        self.tabla.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        self.tabla.grid(row=0, column=0, sticky="nsew")

        scroll_y.grid(row=0, column=1, sticky="ns")

        scroll_x.grid(row=1, column=0, sticky="ew")

        tabla_contenedor.grid_rowconfigure(0, weight=1)

        tabla_contenedor.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":

    raiz = Tk()

    VentanaKardex(raiz)

    raiz.mainloop()
