ciudad = str(input("INGRESA LA CIUDAD DONDE NACISTE: "))
age= int (input("INGRESA TU EDAD:  "))

if(age >= 18):
    #msg= "Esta persona tiene la edad: " str(age) + " puede votar en  " + ciudad
    print(f'Esta persona tiene la edad de {age} puede votar en la ciudad de {ciudad}')
else:
    print("Esta persona no tiene la edad para votar")
