import math # Importiamo il modulo math per usare la costante pi 

def perimetro():
   
    while True:
        
        print("\n Scegli la figura geometrica:")
        print("1. Quadrato")
        print("2. Rettangolo")
        print("3. Cerchio")
        print("4. Rombo")
        print("5. Trapezio")
        print("6. Esci")
        print()

        scelta = input("Inserisci il numero per ottenenere il perimetro desiderato (1-6): " )
        print()



        if scelta == '1':
            ## Perimetro del Quadrato
            
                lato = float(input("Inserisci la lunghezza del lato: "))
                if lato <= 0:
                     print("La lunghezza non puo' essere negativa.")
                     continue
                perimetro = 4 * lato
                print(f" Il perimetro del Quadrato con lato {lato} è: {perimetro}")
                print()

             

        elif scelta == '2':
            ## Perimetro del Rettangolo
            
                base = float(input("Inserisci la lunghezza della base del rettangolo: "))
                altezza = float(input("Inserisci la lunghezza dell'altezza del rettangolo: "))
                if base <= 0 or altezza <= 0:
                      print("La lunghezza non puo' essere negativa.")
                      continue
                perimetro =  (2*base + 2*altezza)
                print(f"Il perimetro del Rettangolo con base {base} e altezza {altezza} è: {perimetro}")
                print()
            

        elif scelta == '3':
            ## Perimetro del Cerchio (Circonferenza)
            
                raggio = float(input("Inserisci la lunghezza del raggio: "))
                if raggio <= 0:
                      print("La lunghezza non puo' essere negativa.")
                      continue
                
                perimetro = 2 * math.pi * raggio
                print(f" Il perimetro (Circonferenza) del Cerchio con raggio {raggio} è: {perimetro}") 
                print()
            

        elif scelta == '4':
            ## Perimetro del Rombo (P = 4 * lato)
            try:
                lato = float(input("Inserisci la lunghezza del lato del rombo: "))
                if lato <= 0:
                    print("La lunghezza non puo' essere negativa o zero.")
                    continue
                perimetro = 4 * lato
                print(f"Il perimetro del Rombo con lato {lato} è: {perimetro}")
            except ValueError:
                print("Inserisci un numero valido.")
                print()

        
        elif scelta == '5':
            ## Perimetro del Trapezio Isoscele 
            try:
                base_maggiore = float(input("Inserisci la lunghezza della Base Maggiore: "))
                base_minore = float(input("Inserisci la lunghezza della Base Minore: "))
                lato_obliquo = float(input("Inserisci la lunghezza del lato obliquo: "))

                if base_maggiore <= 0 or base_minore <= 0 or lato_obliquo <= 0:
                    print("Le lunghezze non possono essere negative o zero.")
                    continue
                
                #
                if base_minore >= base_maggiore:
                    print(" La Base Minore deve essere inferiore alla Base Maggiore in un trapezio.")
                    continue

                perimetro = base_maggiore + base_minore + 2 * lato_obliquo
                print(f"Il perimetro del Trapezio Isoscele è: {perimetro}")
            except ValueError:
                print(" Errore: Inserisci numeri validi.")
                print()


        elif scelta == '6':
        
            print("Fine programma")

            break

        else:
            
            print(" Scelta non riconusciuta, inserisci un numero valido")


perimetro()