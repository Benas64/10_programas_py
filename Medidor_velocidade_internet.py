# Nesse programa, o usuário digita a velocidade de download e upload de sua internet e o programa calcula o tempo que levaria para baixar um arquivo de 1GB e 5GB
# Código por: Benicio Macedo Silva 

# Importando biblioteca Tkinter
import tkinter
from tkinter import*

# Importando a boblioteca Pillow
from PIL import ImageTk, Image

# Importando a biblioteca speedtest
import speedtest


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
frame_logo= Frame (janela,width=350,height=60, bg= cor1)
frame_logo.place (relx= 0.01, rely= 0.01, relwidth= 0.98, relheight= 0.98)
frame_logo.grid(row=1, column=0,padx=1, pady=0, sticky=W+E+N+S)

frame_corpo= Frame (janela,width=350,height=140, bg= cor1)
frame_corpo.place (relx= 0.01, rely= 0.01, relwidth= 0.98, relheight= 0.98)
frame_corpo.grid(row=2, column=0,padx=1, pady=0, sticky=W+E+N+S)

# Criando o logo

imagem= ImageTk.PhotoImage(Image.open("speed.png"))
label= Label(frame_logo,image=imagem)
l_logo_imagem= Label(frame_logo,height=60,image=imagem,compound=LEFT,padx=10, bg= cor1, fg= cor0, font= "Arial 10 bold")
l_logo_imagem.place(x=20, y=0)

l_logo_texto= Label(frame_logo,text="Teste de velocidade de internet",height=60,image=imagem,compound=LEFT,padx=10,anchor=NE, bg= cor1, fg= cor0, font= "Arial 10 bold")
l_logo_texto.place(x=75, y=10)

l_logo_linha= Label(frame_logo,width=350,compound=LEFT,padx=10,anchor=NW, bg= cor2, font= "Arial 10 bold")
l_logo_linha.place(x=0, y=57)

# Função para calcular o tempo de download
def teste():
    speed=speedtest.Speedtest()
    download= f"{'{:.2f}'.format(speed.download()/1024/1024)} Mb/s"
    upload= f"{'{:.2f}'.format(speed.upload()/1024/1024)} Mb/s"
    print(download,upload)

    l_download[Text]= download
    l_upload[Text]= upload

# Configurando o frame corpo

l_download= Label(frame_corpo,width=350,compound=LEFT,padx=10,anchor=NW, bg= cor2, font= "Arial 10 bold")
l_download.place(x=0, y=57)

l_upload= Label(frame_corpo,width=350,compound=LEFT,padx=10,anchor=NW, bg= cor2, font= "Arial 10 bold")
l_upload.place(x=0, y=57)


# Importando Biblioca speedtest
import speedtest

speed=speedtest.Speedtest()
download= speed.download()

print("A velocidade de download é: ", download)
janela=mainloop()

# Criando a função



