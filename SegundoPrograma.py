print ("Neste programa, vamos calcular um número inteiro elevado a X, sendo X um número inteiro, também.")
print ("Qual o valor da base?")
baseStr = input()
baseInt = int(baseStr)
print ("Qual o valor do expoente?")
expoenteStr = input()
expoenteInt = int(expoenteStr)
respostaInt = baseInt ** expoenteInt
print ("O resultado de " + baseStr + " elevado à " + expoenteStr + " é " + str(respostaInt))
