from tkinter import *
from tkinter import messagebox
#import letras

class Window:
    def __init__(self, Wnd):
        # Configurações da tela 
        Wnd.title("Trabalho CG - 2022")
        Wnd.minsize(width = "700", height = "500")
        self.inputs(Wnd)
        self.framesTela(Wnd)
        self.CreateMenu(Wnd)

    def inputs(self, Wnd):
        # input da string
        Label(Wnd, text='Digite a String (max. 5 letras):').grid(row=0)

        #input comprimento dos poliedros (dimensão de z)
        Label(Wnd, text='Comprimento dos poliedros:').grid(row=1)
        e1 = Entry(Wnd)
        e2 = Entry(Wnd)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        btn = Button(Wnd, text="Ok")
        btn.grid(row=1, column=2)

    def framesTela(self,Wnd): #interface das 3 viewports (frente, lateral e topo)
        fonte = ("Roboto", "10", "bold")

        self.FrameFrente = LabelFrame(Wnd, bg='#c7cce7', text = "Frente ", font = fonte)
        self.FrameFrente.grid(row=3, column=0, columnspan=1, ipadx= 180 , ipady= 140, padx= 1, pady=5)

        self.FrameLateral = LabelFrame(Wnd, bg='#c7cce7', text = "Lateral", font = fonte)
        self.FrameLateral.grid(row=3, column=1, columnspan=1, ipadx= 180 , ipady= 140, padx= 1, pady=5)

        self.FrameTopo = LabelFrame(Wnd, bg='#c7cce7', text = "Topo ", font = fonte) 
        self.FrameTopo.grid(row=4, column=0, columnspan=1, ipadx= 180 , ipady= 140, padx= 1, pady=1)

        # 4ª viewport projeção perspectiva ou paralela 
        self.FramePerspectiva = LabelFrame(Wnd, bg='#c7cce7', text = "Perspectiva", font = fonte)
        self.FramePerspectiva.grid(row=4, column=1, columnspan=1, ipadx= 180 , ipady= 140, padx= 1, pady=1)

        self.FrameOpcoes = LabelFrame(Wnd, bg='#c7cce7', text="Menu - Opções", font = fonte)
        self.FrameOpcoes.grid(row=0, column=2, rowspan=100, ipadx=100, ipady=308)

    def ClearCanvas(self):
        self.canvas.delete("all")

    def AboutTI(self):
        messagebox.showinfo(title = "Sobre...", message = "Trabalho de CG feito pelas alunas Alessandra e Ana Paula")

    def CreateMenu(self, Wnd) :
        MenuBar = Menu(Wnd)

        MenuArq = Menu(MenuBar, tearoff = 0)
        MenuArq.add_command(label = "Novo") #adicionar funcao comando
        MenuArq.add_command(label = "Salvar") #adicionar funcao comando
        MenuArq.add_command(label = "Limpar", command = self.ClearCanvas)
        MenuArq.add_separator()
        MenuArq.add_command(label = "Sair", command = Wnd.quit)
        MenuBar.add_cascade(label = "Arquivo", menu = MenuArq)

        MenuSobre = Menu(MenuBar, tearoff = 0)
        MenuSobre.add_command(label = "Fonte Tipográfica ©", command = self.AboutTI)
        MenuBar.add_cascade(label = "Sobre...", menu = MenuSobre)

        # botão salvar e de abrir outras cenas

        Wnd.config(menu = MenuBar)

    def Transformacoes(self, Wnd):
        #opções de transformações geo.
        print("a")

################################################################################################################################################
mainWindow = Tk()
Window(mainWindow)
mainWindow.mainloop()