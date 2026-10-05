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


class VentanaCirugias:

    def __init__(self, ventana, al_cerrar=None):

        self.ventana = ventana
        self.al_cerrar = al_cerrar
        self.ventana.title("Sistema Hospitalario - Cirugías")

        self.ventana.resizable(True, True)

        ancho = 1100
        alto = 700

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
            text="Registro de cirugías",
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            font=("Segoe UI", 22, "bold"),
        ).pack(anchor="w")

        Label(
            contenido,
            text="Administra información de cirugías, pacientes y personal médico.",
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

        campos = [
            ("ID", 0),
            ("CI Paciente", 1),
            ("CI Doctor", 2),
            ("N° Quirófano", 3),
            ("CI Enfermera", 4),
        ]

        self.txtId = Entry(formulario, width=25)

        self.txtPaciente = Entry(formulario, width=25)

        self.txtDoctor = Entry(formulario, width=25)

        self.txtQuirofano = Entry(formulario, width=25)

        self.txtEnfermera = Entry(formulario, width=25)

        entradas = [
            self.txtId,
            self.txtPaciente,
            self.txtDoctor,
            self.txtQuirofano,
            self.txtEnfermera,
        ]

        for (texto, fila), entrada in zip(campos, entradas):

            Label(
                formulario,
                text=texto,
                bg=COLOR_BLANCO,
                fg=COLOR_TEXTO,
                font=("Segoe UI", 10, "bold"),
            ).grid(row=fila, column=0, sticky=W, pady=5)

            entrada.grid(row=fila, column=1, padx=20, pady=5)

        Label(
            formulario, text="Fecha", bg=COLOR_BLANCO, fg=COLOR_TEXTO, font=("Segoe UI", 10, "bold")
        ).grid(row=0, column=2, padx=30, sticky=W)

        self.txtFecha = Entry(formulario, width=25)

        self.txtFecha.grid(row=0, column=3, pady=5)

        Label(
            formulario, text="Tipo", bg=COLOR_BLANCO, fg=COLOR_TEXTO, font=("Segoe UI", 10, "bold")
        ).grid(row=1, column=2, padx=30, sticky=W)

        self.txtTipo = Entry(formulario, width=25)

        self.txtTipo.grid(row=1, column=3, pady=5)

        Label(
            formulario,
            text="Descripción",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=("Segoe UI", 10, "bold"),
        ).grid(row=2, column=2, padx=30, sticky=W)

        self.txtDescripcion = Entry(formulario, width=25)

        self.txtDescripcion.grid(row=2, column=3, pady=5)

        Label(
            formulario,
            text="Estado",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=("Segoe UI", 10, "bold"),
        ).grid(row=3, column=2, padx=30, sticky=W)

        self.cmbEstado = ttk.Combobox(
            formulario, width=22, state="readonly", values=["Programada", "Realizada", "Cancelada"]
        )

        self.cmbEstado.grid(row=3, column=3, pady=5)

        botones = Frame(contenido, bg=COLOR_FONDO)

        botones.pack(pady=15)

        self.btnNuevo = Button(
            botones,
            text="Nuevo",
            width=12,
            bg=COLOR_AZUL_CLARO,
            fg=COLOR_AZUL_OSCURO,
            activebackground=COLOR_AZUL_HOVER,
            relief=FLAT,
            bd=0,
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
        )

        self.btnNuevo.grid(row=0, column=0, padx=5)

        self.btnGuardar = Button(
            botones,
            text="Guardar",
            width=12,
            bg=COLOR_AZUL,
            fg=COLOR_BLANCO,
            activebackground=COLOR_AZUL_OSCURO,
            relief=FLAT,
            bd=0,
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
        )

        self.btnGuardar.grid(row=0, column=1, padx=5)

        self.btnModificar = Button(
            botones,
            text="Modificar",
            width=12,
            bg=COLOR_AZUL_CLARO,
            fg=COLOR_AZUL_OSCURO,
            activebackground=COLOR_AZUL_HOVER,
            relief=FLAT,
            bd=0,
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
        )

        self.btnModificar.grid(row=0, column=2, padx=5)

        self.btnEliminar = Button(
            botones,
            text="Eliminar",
            width=12,
            bg=COLOR_AZUL_CLARO,
            fg=COLOR_AZUL_OSCURO,
            activebackground=COLOR_AZUL_HOVER,
            relief=FLAT,
            bd=0,
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
        )

        self.btnEliminar.grid(row=0, column=3, padx=5)

        self.btnSalir = Button(
            botones,
            text="Salir",
            width=12,
            bg=COLOR_BLANCO,
            fg=COLOR_AZUL_OSCURO,
            activebackground=COLOR_AZUL_HOVER,
            relief="solid",
            bd=1,
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
        )

        self.btnSalir.grid(row=0, column=4, padx=5)

        # TABLA

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
            columns=(
                "id",
                "paciente",
                "doctor",
                "quirofano",
                "enfermera",
                "fecha",
                "tipo",
                "descripcion",
                "estado",
            ),
            show="headings",
        )

        columnas = [
            ("id", "ID"),
            ("paciente", "Paciente"),
            ("doctor", "Doctor"),
            ("quirofano", "Quirófano"),
            ("enfermera", "Enfermera"),
            ("fecha", "Fecha"),
            ("tipo", "Tipo"),
            ("descripcion", "Descripción"),
            ("estado", "Estado"),
        ]

        for col, texto in columnas:

            self.tabla.heading(col, text=texto)

        scroll_y = ttk.Scrollbar(contenedor_tabla, orient=VERTICAL, command=self.tabla.yview)

        scroll_x = ttk.Scrollbar(contenedor_tabla, orient=HORIZONTAL, command=self.tabla.xview)

        self.tabla.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        self.tabla.grid(row=0, column=0, sticky="nsew")

        scroll_y.grid(row=0, column=1, sticky="ns")

        scroll_x.grid(row=1, column=0, sticky="ew")

        contenedor_tabla.grid_rowconfigure(0, weight=1)

        contenedor_tabla.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":

    raiz = Tk()

    VentanaCirugias(raiz)

    raiz.mainloop()
