num1=1
num2=1
i=1

numero=int(input("Ingrese cantidad de nuemros de la serie de Fibonacci: "))
while numero <= 0:
  print("Ingrese un valor mayor a 0")
  numero=int(input("Ingrese cantidad de nuemros de la serie de Fibonacci: "))

while i <= numero :
    print(num1, end=" ")
    total=num1+num2
    num1=num2
    num2=total
    i += 1