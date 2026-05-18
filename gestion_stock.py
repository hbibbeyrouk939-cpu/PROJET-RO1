import math

def calculate_eoq():
    D = 1200 
    K = 50   
    h = 2    

    Q_opt = math.sqrt((2 * D * K) / h)
    
    print(f"--- Résultat EOQ ---")
    print(f"Quantité économique de commande (Q*) : {Q_opt:.2f} unités")
    print(f"Nombre de commandes par an : {D/Q_opt:.2f}")

if __name__ == "__main__":
    calculate_eoq()
