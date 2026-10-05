from tkinter import *
from tkinter import ttk
from Inicio import Inicio

COLOR_FONDO = "#EEF4FB"
COLOR_PANEL_IZQ = "#3B82F6"
COLOR_PANEL_DER = "#FFFFFF"

COLOR_TEXTO = "#1F2937"
COLOR_SECUNDARIO = "#6B7280"

COLOR_BOTON = "#2563EB"
COLOR_BOTON_HOVER = "#1D4ED8"

FUENTE_TITULO = ("Segoe UI", 24, "bold")
FUENTE_SUB = ("Segoe UI", 11)
FUENTE_LABEL = ("Segoe UI", 10)
FUENTE_ENTRY = ("Segoe UI", 11)
FUENTE_BOTON = ("Segoe UI", 11, "bold")


class InicioV:

    def __init__(self, ventana):

        self.ventana = ventana

        self.logica = Inicio(self)

        self.configurar_ventana()

        self.crear_estilos()

        self.crear_interfaz()

    def configurar_ventana(self):

        self.ventana.title("Hospital Privado")

        self.ventana.geometry("1200x700")

        self.ventana.minsize(950, 600)

        self.ventana.configure(bg=COLOR_FONDO)

    def crear_estilos(self):

        self.estilo = ttk.Style()

        self.estilo.theme_use("clam")

        self.estilo.configure("Modern.TEntry", padding=8, font=FUENTE_ENTRY)

    def crear_interfaz(self):

        self.panel_izquierdo = Frame(self.ventana, bg=COLOR_PANEL_IZQ)

        self.panel_izquierdo.pack(side=LEFT, fill=BOTH, expand=True)

        self.panel_derecho = Frame(self.ventana, bg=COLOR_PANEL_DER, width=450)

        self.panel_derecho.pack(side=RIGHT, fill=Y)

        self.panel_derecho.pack_propagate(False)

        self.crear_panel_izquierdo()

        self.contenedor = Frame(self.panel_derecho, bg=COLOR_PANEL_DER)

        self.contenedor.place(relx=0.5, rely=0.5, anchor="center")

        self.crear_login()

    def crear_panel_izquierdo(self):

        contenedor = Frame(self.panel_izquierdo, bg=COLOR_PANEL_IZQ)

        contenedor.place(relx=0.5, rely=0.5, anchor="center")

        Label(
            contenedor, text="🏥", bg=COLOR_PANEL_IZQ, fg="white", font=("Segoe UI Emoji", 72)
        ).pack(pady=(0, 20))

        Label(
            contenedor,
            text="Hospital Privado",
            bg=COLOR_PANEL_IZQ,
            fg="white",
            font=("Segoe UI", 30, "bold"),
        ).pack()

        Label(
            contenedor,
            text="Sistema de Gestión Hospitalaria",
            bg=COLOR_PANEL_IZQ,
            fg="#D6E4FF",
            font=("Segoe UI", 14),
        ).pack(pady=(8, 35))

        Label(
            contenedor,
            text="Administra pacientes, doctores,\n"
            "consultas, laboratorios,\n"
            "cirugías y reportes desde\n"
            "una sola plataforma.",
            justify="center",
            bg=COLOR_PANEL_IZQ,
            fg="white",
            font=("Segoe UI", 12),
        ).pack()

        Frame(contenedor, bg="#8CB8FF", height=2, width=250).pack(pady=35)

        Label(
            contenedor, text="Versión 1.0", bg=COLOR_PANEL_IZQ, fg="#D6E4FF", font=("Segoe UI", 10)
        ).pack(pady=(10, 0))

    def crear_login(self):

        Label(
            self.contenedor,
            text="Bienvenido",
            bg=COLOR_PANEL_DER,
            fg=COLOR_TEXTO,
            font=FUENTE_TITULO,
        ).pack(pady=(20, 5))

        Label(
            self.contenedor,
            text="Ingrese sus credenciales para continuar",
            bg=COLOR_PANEL_DER,
            fg=COLOR_SECUNDARIO,
            font=FUENTE_SUB,
        ).pack(pady=(0, 35))

        Label(
            self.contenedor, text="Usuario", bg=COLOR_PANEL_DER, fg=COLOR_TEXTO, font=FUENTE_LABEL
        ).pack(anchor="w")

        self.txtUsuario = ttk.Entry(
            self.contenedor, width=35, style="Modern.TEntry", font=FUENTE_ENTRY
        )

        self.txtUsuario.pack(ipady=8, pady=(5, 20))

        Label(
            self.contenedor,
            text="Contraseña",
            bg=COLOR_PANEL_DER,
            fg=COLOR_TEXTO,
            font=FUENTE_LABEL,
        ).pack(anchor="w")

        self.txtClave = ttk.Entry(
            self.contenedor, show="*", width=35, style="Modern.TEntry", font=FUENTE_ENTRY
        )

        self.txtClave.pack(ipady=8, pady=(5, 30))

        self.txtClave.bind("<Return>", lambda e: self.logica.iniciar_sesion())

        self.btnIngresar = Button(
            self.contenedor,
            text="Iniciar sesión",
            bg=COLOR_BOTON,
            fg="white",
            activebackground=COLOR_BOTON_HOVER,
            activeforeground="white",
            relief=FLAT,
            bd=0,
            cursor="hand2",
            font=FUENTE_BOTON,
            width=28,
            height=2,
            command=self.logica.iniciar_sesion,
        )

        self.btnIngresar.pack(pady=10)

        self.btnIngresar.bind("<Enter>", self.entrar_boton)

        self.btnIngresar.bind("<Leave>", self.salir_boton)

        Label(
            self.contenedor,
            text="Base de datos: bdhospital_privado",
            bg=COLOR_PANEL_DER,
            fg=COLOR_SECUNDARIO,
            font=("Segoe UI", 9),
        ).pack(pady=(40, 0))

    def entrar_boton(self, event):

        self.btnIngresar.configure(bg=COLOR_BOTON_HOVER)

    def salir_boton(self, event):

        self.btnIngresar.configure(bg=COLOR_BOTON)
