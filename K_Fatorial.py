import sys

outroNum = "Sim" #Condição para rodar o programa
print ("Neste programa vamos calcular o valor de k!")

while outroNum in ("Sim", "S", "sim", "s"):
    print ("Qual o valor de K?")
    k_str = input () #Lê a entrada como String
    k_int = int(k_str) #Converte a entrada para Integer
        
    k_fat = 1
    i = 1

    while i <= k_int: #Calcula k!
          k_fat = k_fat*i
          i = i+1

    print (k_fat)
          
    print ("Deseja calcular outro número?")
    outroNum = input ()

print ("Então tchau!")
sys.exit ()
