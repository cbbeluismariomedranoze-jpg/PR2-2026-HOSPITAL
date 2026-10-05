from tkinter import *
from tkinter import messagebox

from MenuPacientes import menu_pacientes
from MenuConsultas import menu_consultas
from MenuCirugias import menu_cirugias
from MenuReportes import menu_reportes
from Busquedas import menu_busquedas
from Usuarios import Usuarios


class MenuPricipal:
    def __init__(self, vista, datos_usuario):
        self.vista = vista
        self.datos_usuario = datos_usuario

    def abrir_submenu(self, funcion_menu):
        self.vista.ventana.withdraw()

        ventana_hija = Toplevel(self.vista.ventana)
        funcion_menu(ventana_hija, lambda: self.volver_al_menu(ventana_hija))

        ventana_hija.protocol("WM_DELETE_WINDOW", lambda: self.volver_al_menu(ventana_hija))

    def volver_al_menu(self, ventana_hija):
        ventana_hija.destroy()
        self.vista.ventana.deiconify()  # vuelve a mostrar el menú

    def abrir_pacientes(self):
        self.abrir_submenu(menu_pacientes)

    def abrir_consultas(self):
        self.abrir_submenu(menu_consultas)

    def abrir_cirugias(self):
        self.abrir_submenu(menu_cirugias)

    def abrir_busquedas(self):
        self.abrir_submenu(menu_busquedas)

    def abrir_reportes(self):
        self.abrir_submenu(menu_reportes)

    def abrir_usuarios(self):

        if str(self.datos_usuario.get("nivel", "")).strip().lower() != "administrador":
            messagebox.showwarning(
                "Acceso restringido",
                "Solo un usuario con nivel 'Administrador' puede "
                "acceder a la gestión de usuarios.",
            )
            return
        self.abrir_submenu(lambda ventana, al_cerrar: Usuarios(ventana, al_cerrar))

    def salir(self):
        respuesta = messagebox.askyesno("Salir", "¿Desea cerrar el sistema?")
        if respuesta:
            self.vista.ventana.destroy()

    def cerrar_sesion(self):
        respuesta = messagebox.askyesno(
            "Cerrar Sesión", "¿Está seguro de que quiere cerrar sesión?"
        )
        if respuesta:
            self.vista.ventana.destroy()
            from InicioV import InicioV

            nueva_ventana = Tk()
            InicioV(nueva_ventana)
            nueva_ventana.mainloop()


if __name__ == "__main__":

    from tkinter import Tk
    from MenuPrincipalV import MenuPrincipalV

    datos_usuario = {
        "id": 0,
        "nombres": "Prueba",
        "usuario": "admin",
        "nivel": "admin",
        "estado": 1,
    }

    ventana = Tk()
    app = MenuPrincipalV(ventana, datos_usuario)
    ventana.mainloop()
