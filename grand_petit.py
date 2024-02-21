from random import randint
import pygame
import time

def bouton(ecran,centre,couleur,w,h):
    """Dessiner un bouton

    Paramètres
    ----------
    ecran : la fenêtre de jeu sur laquelle sera dessiné le bouton
    centre : tuple (x,y)
        coordonnées du centre du bouton
    couleur : tuple (r,g,b)
        la couleur en RGB du bouton
    w : int
        la largeur de la surface
    h : int
        la hauteur de la surface

    Retourne
    --------
    bouton : rect
        le bouton
    """
    surface = pygame.Surface((w,h))
    surface.fill(couleur)
    bouton = surface.get_rect()
    bouton.center= centre
    ecran.blit(surface,bouton)
    return bouton

def texte_bouton(ecran,bouton,texte,taille,couleur=(0,0,0)):
    """Ajouter du texte sur un bouton

    Paramètres
    ----------
    ecran : la fenêtre
    bouton : rect
        un bouton (créé avec la fonction bouton
    texte : str
        le texte à ajouter sur le bouton
    taille : int
        la taille de la police
    couleur : tuple (r,g,b)
        la couleur de la police

    Retourne
    --------
    bouton = le bouton avec le texte
    """
    police = pygame.font.Font(None,taille)
    surface = police.render(texte,True,couleur)
    txt = surface.get_rect(center=bouton.center)
    ecran.blit(surface,txt)
    return bouton  

def titre(ecran,centre,texte,taille,couleur=(0,0,0)):
    """Ajouter un texte à l'écran

    Paramètres
    ----------
    ecran : l'écran où va s'afficher le texte
    centre : tuple (x,y)
        les coordonnées du centre du texte
    texte : str
        le texte à afficher
    taille : int
        la taille dela police
    couleur : tuple (r,g,b)
        la couleur du texte
    """
    police = pygame.font.Font(None,taille)
    surface = police.render(texte,True,couleur)
    rect = surface.get_rect()
    rect.center = centre
    ecran.blit(surface,rect)

def afficher_page(ecran,largeur,hauteur,couleur_fond,textes,boutons):
    ecran.fill(couleur_fond)
    coord = []
    if boutons != []:
        for b in boutons :
            # b = (centre,couleur,w,h,texte,taille_txt,couleur_txt)
            # boutons = {b1,b2,b3}
            rect = bouton(ecran,b[0],b[1],b[2],b[3])
            rect = texte_bouton(ecran,rect,b[4],b[5])
            coord.append(rect)
    if textes != []:
        for t in textes :
            # t = (centre,texte,taille)
            titre(ecran,t[0],t[1],t[2])
    pygame.display.flip()
    return coord

def grand_petit():
    pygame.init()
    largeur = pygame.display.Info().current_w
    hauteur = pygame.display.Info().current_h
    ecran = pygame.display.set_mode([largeur,hauteur-60]) # (largeur,hauteur)
    pygame.display.set_caption("Plus grand, plus petit")
    ecran.fill((255, 255, 255))
    # Positions
    centre = (largeur//2,hauteur//2)
    haut = (largeur//2,hauteur//5)
    centre_haut = (largeur//2,hauteur//3+50)
    bas = (largeur//2,hauteur//2+100)

    # Couleurs
    blanc = (255,255,255)
    bleu = (204,229,255)

    dico = {"accueil":([(haut,"Bienvenue dans Plus grand plus petit !",50),
                        (centre_haut,"Le but du jeu est de deviner un nombre entre 1 et 1000 en un nombre d'essais réduits",40)],
                       [(bas,bleu,250,100,"C'est parti !",50)]),
            "essais":([(haut,"Combien d'essais maximum souhaitez vous ?",50),
                    (centre_haut,"Entrez le nombre puis appuyez sur la touche Espace",40)],
                   [(centre,bleu,100,50,None,40)]),
            "jeu":([(haut,"Entrez un nombre entre 1 et 1000 puis appuyez sur la touche Entrée",50)],
                   [(centre,bleu,100,50,None,40)]),
            "victoire":([(haut,"Bravo ! Vous avez gagné :)",60)],[]),
            "défaite":([(haut,"Dommage, vous avez perdu :(",60)],
                       [])}

    cles = [pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,
            pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,
            pygame.K_8,pygame.K_9]

    running = True
    rect_acc = afficher_page(ecran,largeur,hauteur,blanc,dico["accueil"][0],dico["accueil"][1])[0]
    
    while running :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                # si on touche la petite croix
                pygame.quit()
                running = False
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # si on appuie sur la touche echap
                pygame.quit()
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN :
                position = pygame.mouse.get_pos()
                
                if rect_acc.x <= position[0] <= rect_acc.x+rect_acc.width:
                    if rect_acc.y <= position[1] <= rect_acc.y+rect_acc.height:
                        rect_essais = afficher_page(ecran,largeur,hauteur,blanc,dico["essais"][0],dico["essais"][1])[0]
                        nb_essais = ""
                        
            elif event.type == pygame.KEYDOWN and event.key != pygame.K_ESCAPE:
                for i in range(len(cles)):
                    if event.key == cles[i]:
                        c = chr(cles[i])
                        nb_essais = int(str(nb_essais)+str(c))
                        rect_essais = bouton(ecran,centre,bleu,100,50)
                        rect_essais = texte_bouton(ecran,rect_essais,str(nb_essais),40)
                        pygame.display.flip()

                if event.key == pygame.K_BACKSPACE:
                    nb_essais = str(nb_essais)[:-1]
                    if nb_essais == "" :
                        rect_essais = bouton(ecran,centre,bleu,100,50)
                    else :
                        nb_essais = int(nb_essais)
                        rect_essais = bouton(ecran,centre,bleu,100,50)
                        rect_essais = texte_bouton(ecran,rect_essais,str(nb_essais),40)
                    pygame.display.flip()

                elif event.key == pygame.K_SPACE:
                    print("Vous avez",nb_essais,"essais maximum")
                    running = False
                    choix = ""

    secret = randint(1,1000)
    essais = 0
    rect_choix = afficher_page(ecran,largeur,hauteur,blanc,dico["jeu"][0],dico["jeu"][1])[0]

    while secret != choix and essais < nb_essais :

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                # si on touche la petite croix
                pygame.quit()
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # si on appuie sur la touche echap
                pygame.quit()
       
            elif event.type == pygame.KEYDOWN and event.key != pygame.K_ESCAPE:
                for i in range(len(cles)):
                    if event.key == cles[i]:
                        c = chr(cles[i])
                        choix = int(str(choix)+str(c))
                        rect_choix = bouton(ecran,centre,bleu,100,50)
                        rect_choix = texte_bouton(ecran,rect_choix,str(choix),40)
                        pygame.display.flip()

                if event.key == pygame.K_BACKSPACE:
                    choix = str(choix)[:-1]
                    if choix == "" :
                        rect_choix = bouton(ecran,centre,bleu,100,50)
                    else :
                        choix = int(choix)
                        rect_choix = bouton(ecran,centre,bleu,100,50)
                        rect_choix = texte_bouton(ecran,rect_choix,str(choix),40)
                    pygame.display.flip()

                elif event.key == pygame.K_RETURN:
                    print("Vous avez choisi le nombre",choix)
                    
                    if choix > secret :
                        titre(ecran,bas,"Votre nombre est trop grand",40)
                        pygame.display.flip()
                        time.sleep(2)
                        rect_choix = afficher_page(ecran,largeur,hauteur,blanc,dico["jeu"][0],dico["jeu"][1])[0]
                        pygame.display.flip()
                        essais += 1
                        choix = ""

                    elif choix < secret :
                        titre(ecran,bas,"Votre nombre est trop petit",40)
                        pygame.display.flip()
                        time.sleep(2)
                        rect_choix = afficher_page(ecran,largeur,hauteur,blanc,dico["jeu"][0],dico["jeu"][1])[0]
                        pygame.display.flip()
                        essais += 1
                        choix = ""

    if secret == choix :
        time.sleep(2)
        print("Bravo, vous avez trouvé en",essais,"essais")
        afficher_page(ecran,largeur,hauteur,blanc,dico["victoire"][0],dico["victoire"][1])
        titre(ecran,centre,str("Le nombre était bien "+str(secret)),50)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        return True
    
    elif essais >= nb_essais :
        time.sleep(2)
        print("Nombre d'essais dépassé.")
        print("Dommage, vous avez perdu.")
        afficher_page(ecran,largeur,hauteur,blanc,dico["défaite"][0],dico["défaite"][1])
        titre(ecran,centre,str("Le nombre était "+str(secret)),50)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        return False
            

