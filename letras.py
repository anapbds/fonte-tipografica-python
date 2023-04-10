from tkinter import *
import numpy as np
import math

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
                    [60,10,0,1],
                    [70,20,0,1],
                    [30,20,0,1],
                    [20,30,0,1],
                    [20,70,0,1],
                    [30,80,0,1],
                    [60,80,0,1],
                    [70,70,0,1],
                    [70,80,0,1],
                    [60,90,0,1],
                    [20,90,0,1]])
    n_pontos=np.array([14,0,0,80])
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

def letraL():
    pontos=np.array([[10,90,0,1],
                    [10,10,0,1],
                    [25,10,0,1],
                    [25,75,0,1],
                    [60,75,0,1],
                    [60,90,0,1]])
    n_pontos=np.array([6,0,0,70])
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

m_ponto=np.array([[10,90,0,1],
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
   # qtde_pontos=[9,4,4]
#    return (pontos,n_pontos)
#def imprime_Letra2D(m_ponto, qtde_pontos):
for i in range(8):
    canvas.create_line(m_ponto[i][0],m_ponto[i][1],m_ponto[i+1][0],m_ponto[i+1][1], fill = "black",width=2)
canvas.create_line(m_ponto[i+1][0],m_ponto[i+1][1],m_ponto[0][0],m_ponto[0][1], fill = "black",width=2)
fim=m_ponto[i+1][0]+10
if 3>0:
        a= 9
        for i in range(a,a+8-1):
            canvas.create_line(m_ponto[i][0],m_ponto[i][1],m_ponto[i+1][0],m_ponto[i+1][1], fill = "black",width=2)
        canvas.create_line(m_ponto[i+1][0],m_ponto[i+1][1],m_ponto[a][0],m_ponto[a][1], fill = "black",width=2)

### somar o fim da outra letra e imprimir a nova
m_ponto=np.array([[10,90,0,1],
                    [10,10,0,1],
                    [70,10,0,1],
                    [70,20,0,1],
                    [25,20,0,1],
                    [25,40,0,1],
                    [60,40,0,1],
                    [60,50,0,1],
                    [25,50,0,1],
                    [25,80,0,1],
                    [70,80,0,1],
                    [70,90,0,1]])
   # n_pontos=np.array([12,0,0])
for i in range(0,11):
    canvas.create_line(fim+m_ponto[i][0],m_ponto[i][1],fim+m_ponto[i+1][0],m_ponto[i+1][1], fill = "black",width=2)
canvas.create_line(fim+m_ponto[i+1][0],m_ponto[i+1][1],fim+m_ponto[0][0],m_ponto[0][1], fill = "black",width=2)
fim+= m_ponto[i][0] +10

m_ponto=np.array([[10,90,0,1],
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

for i in range(0,11):
    canvas.create_line(fim+m_ponto[i][0],m_ponto[i][1],fim+m_ponto[i+1][0],m_ponto[i+1][1], fill = "black",width=2)
canvas.create_line(fim+m_ponto[i+1][0],m_ponto[i+1][1],fim+m_ponto[0][0],m_ponto[0][1], fill = "black",width=2)


janela.mainloop()

