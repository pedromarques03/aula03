nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))
nota3 = float(input("Digite sua terceira nota:"))
media = nota1+nota2+nota3/3
print (f"sua media é {media}")
if  media>=7 :
    print ("aprovado")
else :
    if  media<=4 :
        print ("reprovado")
    else :
        print ("recuperacao")