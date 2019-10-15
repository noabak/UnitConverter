print(" *** Bienvenido al conversor de kms a millas ***")
kilometros=0
millas=0
repetir= True

while repetir== True:
    kilometros= int(input("Por favor introducir la cantidad en Kilómetros:"))
    print(kilometros,"km = ",kilometros*0.621371,"millas")
    rep= input("Desea convertir otra cantidad?, escribir 'Y' o 'N':")
    if rep.upper()=="N":
        repetir= False
        print("Hasta la próxima!")
        break


