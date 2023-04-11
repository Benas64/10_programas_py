# Nesse programa, o usuário digita a velocidade de download e upload de sua internet e o programa calcula o tempo que levaria para baixar um arquivo de 1GB e 5GB
# Código por: Benicio Macedo Silva 

# Importando biblioteca Tkinter
import tkinter
from tkinter import*

# Importando a boblioteca Pillow
from PIL import ImageTk, Image

# cores
cor0= "#00100A" #preta
cor1= "#F2FBF7" #branca
cor2= "#FF0000" #vermelha
cor3= "#00FF00" #verde
cor4= "#FFFF00" #amarela
cor5= "#0A0AE0" #azul


# Criando a janela
janela= Tk ()
janela.title ("Medidor de velocidade de internet")
janela.geometry ("350x200")
janela.configure (bg= cor1)
janela.resizable(width= False, height= False)

#divindo a janela em dois frames
frame_logo= Frame (janela,width=350,height=60, bg= cor0)
frame_logo.place (relx= 0.01, rely= 0.01, relwidth= 0.98, relheight= 0.98)
frame_logo.grid(row=1, column=0,padx=1, pady=0, sticky=W+E+N+S)

frame_corpo= Frame (janela,width=350,height=140, bg= cor1)
frame_corpo.place (relx= 0.01, rely= 0.01, relwidth= 0.98, relheight= 0.98)
frame_corpo.grid(row=2, column=0,padx=1, pady=0, sticky=W+E+N+S)

# Criando o logo

imagem= ImageTk.PhotoImage(Image.open("speed.png"))
label= Label(frame_logo, image=imagem)
label.place(relx= 0.01, rely= 0.01, relwidth= 0.98, relheight= 0.98)




janela=mainloop()

# Criando a função



