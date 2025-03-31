nome = input("Digite seu nome:")
idade =int(input  ("Digite sua idade:"))
salario =float(input ("Digite seu salario:"))
percentual = float(input ("Digite o percentual:"))
aumento = salario*percentual/100
novosalario = salario+aumento
print (f"{nome}, vote tem {idade} anos. seu salario atual {salario}, voce teve {aumento} de aumento e seu novo salario sera{novosalario:.2f}")