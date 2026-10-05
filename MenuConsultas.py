from tkinter import *

from Reservas import Reservas
from Atenciones import Atenciones
from Diagnosticos import Diagnosticos
from Laboratorios import Laboratorios
from Consultorios import Consultorios

COLOR_FONDO = "#F4F8FC"
COLOR_AZUL_OSCURO = "#174EA6"
COLOR_AZUL = "#2563EB"
COLOR_AZUL_CLARO = "#EAF3FF"
COLOR_AZUL_HOVER = "#DCEBFF"
COLOR_BLANCO = "#FFFFFF"
COLOR_TEXTO = "#172B4D"
COLOR_SECUNDARIO = "#718096"
COLOR_BORDE = "#DCE6F2"


FUENTE_TITULO = ("Segoe UI", 24, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 11)
FUENTE_TARJETA = ("Segoe UI", 14, "bold")
FUENTE_DESCRIPCION = ("Segoe UI", 10)


class MenuConsultas:

    def __init__(self, ventana, al_cerrar=None):

        self.ventana = ventana
        self.al_cerrar = al_cerrar
        self.ventana.title("Gestión de Consultas")

        self.ventana.resizable(True, True)

        ancho = 1200
        alto = 750

        pantalla_ancho = self.ventana.winfo_screenwidth()
        pantalla_alto = self.ventana.winfo_screenheight()

        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)

        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

        self.ventana.minsize(1100, 700)

        self.ventana.configure(bg=COLOR_FONDO)

        self.crear_interfaz()

    def crear_interfaz(self):

        Frame(self.ventana, bg=COLOR_AZUL, height=6).pack(fill=X)

        barra = Frame(self.ventana, bg=COLOR_BLANCO, height=75)

        barra.pack(fill=X)

        barra.pack_propagate(False)

        logo = Frame(barra, bg=COLOR_BLANCO)

        logo.pack(side=LEFT, padx=40)

        Label(logo, text="✚", bg=COLOR_BLANCO, fg=COLOR_AZUL, font=("Segoe UI", 28, "bold")).pack(
            side=LEFT, padx=(0, 12)
        )

        texto_logo = Frame(logo, bg=COLOR_BLANCO)

        texto_logo.pack(side=LEFT)

        Label(
            texto_logo,
            text="Hospital Privado",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w")

        Label(
            texto_logo,
            text="Sistema de gestión hospitalaria",
            bg=COLOR_BLANCO,
            fg=COLOR_SECUNDARIO,
            font=("Segoe UI", 9),
        ).pack(anchor="w")

        contenido = Frame(self.ventana, bg=COLOR_FONDO)

        contenido.pack(fill=BOTH, expand=True, padx=60, pady=35)

        Label(
            contenido,
            text="Gestión de consultas",
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            font=FUENTE_TITULO,
        ).pack(anchor="w")

        Label(
            contenido,
            text="Administra reservas, atenciones, diagnósticos, laboratorios y consultorios.",
            bg=COLOR_FONDO,
            fg=COLOR_SECUNDARIO,
            font=FUENTE_SUBTITULO,
        ).pack(anchor="w", pady=(5, 30))

        tarjetas = Frame(contenido, bg=COLOR_FONDO)

        tarjetas.pack(fill=BOTH, expand=True)

        tarjetas.columnconfigure(0, weight=1)

        tarjetas.columnconfigure(1, weight=1)

        for fila in range(3):

            tarjetas.rowconfigure(fila, minsize=180)

        self.crear_tarjeta(
            tarjetas,
            0,
            0,
            "📅",
            "Reservas",
            "Gestiona las reservas de consultas.",
            self.abrir_reservas,
        )

        self.crear_tarjeta(
            tarjetas,
            0,
            1,
            "🩺",
            "Atenciones",
            "Registra y administra las atenciones médicas.",
            self.abrir_atenciones,
        )

        self.crear_tarjeta(
            tarjetas,
            1,
            0,
            "📋",
            "Diagnósticos",
            "Administra los diagnósticos de pacientes.",
            self.abrir_diagnosticos,
        )

        self.crear_tarjeta(
            tarjetas,
            1,
            1,
            "🧪",
            "Laboratorios",
            "Gestiona resultados y estados de laboratorio.",
            self.abrir_laboratorios,
        )

        self.crear_tarjeta(
            tarjetas,
            2,
            0,
            "🏥",
            "Consultorios",
            "Administra los consultorios disponibles.",
            self.abrir_consultorios,
        )

        Button(
            contenido,
            text="←  Volver",
            bg=COLOR_BLANCO,
            fg=COLOR_AZUL_OSCURO,
            activebackground=COLOR_AZUL_HOVER,
            activeforeground=COLOR_AZUL_OSCURO,
            relief="solid",
            bd=1,
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
            padx=20,
            pady=8,
            command=self.cerrar,
        ).pack(anchor="e", pady=(20, 0))

    def crear_tarjeta(self, contenedor, fila, columna, icono, titulo, descripcion, comando):

        tarjeta = Frame(
            contenedor,
            bg=COLOR_BLANCO,
            highlightbackground=COLOR_BORDE,
            highlightthickness=1,
            cursor="hand2",
        )

        tarjeta.grid(row=fila, column=columna, padx=15, pady=15, sticky="nsew")

        tarjeta.config(width=450, height=180)

        tarjeta.grid_propagate(False)

        contenido = Frame(tarjeta, bg=COLOR_BLANCO)

        contenido.pack(fill=BOTH, expand=True, padx=30, pady=25)

        icono_frame = Frame(contenido, bg=COLOR_AZUL_CLARO, width=75, height=75)

        icono_frame.pack(anchor="w")

        icono_frame.pack_propagate(False)

        lbl_icono = Label(
            icono_frame,
            text=icono,
            bg=COLOR_AZUL_CLARO,
            fg=COLOR_AZUL_OSCURO,
            font=("Segoe UI Emoji", 32),
        )

        lbl_icono.pack(expand=True)

        lbl_titulo = Label(
            contenido, text=titulo, bg=COLOR_BLANCO, fg=COLOR_TEXTO, font=FUENTE_TARJETA
        )

        lbl_titulo.pack(anchor="w", pady=(12, 5))

        lbl_descripcion = Label(
            contenido,
            text=descripcion,
            bg=COLOR_BLANCO,
            fg=COLOR_SECUNDARIO,
            font=FUENTE_DESCRIPCION,
            wraplength=380,
            justify=LEFT,
        )

        lbl_descripcion.pack(anchor="w")

        widgets = [tarjeta, contenido, icono_frame, lbl_icono, lbl_titulo, lbl_descripcion]

        for widget in widgets:

            widget.bind("<Button-1>", lambda e, cmd=comando: cmd())

            widget.bind("<Enter>", lambda e, t=tarjeta, w=widgets: self.hover_tarjeta(t, w))

            widget.bind("<Leave>", lambda e, t=tarjeta, w=widgets: self.normal_tarjeta(t, w))

    def hover_tarjeta(self, tarjeta, widgets):

        tarjeta.configure(bg=COLOR_AZUL_HOVER, highlightbackground=COLOR_AZUL)

        for widget in widgets:

            if widget == widgets[2] or widget == widgets[3]:

                widget.configure(bg=COLOR_AZUL_CLARO)

            else:

                widget.configure(bg=COLOR_AZUL_HOVER)

    def normal_tarjeta(self, tarjeta, widgets):

        tarjeta.configure(bg=COLOR_BLANCO, highlightbackground=COLOR_BORDE)

        for widget in widgets:

            if widget == widgets[2] or widget == widgets[3]:

                widget.configure(bg=COLOR_AZUL_CLARO)

            else:

                widget.configure(bg=COLOR_BLANCO)

    def abrir_hijo(self, ClaseVentana):
        self.ventana.withdraw()

        ventana_hija = Toplevel(self.ventana)
        ClaseVentana(ventana_hija, lambda: self.volver(ventana_hija))

        ventana_hija.protocol("WM_DELETE_WINDOW", lambda: self.volver(ventana_hija))

    def volver(self, ventana_hija):
        ventana_hija.destroy()
        self.ventana.deiconify()

    def cerrar(self):
        if self.al_cerrar:
            self.al_cerrar()
        else:
            self.ventana.destroy()

    def abrir_reservas(self):
        self.abrir_hijo(Reservas)

    def abrir_atenciones(self):
        self.abrir_hijo(Atenciones)

    def abrir_diagnosticos(self):
        self.abrir_hijo(Diagnosticos)

    def abrir_laboratorios(self):
        self.abrir_hijo(Laboratorios)

    def abrir_consultorios(self):
        self.abrir_hijo(Consultorios)


def menu_consultas(ventana, al_cerrar=None):
    return MenuConsultas(ventana, al_cerrar)


if __name__ == "__main__":

    ventana = Tk()
    menu_consultas(ventana)
    ventana.mainloop()
