
import sys
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import _support
import math

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    _support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    _support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("913x580+300+502")
        top.title("Calculadora")
        top.configure(background="#d9d9d9")

        self.Sumar = ttk.Button(top)
        self.Sumar.place(relx=0.055, rely=0.380, height=52, width=183)
        self.Sumar.configure(takefocus="")
        self.Sumar.configure(text='''Sumar''')
        self.Sumar.configure(width=183)

        self.titulo = ttk.Label(top)
        self.titulo.place(relx=0.30, rely=0.005, height=36, width=600)
        self.titulo.configure(background="#d9d9d9")
        self.titulo.configure(foreground="#000000")
        self.titulo.configure(font="TkDefaultFont")
        self.titulo.configure(relief='flat')
        self.titulo.configure(text='''Ingrese 2 diferentes numeros para realizar cualquier operacion''')

        self.numero1Entry = tk.Entry(top)
        self.numero1Entry.place(relx=0.088, rely=0.069,height=44, relwidth=0.355)
        self.numero1Entry.configure(background="white")
        self.numero1Entry.configure(disabledforeground="#a3a3a3")
        self.numero1Entry.configure(font="TkFixedFont")
        self.numero1Entry.configure(foreground="#000000")
        self.numero1Entry.configure(insertbackground="black")
        self.numero1Entry.configure(width=324)

        self.numero1Label = tk.Label(top)
        self.numero1Label.place(relx=0.197, rely=0.155, height=38, width=114)
        self.numero1Label.configure(background="#d9d9d9")
        self.numero1Label.configure(disabledforeground="#a3a3a3")
        self.numero1Label.configure(foreground="#000000")
        self.numero1Label.configure(text='''Numero 1''')

        self.numero2Entry = tk.Entry(top)
        self.numero2Entry.place(relx=0.515, rely=0.069,height=44, relwidth=0.355)
        self.numero2Entry.configure(background="white")
        self.numero2Entry.configure(disabledforeground="#a3a3a3")
        self.numero2Entry.configure(font="TkFixedFont")
        self.numero2Entry.configure(foreground="#000000")
        self.numero2Entry.configure(highlightbackground="#d9d9d9")
        self.numero2Entry.configure(highlightcolor="black")
        self.numero2Entry.configure(insertbackground="black")
        self.numero2Entry.configure(selectbackground="#c4c4c4")
        self.numero2Entry.configure(selectforeground="black")

        self.numero2 = tk.Label(top)
        self.numero2.place(relx=0.624, rely=0.155, height=38, width=114)
        self.numero2.configure(activebackground="#f9f9f9")
        self.numero2.configure(activeforeground="black")
        self.numero2.configure(background="#d9d9d9")
        self.numero2.configure(disabledforeground="#a3a3a3")
        self.numero2.configure(foreground="#000000")
        self.numero2.configure(highlightbackground="#d9d9d9")
        self.numero2.configure(highlightcolor="black")
        self.numero2.configure(text='''Numero 2''')

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.318, rely=0.241, height=36, width=114)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief='flat')
        self.TLabel1.configure(text='''Resultado:''')

        self.resultado = ttk.Label(top)
        self.resultado.place(relx=0.46, rely=0.241, height=36, width=100)
        self.resultado.configure(background="#d9d9d9")
        self.resultado.configure(foreground="#000000")
        self.resultado.configure(font="TkDefaultFont")
        self.resultado.configure(relief='flat')
        self.resultado.configure(text='''0''')

        self.Restar = ttk.Button(top)
        self.Restar.place(relx=0.372, rely=0.380, height=52, width=183)
        self.Restar.configure(takefocus="")
        self.Restar.configure(text='''Restar''')

        self.Limpiar = ttk.Button(top)
        self.Limpiar.place(relx=0.701, rely=0.240, height=52, width=183)
        self.Limpiar.configure(takefocus="")
        self.Limpiar.configure(text='''Borrar datos''')

        self.Dividir = ttk.Button(top)
        self.Dividir.place(relx=0.701, rely=0.380, height=52, width=183)
        self.Dividir.configure(takefocus="")
        self.Dividir.configure(text='''Dividir''')

        self.Multiplicar = ttk.Button(top)
        self.Multiplicar.place(relx=0.055, rely=0.569, height=52, width=183)
        self.Multiplicar.configure(takefocus="")
        self.Multiplicar.configure(text='''Multiplicar''')

        self.RaizCuadrada = ttk.Button(top)
        self.RaizCuadrada.place(relx=0.372, rely=0.569, height=52, width=183)
        self.RaizCuadrada.configure(takefocus="")
        self.RaizCuadrada.configure(text='''Raiz cuadrada''')

        self.Historial = ttk.Button(top)
        self.Historial.place(relx=0.372, rely=0.758, height=52, width=183)
        self.Historial.configure(takefocus="")
        self.Historial.configure(text='''Anterior Valor''')

        self.Exponente = ttk.Button(top)
        self.Exponente.place(relx=0.701, rely=0.569, height=52, width=183)
        self.Exponente.configure(takefocus="")
        self.Exponente.configure(text='''Exponente''')

        self.historialLabel = ttk.Label(top)
        self.historialLabel.place(relx=0.701, rely=0.758, height=36, width=100)
        self.historialLabel.configure(background="#d9d9d9")
        self.historialLabel.configure(foreground="#000000")
        self.historialLabel.configure(font="TkDefaultFont")
        self.historialLabel.configure(relief='flat')
        self.historialLabel.configure(text='''-''')

        '''
        Se asignan los metodos al hacer click en cada boton.
        Se utiliza lambda porque cuando se corre el programa se espera a que el metodo reciba un parametro, 
        pero de esta forma espera hasta que sea ejecutada la accion.
        '''
        self.Sumar.configure(command = lambda : self.hacerClick("sumar"))
        self.Restar.configure(command=lambda: self.hacerClick("restar"))
        self.Multiplicar.configure(command=lambda: self.hacerClick("multiplicacion"))
        self.Dividir.configure(command=lambda: self.hacerClick("dividir"))
        self.RaizCuadrada.configure(command=lambda: self.hacerClick("raizCuadrada"))
        self.Exponente.configure(command=lambda: self.hacerClick("exponente"))
        self.Limpiar.configure(command= self.limpiarDatos)
        self.Historial.configure(command = self.mostrarHistorial)

    '''
    Metodos encargados de realizar las operaciones matematicas.
    '''
    def sumar(self, numero1, numero2):
        return float(numero1) + float(numero2)

    def resta(self, numero1, numero2):
        return float(numero1) - float(numero2)

    def multiplicacion(self, numero1, numero2):
        return float(numero1) * float(numero2)

    def division(self, numero1, numero2):
        return float(numero1) / float(numero2)

    def raizCuadrada(self, numero1):
        if float(numero1) > 0:
            return math.sqrt(float(numero1))
        else:
            return print("Valor tiene que ser mayor a 0.")

    def exponente(self, numero1, numero2):
        return pow(float(numero1), float(numero2))

    '''
    Esta funcion es la encargada de recibir como parametro un valor y llamar a la funcion encargada de realizar la
    operacion matematica.
    '''
    def hacerClick(self, operacion):
        '''
        Se trae los valores de los campos ingresados por el usuario  y los asigna a una variable.
        '''
        numero1= str(self.numero1Entry.get())
        numero2 = str(self.numero2Entry.get())

        '''
        Aqui valida que los datos recibidos sean numeros y no esten vacios.
        Despues de la validacion inserta los valores en la lista de historial.
        '''
        if numero1.isdigit() and numero2.isdigit() and numero1 and numero2:
            if operacion == "sumar":
                resultadoDeOperacion = self.sumar(numero1, numero2)
                self.resultado.configure(text=str(resultadoDeOperacion))
                self.guardarHistorial(resultadoDeOperacion)
            elif operacion == "restar":
                resultadoDeOperacion = self.resta(numero1, numero2)
                self.resultado.configure(text=str(resultadoDeOperacion))
                self.guardarHistorial(resultadoDeOperacion)
            elif operacion == "multiplicacion":
                resultadoDeOperacion = self.multiplicacion(numero1, numero2)
                self.resultado.configure(text=str(resultadoDeOperacion))
                self.guardarHistorial(resultadoDeOperacion)
            elif operacion == "dividir":
                resultadoDeOperacion = self.division(numero1, numero2)
                self.resultado.configure(text=str(resultadoDeOperacion))
                self.guardarHistorial(resultadoDeOperacion)
            elif operacion == "raizCuadrada":
                resultadoDeOperacion = self.raizCuadrada(numero1)
                self.resultado.configure(text=str(resultadoDeOperacion))
                self.guardarHistorial(resultadoDeOperacion)
            elif operacion == "exponente":
                resultadoDeOperacion = self.exponente(numero1, numero2)
                self.resultado.configure(text=str(resultadoDeOperacion))
                self.guardarHistorial(resultadoDeOperacion)
        else:
                print("Ingreso datos incorrectos.")

    '''
    Metodo encargado de limpiar la pantalla.
    '''
    def limpiarDatos(self):
        self.numero1Entry.delete(0, "end")
        self.numero2Entry.delete(0, "end")

    '''
    Metodo encargado de guardar los resultados en una lista para el historial
    '''
    listaTest = []
    cont = 0
    def guardarHistorial(self, resultadoDeOperacion):
        self.listaTest.insert(self.cont, resultadoDeOperacion)
        self.cont +=1

    '''
    Metodo encargado de mostrar el anterior resultado.
    Evalua si se ha realizado alguna operacion anterior para mostrar los valores.
    '''
    def mostrarHistorial(self):
        if self.listaTest:
            if len(self.listaTest) == 1:
                self.historialLabel.configure(text=str(self.listaTest[0]))
            else:
                self.historialLabel.configure(text= str(self.listaTest[-2]))
        else:
            print("No ha realizado ninguna operacion.")

'''
El metodo main que se encarga de llamar la funcion de crear y mostrar la parte grafica de la Calculadora.
'''
if __name__ == '__main__':
    vp_start_gui()