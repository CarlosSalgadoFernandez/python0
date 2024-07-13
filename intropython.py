print("hola mundo")
print("ejercicios")
print("1 Minimo dos números a y b")
a=2
b=4
def minimo(a,b):
    print("El número menor es",min(a,b))
minimo(a,b)

print("2 revertir una cadena ")
cadena=input("escribe un texto: ")
def alreves(texto):
    letras = texto.split(' ')
    otrotexto = ' '.join(reversed(letras))
    print(otrotexto)

alreves(cadena)