
def par(t):
    if t%2 == 0:
        return (f"{t} é par")
    else:
        return (f"{t} é impar")
numero = int(input("Digite um numero: "))
print (f"{par(numero)}") 
