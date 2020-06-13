from tkinter import ttk
from tkinter import *
import datetime

class Operaciones:
    
    def __init__(self, window):
        #Valores de alto y ancho para la ventana
        ancho = 450
        alto = 250

        self.wind = window
        self.wind.geometry(str(ancho)+"x"+str(alto))
        self.wind.resizable(0,0)
        self.wind.columnconfigure(0, weight=1)
        self.wind.title("Examen Final")

        #Creacion de Frame y Label principales
        frame = LabelFrame(self.wind, text = "BIENVENIDO")
        frame.config(font = ("", 15), borderwidth= "0")
        frame.grid(row = 0, column = 0, pady = 30)
        
        #Creacion de los Label y Entry 
        Label(frame, text = "Nombre ").grid(row = 0, column = 0, columnspan = 2)
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 0, column = 2, columnspan = 3, sticky = W + E)

        Label(frame, text = "Apellido ").grid(row = 1, column = 0, columnspan = 2)
        self.var2 = Entry(frame)
        self.var2.grid(row = 1, column = 2, columnspan = 3, sticky = W + E)

        Label(frame, text = "Día ").grid(row = 2, column = 0, columnspan = 2)
        self.var3 = Entry(frame)
        self.var3.grid(row = 2, column = 2, columnspan = 3, sticky = W + E)

        Label(frame, text = "Mes ").grid(row = 3, column = 0, columnspan = 2)
        self.var4 = Entry(frame)
        self.var4.grid(row = 3, column = 2, columnspan = 3, sticky = W + E)

        Label(frame, text = "Año ").grid(row = 4, column = 0, columnspan = 2)
        self.var5 = Entry(frame)
        self.var5.grid(row = 4, column = 2, columnspan = 3, sticky = W + E)

        #Creacion de botones
        ttk.Button(frame, text = "Función 1", command = self.fechaHexa).grid(row = 5, column = 0)
        ttk.Button(frame, text = "Función 2", command = self.horaVida).grid(row = 5, column = 1)
        ttk.Button(frame, text = "Función 3", command = self.nombreApellidoPar).grid(row = 5, column = 2)
        ttk.Button(frame, text = "Función 4", command = self.contarVocalesConsonantes).grid(row = 5, column = 3)
        ttk.Button(frame, text = "Función 5", command = self.nombreApellidoInvertido).grid(row = 5, column = 4)

        #Impresion de la respuesta
        self.resultado = Label(self.wind, text = '', fg = "#000")
        self.resultado.grid(row = 1, column= 0, columnspan = 2, sticky = W + E)

    #Creacion de funciones para botones
    #Funcion de validacion de campos
    def validation(self):
        return (len(self.var1.get()) != 0 and len(self.var2.get()) != 0) or (len(self.var3.get()) != 0 and len(self.var4.get() ) != 0 and len(self.var5.get() ) != 0)

    #Creacion de funcion para fecha en hexadecimal
    def fechaHexa(self):
        if self.validation():
            dia = int(self.var3.get())
            mes = int(self.var4.get())
            año = int(self.var5.get())
            diaHexa = str(hex(dia).rstrip("L").lstrip("0x") or "0")
            mesHexa = str(hex(mes).rstrip("L").lstrip("0x") or "0")
            añoHexa = str(hex(año).rstrip("L").lstrip("0x") or "0")
            dia = str(dia)
            mes = str(mes)
            año = str(año)
            self.resultado["text"] = dia+"/"+mes+"/"+año+'{}'.format(" = "+diaHexa+"/"+mesHexa+"/"+añoHexa)
        else:
            self.resultado['text'] = 'Los campos son requeridos'

    #Creacion de funcion para calcular las horas vividas
    def horaVida(self):
        if self.validation():
            dia = int(self.var3.get())
            mes = int(self.var4.get())
            año = int(self.var5.get())
            fechaN = datetime.datetime(año, mes, dia)
            fechaH  = datetime.datetime.now()
            diferenciaTiempo = fechaH - fechaN
            resultado = diferenciaTiempo.days * 24              
            self.resultado["text"] = 'Has vivido: {}'.format(resultado)+" horas"
        else:
            self.resultado['text'] = 'Los campos son requeridos'

    #Creacion de funcion para determinar si el numero de caracteres de nombre y apellido son par o impar
    def nombreApellidoPar(self):
        if self.validation():
            nombre = str(self.var1.get())
            apellido = str(self.var2.get())
            parImpar= nombre + apellido
            resultado = len(parImpar)

            if resultado%2 == 0:
                resultado = "par"
            else:
                resultado = "impar"

            self.resultado["text"] = '{}'.format(nombre+" "+apellido+" su nombre junto con su apellido es "+ resultado)
        else:
            self.resultado['text'] = 'Los campos son requeridos'
        
    #Creacion de funcion para contar vocales y consonantes
    def contarVocalesConsonantes(self):
        if self.validation():
            nombre = str(self.var1.get())
            apellido = str(self.var2.get())
            vocal = 0
            consonante = 0
            vocal_2 = 0
            consonante_2 = 0

            for c in nombre:
                if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'á' or c == 'é' or c == 'i' or c == 'í' or c =='ó' or c == 'ú' or c == 'ü' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U' or c == 'Á' or c == 'É' or c == 'Í' or c =='Ó' or c == 'Ú':
                    vocal=vocal+1
                else:   
                    consonante=consonante+1

            for c in apellido:
                if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'á' or c == 'é' or c == 'i' or c == 'í' or c =='ó' or c == 'ú' or c == 'ü' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U' or c == 'Á' or c == 'É' or c == 'Í' or c =='Ó' or c == 'Ú':
                    vocal_2=vocal_2+1
                else:   
                    consonante_2=consonante_2+1

            self.resultado["text"] = '{}'.format(nombre+" tiene "+str(vocal)+" vocales y "+str(consonante)+" consonantes, "+apellido+" tiene "+str(vocal_2)+" vocales y "+str(consonante_2)+" consonantes")
        else:
            self.resultado['text'] = 'Los campos son requeridos'

    #Creacion funcion para invertir nombre y apellido
    def nombreApellidoInvertido(self):
        if self.validation():
            nombre = str(self.var1.get())
            apellido = str(self.var2.get())
            nombreApellido= nombre + apellido
            resultado = nombreApellido[::-1]
            
            self.resultado["text"] = nombre+" "+apellido+" al revés es "+'{}'.format(resultado)
        else:
            self.resultado['text'] = 'Los campos son requeridos'

if __name__ == "__main__":
    window = Tk()

    ope = Operaciones(window)

    window.mainloop()