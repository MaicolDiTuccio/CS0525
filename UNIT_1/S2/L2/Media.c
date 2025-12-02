#include <stdio.h> 

int main() {
    // Dichiarazione delle variabili
    int num;        // Variabile per memorizzare ogni numero intero inserito dall'utente.
    int conta;      // Contatore per tenere traccia di quanti numeri sono stati inseriti.
    float media;    // Variabile per memorizzare il risultato finale della media.
    float somma;    // Variabile per accumulare la somma di tutti i numeri.
     
   
    printf("Inserisci numeri (Inserisci carattere per terminare)\n ");

    
    somma = 0; // La somma iniziale deve essere zero.
    conta = 0; // Il contatore iniziale deve essere zero.

    
    printf("Inserisci il  numero: ");
    
    // Inizio del ciclo while
    // La condizione controlla il risultato di scanf.
    // scanf("%d", &num) restituisce 1 se è riuscito a leggere un numero intero.
    // Se l'utente inserisce un carattere non numerico (es. 's'), scanf fallisce e restituisce 0,
    // interrompendo così il ciclo 'while'.
    while(scanf("%d", &num)){
        somma = somma + num; // Aggiorna la somma con il nuovo numero inserito.
        conta++;             // Incrementa il contatore dei numeri inseriti.
        printf("Inserisci  numero: "); // Richiesta del numero successivo.
    }
    
    // Controllo finale dopo l'uscita dal ciclo
    // Se 'conta' è 0, significa che non è stato inserito nessun numero valido.
    if (!conta) { // !conta è equivalente a (conta == 0)
        printf("La media e' nulla \n");
    }
    else {
        
        media = somma / conta; // Calcolo della media: somma totale divisa per il numero di elementi.
        
    
        printf("\n La media dei numeri è: %.2f\n", media); // Stampa il risultato con due cifre decimali (%.2f).
    }
    
    return 0; // Indica che il programma è terminato con successo.
}