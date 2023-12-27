from random import randint

def grand_petit():
    tours = int(input("Combien d'essais maximum souhaitez-vous ? "))
    secret = randint(1,1000)
    choix = int(input("Entrez un nombre entre 1 et 1000 : "))
    essais = 1
    while secret != choix and essais < tours:
        if secret < choix :
            print("Votre nombre est trop grand")
            choix = int(input("Entrez un nombre entre 1 et 1000 : "))
        else :
            print("Votre nombre est trop petit")
            choix = int(input("Entrez un nombre entre 1 et 1000 : "))
        essais = essais + 1
    if secret == choix :
        print("Bravo, vous avez trouvé en",essais,"essais")
        win = True
    else :
        print("Nombre d'essais dépassé.")
        print("Dommage, vous avez perdu.")
        win = False
    return win


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





    
