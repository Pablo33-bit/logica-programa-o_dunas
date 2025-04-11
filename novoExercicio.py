
# Condicional Composta Multipla
nota= float(input("Qual sua nota?"))
if nota <=0 or nota >10:
    print("ERRO!!!!")
elif nota >= 8:
    print("MISSION SUCESS")
elif nota >=6:
    print("Voce ta indo no caminho certo")
elif nota >= 3:
    print("Tente melhor na proxima vez")
else:
    print("Ta vacilando")
    
nota1 = float(input("Dê uma nota para o filme:"))
nota2= float(input("Dê uma nota para o filme:"))

if nota1 and nota2 <=0 or nota1 and nota2 >100:
    print("Já tá querendo demais né?")
elif nota1 and nota2 >= 90:
    print("Que Filme brabo")
elif nota1 and nota2 >= 80:
    print("Filme Legal")
elif nota1 and nota2 >= 70:
    print("Filme razoavel")
elif nota1 and nota2 >= 60:
    print("Filme ruim")

elif nota1 and nota2 >= 50:
    print("Filme muito ruim")
elif nota1 and nota2 >= 40:
    print("Filme horrivel")
elif nota1 and nota2 >= 30:
    print("Filme insuportavel")
elif nota1 and nota2 >= 20:
    print("Filme insuportavel")
elif nota1 and nota2 >= 10:
    print("Filme insuportavel")
elif nota1 and nota2 >= 0:
    print("Filme insuportavel")

   
