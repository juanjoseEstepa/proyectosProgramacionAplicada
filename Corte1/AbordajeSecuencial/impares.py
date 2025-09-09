#Este ejercicio vale una decima para el primer corte
try:
    while True:
        try: 
            num=int(input("ingrese un numero impar, control C para terminar: "))
            if num % 2 !=0: 
                print("este numero es impar ")
            else:
                 print("este numero es par") 

        except ValueError:
            print("valor incorrecto vuelva a intentar")

except KeyboardInterrupt:
    print("\n programa terminado")
        
        

