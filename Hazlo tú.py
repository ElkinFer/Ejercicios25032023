print ("Bienvenido a la materia de programación")

notas = 0
cantnotas = 0
for i in range(1,5,1):
    talleres = float(input("Ingrese la nota obtenida en el taller entre 1.0 y 5.0: "))
    notas = notas + 1
    cantnotas = cantnotas + talleres/4
    print (cantnotas)
    if 0.0<=cantnotas<=2.9:
        print ("Reprobaste la asignatura")
    else:
        print("Aprobaste con buenos resultados")
    
    
    
    
    
    
    
    
#0 2.9 reprobo asugnatura, 3 y 4 pasaste raspando, +4 aprobaste con buenos resultados
    