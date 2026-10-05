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
COLOR_ROJO = "#DC2626"


class VentanaEspecialidades:

    def __init__(self, ventana, al_cerrar=None):

        self.ventana = ventana
        self.al_cerrar = al_cerrar
        self.ventana.title("Sistema Hospitalario - Especialidades")

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
            text="Registro de especialidades",
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            font=("Segoe UI", 22, "bold"),
        ).pack(anchor="w")

        Label(
            contenido,
            text="Administra las especialidades médicas disponibles.",
            bg=COLOR_FONDO,
            fg=COLOR_SECUNDARIO,
            font=("Segoe UI", 10),
        ).pack(anchor="w", pady=(5, 20))

        datos = Frame(
            contenido, bg=COLOR_BLANCO, highlightbackground=COLOR_BORDE, highlightthickness=1
        )

        datos.pack(fill=X)

        formulario = Frame(datos, bg=COLOR_BLANCO)

        formulario.pack(padx=25, pady=20)

        Label(
            formulario,
            text="Especialidad",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=("Segoe UI", 10, "bold"),
        ).grid(row=0, column=0, sticky=W, pady=5)

        self.txtEspecialidad = Entry(formulario, width=55)

        self.txtEspecialidad.grid(row=0, column=1, pady=5, padx=20)

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
                font=("Segoe UI", 10, "bold"),
            )

            boton.grid(row=0, column=columna, padx=5)

            setattr(self, nombre, boton)

        tabla_frame = Frame(
            contenido, bg=COLOR_BLANCO, highlightbackground=COLOR_BORDE, highlightthickness=1
        )

        tabla_frame.pack(fill=BOTH, expand=True)

        estilo = ttk.Style()

        estilo.configure("Treeview", font=("Segoe UI", 9), rowheight=30)

        estilo.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

        self.tabla = ttk.Treeview(tabla_frame, columns=("especialidad",), show="headings")

        self.tabla.heading("especialidad", text="Especialidad")

        self.tabla.column("especialidad", width=700, anchor="center")

        scrollbar = ttk.Scrollbar(tabla_frame, orient=VERTICAL, command=self.tabla.yview)

        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side="left", fill=BOTH, expand=True)

        scrollbar.pack(side="right", fill="y")


if __name__ == "__main__":

    raiz = Tk()

    VentanaEspecialidades(raiz)

    raiz.mainloop()
