from tkinter import *
from tkinter import messagebox
from random import randint
import letras

class Window:
    def __init__(self, Wnd):
        # Configurações da tela 
        Wnd.title("Trabalho CG - 2022")
        Wnd.minsize(width = "700", height = "500")
        self.framesTela(Wnd)
        self.CreateMenu(Wnd)
        # input da string
        #input comprimento dos poliedros (dimensão de z)
        Label(Wnd, text='Digite a String (max. 5 letras):').grid(row=0)
        Label(Wnd, text='Comprimento dos poliedros:').grid(row=1)
        e1 = Entry(Wnd)
        e2 = Entry(Wnd)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

#interface das 3 viewports (frente, lateral e topo)
    def framesTela(self,Wnd):
        self.FrameFrente = Frame(Wnd)
        self.FrameFrente.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        
        self.FrameLateral =  Frame(Wnd)

        
        self.FrameTopo = Frame(Wnd) 

        
        self.FrameOpcoes = Frame(Wnd)


#opções de transformações geo.

# botão salvar e de abrir outras cenas

# 4ª viewport projeção perspectiva ou paralela 
    def ClearCanvas(self):
        self.canvas.delete("all")

    def AboutTI(self):
        messagebox.showinfo(title = "Sobre...", message = "Trabalho de CG feito pelas alunas Alessandra e Ana Paula")

    def CreateMenu(self, Wnd) :
        MenuBar = Menu(Wnd)

        MenuArq = Menu(MenuBar, tearoff = 0)
        MenuArq.add_command(label = "Limpar", command = self.ClearCanvas)
        MenuArq.add_separator()
        MenuArq.add_command(label = "Sair", command = Wnd.quit)
        MenuBar.add_cascade(label = "Arquivo", menu = MenuArq)

        MenuSobre = Menu(MenuBar, tearoff = 0)
        MenuSobre.add_command(label = "Fonte Tipográfica ©", command = self.AboutTI)
        MenuBar.add_cascade(label = "Sobre...", menu = MenuSobre)

        Wnd.config(menu = MenuBar)

################################################################################################################################################
mainWindow = Tk()
Window(mainWindow)
mainWindow.mainloop()