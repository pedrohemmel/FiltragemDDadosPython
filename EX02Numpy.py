import numpy as np

##Criando as arrays que vão auxilar na filtragem dos dados
arrAnos = np.array([])
arrAlturas = np.array([])
quantidadeAlturasFiltradas = 0
somaTotalAlturasFiltradas = 0
mediaAlturasFiltradas = 0.0

##Resgatando todos elementos dos arquivos e formatando os mesmos
with open("/Users/pedrodeoliveira/Downloads/altura.txt", "r") as alturas:
    for altura in alturas:
        cont = 0
        alturaEstruturada = ""
        #Formatando as alturas com a quantidade de caracteres manipulada
        while cont <= 3:
            alturaEstruturada = alturaEstruturada + altura[cont]
            cont = cont + 1
        arrAlturas = np.append(arrAlturas, alturaEstruturada)
        
with open("/Users/pedrodeoliveira/Downloads/anos.txt", "r") as anos:
    for ano in anos:
        cont = 0
        anoEstruturado = ""
        #Formatando os anos com a quantidade de caracteres manipulada
        while cont <= 4:
            if(ano[cont] != "."): 
                anoEstruturado = anoEstruturado + ano[cont]
                
            cont = cont + 1
        arrAnos = np.append(arrAnos, anoEstruturado)
            

##Estruturando a lógica de filtragem dos dados
cont = 0

for arrAno in arrAnos:
    #Estrutura condicional para filtrar as alturas de quem nasceu nos seguintes anos
    if int(arrAno) >= 1998 and int(arrAno) <= 2005:
        somaTotalAlturasFiltradas = somaTotalAlturasFiltradas + float(arrAlturas[cont])
        quantidadeAlturasFiltradas = quantidadeAlturasFiltradas + 1
    cont = cont + 1

mediaAlturasFiltradas = somaTotalAlturasFiltradas / quantidadeAlturasFiltradas

print("A média das alturas de quem nasceu entre 1998 e 2005 é ", round(mediaAlturasFiltradas, 2)) 
    




