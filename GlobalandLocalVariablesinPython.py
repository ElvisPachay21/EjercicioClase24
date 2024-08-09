#Scope (o alcance) de variables
# 1. Scope Global

valor_numerico = 80

def PresentarValorNumerico():
    print(valor_numerico)
def PresentarValorNumericoConMensajeAdicional():
    print("El valor es:", valor_numerico)

def PresentarUnNuevoValor():
    print(100)
    
    mensajeHolamundo = "Hola Mundo"
    
    def MuestraHolaMundo():
        print("Esta es una ejecucion desde la funcion interna")
        print(mensajeHolamundo)
        
    MuestraHolaMundo()
    print(mensajeHolamundo)

PresentarValorNumerico()
PresentarValorNumericoConMensajeAdicional()

