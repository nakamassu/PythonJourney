import sys, random

#Introdução e Condição Inicial
A = "Sim" #Variável de condição para o programa do sorteio rodar
print ("Neste programa, vamos sortear um ganhador.")
print ("O número de saída é o ID do respondente Ganhador")
print ("")

#Usuário indica quantos respondentes conseguiu na Pesquisa
print ("Quantos respondentes vocês conseguiram?") 
Quantidade_Respondentes_STR = input()
Quantidade_Respondentes_INT = int (Quantidade_Respondentes_STR)

#Loop do Programa
while A in ("Sim", "S", "sim", "s"): #Loop para rodar o programa
    print ("")
    Ganhador = random.randint(1, Quantidade_Respondentes_INT) #Sorteia um número aleatório entre 1 e o número de respondentes
    print ("Número sorteado: ", Ganhador)
    print ("")
    print ("Deseja sortear outro número?")
    A = input ()

#Saída Final
print ("Então, o ganhador é o respondente: #", Ganhador)
sys.exit ()
