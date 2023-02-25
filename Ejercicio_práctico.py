hombre = 0
mujer = 0
acum = 0 
for i in range(1,11,1):
    
    genero = int(input("Ingrese 1 para hombre o 2 para mujer "))
    if genero==1:
        hombre = hombre + 1
    else:
        mujer = mujer + 1
    
    cantper = hombre+mujer
        
print("Mujeres = ", mujer)
print ("Hombres = ", hombre)
print ("Cantidad de personas en el grupo=",cantper)
        