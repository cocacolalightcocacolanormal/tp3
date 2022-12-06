import random
# On definit les differentes variables du programme a leur valeur initial
niveau_vie = 20
numero_adversaire = 0
nombre_victoires = 0
nombre_defaites = 0
dice = 0
#On creer une boucle pour les differents choix qu'on peut faire, qui sagit en effet du jeu en tant que tel. Pour chaque tour, le niveau de l'adversaire est aleatoire entre 1 et 6.
# Si le joueur fait le choix 1, on definit le numero du de entre 1 et 6. Si le nombre du de est plus grand que le
# niveau de l'adversaire, on ajoute le niveau de l'adversaire au nombre de vie du joueur. Si l'inverse est vrai, on enleve
# le niveau de l'adversaire au niveau de vie du joueur. On garde aussi compte du numero de l'adversaire et du nombre de defaites et de victoires du joueur.
boucle_jeu = True
while boucle_jeu:
   numero_adversaire = numero_adversaire + 1
   force_adversaire = random.randint(1, 6)
   print("Vous tombez face à face avec un adversaire de difficulté", force_adversaire, )
   print("Niveau de vie:", niveau_vie, )
   choix = int(input("Que voulez-vous faire?\n"
                     "1- Combattre cet adversaire \n"
                     "2- Contourner cet adversaire et aller ouvrir une autre porte \n"
                     "3- Afficher les règles du jeu \n" "4- Quitter la partie \n"))
   if choix == 1:
       dice = random.randint(1, 6)
       if dice <= force_adversaire:
           print("Vous avez perdu")
           niveau_vie = niveau_vie - force_adversaire
           nombre_defaites = nombre_defaites + 1
           print("Adversaire:", numero_adversaire, "\n"
                                               "Force de l'adversaire", force_adversaire, "\n"
                                                                                          "Niveau de vie de l'usager:",
             niveau_vie, "\n"
                         "Combat", numero_adversaire, "\n"
                                                      ":", nombre_victoires, "vs", nombre_defaites, )
       elif dice > numero_adversaire:
           print("Vous avez gagner")
           niveau_vie = niveau_vie + force_adversaire
           nombre_victoires = nombre_victoires + 1
           print("Adversaire:", numero_adversaire, "\n"
                                               "Force de l'adversaire", force_adversaire, "\n"
                                                                                          "Niveau de vie de l'usager:",
             niveau_vie, "\n"
                         "Combat", numero_adversaire, "\n"
                                                      ":", nombre_victoires, "vs", nombre_defaites, )

# On donne au joueur l'option de contourner l'adversaire, ce qui lui couterait un niveau de vie.
   if choix == 2:
       print("Vous decidez de contourner cet adversaire")
       niveau_vie = niveau_vie - 1

# Si le joueur choisit l'option 3, on lui affiche les regles du jeu
   if choix == 3:
       print("Les regles de se jeu sont simple; Un personnage circule dans un couloir, \n"
             "a chaque extremite de se couloir il se retrouve une porte \n"
             "Chaque porte est un niveau et l'usager doit vaincre un monstre d'une force aleatoire \n"
             "Un de sera lancer; si le total des de lancer est plus haut que la force du monstre l'usager gagne \n"
             "sinon l'usager perd le combat et perdra autant de points de vie que la force du monstre affronte")
# Si le joueur choisit de quitter la partie, on termine la boucle
   if choix == 4:
       print("Bye bye!")
       boucle_jeu = False

# Si le joueur a un nombre de vie plus petit ou egal a zero, on termine le boucle
   if niveau_vie <= 0:
       print("Vous etes mort.")
       boucle_jeu = False

      
