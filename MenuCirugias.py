from tkinter import *

from Cirugias import Cirugias
from Quirofanos import Quirofanos
from Kardex import Kardex

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
FUENTE_TARJETA = ("Segoe UI", 13, "bold")
FUENTE_DESCRIPCION = ("Segoe UI", 9)


class MenuCirugias:

    def __init__(self, ventana, al_cerrar=None):

        self.ventana = ventana
        self.al_cerrar = al_cerrar
        self.ventana.title("Gestión de Cirugías")

        self.ventana.resizable(False, False)

        ancho = 1100
        alto = 650

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

        contenido.pack(fill=BOTH, expand=True, padx=55, pady=30)

        Label(
            contenido,
            text="Gestión de cirugías",
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            font=FUENTE_TITULO,
        ).pack(anchor="w")

        Label(
            contenido,
            text="Administra cirugías, quirófanos y kardex hospitalario.",
            bg=COLOR_FONDO,
            fg=COLOR_SECUNDARIO,
            font=FUENTE_SUBTITULO,
        ).pack(anchor="w", pady=(4, 25))

        tarjetas = Frame(contenido, bg=COLOR_FONDO)

        tarjetas.pack(fill=BOTH, expand=True)

        tarjetas.columnconfigure(0, weight=1)

        tarjetas.columnconfigure(1, weight=1)

        tarjetas.rowconfigure(0, weight=1)

        tarjetas.rowconfigure(1, weight=1)

        self.crear_tarjeta(
            tarjetas,
            0,
            0,
            "🏥",
            "Cirugías",
            "Registra y administra los procedimientos quirúrgicos.",
            self.abrir_cirugias,
        )

        self.crear_tarjeta(
            tarjetas,
            0,
            1,
            "🚪",
            "Quirófanos",
            "Gestiona los quirófanos disponibles del hospital.",
            self.abrir_quirofanos,
        )

        self.crear_tarjeta(
            tarjetas,
            1,
            0,
            "📦",
            "Kardex",
            "Administra el control y registro del kardex.",
            self.abrir_kardex,
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
            padx=18,
            pady=7,
            command=self.cerrar,
        ).pack(anchor="e", pady=(18, 0))

    def crear_tarjeta(self, contenedor, fila, columna, icono, titulo, descripcion, comando):

        tarjeta = Frame(
            contenedor,
            bg=COLOR_BLANCO,
            highlightbackground=COLOR_BORDE,
            highlightthickness=1,
            cursor="hand2",
        )

        tarjeta.grid(row=fila, column=columna, padx=12, pady=12, sticky="nsew")

        contenido = Frame(tarjeta, bg=COLOR_BLANCO, cursor="hand2")

        contenido.pack(fill=BOTH, expand=True, padx=25, pady=20)

        icono_frame = Frame(contenido, bg=COLOR_AZUL_CLARO, width=65, height=65, cursor="hand2")

        icono_frame.pack(anchor="w")

        icono_frame.pack_propagate(False)

        Label(
            icono_frame,
            text=icono,
            bg=COLOR_AZUL_CLARO,
            font=("Segoe UI Emoji", 27),
            cursor="hand2",
        ).pack(expand=True)

        Label(
            contenido,
            text=titulo,
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=FUENTE_TARJETA,
            cursor="hand2",
        ).pack(anchor="w", pady=(18, 5))

        Label(
            contenido,
            text=descripcion,
            bg=COLOR_BLANCO,
            fg=COLOR_SECUNDARIO,
            font=FUENTE_DESCRIPCION,
            cursor="hand2",
            wraplength=350,
            justify=LEFT,
        ).pack(anchor="w")

        Label(
            contenido,
            text="Abrir  →",
            bg=COLOR_BLANCO,
            fg=COLOR_AZUL,
            font=("Segoe UI", 9, "bold"),
            cursor="hand2",
        ).pack(anchor="e", pady=(15, 0))

        widgets = (
            [tarjeta, contenido, icono_frame]
            + list(contenido.winfo_children())
            + list(icono_frame.winfo_children())
        )

        for widget in widgets:

            widget.bind("<Button-1>", lambda e, cmd=comando: cmd())

            widget.bind("<Enter>", lambda e, t=tarjeta: self.hover_tarjeta(t))

            widget.bind("<Leave>", lambda e, t=tarjeta: self.normal_tarjeta(t))

    def hover_tarjeta(self, tarjeta):

        tarjeta.configure(bg=COLOR_AZUL_HOVER, highlightbackground=COLOR_AZUL)

        for widget in tarjeta.winfo_children():

            widget.configure(bg=COLOR_AZUL_HOVER)

            for hijo in widget.winfo_children():

                try:
                    hijo.configure(bg=COLOR_AZUL_HOVER)
                except:
                    pass

    def normal_tarjeta(self, tarjeta):

        tarjeta.configure(bg=COLOR_BLANCO, highlightbackground=COLOR_BORDE)

        for widget in tarjeta.winfo_children():

            widget.configure(bg=COLOR_BLANCO)

            for hijo in widget.winfo_children():

                try:
                    if widget == tarjeta.winfo_children()[1]:
                        hijo.configure(bg=COLOR_BLANCO)
                    else:
                        hijo.configure(bg=COLOR_AZUL_CLARO)
                except:
                    pass

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

    def abrir_cirugias(self):
        self.abrir_hijo(Cirugias)

    def abrir_quirofanos(self):
        self.abrir_hijo(Quirofanos)

    def abrir_kardex(self):
        self.abrir_hijo(Kardex)


def menu_cirugias(ventana, al_cerrar=None):
    return MenuCirugias(ventana, al_cerrar)


if __name__ == "__main__":

    ventana = Tk()
    menu_cirugias(ventana)
    ventana.mainloop()
