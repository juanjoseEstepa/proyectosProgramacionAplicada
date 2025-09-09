#Este ejercicio vale una decima para el primer corte

try:
    while True:
        try:
            value=int(input("ingrese un numero y contro C para terminnar : "))
            
            for i in range(1,value+1):
                conta = 0
            for n in range(1, i+1):
                residue = i%n
            if residue == 0:
                conta = conta + 1
            
           
            if conta == 2:
                print(f'{i} es un primo')
                print("\n")
            else:
                print(f'{i} NO es un primo')
                print("\n")
    
        
            
        except ValueError:
            print("VALOR ERRONEO")
except KeyboardInterrupt:
    print("PROGRMA TERMINADO")          

    