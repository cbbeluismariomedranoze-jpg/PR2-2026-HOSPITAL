from tkinter import *
from tkinter import ttk

from MenuPricipal import MenuPricipal

COLOR_FONDO = "#F4F8FC"
COLOR_AZUL_OSCURO = "#174EA6"
COLOR_AZUL = "#2563EB"
COLOR_AZUL_CLARO = "#EAF3FF"
COLOR_AZUL_HOVER = "#DCEBFF"
COLOR_BLANCO = "#FFFFFF"
COLOR_TEXTO = "#172B4D"
COLOR_SECUNDARIO = "#718096"
COLOR_BORDE = "#DCE6F2"
COLOR_CERRAR = "#E5484D"

FUENTE_LOGO = ("Segoe UI", 18, "bold")
FUENTE_TITULO = ("Segoe UI", 27, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 11)
FUENTE_TARJETA = ("Segoe UI", 13, "bold")
FUENTE_DESCRIPCION = ("Segoe UI", 9)
FUENTE_BOTON = ("Segoe UI", 10, "bold")


class MenuPrincipalV:

    def __init__(self, ventana, datos_usuario):

        self.ventana = ventana
        self.datos_usuario = datos_usuario

        self.logica = MenuPricipal(self, datos_usuario)

        self.configurar_ventana()
        self.crear_interfaz()

    def configurar_ventana(self):

        self.ventana.title("Hospital Privado")

        self.ventana.geometry("1250x700")

        self.ventana.minsize(1000, 650)

        self.ventana.configure(bg=COLOR_FONDO)

    def crear_interfaz(self):

        franja = Frame(self.ventana, bg=COLOR_AZUL, height=5)

        franja.pack(fill=X)

        self.barra_superior = Frame(self.ventana, bg=COLOR_BLANCO, height=72)

        self.barra_superior.pack(fill=X)

        self.barra_superior.pack_propagate(False)

        contenedor_logo = Frame(self.barra_superior, bg=COLOR_BLANCO)

        contenedor_logo.pack(side=LEFT, padx=35)

        Label(
            contenedor_logo, text="✚", bg=COLOR_BLANCO, fg=COLOR_AZUL, font=("Segoe UI", 25, "bold")
        ).pack(side=LEFT, padx=(0, 10))

        contenedor_texto_logo = Frame(contenedor_logo, bg=COLOR_BLANCO)

        contenedor_texto_logo.pack(side=LEFT)

        Label(
            contenedor_texto_logo,
            text="Hospital Privado",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=FUENTE_LOGO,
        ).pack(anchor="w")

        Label(
            contenedor_texto_logo,
            text="Sistema de gestión hospitalaria",
            bg=COLOR_BLANCO,
            fg=COLOR_SECUNDARIO,
            font=("Segoe UI", 8),
        ).pack(anchor="w")

        usuario = Frame(self.barra_superior, bg=COLOR_BLANCO)

        usuario.pack(side=RIGHT, padx=25)

        Button(
            usuario,
            text="⎋",
            bg=COLOR_BLANCO,
            fg=COLOR_CERRAR,
            relief=FLAT,
            bd=0,
            font=("Segoe UI", 17, "bold"),
            cursor="hand2",
            command=self.logica.cerrar_sesion,
        ).pack(side=RIGHT, padx=(12, 0))

        datos = Frame(usuario, bg=COLOR_BLANCO)

        datos.pack(side=RIGHT)

        Label(
            datos,
            text=self.datos_usuario["nombres"],
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="e")

        Label(
            datos,
            text=self.datos_usuario["nivel"],
            bg=COLOR_BLANCO,
            fg=COLOR_SECUNDARIO,
            font=("Segoe UI", 8),
        ).pack(anchor="e")

        contenedor = Frame(self.ventana, bg=COLOR_FONDO)

        contenedor.pack(fill=BOTH, expand=True, padx=45, pady=30)

        Label(
            contenedor, text="Bienvenido", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TITULO
        ).pack(anchor="w")

        Label(
            contenedor,
            text="Administra de manera sencilla la información del Hospital Privado.",
            bg=COLOR_FONDO,
            fg=COLOR_SECUNDARIO,
            font=FUENTE_SUBTITULO,
        ).pack(anchor="w", pady=(3, 22))

        hero = Frame(contenedor, bg=COLOR_AZUL_CLARO, height=150)

        hero.pack(fill=X, pady=(0, 25))

        hero.pack_propagate(False)

        hero_texto = Frame(hero, bg=COLOR_AZUL_CLARO)

        hero_texto.pack(side=LEFT, fill=Y, padx=30, pady=25)

        Label(
            hero_texto,
            text="Gestión hospitalaria",
            bg=COLOR_AZUL_CLARO,
            fg=COLOR_AZUL_OSCURO,
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w")

        Label(
            hero_texto,
            text="Accede a los principales módulos del sistema.",
            bg=COLOR_AZUL_CLARO,
            fg=COLOR_SECUNDARIO,
            font=("Segoe UI", 10),
        ).pack(anchor="w", pady=(6, 0))

        decoracion = Frame(hero, bg=COLOR_AZUL)

        decoracion.pack(side=RIGHT, fill=Y)

        Label(
            decoracion, text="✚", bg=COLOR_AZUL, fg=COLOR_BLANCO, font=("Segoe UI", 55, "bold")
        ).pack(padx=60, pady=20)

        Label(
            contenedor,
            text="Módulos principales",
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            font=("Segoe UI", 15, "bold"),
        ).pack(anchor="w", pady=(0, 10))

        self.tarjetas = Frame(contenedor, bg=COLOR_FONDO)

        self.tarjetas.pack(fill=BOTH, expand=True)

        self.crear_tarjetas()

    def crear_tarjetas(self):

        for columna in range(6):

            self.tarjetas.columnconfigure(columna, weight=1)

        self.crear_tarjeta(
            0, 0, "♙", "Pacientes", "Gestión de pacientes", self.logica.abrir_pacientes
        )

        self.crear_tarjeta(
            0, 1, "▣", "Consultas", "Administración de consultas", self.logica.abrir_consultas
        )

        self.crear_tarjeta(0, 2, "✚", "Cirugías", "Gestión de cirugías", self.logica.abrir_cirugias)

        self.crear_tarjeta(
            0, 3, "🔍", "Búsquedas", "Consultar información", self.logica.abrir_busquedas
        )

        self.crear_tarjeta(0, 4, "▤", "Reportes", "Generar reportes", self.logica.abrir_reportes)

        self.crear_tarjeta(
            0, 5, "👤", "Usuarios", "Gestión de usuarios del sistema", self.logica.abrir_usuarios
        )

    def crear_tarjeta(self, fila, columna, icono, titulo, descripcion, comando):

        tarjeta = Frame(
            self.tarjetas,
            bg=COLOR_BLANCO,
            cursor="hand2",
            highlightbackground=COLOR_BORDE,
            highlightthickness=1,
        )

        tarjeta.grid(row=fila, column=columna, padx=7, pady=7, sticky="nsew")

        icono_frame = Frame(tarjeta, bg=COLOR_AZUL_CLARO, width=48, height=48)

        icono_frame.pack(anchor="w", padx=18, pady=(18, 12))

        icono_frame.pack_propagate(False)

        Label(
            icono_frame,
            text=icono,
            bg=COLOR_AZUL_CLARO,
            fg=COLOR_AZUL,
            font=("Segoe UI", 20, "bold"),
        ).pack(expand=True)

        Label(tarjeta, text=titulo, bg=COLOR_BLANCO, fg=COLOR_TEXTO, font=FUENTE_TARJETA).pack(
            anchor="w", padx=18
        )

        Label(
            tarjeta, text=descripcion, bg=COLOR_BLANCO, fg=COLOR_SECUNDARIO, font=FUENTE_DESCRIPCION
        ).pack(anchor="w", padx=18, pady=(4, 18))

        widgets = [tarjeta, icono_frame] + list(tarjeta.winfo_children())

        for widget in widgets:

            widget.bind("<Button-1>", lambda e, cmd=comando: cmd())

            widget.bind(
                "<Enter>", lambda e, t=tarjeta, i=icono_frame: self.hover_tarjeta(t, i, True)
            )

            widget.bind(
                "<Leave>", lambda e, t=tarjeta, i=icono_frame: self.hover_tarjeta(t, i, False)
            )

    def hover_tarjeta(self, tarjeta, icono_frame, activo):

        if activo:

            tarjeta.configure(bg=COLOR_AZUL_HOVER)

            icono_frame.configure(bg=COLOR_AZUL)

            for widget in tarjeta.winfo_children():

                if isinstance(widget, Label):

                    widget.configure(bg=COLOR_AZUL_HOVER)

            for widget in icono_frame.winfo_children():

                widget.configure(bg=COLOR_AZUL, fg=COLOR_BLANCO)

        else:

            tarjeta.configure(bg=COLOR_BLANCO)

            icono_frame.configure(bg=COLOR_AZUL_CLARO)

            for widget in tarjeta.winfo_children():

                if isinstance(widget, Label):

                    widget.configure(bg=COLOR_BLANCO)

            for widget in icono_frame.winfo_children():

                widget.configure(bg=COLOR_AZUL_CLARO, fg=COLOR_AZUL)

    def maximizar(self):

        try:
            self.ventana.state("zoomed")
        except:
            pass
