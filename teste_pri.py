
def par(t):
    if t%2 == 0:
        return (f"{t} é par")
    else:
        return "É impar"
numero = int(input("Digite um numero: "))
print (f"{par(numero)}") 
