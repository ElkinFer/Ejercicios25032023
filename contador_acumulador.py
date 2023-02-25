count = 0 #contador
total = 0 #acumulador
for i in range(1,6,1):
    #Instrucciones que se van a repetir
    precio = int(input("Ingrese un valor: "))
    cant = int(input("Ingrese la cantidad: "))
    count = count+1 #iniciar el contador dentro del ciclo
    subtotal = precio*cant
    print("subTotal = ", subtotal)
    total = total+subtotal
print("Se registraron",count,"referencias")
print("El total a pagar es = ",total)
bill = int(input("Ingrese el valor del billete: "))
cambio = bill-total    

print ("El billete recibido es= ",bill)  
print("Su cambio es= ", cambio)
 