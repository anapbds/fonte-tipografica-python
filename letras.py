from tkinter import *
import numpy as np
import math

def letra0():
    pontos=np.array([[10,80,0,1],
                    [10,20,0,1],
                    [25,10,0,1],
                    [50,10,0,1],
                    [65,20,0,1],
                    [65,80,0,1],
                    [50,90,0,1],
                    [25,90,0,1],# fim---meio
                    [25,65,0,1],
                    [25,35,0,1],
                    [35,25,0,1],
                    [40,25,0,1],
                    [50,35,0,1],
                    [50,65,0,1],
                    [40,75,0,1],
                    [35,75,0,1]])
    n_pontos=np.array([8,8,0,75])
    return (pontos,n_pontos)

def letra1():
    pontos=np.array([[10,40,0,1],
                  [40,10,0,1],
                  [60,10,0,1],
                  [60,90,0,1],
                  [40,90,0,1],
                  [40,35,0,1],
                  [25,50,0,1]])
    n_pontos=np.array([7,0,0,70]) # pontos ao redor, pontos em uma das partes de dentro, pontos em outra das partes de dentro, xmáximo
    return (pontos,n_pontos)

def letra2():
    pontos=np.array([[10,10,0,1],
                    [50,10,0,1],
                    [50,60,0,1],
                    [65,80,0,1],
                    [60,90,0,1],
                    [50,85,0,1],
                    [40,90,0,1],
                    [10,90,0,1],
                    [10,55,0,1],
                    [35,55,0,1],
                    [35,25,0,1],
                    [10,25,0,1],# fim---meio
                    [25,70,0,1],
                    [35,70,0,1],
                    [35,75,0,1],
                    [25,75,0,1]])
    n_pontos=np.array([12,4,0,75]) # pontos ao redor, pontos em uma das partes de dentro, pontos em outra das partes de dentro, xmáximo
    return (pontos,n_pontos)

def letra3():
    pontos=np.array([[10,10,0,1],
                  [60,10,0,1],
                  [60,90,0,1],
                  [10,90,0,1],
                  [10,75,0,1],
                  [45,75,0,1],
                  [45,55,0,1],
                  [20,55,0,1],
                  [20,40,0,1],
                  [45,40,0,1],
                  [45,25,0,1],
                  [10,25,0,1]])
    n_pontos=np.array([12,0,0,70]) # pontos ao redor, pontos em uma das partes de dentro, pontos em outra das partes de dentro, xmáximo
    return (pontos,n_pontos)

def letra4():
    pontos=np.array([[10,10,0,1],
                  [25,10,0,1],
                  [25,40,0,1],
                  [45,40,0,1],
                  [45,10,0,1],
                  [60,10,0,1],
                  [60,90,0,1],
                  [45,90,0,1],
                  [45,55,0,1],
                  [10,55,0,1]])
    n_pontos=np.array([10,0,0,70]) # pontos ao redor, pontos em uma das partes de dentro, pontos em outra das partes de dentro, xmáximo
    return (pontos,n_pontos)

def letra5():
    pontos=np.array([[10,10,0,1],
                  [60,10,0,1],
                  [60,25,0,1],
                  [25,25,0,1],
                  [25,35,0,1],
                  [60,35,0,1],
                  [60,90,0,1],
                  [10,90,0,1], 
                  [10,75,0,1],
                  [45,75,0,1],
                  [45,50,0,1],
                  [10,50,0,1]])
    n_pontos=np.array([12,0,0,70]) # pontos ao redor, pontos em uma das partes de dentro, pontos em outra das partes de dentro, xmáximo
    return (pontos,n_pontos)

def letra6():
    pontos=np.array([[10,10,0,1],
                  [60,10,0,1],
                  [60,25,0,1],
                  [25,25,0,1],
                  [25,55,0,1],
                  [60,55,0,1],
                  [60,90,0,1],
                  [10,90,0,1], #fim
                  [25,67,0,1],
                  [45,67,0,1],
                  [45,78,0,1],
                  [25,78,0,1]])
    n_pontos=np.array([8,4,0,70]) # pontos ao redor, pontos em uma das partes de dentro, pontos em outra das partes de dentro, xmáximo
    return (pontos,n_pontos)

def letra7():
    pontos=np.array([[10,10,0,1],
                  [55,10,0,1],
                  [55,40,0,1],
                  [70,40,0,1],
                  [70,55,0,1],
                  [55,55,0,1],
                  [55,90,0,1],
                  [40,90,0,1],
                  [40,55,0,1],
                  [25,55,0,1],
                  [25,40,0,1],
                  [40,40,0,1],
                  [40,25,0,1],
                  [10,25,0,1]])
    n_pontos=np.array([17,0,0,80]) # pontos ao redor, pontos em uma das partes de dentro, pontos em outra das partes de dentro, xmáximo
    return (pontos,n_pontos)

def letra8():
    pontos=np.array([[10,10,0,1],
                  [60,10,0,1],
                  [60,40,0,1],
                  [50,50,0,1],
                  [60,60,0,1],
                  [60,90,0,1],
                  [10,90,0,1],
                  [10,60,0,1],
                  [20,50,0,1],
                  [10,40,0,1],#fim
                  [25,25,0,1],
                  [45,25,0,1],
                  [45,40,0,1],
                  [25,40,0,1],# meio
                  [25,60,0,1],
                  [45,60,0,1],
                  [45,75,0,1],
                  [25,75,0,1]])
    n_pontos=np.array([10,4,4,70]) # pontos ao redor, pontos em uma das partes de dentro, pontos em outra das partes de dentro, xmáximo
    return (pontos,n_pontos)

def letra9():
    pontos=np.array([[10,10,0,1],
                  [60,10,0,1],
                  [60,90,0,1],
                  [45,90,0,1],
                  [45,60,0,1],
                  [10,60,0,1], #fim
                  [25,25,0,1],
                  [45,25,0,1],
                  [45,45,0,1],
                  [25,45,0,1]])
    n_pontos=np.array([6,4,0,70]) # pontos ao redor, pontos em uma das partes de dentro, pontos em outra das partes de dentro, xmáximo
    return (pontos,n_pontos)

def letraA():
    pontos=np.array([[10,90,0,1],
                    [35,10,0,1],
                    [65,10,0,1],
                    [90,90,0,1],
                    [70,90,0,1],
                    [64,70,0,1],
                    [36,70,0,1],
                    [30,90,0,1],# fim---meio
                    [50,30,0,1],
                    [60,60,0,1],
                    [40,60,0,1]])
    n_pontos=np.array([8,3,0,100]) # pontos ao redor, pontos em uma das partes de dentro, pontos em outra das partes de dentro, xmáximo
    return (pontos,n_pontos)

def letraB():
    pontos=np.array([[10,90,0,1],
                    [10,10,0,1],
                    [50,10,0,1],
                    [60,20,0,1],
                    [60,30,0,1],
                    [35,40,0,1],
                    [60,50,0,1],
                    [60,80,0,1],
                    [50,90,0,1],# fim---meio
                    [25,30,0,1],
                    [40,30,0,1],
                    [40,20,0,1],
                    [25,20,0,1],### segunda parte
                    [25,60,0,1],
                    [45,60,0,1],
                    [45,80,0,1],
                    [25,80,0,1]])
    n_pontos=np.array([9,4,4,70])
    return (pontos,n_pontos)

def letraC():
    pontos=np.array([[10,80,0,1],
                    [10,20,0,1],
                    [20,10,0,1],
                    [65,10,0,1],
                    [80,20,0,1],
                    [80,35,0,1],
                    [60,25,0,1],
                    [35,25,0,1],
                    [25,35,0,1],
                    [25,65,0,1],
                    [35,75,0,1],
                    [65,75,0,1],
                    [80,65,0,1],
                    [80,80,0,1],
                    [65,90,0,1],
                    [20,90,0,1]])
    n_pontos=np.array([16,0,0,90])
    return (pontos,n_pontos)

def letraD():
    pontos=np.array([[10,90,0,1],
                    [10,10,0,1],
                    [50,10,0,1],
                    [60,20,0,1],
                    [60,80,0,1],
                    [50,90,0,1],# fim---meio
                    [25,20,0,1],
                    [25,75,0,1],
                    [45,75,0,1],
                    [50,70,0,1],
                    [50,25,0,1],
                    [45,20,0,1]])
    n_pontos=np.array([6,6,0,70])
    return (pontos,n_pontos)

def letraE():
    pontos=np.array([[10,90,0,1],
                    [10,10,0,1],
                    [60,10,0,1],
                    [60,20,0,1],
                    [25,20,0,1],
                    [25,40,0,1],
                    [50,40,0,1],
                    [50,50,0,1],
                    [25,50,0,1],
                    [25,80,0,1],
                    [60,80,0,1],
                    [60,90,0,1]])
    n_pontos=np.array([12,0,0,70])
    return (pontos,n_pontos)

def letraF():
    pontos=np.array([[10,90,0,1],
                    [10,10,0,1],
                    [60,10,0,1],
                    [60,20,0,1],
                    [25,20,0,1],
                    [25,40,0,1],
                    [50,40,0,1],
                    [50,50,0,1],
                    [25,50,0,1],
                    [25,90,0,1]])
    n_pontos=np.array([10,0,0,70])
    return (pontos,n_pontos)

def letraG():
    pontos=np.array([[10,80,0,1],
                    [10,20,0,1],
                    [20,10,0,1],
                    [65,10,0,1],
                    [80,20,0,1],
                    [80,35,0,1],
                    [60,25,0,1],
                    [35,25,0,1],
                    [25,35,0,1],
                    [25,65,0,1],
                    [35,75,0,1],
                    [65,75,0,1],
                    [65,65,0,1],
                    [50,65,0,1],
                    [50,50,0,1],
                    [80,50,0,1],
                    [80,80,0,1],
                    [65,90,0,1],
                    [20,90,0,1]])
    n_pontos=np.array([19,0,0,90])
    return (pontos,n_pontos)

def letraH():
    pontos=np.array([[10,90,0,1],
                    [10,10,0,1],
                    [25,10,0,1],
                    [25,40,0,1],
                    [55,40,0,1],
                    [55,10,0,1],
                    [70,10,0,1],
                    [70,90,0,1],
                    [55,90,0,1],
                    [55,55,0,1],
                    [25,55,0,1],
                    [25,90,0,1]])
    n_pontos=np.array([12,0,0,80])
    return (pontos,n_pontos)

def letraI():
    pontos=np.array([[10,90,0,1],
                    [10,10,0,1],
                    [30,10,0,1],
                    [30,90,0,1]])
    n_pontos=np.array([4,0,0,40])
    return (pontos,n_pontos)

def letraJ():
    pontos=np.array([[10,60,0,1],
                    [10,80,0,1],
                    [20,90,0,1],
                    [50,90,0,1],
                    [60,80,0,1],
                    [60,10,0,1],
                    [45,10,0,1],
                    [45,75,0,1],
                    [25,75,0,1],
                    [25,60,0,1]])
    n_pontos=np.array([10,0,0,70])
    return (pontos,n_pontos)

def letrak():
    pontos=np.array([[10,90,0,1],
                    [10,10,0,1],
                    [30,10,0,1],
                    [30,40,0,1],
                    [60,10,0,1],
                    [80,10,0,1],
                    [55,45,0,1],
                    [80,90,0,1],
                    [60,90,0,1],
                    [40,60,0,1],
                    [30,70,0,1],
                    [30,90,0,1]])
    n_pontos=np.array([12,0,0,100])
    return (pontos,n_pontos)
    
def letraL():
    pontos=np.array([[10,90,0,1],
                    [10,10,0,1],
                    [25,10,0,1],
                    [25,75,0,1],
                    [60,75,0,1],
                    [60,90,0,1]])
    n_pontos=np.array([6,0,0,70])
    return (pontos,n_pontos)

def letraM():
    pontos=np.array([[10,90,0,1],
                    [10,10,0,1],
                    [25,10,0,1],
                    [50,55,0,1],
                    [75,10,0,1],
                    [90,10,0,1],
                    [90,90,0,1],
                    [75,90,0,1],
                    [75,40,0,1],
                    [55,90,0,1],
                    [45,90,0,1],
                    [25,40,0,1],
                    [25,90,0,1]])

    n_pontos=np.array([13,0,0,100])
    return (pontos,n_pontos)

def letraN():
    pontos=np.array([[10,90,0,1],
                    [10,10,0,1],
                    [25,10,0,1],
                    [60,60,0,1],
                    [60,10,0,1],
                    [75,10,0,1],
                    [75,90,0,1],
                    [60,90,0,1],
                    [25,40,0,1],
                    [25,90,0,1]])

    n_pontos=np.array([10,0,0,90])
    return (pontos,n_pontos)

def letraO():
    pontos=np.array([[10,80,0,1],
                    [10,20,0,1],
                    [25,10,0,1],
                    [60,10,0,1],
                    [75,20,0,1],
                    [75,80,0,1],
                    [60,90,0,1],
                    [25,90,0,1],# fim---meio
                    [25,65,0,1],
                    [25,35,0,1],
                    [35,25,0,1],
                    [50,25,0,1],
                    [60,35,0,1],
                    [60,65,0,1],
                    [50,75,0,1],
                    [35,75,0,1]])
    n_pontos=np.array([8,8,0,85])
    return (pontos,n_pontos)

def letraP():
    pontos=np.array([[10,90,0,1],
                    [10,10,0,1],
                    [55,10,0,1],
                    [70,20,0,1],
                    [70,40,0,1],
                    [55,50,0,1],
                    [25,50,0,1],
                    [25,90,0,1],# fim---meio
                    [25,25,0,1],
                    [55,25,0,1],
                    [55,35,0,1],
                    [25,35,0,1]])
    n_pontos=np.array([8,4,0,80])
    return (pontos,n_pontos)

def letraQ():
    pontos=np.array([[10,80,0,1],
                    [10,20,0,1],
                    [25,10,0,1],
                    [60,10,0,1],
                    [75,20,0,1],
                    [75,75,0,1],
                    [85,85,0,1],
                    [80,95,0,1],
                    [65,85,0,1],
                    [60,90,0,1],
                    [25,90,0,1],# fim---meio
                    [25,65,0,1],
                    [25,35,0,1],
                    [35,25,0,1],
                    [50,25,0,1],
                    [60,35,0,1],
                    [60,60,0,1],
                    [50,50,0,1],
                    [45,65,0,1],
                    [55,75,0,1],
                    [35,75,0,1]])
    n_pontos=np.array([11,10,0,95])
    return (pontos,n_pontos)

def letraR():
    pontos=np.array([[10,90,0,1],
                    [10,10,0,1],
                    [60,10,0,1],
                    [70,20,0,1],
                    [70,40,0,1],
                    [45,50,0,1],
                    [70,90,0,1],
                    [55,90,0,1],
                    [25,50,0,1],
                    [25,90,0,1],# fim---meio
                    [25,25,0,1],
                    [50,25,0,1],
                    [50,35,0,1],
                    [25,35,0,1]])
    n_pontos=np.array([10,4,0,80])
    return (pontos,n_pontos)

def letraS():
    pontos=np.array([[60,75,0,1],
                  [60,70,0,1],
                  [10,45,0,1],
                    [10,20,0,1],
                    [20,10,0,1],
                    [65,10,0,1],
                    [80,20,0,1],
                    [80,35,0,1],
                    [60,25,0,1],
                    [35,25,0,1],
                    [25,35,0,1],
                    [80,60,0,1],
                    [80,80,0,1],
                    [70,90,0,1],
                    [20,90,0,1],
                    [10,80,0,1],
                    [10,65,0,1],
                    [20,65,0,1],
                    [30,75,0,1]])
    n_pontos=np.array([19,0,0,90])
    return (pontos,n_pontos)

def letraT():
    pontos=np.array([[10,10,0,1],
                    [85,10,0,1],
                    [85,25,0,1],
                    [55,25,0,1],
                    [55,90,0,1],
                    [40,90,0,1],
                    [40,25,0,1],
                    [10,25,0,1]])
    n_pontos=np.array([8,0,0,95])
    return (pontos,n_pontos)

def letraU():
    pontos=np.array([[10,10,0,1],
                  [10,80,0,1],
                  [20,90,0,1],
                  [60,90,0,1],
                  [70,80,0,1],
                  [70,10,0,1],
                  [55,10,0,1],
                  [55,70,0,1],
                  [50,75,0,1],
                  [30,75,0,1],
                  [25,70,0,1],
                  [25,10,0,1]])
    n_pontos=np.array([12,0,0,80])
    return (pontos,n_pontos)

def letraV():
    pontos=np.array([[10,10,0,1],
                  [30,90,0,1],
                  [50,90,0,1],
                  [70,10,0,1],
                  [50,10,0,1],
                  [40,65,0,1],
                  [30,10,0,1]])
    n_pontos=np.array([7,0,0,80])
    return (pontos,n_pontos)

def letraX():
    pontos=np.array([[10,10,0,1],
                  [25,10,0,1],
                  [45,40,0,1],
                  [65,10,0,1],
                  [80,10,0,1],
                  [60,50,0,1],
                  [80,90,0,1],
                  [65,90,0,1],
                  [45,60,0,1],
                  [25,90,0,1],
                  [10,90,0,1],
                  [30,50,0,1]])
    n_pontos=np.array([12,0,0,90])
    return (pontos,n_pontos)

def letraY():
    pontos=np.array([[10,10,0,1],
                  [30,60,0,1],
                  [30,90,0,1],
                  [50,90,0,1],
                  [50,60,0,1],
                  [70,10,0,1],
                  [55,10,0,1],
                  [40,45,0,1],
                  [25,10,0,1]])
    n_pontos=np.array([9,0,0,80])
    return (pontos,n_pontos)

def letraZ():
    pontos=np.array([[10,10,0,1],
                  [90,10,0,1],
                  [90,25,0,1],
                  [40,75,0,1],
                  [90,75,0,1],
                  [90,90,0,1],
                  [10,90,0,1],
                  [10,75,0,1],
                  [60,25,0,1],
                  [10,25,0,1]])
    n_pontos=np.array([10,0,0,100])
    return (pontos,n_pontos)

def imprime_Letra2D(m_ponto, qtde_pontos,qtde_letras):### organizar a quantidade das letras para fazer um for
    for i in range(qtde_pontos[0]-1):
        canvas.create_line(m_ponto[i][0],m_ponto[i][1],m_ponto[i+1][0],m_ponto[i+1][1], fill = "black",width=2)
    canvas.create_line(m_ponto[i+1][0],m_ponto[i+1][1],m_ponto[0][0],m_ponto[0][1], fill = "black",width=2)
    if qtde_pontos[1]>0:
        a= qtde_pontos[0]
        for i in range(a,a+qtde_pontos[1]-1):
            canvas.create_line(m_ponto[i][0],m_ponto[i][1],m_ponto[i+1][0],m_ponto[i+1][1], fill = "black",width=2)
        canvas.create_line(m_ponto[i+1][0],m_ponto[i+1][1],m_ponto[a][0],m_ponto[a][1], fill = "black",width=2)
         


#---------------------------------------------------------------------------------------------------------------

janela=Tk()

# Set the size of the tkinter window
janela.geometry("500x500")

# Create a canvas widget
canvas=Canvas(janela, width=500, height=500)
canvas.pack()

# Add a line in canvas widget

m_ponto=np.array([[10,10,0,1],
                    [50,10,0,1],
                    [50,60,0,1],
                    [65,80,0,1],
                    [60,90,0,1],
                    [50,85,0,1],
                    [40,90,0,1],
                    [10,90,0,1],
                    [10,55,0,1],
                    [35,55,0,1],
                    [35,25,0,1],
                    [10,25,0,1],# fim---meio
                    [25,70,0,1],
                    [35,70,0,1],
                    [35,75,0,1],
                    [25,75,0,1]])
   # qtde_pontos=[9,4,4]
#    return (pontos,n_pontos)
#def imprime_Letra2D(m_ponto, qtde_pontos):
maximo = m_ponto[0][0]
for i in range(11):
    if(maximo< m_ponto[i+1][0]):
        maximo= m_ponto[i+1][0]
    canvas.create_line(m_ponto[i][0],m_ponto[i][1],m_ponto[i+1][0],m_ponto[i+1][1], fill = "black",width=2)
canvas.create_line(m_ponto[i+1][0],m_ponto[i+1][1],m_ponto[0][0],m_ponto[0][1], fill = "black",width=2)
fim=maximo
if 3>0:
        a= 4
        for i in range(12,15):
            canvas.create_line(m_ponto[i][0],m_ponto[i][1],m_ponto[i+1][0],m_ponto[i+1][1], fill = "black",width=2)
        canvas.create_line(m_ponto[i+1][0],m_ponto[i+1][1],m_ponto[12][0],m_ponto[12][1], fill = "black",width=2)
        
### somar o fim da outra letra e imprimir a nova
m_ponto=np.array([[10,10,0,1],
                  [25,10,0,1],
                  [45,40,0,1],
                  [65,10,0,1],
                  [80,10,0,1],
                  [60,50,0,1],
                  [80,90,0,1],
                  [65,90,0,1],
                  [45,60,0,1],
                  [25,90,0,1],
                  [10,90,0,1],
                  [30,50,0,1]])
   # n_pontos=np.array([12,0,0])
maximo = 0
for i in range(0,11):
    if(maximo< m_ponto[i+1][0]):
        maximo= m_ponto[i+1][0]
    canvas.create_line(fim+m_ponto[i][0],m_ponto[i][1],fim+m_ponto[i+1][0],m_ponto[i+1][1], fill = "black",width=2)
canvas.create_line(fim+m_ponto[i+1][0],m_ponto[i+1][1],fim+m_ponto[0][0],m_ponto[0][1], fill = "black",width=2)
fim+= maximo +10

m_ponto=np.array([[10,10,0,1],
                  [60,10,0,1],
                  [60,25,0,1],
                  [25,25,0,1],
                  [25,35,0,1],
                  [60,35,0,1],
                  [60,90,0,1],
                  [10,90,0,1], 
                  [10,75,0,1],
                  [45,75,0,1],
                  [45,50,0,1],
                  [10,50,0,1]])
maximo=0
for i in range(0,11):
    if(maximo< m_ponto[i+1][0]):
        maximo= m_ponto[i+1][0]
    canvas.create_line(fim+m_ponto[i][0],m_ponto[i][1],fim+m_ponto[i+1][0],m_ponto[i+1][1], fill = "black",width=2)
canvas.create_line(fim+m_ponto[i+1][0],m_ponto[i+1][1],fim+m_ponto[0][0],m_ponto[0][1], fill = "black",width=2)


janela.mainloop()

