from tkinter import *
from tkinter import ttk
from Conexion import conectar


COLOR_FONDO = "#F4F8FC"
COLOR_AZUL = "#2563EB"
COLOR_BLANCO = "#FFFFFF"
COLOR_TEXTO = "#172B4D"
COLOR_SECUNDARIO = "#718096"
COLOR_BORDE = "#DCE6F2"



class RepConsultorios:


    def __init__(self, ventana):

        self.ventana = ventana


        self.ventana.title(
            "Sistema Hospitalario - Reporte de Consultorios"
        )


        self.ventana.resizable(
            True,
            True
        )


        ancho = 1200
        alto = 600


        pantalla_ancho = self.ventana.winfo_screenwidth()
        pantalla_alto = self.ventana.winfo_screenheight()


        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)


        self.ventana.geometry(
            f"{ancho}x{alto}+{x}+{y}"
        )


        self.ventana.configure(
            bg=COLOR_FONDO
        )



        Frame(
            self.ventana,
            bg=COLOR_AZUL,
            height=5
        ).pack(
            fill=X
        )



        barra = Frame(
            self.ventana,
            bg=COLOR_BLANCO,
            height=70
        )


        barra.pack(
            fill=X
        )


        barra.pack_propagate(False)



        logo = Frame(
            barra,
            bg=COLOR_BLANCO
        )


        logo.pack(
            side=LEFT,
            padx=35
        )



        Label(
            logo,
            text="✚",
            bg=COLOR_BLANCO,
            fg=COLOR_AZUL,
            font=("Segoe UI",25,"bold")
        ).pack(
            side=LEFT,
            padx=(0,10)
        )



        texto_logo = Frame(
            logo,
            bg=COLOR_BLANCO
        )


        texto_logo.pack(
            side=LEFT
        )



        Label(
            texto_logo,
            text="Hospital Privado",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=("Segoe UI",17,"bold")
        ).pack(
            anchor="w"
        )



        Label(
            texto_logo,
            text="Sistema de gestión hospitalaria",
            bg=COLOR_BLANCO,
            fg=COLOR_SECUNDARIO,
            font=("Segoe UI",8)
        ).pack(
            anchor="w"
        )



        contenido = Frame(
            self.ventana,
            bg=COLOR_FONDO
        )


        contenido.pack(
            fill=BOTH,
            expand=True,
            padx=40,
            pady=25
        )



        Label(
            contenido,
            text="Reporte de consultorios",
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            font=("Segoe UI",22,"bold")
        ).pack(
            anchor="w"
        )



        Label(
            contenido,
            text="Consulta la información de los consultorios disponibles.",
            bg=COLOR_FONDO,
            fg=COLOR_SECUNDARIO,
            font=("Segoe UI",10)
        ).pack(
            anchor="w",
            pady=(5,20)
        )



        tabla_frame = Frame(
            contenido,
            bg=COLOR_BLANCO,
            highlightbackground=COLOR_BORDE,
            highlightthickness=1
        )


        tabla_frame.pack(
            fill=BOTH,
            expand=True
        )



        contenedor = Frame(
            tabla_frame,
            bg=COLOR_BLANCO
        )


        contenedor.pack(
            fill=BOTH,
            expand=True,
            padx=10,
            pady=10
        )



        estilo = ttk.Style()


        estilo.configure(
            "Treeview",
            font=("Segoe UI",9),
            rowheight=30
        )


        estilo.configure(
            "Treeview.Heading",
            font=("Segoe UI",10,"bold")
        )



        self.tabla = ttk.Treeview(
            contenedor,
            columns=(
                "nro",
                "detalle",
                "ubicacion"
            ),
            show="headings"
        )



        columnas = [
            ("nro","N° Consultorio",150),
            ("detalle","Detalle",450),
            ("ubicacion","Ubicación",250)
        ]



        for columna,texto,ancho in columnas:


            self.tabla.heading(
                columna,
                text=texto
            )


            self.tabla.column(
                columna,
                width=ancho,
                anchor="center"
            )



        scroll_y = ttk.Scrollbar(
            contenedor,
            orient=VERTICAL,
            command=self.tabla.yview
        )


        scroll_x = ttk.Scrollbar(
            contenedor,
            orient=HORIZONTAL,
            command=self.tabla.xview
        )



        self.tabla.configure(
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )



        self.tabla.grid(
            row=0,
            column=0,
            sticky="nsew"
        )


        scroll_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )


        scroll_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )



        contenedor.grid_rowconfigure(
            0,
            weight=1
        )


        contenedor.grid_columnconfigure(
            0,
            weight=1
        )



        self.cargar()



    def cargar(self):

        conexion = conectar()

        cursor = conexion.cursor()


        cursor.execute(
            "SELECT * FROM consultorios"
        )



        for fila in cursor.fetchall():

            self.tabla.insert(
                "",
                END,
                values=fila
            )


        conexion.close()



if __name__ == "__main__":


    raiz = Tk()


    RepConsultorios(
        raiz
    )


    raiz.mainloop()