from tkinter import *
import Conversão_de_Número as sp


def binario():
    textoInserir=Label(app,text="Insira o número Binário aqui:",background="#2fb",foreground="#009",anchor=W)
    textoInserir.place(x=150,y=50,width=160,height=20)
    receberNumero=Entry(app)
    receberNumero.place(x=150,y=70,width=200,height=20)

    textoResultado=Label(app,text="Número decimal:",background="#2fb",foreground="#009",anchor=W)
    textoResultado.place(x=150,y=110,width=113,height=20)
    resultado=Entry(app)
    resultado.place(x=150,y=130,width=200,height=20)
    
    def executarComando():
        numeroCalcular = receberNumero.get()
        respostaCalcular = sp.binarioParaDecimal(numeroCalcular)
        resultado.delete(0, END)
        resultado.insert(0,str(respostaCalcular))
        return respostaCalcular
    
    botao=Button(app,text="Converter",command=executarComando)
    botao.place(x=150,y=160,width=100,height=20) 

def hexadecimal():
    textoInserir=Label(app,text="Insira o número Hexadecimal aqui:",background="#2fb",foreground="#009",anchor=W)
    textoInserir.place(x=150,y=50,width=160,height=20)
    receberNumero=Entry(app)
    receberNumero.place(x=150,y=70,width=200,height=20)

    textoResultado=Label(app,text="Número decimal:",background="#2fb",foreground="#009",anchor=W)
    textoResultado.place(x=150,y=110,width=113,height=20)
    resultado=Entry(app)
    resultado.place(x=150,y=130,width=200,height=20)
    
    def executarComando():
        numeroCalcular = receberNumero.get()
        respostaCalcular = sp.hexadecimalParaDecimal(numeroCalcular)
        resultado.delete(0, END)
        resultado.insert(0,str(respostaCalcular))
        return respostaCalcular
    
    botao=Button(app,text="Converter",command=executarComando)
    botao.place(x=150,y=160,width=100,height=20)

def octal():
    textoInserir=Label(app,text="Insira o número octal aqui:",background="#2fb",foreground="#009",anchor=W)
    textoInserir.place(x=150,y=50,width=160,height=20)
    receberNumero=Entry(app)
    receberNumero.place(x=150,y=70,width=200,height=20)

    textoResultado=Label(app,text="Número decimal:",background="#2fb",foreground="#009",anchor=W)
    textoResultado.place(x=150,y=110,width=113,height=20)
    resultado=Entry(app)
    resultado.place(x=150,y=130,width=200,height=20)
    
    def executarComando():
        numeroCalcular = receberNumero.get()
        respostaCalcular = sp.octalParaDecimal(numeroCalcular)
        resultado.delete(0, END)
        resultado.insert(0,str(respostaCalcular))
        return respostaCalcular
    
    botao=Button(app,text="Converter",command=executarComando)
    botao.place(x=150,y=160,width=100,height=20)
    
def claro():
    global corFundo
    corFundo="#dde"
    app.configure(background=corFundo)
def escuro():
    global corFundo
    corFundo="#222"
    app.configure(background=corFundo)
    
app=Tk()
app.title("Números posicionais")
app.geometry("500x300")
corFundo="#dde"
app.configure(background=corFundo)

binario()

barraMenu=Menu(app)
sistemasPosionais=Menu(barraMenu,tearoff=0)
sistemasPosionais.add_command(label="Binário",command=binario)
sistemasPosionais.add_command(label="Hexadecimal",command=hexadecimal)
sistemasPosionais.add_command(label="Octal",command=octal)
barraMenu.add_cascade(label="Sistemas posicionais",menu=sistemasPosionais) 

tema=Menu(barraMenu,tearoff=0)
tema.add_command(label="Modo Claro",command=claro)
tema.add_command(label="Modo Escuro", command=escuro)
barraMenu.add_cascade(label="Configuração",menu=tema)

app.config(menu=barraMenu)
app.mainloop()