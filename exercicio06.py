nome1 = input ("Digite o nome do primeiro time:")
time1 = int(input("Quantidade de gol do primeiro time:"))
nome2 = input ("Digite o nome do segundo time:")
time2 = int(input("Quantidade de gol do segundo time:"))
if time1==time2 :
    print ("empatado")
else :
    if time1>time2 :
        print (f"vencedor {nome1}")
    else :
        print (f"vencedor {nome2}")