import os 

def binarioParaDecimal(numeroBinario):
    potencia=0
    base=2
    resultado=0
    numeroLen=len(numeroBinario)
    numeroLen = numeroLen - 1
    
    for x in numeroBinario:
        if x != "0" and  x != "1":
            numeroBinario="Caracter não suportado"
            return numeroBinario

    try:
        while True:
            
            if numeroLen < 0:
                break
            
            numero_inteiro=int(numeroBinario[numeroLen])
            opereção=(base**potencia) * numero_inteiro
            numeroLen-=1
            potencia+=1 
            resultado += opereção
                        
        return resultado
    
    except:
        print("Erro") 
    

def hexadecimalParaDecimal(numeroHexadecimal):
    potencia=0
    base=16
    resultado=0
    numeroLen=len(numeroHexadecimal)
    numeroLen = numeroLen - 1
    listaHexadecimal=[
                    "a", "A", "b", "B",  "c",  "C",  "d",  "D", 
                    "e",  "E", "f",  "F", "0", "1",  "2", "3",  "4",  "5",  "6",  "7",  "8",  "9"
    ]   
     

    resposta = all(x in listaHexadecimal for x in numeroHexadecimal)
    
    if not resposta:
        return "Caractere não suportado"

    

    while True:
        
        if numeroLen < 0:
            break
        
        if numeroHexadecimal[numeroLen] == listaHexadecimal[0] or numeroHexadecimal[numeroLen] == listaHexadecimal[1]:
            numero_inteiro = 10 
        
        elif numeroHexadecimal[numeroLen] == listaHexadecimal[2] or numeroHexadecimal[numeroLen] ==  listaHexadecimal[3]:
            numero_inteiro = 11 
        
        elif numeroHexadecimal[numeroLen] == listaHexadecimal[4] or numeroHexadecimal[numeroLen] ==  listaHexadecimal[5]:
            numero_inteiro = 12 

        elif numeroHexadecimal[numeroLen] == listaHexadecimal[6] or numeroHexadecimal[numeroLen] ==  listaHexadecimal[7]:
            numero_inteiro = 13 
        
        elif numeroHexadecimal[numeroLen] == listaHexadecimal[8] or numeroHexadecimal[numeroLen] ==  listaHexadecimal[9]:
            numero_inteiro = 14 
        
        elif numeroHexadecimal[numeroLen] == listaHexadecimal[10] or numeroHexadecimal[numeroLen] ==  listaHexadecimal[11]:
            numero_inteiro = 15 

        else:
            numero_inteiro=int(numeroHexadecimal[numeroLen])
        
        opereção=(base**potencia) * numero_inteiro
        numeroLen-=1
        potencia+=1 
        resultado += opereção
                    
    return resultado


def octalParaDecimal(numeroOctal):
    potencia=0
    base=8
    resultado=0
    numeroLen=len(numeroOctal)
    numeroLen = numeroLen - 1
    listaOctal=["0", "1", "2", "3", "4", "5", "6", "7"]
    resposta=all(x in listaOctal for x in numeroOctal)

    if not resposta:
        resposta="caracter não suportado"
        return resposta
    
    try:
        while True:
            
            if numeroLen < 0:
                break
            
            numero_inteiro=int(numeroOctal[numeroLen])
            opereção=(base**potencia) * numero_inteiro
            numeroLen-=1
            potencia+=1 
            resultado += opereção
                        
        return resultado
    
    except:
        print("Erro") 


    






