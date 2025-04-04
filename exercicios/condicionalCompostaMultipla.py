nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("DIgite a segunda nota:"))

media = (nota1 + nota2 ) / 2
print (media)
if media >=6:
    print("Aprovado")
elif media >= 4:
    print("Recuperaçao")
else: 
    print("Reprovado")
#Condicional Composta Multipla
time1 = float(input("Digite o numero de gols do time 1:"))
time2 = float(input("Digite o numero de gols do time 2:"))
if time1 > time2 :
    print("Time 1 venceu")
elif time1 < time2 :
    print("Time 2 venceu")
else:
    print("Empate")
