from tkinter.constants import N
from Azul import *
from typing import overload
from upemtk import *
from random import *



def sac_des_100_tuile(n):
    "Crée le sac des 100 tuiles mélangée"
    if n == 5:
        nb_tuiles = 20
    else:
        nb_tuiles = 36
    liste_des_100_tuiles = []
    liste_des_couleurs = ['Blue','Yellow','Orange','#ed4b6f','Black']

    for i in liste_des_couleurs:
        for j in range(nb_tuiles):
            liste_des_100_tuiles.append(i)
    shuffle(liste_des_100_tuiles)
    
    return liste_des_100_tuiles

#########################################################################################################################################
#########################################################################################################################################

def tuile_dans_les_fabrique(lst_tuile,k,n):
    "Dessine les tuiles dans les fabriques et leurs assigne une couleur aléatoire"
    "De plus on récupère les coordonnées de chaque rectangle, leur couleur et on récupère le rectangle"

    lst_rec_c_xy = []

    abscisse = 65
    abscisse1 = 95
    ordonne = 70
    ordonne1 = 100


    lst_des_rectangles = [[],[],[],[],[]]
    lst_couleur = [[],[],[],[],[]]
    lst_coordonnee = [[],[],[],[],[]]
    if n == 9:
        lst_des_rectangles = [[],[],[],[],[],[],[],[],[]]
        lst_couleur = [[],[],[],[],[],[],[],[],[]]
        lst_coordonnee = [[],[],[],[],[],[],[],[],[]]

    coor = -1
    
    for i in range(n):
        coor += 1
        for j in range(2):
            for z in range(2):
                k -= 1
                
                choix_couleur_aleatoire = randint(0,k) ### k permet de délimiter le randint en fonction de la longueur de la liste des tuiles
                
                couleur = lst_tuile[choix_couleur_aleatoire]
                
                lst_tuile.remove(lst_tuile[choix_couleur_aleatoire])
                a = rectangle(abscisse,ordonne,abscisse1,ordonne1,'Black',couleur)
                lst = []
                
                coordonne = (abscisse,ordonne)
                coordonne1 = (abscisse1,ordonne1)


                ### Insération des coordonnees dans la listes des coordonnees
                lst.append(coordonne)
                lst.append(coordonne1)

                lst_coordonnee[coor].append(lst)
                lst_des_rectangles[coor].append(a)
                lst_couleur[coor].append(couleur)

                abscisse += 35
                abscisse1 += 35

            ordonne = 100
            ordonne1 = 130
            abscisse -= 70
            abscisse1 -= 70
        if n == 5:
            abscisse += 275
            abscisse1 += 275
        else:
            abscisse += 130
            abscisse1 += 130
        ordonne = 70
        ordonne1 = 100

    lst_rec_c_xy.append(lst_des_rectangles)
    lst_rec_c_xy.append(lst_couleur)
    lst_rec_c_xy.append(lst_coordonnee)

    return lst_rec_c_xy, lst_tuile, k

def clicl():
    "Prend les coordonnées du clic"
    a = attente_clic()
    x = a[0]
    y = a[1]

    return x, y

#########################################################################################################################################
#########################################################################################################################################

def zone_clic(lst_rec_c_xy, lst_rec_c_xy_restantes, bot_joue):
    "Détermine la zone du clic"
    
    lst_xy = lst_rec_c_xy[2]
    lst_xy_rest = lst_rec_c_xy_restantes[2]

    if bot_joue == True:
        k = randint(1,2)
        if lst_xy == []:
            k = 2

        if lst_xy_rest == []:
            k = 1

        if k == 1:
            
            i = randint(0, len(lst_xy)-1)
            j = randint(0, len(lst_xy[i])-1)
            zoneclic = True
        
        if k == 2:

            i = randint(0, len(lst_xy_rest)-1)
            j = False
            zoneclic = False
        
        return zoneclic, i, j

    joueur_clic_sur_tuile = False

    while joueur_clic_sur_tuile == False:

        x, y = clicl()
        
        for i in range(len(lst_xy)): 
            
            for j in range(len(lst_xy[i])):
                
                a = lst_xy[i][j] ### Prend les tuples avec les coordonnées d'une tuile
                
                x1 = a[0][0] ### coordonne 1 ere abscisse dans la liste des coordonnees
                x2 = a[1][0] ### coordonne 1 ere ordonne "
                y1 = a[0][1] ### coordonne 2 eme abscisse "
                y2 = a[1][1] ### coordonne 2 eme ordonne "

                

                if x1 <= x and x2 >= x and y1 <= y and y2 >= y: ### Verifie si le clic est dans ses coordonnees
                    
                    joueur_clic_sur_tuile = True

                    return True, i, j
        
        for i in range(len(lst_xy_rest)): 
            
            
                
            a = lst_xy_rest[i] ### Prend les tuples avec les coordonnées d'une tuile
            
            x1 = a[0][0] ### coordonne même chose que au dessus pour les 4
            x2 = a[1][0]
            y1 = a[0][1]
            y2 = a[1][1]

            if x1 <= x and x2 >= x and y1 <= y and y2 >= y: ### Verifie si le clic est dans ses coordonnees
                
                joueur_clic_sur_tuile = True
                j = False
                return False, i, j

#########################################################################################################################################
#########################################################################################################################################

def efface_rectangle(lst_rec_c_xy, lst_rec_c_xy_restantes, i, j, zoneclic):
    "On efface le rectangle sélectionner et ceux présents dans la fabrique, on supprime leurs coordonnee, couleur et rectangle de nos liste"
    
    lst_rec = lst_rec_c_xy[0]
    lst_c = lst_rec_c_xy[1] 
    lst_xy = lst_rec_c_xy[2]
    
    lst_rec_rest = lst_rec_c_xy_restantes[0]
    lst_c_rest = lst_rec_c_xy_restantes[1]
    lst_xy_rest = lst_rec_c_xy_restantes[2]


    if zoneclic == True:
        
            
        nbr_couleur = 0
        couleur = lst_c[i][j] ### On prend la couleur de la tuile sélectionner 

        lst_c_non_selec = [] ### Liste des couleurs des tuiles qui ne seront pas sélectionné par la suite

        for x in range(len(lst_c[i])): ### Regarde dans la fabrique si il y a d'autres tuile de même couleur que la sélectionné
            
            if lst_c[i][x] == couleur:
                
                nbr_couleur += 1
                efface(lst_rec[i][x]) ### On efface les rectangles qui ont la même couleur
            else:
                lst_c_non_selec.append(lst_c[i][x]) ### Liste des couleurs des tuiles non sélectionné

            efface(lst_rec[i][x]) ### On efface de tout les cas les tuiles dans la fabrique 

        ##############################    
        ### On met à jour nos 3 listes 

        lst_rec.remove(lst_rec[i]) 
        lst_xy.remove(lst_xy[i])
        lst_c.remove(lst_c[i])

        lst_rec_c_xy[0] = lst_rec
        lst_rec_c_xy[1] = lst_c
        lst_rec_c_xy[2] = lst_xy
        return couleur, nbr_couleur, lst_c_non_selec, lst_rec_c_xy

    if zoneclic == False:

        
        nbr_couleur = 0
        
        couleur = lst_c_rest[i]
        
        lst_c_non_selec = []
        lst_supp = []
        lst_supp1 = []
        lst_supp2 = []
        
        for x in range(len(lst_c_rest)):
            
            if lst_c_rest[x] == couleur:
                nbr_couleur += 1
                efface(lst_rec_rest[x][0])
                
                ### On met dans des listes les éléments qu'on devra supprimer

                lst_supp.append(lst_rec_rest[x])
                lst_supp1.append(lst_xy_rest[x])
                lst_supp2.append(lst_c_rest[x])
            else:
                pass

        #################################################################################    
        ### On supprime les élément dans les liste originales avec celles créent au dessus

        for k in lst_supp:
            for t in lst_rec_rest:
                if k == t:
                    lst_rec_rest.remove(t)
        for k in lst_supp1:
            for t in lst_xy_rest:
                if k == t:
                    lst_xy_rest.remove(t)

        for k in lst_supp2:
            for t in lst_c_rest:
                if k == t:
                    lst_c_rest.remove(t)

        lst_rec_c_xy_restantes[0] = lst_rec_rest
        lst_rec_c_xy_restantes[1] = lst_c_rest
        lst_rec_c_xy_restantes[2] = lst_xy_rest

        return couleur, nbr_couleur, lst_c_non_selec, lst_rec_c_xy_restantes

#########################################################################################################################################
#########################################################################################################################################

def tuile_restante(lst_c_non_selec, abs, abs1, ord, ord1, lst_rec_c_xy_restantes):
    "Récuperation des tuiles restante des fabrique, pour les placé au milieu on récupère leur coordonnee, couleur et rectangle, pour le plateau du joueur 1"
    
    lst_rectangle_restant = lst_rec_c_xy_restantes[0]
    lst_c_tuiles_restantes = lst_rec_c_xy_restantes[1]
    lst_coordonnee_tuile_restante = lst_rec_c_xy_restantes[2]

    for k in lst_c_non_selec:
        lst_coordonnee = [] 
        lst_rect = []
        lst_c_tuiles_restantes.append(k)
        
        if abs1 >= 760: ### Cette condition permet de mettre à jour l'abscisse et l'ordonne des tuile dans le milieu du plato pour les mettre en colonne 
            abs = 485
            abs1 = 515
            ord += 40
            ord1 += 40

        rect = rectangle(abs, ord, abs1, ord1, k, k)

        coor = (abs,ord)
        coor1 = (abs1,ord1)

        ###  Remplissage des listes de tuiles restantesdes fabriques

        lst_rect.append(rect)
        lst_rectangle_restant.append(lst_rect)
        lst_coordonnee.append(coor)
        lst_coordonnee.append(coor1)
        
        lst_coordonnee_tuile_restante.append(lst_coordonnee)
        
        abs += 35
        abs1 += 35
    lst_rec_c_xy_restantes[0] = lst_rectangle_restant
    lst_rec_c_xy_restantes[1] = lst_c_tuiles_restantes
    lst_rec_c_xy_restantes[2] = lst_coordonnee_tuile_restante
    return abs, abs1, ord, ord1, lst_rec_c_xy_restantes


#########################################################################################################################################
#########################################################################################################################################

lst_abs_plancher = [[15,50],[810,845],[15, 50],[810, 845]]
lst_abs_escalier = [[255, 220],[1050,1015],[255, 220],[1050, 1015]]
    
def transposition_rectangle2(num_joueur, couleur, nb_carre, coordonnee_escalier, h1, abscisse_rectangle, abscisse_rectangle1, lst_couleur_esc2, lst_compte, lst_des_tours_de_rangement, lst_des_coordonne_des_plancher, nb_malus, bot_joue):
    "Il deplace les rectangle en fontion du clic de l'utilisateur, dans les règles du jeu"

    ###########################################################
    ########### ###################
    ###########################################################
    
    lst_xy = coordonnee_escalier
    k = False
    numero_joueur = num_joueur

    while k == False:

        num_joueur = numero_joueur

        if bot_joue == True:
            l = randint(1,6)
            if l != 3:
                i = randint(0, len(lst_xy)-1)
                j = randint(0, len(lst_xy[i])-1)
                a = lst_xy[i][j]    
                x1 = a[0][0]
                x2 = a[1][0]
                y1 = a[0][1]
                y2 = a[1][1]

            if l == 3:
                
                lst_xy1 = lst_des_coordonne_des_plancher[num_joueur]
                i = 0
                j = 0

                a = lst_xy1[i][j] 
                  
                x1 = a[0][0]
                x2 = a[1][0]
                y1 = a[0][1]
                y2 = a[1][1]

                if h1 == 0:
                        abscisse_rectangle = lst_abs_plancher[num_joueur][0]
                        abscisse_rectangle1 = lst_abs_plancher[num_joueur][1]
                        
                for m in range(nb_carre):
                    if num_joueur == 2 or num_joueur == 3:
                        ordonne = 860
                        ordonne1 = 890
                        
                    else:
                        ordonne = 510
                        ordonne1 = 540
                        
                    if num_joueur == 1 or num_joueur == 3:
                        if abscisse_rectangle1 > 1115:
                                break
                    else:
                        if abscisse_rectangle1 > 320:
                            break
                    
                    rectangle(abscisse_rectangle, ordonne, abscisse_rectangle1, ordonne1, couleur, couleur)

                    abscisse_rectangle += 45
                    abscisse_rectangle1 += 45

                h1 = 1
                nb_malus += nb_carre
                return h1, abscisse_rectangle, abscisse_rectangle1, lst_couleur_esc2, lst_compte, lst_des_tours_de_rangement, nb_malus
                 
        else:

            i, j, x1, x2, y1, y2, p, nb_malus = clic_joueur_esc(num_joueur, coordonnee_escalier, lst_des_coordonne_des_plancher[num_joueur], nb_carre, h1, abscisse_rectangle, abscisse_rectangle1, couleur, lst_couleur_esc2, lst_compte, lst_des_tours_de_rangement, nb_malus)
            if p == False:   
                return i, j, x1, lst_couleur_esc2, lst_compte, lst_des_tours_de_rangement, nb_malus    

        

        if lst_couleur_esc2[i] == []:
            if num_joueur == 0:
                v = 1
            if num_joueur == 1:
                v = 2
            if num_joueur == 2:
                v = 3
            if num_joueur == 3:
                v = 4
            if not (couleur in lst_des_tours_de_rangement[num_joueur+v][i]):

                num_joueur = numero_joueur

                if h1 == 0:
                    abscisse_rectangle = lst_abs_plancher[num_joueur][0]
                    abscisse_rectangle1 = lst_abs_plancher[num_joueur][1]
                
                x1 = lst_abs_escalier[num_joueur][0]
                x2 = lst_abs_escalier[num_joueur][1]
                
                n = nb_carre
                
                if nb_carre > i+1:

                    n = i+1
                    nb_carre -= i+1
                    h1 = 1
                
                else:

                    n = nb_carre
                    nb_carre = 0
                    
                for k in range(nb_carre):
                    if num_joueur == 1 or num_joueur == 0:  
                        ordonne = 510
                        ordonne1 = 540
                    else: 
                        ordonne = 860
                        ordonne1 = 890
                    if num_joueur == 1 or num_joueur == 3:
                        if abscisse_rectangle1 > 1115:
                            break
                    if num_joueur == 0 or num_joueur == 2:
                        if abscisse_rectangle1 > 320:
                            break
                    
                    rectangle(abscisse_rectangle, ordonne, abscisse_rectangle1, ordonne1, couleur, couleur)
                    
                    abscisse_rectangle += 45
                    abscisse_rectangle1 += 45
                
                nb_malus += nb_carre

                c = 0
                for j in range(n):

                    u = rectangle(x1, y1, x2, y2, couleur, couleur)

                    x1 -= 45
                    x2 -= 45
                    lst_couleur_esc2[i].append(couleur)
                    c += 1
                    if num_joueur != 0:
                        
                        lst_des_tours_de_rangement[num_joueur+num_joueur][i].append(u)
                    else:
                        lst_des_tours_de_rangement[0][i].append(u)
                
                lst_compte[i].append(c)

                return h1, abscisse_rectangle, abscisse_rectangle1, lst_couleur_esc2, lst_compte, lst_des_tours_de_rangement, nb_malus

        

        if lst_couleur_esc2[i] != []:
            if num_joueur == 0:
                v = 1
            if num_joueur == 1:
                v = 2
            if num_joueur == 2:
                v = 3
            if num_joueur == 3:
                v = 4


            if not (couleur in lst_des_tours_de_rangement[num_joueur+v][i]):
               
                if lst_couleur_esc2[i][0] == couleur:
                    
                    if len(lst_couleur_esc2[i]) == i+1:
                        
                        pass

                    else:
                            
                        num_joueur = numero_joueur

                        if h1 == 0:
                            abscisse_rectangle = lst_abs_plancher[num_joueur][0]
                            abscisse_rectangle1 = lst_abs_plancher[num_joueur][1]
                        
                        if num_joueur == 1 or num_joueur == 3:
                            x1 = 1050
                            x2 = 1015

                        if num_joueur == 0 or num_joueur == 2:
                            
                            x1 = 255
                            x2 = 220

                        p = False

                        nb_tuile_escalier = len(lst_couleur_esc2[i])
                            
                        if p == False:

                            n = i+1 - nb_tuile_escalier
                            
                            if nb_carre > n:
                                h1 = 1
                                nb_carre = nb_carre - n
                                
                            else:
                                
                                n = nb_carre
                                nb_carre = 0


                        for k in range(nb_carre):
                            if num_joueur == 1 or num_joueur == 0:
                                ordonne = 510
                                ordonne1 = 540
                            else: 
                                ordonne = 860
                                ordonne1 = 890
                            if num_joueur == 1 or num_joueur == 3:
                                if abscisse_rectangle1 > 1115:
                                    break
                            if num_joueur == 0 or num_joueur == 2:
                                if abscisse_rectangle1 > 320:
                                    break
                            
                            rectangle(abscisse_rectangle,ordonne,abscisse_rectangle1,ordonne1,couleur,couleur)

                            abscisse_rectangle += 45
                            abscisse_rectangle1 += 45

                        nb_malus += nb_carre
                        
                        c = lst_compte[i][0]
                        x1 = x1 + c * -45
                        x2 = x2 + c * -45
                        
                        for j in range(n):
                            
                            u = rectangle(x1,y1,x2,y2,couleur,couleur)
                            
                            x1 -= 45
                            x2 -= 45
                            lst_couleur_esc2[i].append(couleur)
                            lst_compte[i][0] = lst_compte[i][0] + 1
                            if num_joueur != 0:
                                lst_des_tours_de_rangement[num_joueur+num_joueur][i].append(u)
                            
                            else:
                                lst_des_tours_de_rangement[0][i].append(u)
                    
                        return h1, abscisse_rectangle, abscisse_rectangle1, lst_couleur_esc2, lst_compte, lst_des_tours_de_rangement, nb_malus   

#########################################################################################################################################
#########################################################################################################################################

def clic_plancher1(num_joueur, lst_des_coordonne_des_plancher, x, y, nb_carre, h1, abscisse_rectangle, abscisse_rectangle1, couleur, nb_malus):
    "Il deplacce les tuiles dans le plancher"

    #########################################
    ##### ######
    #########################################

    lst_xy = lst_des_coordonne_des_plancher
    
    for i in range(len(lst_xy)): 
            
            for j in range(len(lst_xy[i])):

                a = lst_xy[i][j]
                
                x1 = a[0][0]
                x2 = a[1][0]
                y1 = a[0][1]
                y2 = a[1][1]
                
                if x1 <= x and x2 >= x and y1 <= y and y2 >= y:
                    
                    if h1 == 0:
                        abscisse_rectangle = lst_abs_plancher[num_joueur][0]
                        abscisse_rectangle1 = lst_abs_plancher[num_joueur][1]
                    

                    for k in range(nb_carre):
                        
                        ordonne = 510
                        ordonne1 = 540
                        if num_joueur == 1:
                            if abscisse_rectangle1 > 1115:
                                break

                        if num_joueur == 0:
                            
                            if abscisse_rectangle1 > 320:
                                
                                break
                        if num_joueur > 1:
                            ordonne = 860
                            ordonne1 = 910
                            
                        rectangle(abscisse_rectangle, ordonne, abscisse_rectangle1, ordonne1, couleur, couleur)

                        abscisse_rectangle += 45
                        abscisse_rectangle1 += 45
                    nb_malus += nb_carre
                    h1 = 1
                    return h1, abscisse_rectangle, abscisse_rectangle1, 1, nb_malus
    return h1, abscisse_rectangle, abscisse_rectangle1, 0, nb_malus

#########################################################################################################################################
#########################################################################################################################################

def clic_joueur_esc(num_joueur, coordonnee_escalier, lst_des_coordonne_des_plancher, nb_carre, h1, abscisse_rectangle, abscisse_rectangle1, couleur, lst_couleur_esc2, lst_compte, lst_des_tours_de_rangement, nb_malus):

    lst_xy = coordonnee_escalier
    k = False
    while k == False:

        x, y = clicl()

        h1, abscisse_rectangle, abscisse_rectangle1, p, nb_malus = clic_plancher1(num_joueur, lst_des_coordonne_des_plancher, x, y ,nb_carre, h1, abscisse_rectangle, abscisse_rectangle1, couleur, nb_malus)
        
        if p == 1:
            return h1, abscisse_rectangle, abscisse_rectangle1, lst_couleur_esc2, lst_compte, lst_des_tours_de_rangement, False, nb_malus
        
        for i in range(len(lst_xy)): 
            
            for j in range(len(lst_xy[i])):
                
                a = lst_xy[i][j]
                
                x1 = a[0][0]
                x2 = a[1][0]
                y1 = a[0][1]
                y2 = a[1][1]
                if x1 >= x and x2 <= x and y1 <= y and y2 >= y:
                    return i, j, x1, x2, y1, y2, True, nb_malus       
        
#########################################################################################################################################
#########################################################################################################################################

def mur_de_rangement(lst_dictionnaire_2mur,lst_esc_couleur, lst_des_tours_de_rangement, lst_compte, lst_comptage, score, tuile_visites_tous):
    "Detecte les esacliers plein"

    
    
    
    for m in range(len(lst_esc_couleur)):
        for i in range(len(lst_esc_couleur[m])): ### L'indice m va permettre d'effectuer les opération sur les 2 murs 
           
            if len(lst_esc_couleur[m][i]) == i+1: ### Verifie si l'escalier est plein 
                
                lst_compte[m][i].remove(lst_compte[m][i][0])
                lst_des_tours_de_rangement, lst_esc_couleur, lst_comptage, score, tuile_visites_tous = dessin_mur_de_rangement(lst_dictionnaire_2mur, lst_esc_couleur[m][i][0], i, m, lst_des_tours_de_rangement, lst_esc_couleur, lst_comptage, score, tuile_visites_tous)


    
    return lst_des_tours_de_rangement,lst_esc_couleur, lst_compte, lst_comptage, score, tuile_visites_tous


#########################################################################################################################################
#########################################################################################################################################

def dessin_mur_de_rangement(lst_dictionnaire_2mur, couleur, i, m, lst_des_tours_de_rangement, lst_esc_couleur, lst_comptage, score, tuile_visites_tous):
    "Dessine dans les murs de rangement"

    k = 0
    
    
    for x in lst_dictionnaire_2mur[m]:
        ### On cherche dans le bonne étage puis ensuite la couleur
        k += 1
        if k == i+1:
            for n,y in x[0].items():
                if couleur == n:
                   
                    rectangle(y[0][0], y[0][1], y[1][0], y[1][1], couleur, couleur) ### Dessine la tuile dans le mur
                    
                    ### On selectionne le bonne élément de liste
                    if m == 0:
                        lst_des_tours_de_rangement[m+1][i].append(couleur)
                        s = m +1
                        lst_comptage[0], tuile_visites_tous[0], score[0] = comptage_score(lst_des_tours_de_rangement, lst_comptage[0], score[0], tuile_visites_tous[0], s)
                        
                    if m == 1:
                        
                        lst_des_tours_de_rangement[m+2][i].append(couleur)
                        s = m +2
                        lst_comptage[m], tuile_visites_tous[m], score[m] = comptage_score(lst_des_tours_de_rangement, lst_comptage[m], score[m], tuile_visites_tous[m], s)
                    if m == 2:
                        
                        lst_des_tours_de_rangement[m+3][i].append(couleur)
                        s = m +2
                        lst_comptage[m], tuile_visites_tous[m], score[m] = comptage_score(lst_des_tours_de_rangement, lst_comptage[m], score[m], tuile_visites_tous[m], s)
                    
                    if m == 3: 
                        
                        lst_des_tours_de_rangement[m+4][i].append(couleur)
                        s = m +2
                        lst_comptage[m], tuile_visites_tous[m], score[m] = comptage_score(lst_des_tours_de_rangement, lst_comptage[m], score[m], tuile_visites_tous[m], s)   
                    lst_des_tours_de_rangement, lst_esc_couleur = effacer_escalier(lst_des_tours_de_rangement, i, m, lst_esc_couleur)
    
    return lst_des_tours_de_rangement, lst_esc_couleur, lst_comptage, score, tuile_visites_tous

#########################################################################################################################################
#########################################################################################################################################

def effacer_escalier(lst_des_tours_de_rangement, i, m, lst_esc_couleur):
    "Efface les tuiles des escaliers plein"

    
    k = m
    if m == 1:
        k = m + 1
    if m == 2:
        k = m + 2
    if m == 3:
        k = m + 3
    
        
    
    while lst_des_tours_de_rangement[k][i] != []: ### Tant que tout les élément de la liste ne sont supprimer la boucle continue
        
        if len(lst_des_tours_de_rangement[k][i]) == 0:
            break
        
        efface(lst_des_tours_de_rangement[k][i][0])
        lst_des_tours_de_rangement[k][i].remove(lst_des_tours_de_rangement[k][i][0])
        
        if lst_esc_couleur[m][i] != []:
            
            lst_esc_couleur[m][i].remove(lst_esc_couleur[m][i][0])
     
    return lst_des_tours_de_rangement, lst_esc_couleur

#########################################################################################################################################
#########################################################################################################################################

def bot(num_jouer, lst_rec_c_xy, lst_rec_c_xy_restantes, abs, abs1, ord, ord1, h1, abscisse_rectangle, abscisse_rectangle1, lst_couleur_esc, lst_compte, lst_des_tours_de_rangement, lst_des_coordonne_des_plancher, coordonnee_escalier, nb_malus):


    zoneclic, i, j = zone_clic(lst_rec_c_xy, lst_rec_c_xy_restantes, True)

    if zoneclic == True:
        
        couleur, nb_carre, lst_c_non_selec, lst_rec_c_xy = efface_rectangle(lst_rec_c_xy, lst_rec_c_xy_restantes, i, j, zoneclic)

        abs, abs1, ord, ord1, lst_rec_c_xy_restantes = tuile_restante(lst_c_non_selec, abs, abs1, ord, ord1, lst_rec_c_xy_restantes)

    if zoneclic == False:
        
        couleur, nb_carre, lst_c_non_selec, lst_rec_c_xy_restantes = efface_rectangle(lst_rec_c_xy, lst_rec_c_xy_restantes, i, j, zoneclic)

        abs, abs1, ord, ord1, lst_rec_c_xy_restantes = tuile_restante(lst_c_non_selec, abs, abs1, ord, ord1, lst_rec_c_xy_restantes)
    
    h1, abscisse_rectangle, abscisse_rectangle1, lst_couleur_esc, lst_compte, lst_des_tours_de_rangement, nb_malus = transposition_rectangle2(num_jouer, couleur, nb_carre, coordonnee_escalier, h1, abscisse_rectangle, abscisse_rectangle1, lst_couleur_esc, lst_compte, lst_des_tours_de_rangement, lst_des_coordonne_des_plancher, nb_malus, True)

    return lst_rec_c_xy, lst_rec_c_xy_restantes, abs, abs1, ord, ord1, h1, lst_couleur_esc, lst_compte, abscisse_rectangle, abscisse_rectangle1, nb_malus 


#########################################################################################################################################
#########################################################################################################################################

def partie_avec_un_bot():

    cree_fenetre(1300, 1200,)
    
    plateau_entier(2) # Création du plateau

    score_joueur1 = texte(100,260,0,"Yellow","nw", "Impact",15)
    score_joueur2 = texte(895,260,0,"Yellow","nw", "Impact",15)
    tuile_visites_tous = [set(), set()]

    score = [0,0] 
    
    lst_comptage = [
                    [[None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None] ],

                    [[None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None]]
                    ]

    coordonnee_escalier, coordonnee_escalier2 = escaliers(2) # Création d'escalier avec prise de leur coordonnee

    lst_tuile = sac_des_100_tuile(5) 
    
    
    lst_dictionnaire_2mur = tour_de_rangement(2)
    
    lst_des_tours_de_rangement = [
            
                [ [], [], [], [], [] ], ### liste des rectangles des escaliers Joueur 1      
                [ [], [], [], [], [] ], ### liste des couleurs remplis dans la tour de rangement Joueur 1

                [ [], [], [], [], [] ], ### liste des rectangles des escaliers Joueur 2 
                [ [], [], [], [], [] ]  ### liste des couleurs remplis dans la tour de rangement Joueur 2

                                    ]

    ### Liste des couleurs dans les escaliers

    lst_couleur_esc = [ [[], [], [], [], []], [[], [], [], [], []] ]
    

    ### Le nombre de tuiles dans chaque escalier mis dans des sous listes

    lst_compte = [[[],[],[],[],[]], [[],[],[],[],[]]]
    
    lst_point_malus = [1, 2, 4, 6, 8, 11, 14]
    
    k = 100
    partie_finie = False

    while partie_finie == False:

        
        if lst_tuile == []:
            
            k = 100
            lst_tuile = sac_des_100_tuile(5) 
            

        lst_des_coordonne_des_plancher = ligne_plancher(2) ### Prend les coordonnees du plancher
        
        lst_rec_c_xy, lst_tuile, k = tuile_dans_les_fabrique(lst_tuile,k,5) ## Dans cette liste il y a lst_rectangle, lst_couleur, lst_coordonne = coordonne des tuile dans les fabriques
        

        abs = 485
        abs1 = 515
        ord = 250 
        ord1 = 280
        Fin_de_manche = False
        lst_rec_c_xy_restantes = [[], [], []] # Dans cette liste il y a lst_rectangle_restant, lst_c_tuiles_restante, lst_coordonnee_tuile_restante
        h = 0
        h1 = 0
        abscisse_rectangle = 15
        abscisse_rectangle1 = 50
        
        abscisse_rectangle2 = 810 
        abscisse_rectangle3 = 845

        nb_malus = [0, 0]
        
        while Fin_de_manche == False:
            
            
            t1 = texte(100,5,"Joueur 1 joue",'red','nw',"Purisa",15)

            zoneclic, x, y = zone_clic(lst_rec_c_xy, lst_rec_c_xy_restantes, False)

            if zoneclic == True: ### clic dans les fabrique

                couleur, nb_carre, lst_c_non_selec, lst_rec_c_xy = efface_rectangle(lst_rec_c_xy, lst_rec_c_xy_restantes, x, y, zoneclic)

                abs, abs1, ord, ord1, lst_rec_c_xy_restantes = tuile_restante(lst_c_non_selec, abs, abs1, ord, ord1, lst_rec_c_xy_restantes)

                if couleur  == "#ed4b6f":
                    p = "Pink"
                    couleur_choisi1 = texte(100,25,p,"black","nw", "Purisa",15)
                else:
                    couleur_choisi1 = texte(100,25,couleur,"black","nw", "Purisa",15)
                                    
                    

            if zoneclic == False: ### clic dans la zone du millieu 

                couleur, nb_carre, lst_c_non_selec, lst_rec_c_xy_restantes = efface_rectangle(lst_rec_c_xy, lst_rec_c_xy_restantes, x, y, zoneclic)

                abs, abs1, ord, ord1, lst_rec_c_xy_restantes = tuile_restante(lst_c_non_selec, abs, abs1, ord, ord1, lst_rec_c_xy_restantes)
            
                if couleur  == "#ed4b6f":
                    p = "Pink"
                    couleur_choisi1 = texte(100,25,p,"black","nw", "Purisa",15)
                else:
                    couleur_choisi1 = texte(100,25,couleur,"black","nw", "Purisa",15)
            
            nombre_tuile_choisi1 = texte(170,25,nb_carre,"black","nw", "Purisa",15)

            h, abscisse_rectangle, abscisse_rectangle1, lst_couleur_esc[0], lst_compte[0], lst_des_tours_de_rangement, nb_malus[0] = transposition_rectangle2(0, couleur, nb_carre, coordonnee_escalier, h, abscisse_rectangle, abscisse_rectangle1, lst_couleur_esc[0], lst_compte[0], lst_des_tours_de_rangement, lst_des_coordonne_des_plancher, nb_malus[0], False)
            
            efface(t1)
            efface(couleur_choisi1)
            efface(nombre_tuile_choisi1)
            if lst_rec_c_xy[0] == [] and lst_rec_c_xy[1] == [] and lst_rec_c_xy[2] == [] and lst_rec_c_xy_restantes[0] == [] and lst_rec_c_xy_restantes[1] == [] and lst_rec_c_xy_restantes[2] == []:
                break
            
            


            lst_rec_c_xy, lst_rec_c_xy_restantes, abs, abs1, ord, ord1, h1, lst_couleur_esc[1], lst_compte[1], abscisse_rectangle2, abscisse_rectangle3, nb_malus[1] = bot(1, lst_rec_c_xy, lst_rec_c_xy_restantes, abs, abs1, ord, ord1, h1, abscisse_rectangle2, abscisse_rectangle3, lst_couleur_esc[1], lst_compte[1], lst_des_tours_de_rangement, lst_des_coordonne_des_plancher, coordonnee_escalier2, nb_malus[1])
            
            if lst_rec_c_xy[0] == [] and lst_rec_c_xy[1] == [] and lst_rec_c_xy[2] == [] and lst_rec_c_xy_restantes[0] == [] and lst_rec_c_xy_restantes[1] == [] and lst_rec_c_xy_restantes[2] == []:
                break
        
        lst_des_tours_de_rangement, lst_couleur_esc, lst_compte, lst_comptage, score, tuile_visites_tous = mur_de_rangement(lst_dictionnaire_2mur, lst_couleur_esc, lst_des_tours_de_rangement, lst_compte, lst_comptage, score, tuile_visites_tous)
        
        

        if nb_malus[0] > 7:
            nb_malus[0] = 6
        if nb_malus[1] > 7:
            nb_malus[1] = 6
        if nb_malus[0] != 0:
            nb_malus[0] -= 1
        if nb_malus[1] != 0:
            nb_malus[1] -= 1
        
        score[0] = score[0] - lst_point_malus[nb_malus[0]]
        score[1] = score[1] - lst_point_malus[nb_malus[1]]
        efface(score_joueur1)
        efface(score_joueur2)
        score_joueur1 = texte(100,260,score[0],"Yellow","nw", "Impact",15)
        score_joueur2 = texte(895,260,score[1],"Yellow","nw", "Impact",15)

        partie_finie = verification(lst_comptage)
        if partie_finie == True:
            efface(score_joueur1)
            efface(score_joueur2)

    score, lst_ligne_remplie = comptage_final(lst_comptage, score)
    efface(score_joueur1)
    efface(score_joueur2)
    score_joueur1 = texte(100,260,score[0],"Yellow","nw", "Impact",15)
    score_joueur2 = texte(895,260,score[1],"Yellow","nw", "Impact",15)
    if score[0] > score[1]:
        texte(465,175,"Joueur 1 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)
    if score[0] < score[1]:
        texte(465,175,"Joueur 2 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)
    if score[0] == score[1]:
        if lst_ligne_remplie[0] > lst_ligne_remplie[1]:
            texte(465,175,"Joueur 1 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)
        if lst_ligne_remplie[0] < lst_ligne_remplie[1]:
            texte(465,175,"Joueur 2 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)
        if lst_ligne_remplie[0] == lst_ligne_remplie[1]:
            texte(450,175,"Tout les Joueur ont gagner ! Bravo à vous !","Yellow","nw", "Impact",20)



        
    attente_clic()
    
    ferme_fenetre()

########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################

def partie_joueur_contre_joueur():


    cree_fenetre(1300, 1200,)
    
    plateau_entier(2) # Création du plateau

    score_joueur1 = texte(100,260,0,"Yellow","nw", "Impact",15)
    score_joueur2 = texte(895,260,0,"Yellow","nw", "Impact",15)
    tuile_visites_tous = [set(), set()]

    score = [0,0] 
    
    lst_comptage = [
                    [[None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None] ],

                    [[None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None]]
                    ]

    coordonnee_escalier, coordonnee_escalier2 = escaliers(2) # Création d'escalier avec prise de leur coordonnee

    lst_tuile = sac_des_100_tuile(5) 
    k = 10
    lst_dictionnaire_2mur = tour_de_rangement(2)
    
    lst_des_tours_de_rangement = [
            
                [ [], [], [], [], [] ], ### liste des rectangles des escaliers Joueur 1      
                [ [], [], [], [], [] ], ### liste des couleurs remplis dans la tour de rangement Joueur 1

                [ [], [], [], [], [] ], ### liste des rectangles des escaliers Joueur 2 
                [ [], [], [], [], [] ]  ### liste des couleurs remplis dans la tour de rangement Joueur 2

                                    ]

    ### Liste des couleurs dans les escaliers

    lst_couleur_esc = [ [[], [], [], [], []], [[], [], [], [], []] ]
    

    ### Le nombre de tuiles dans chaque escalier mis dans des sous listes

    lst_compte = [ [ [], [], [], [], [] ], [ [], [], [], [], [] ] ]

    lst_point_malus = [1, 2, 4, 6, 8, 11, 14]

    k = 100
    partie_finie = False
    while partie_finie == False:
        
        if lst_tuile == []:
            
            k = 100
            lst_tuile = sac_des_100_tuile(5) 

        lst_des_coordonne_des_plancher = ligne_plancher(2) ### Prend les coordonnees du plancher
        lst_rec_c_xy, lst_tuile, k = tuile_dans_les_fabrique(lst_tuile,k,5) ## Dans cette liste il y a lst_rectangle, lst_couleur, lst_coordonne = coordonne des tuile dans les fabriques
        

        abs = 485
        abs1 = 515
        ord = 250 
        ord1 = 280
        Fin_de_manche = False
        lst_rec_c_xy_restantes = [[], [], []] # Dans cette liste il y a lst_rectangle_restant, lst_c_tuiles_restante, lst_coordonnee_tuile_restante
        h = 0
        h1 = 0
        abscisse_rectangle = 15
        abscisse_rectangle1 = 50
        
        abscisse_rectangle2 = 810 
        abscisse_rectangle3 = 845

        nb_malus = [0,0]

        while Fin_de_manche == False:
            t1 = texte(100,5,"Joueur 1 joue",'red','nw',"Purisa",15)



            zoneclic, x, y = zone_clic(lst_rec_c_xy, lst_rec_c_xy_restantes, False)

            if zoneclic == True: # fabrique 

                couleur, nb_carre, lst_c_non_selec, lst_rec_c_xy = efface_rectangle(lst_rec_c_xy, lst_rec_c_xy_restantes, x, y, zoneclic)

                abs, abs1, ord, ord1, lst_rec_c_xy_restantes = tuile_restante(lst_c_non_selec, abs, abs1, ord, ord1, lst_rec_c_xy_restantes)
                

                if couleur  == "#ed4b6f":
                    p = "Pink"
                    couleur_choisi1 = texte(100,25,p,"black","nw", "Purisa",15)
                else:
                    couleur_choisi1 = texte(100,25,couleur,"black","nw", "Purisa",15)
                                
                nombre_tuile_choisi1 = texte(170,25,nb_carre,"black","nw", "Purisa",15)
                

            if zoneclic == False: # millieu 

                couleur, nb_carre, lst_c_non_selec, lst_rec_c_xy_restantes = efface_rectangle(lst_rec_c_xy, lst_rec_c_xy_restantes, x, y, zoneclic)

                abs, abs1, ord, ord1, lst_rec_c_xy_restantes = tuile_restante(lst_c_non_selec, abs, abs1, ord, ord1, lst_rec_c_xy_restantes)
                
                
                if couleur  == "#ed4b6f":
                    p = "Pink"
                    couleur_choisi1 = texte(100,25,p,"black","nw", "Purisa",15)
                else:
                    couleur_choisi1 = texte(100,25,couleur,"black","nw", "Purisa",15)
            
                nombre_tuile_choisi1 = texte(170,25,nb_carre,"black","nw", "Purisa",15)

            
            h, abscisse_rectangle, abscisse_rectangle1, lst_couleur_esc[0], lst_compte[0], lst_des_tours_de_rangement, nb_malus[0] = transposition_rectangle2(0, couleur, nb_carre, coordonnee_escalier, h, abscisse_rectangle, abscisse_rectangle1, lst_couleur_esc[0], lst_compte[0], lst_des_tours_de_rangement, lst_des_coordonne_des_plancher, nb_malus[0], False)



            if lst_rec_c_xy[0] == [] and lst_rec_c_xy[1] == [] and lst_rec_c_xy[2] == [] and lst_rec_c_xy_restantes[0] == [] and lst_rec_c_xy_restantes[1] == [] and lst_rec_c_xy_restantes[2] == []:
                break
            efface(t1)
            efface(couleur_choisi1)
            efface(nombre_tuile_choisi1)
            
            
            t2 =texte(1000,5,"Joueur 2 joue",'red','nw',"Purisa",15)


            zoneclic, x, y = zone_clic(lst_rec_c_xy, lst_rec_c_xy_restantes, False)

            if zoneclic == True:

                couleur, nb_carre, lst_c_non_selec, lst_rec_c_xy = efface_rectangle(lst_rec_c_xy, lst_rec_c_xy_restantes, x, y, zoneclic)

                abs, abs1, ord, ord1, lst_rec_c_xy_restantes = tuile_restante(lst_c_non_selec, abs, abs1, ord, ord1, lst_rec_c_xy_restantes)
                
                
                if couleur  == "#ed4b6f":
                    p = "Pink"
                    couleur_choisi2 = texte(1000,25,p,"black","nw", "Purisa",15)
                else:
                    couleur_choisi2 = texte(1000,25,couleur,"black","nw", "Purisa",15)
            
                nombre_tuile_choisi2 = texte(1070,25,nb_carre,"black","nw", "Purisa",15)


        
            if zoneclic == False:

                couleur, nb_carre, lst_c_non_selec, lst_rec_c_xy_restantes = efface_rectangle(lst_rec_c_xy, lst_rec_c_xy_restantes, x, y, zoneclic)

                abs, abs1, ord, ord1, lst_rec_c_xy_restantes = tuile_restante(lst_c_non_selec, abs, abs1, ord, ord1, lst_rec_c_xy_restantes)
                
                if couleur  == "#ed4b6f":
                    p = "Pink"
                    couleur_choisi2 = texte(1000,25,p,"black","nw", "Purisa",15)
                else:
                    couleur_choisi2 = texte(1000,25,couleur,"black","nw", "Purisa",15)
            
                nombre_tuile_choisi2 = texte(1070,25,nb_carre,"black","nw", "Purisa",15)

            
            h1, abscisse_rectangle2, abscisse_rectangle3, lst_couleur_esc[1], lst_compte[1], lst_des_tours_de_rangement, nb_malus[1] = transposition_rectangle2(1, couleur, nb_carre, coordonnee_escalier2, h1, abscisse_rectangle2, abscisse_rectangle3, lst_couleur_esc[1], lst_compte[1], lst_des_tours_de_rangement, lst_des_coordonne_des_plancher, nb_malus[1], False)
            

            if lst_rec_c_xy[0] == [] and lst_rec_c_xy[1] == [] and lst_rec_c_xy[2] == [] and lst_rec_c_xy_restantes[0] == [] and lst_rec_c_xy_restantes[1] == [] and lst_rec_c_xy_restantes[2] == []:
                break
            efface(t2)
            efface(couleur_choisi2)
            efface(nombre_tuile_choisi2)
        
        efface(t1)
        efface(couleur_choisi1)
        efface(nombre_tuile_choisi1)
            
        efface(t2)
        efface(couleur_choisi2)
        efface(nombre_tuile_choisi2)
        
        lst_des_tours_de_rangement, lst_couleur_esc,lst_compte, lst_comptage, score, tuile_visites_tous = mur_de_rangement(lst_dictionnaire_2mur, lst_couleur_esc, lst_des_tours_de_rangement, lst_compte, lst_comptage, score, tuile_visites_tous)
        




        if nb_malus[0] > 7:
            nb_malus[0] = 6
        if nb_malus[1] > 7:
            nb_malus[1] = 6
        if nb_malus[0] != 0:
            nb_malus[0] -= 1
        if nb_malus[1] != 0:
            nb_malus[1] -= 1
        
        score[0] = score[0] - lst_point_malus[nb_malus[0]]
        score[1] = score[1] - lst_point_malus[nb_malus[1]]
        efface(score_joueur1)
        efface(score_joueur2)
        score_joueur1 = texte(100,260,score[0],"Yellow","nw", "Impact",15)
        score_joueur2 = texte(895,260,score[1],"Yellow","nw", "Impact",15)

        partie_finie = verification(lst_comptage)
        if partie_finie == True:
            efface(score_joueur1)
            efface(score_joueur2)

    score, lst_ligne_remplie = comptage_final(lst_comptage, score)
    efface(score_joueur1)
    efface(score_joueur2)
    score_joueur1 = texte(100,260,score[0],"Yellow","nw", "Impact",15)
    score_joueur2 = texte(895,260,score[1],"Yellow","nw", "Impact",15)
    if score[0] > score[1]:
        texte(465,175,"Joueur 1 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)
    if score[0] < score[1]:
        texte(465,175,"Joueur 2 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)
    if score[0] == score[1]:
        if lst_ligne_remplie[0] > lst_ligne_remplie[1]:
            texte(465,175,"Joueur 1 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)
        if lst_ligne_remplie[0] < lst_ligne_remplie[1]:
            texte(465,175,"Joueur 2 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)
        if lst_ligne_remplie[0] == lst_ligne_remplie[1]:
            texte(450,175,"Tout les Joueur ont gagner ! Bravo à vous !","Yellow","nw", "Impact",20)
    attente_clic()
    
    ferme_fenetre()

##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################

def partie_avec_trois_bot():

    cree_fenetre(1300, 1200,)
    
    plateau_entier(4) # Création du plateau

    score_joueur1 = texte(100,260,0,"Yellow","nw", "Impact",15)
    score_joueur2 = texte(895,260,0,"Yellow","nw", "Impact",15)
    score_joueur3 = texte(100,610,0,"Yellow","nw", "Impact",15)
    score_joueur4 = texte(895,610,0,"Yellow","nw", "Impact",15)
    tuile_visites_tous = [set(), set(), set(), set()]

    score = [0,0,0,0] 
    
    lst_comptage = [
                    [[None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None] ],

                    [[None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None]],

                    [[None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None]],

                    [[None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None], 
                    [None, None, None, None, None]]
                    ]

    coordonnee_escalier = escaliers(4) # Création d'escalier avec prise de leur coordonnee

    lst_tuile = sac_des_100_tuile(9) 
    
    
    lst_dictionnaire_2mur = tour_de_rangement(4)
    
    lst_des_tours_de_rangement = [
            
                [ [], [], [], [], [] ], ### liste des rectangles des escaliers Joueur 1      
                [ [], [], [], [], [] ], ### liste des couleurs remplis dans la tour de rangement Joueur 1

                [ [], [], [], [], [] ], ### liste des rectangles des escaliers Joueur 2 
                [ [], [], [], [], [] ], ### liste des couleurs remplis dans la tour de rangement Joueur 2

                [ [], [], [], [], [] ], ### liste des rectangles des escaliers Joueur 3 
                [ [], [], [], [], [] ], ### liste des couleurs remplis dans la tour de rangement Joueur 3

                [ [], [], [], [], [] ], ### liste des rectangles des escaliers Joueur 4
                [ [], [], [], [], [] ]  ### liste des couleurs remplis dans la tour de rangement Joueur 4

                                    ]

    ### Liste des couleurs dans les escaliers

    lst_couleur_esc = [ [[], [], [], [], []]
                       ,[[], [], [], [], []]
                       ,[[], [], [], [], []]
                       ,[[], [], [], [], []] ]

    ### Le nombre de tuiles dans chaque escalier mis dans des sous listes

    lst_compte = [[[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]]]
    
    lst_point_malus = [1, 2, 4, 6, 8, 11, 14]
    
    k = 180
    partie_finie = False

    while partie_finie == False:

        
        if lst_tuile == []:
            
            k = 180
            lst_tuile = sac_des_100_tuile(9) 
            

        lst_des_coordonne_des_plancher = ligne_plancher(4) ### Prend les coordonnees du plancher
        
        lst_rec_c_xy, lst_tuile, k = tuile_dans_les_fabrique(lst_tuile,k,9) ## Dans cette liste il y a lst_rectangle, lst_couleur, lst_coordonne = coordonne des tuile dans les fabriques
        

        abs = 485
        abs1 = 515
        ord = 250 
        ord1 = 280
        Fin_de_manche = False
        lst_rec_c_xy_restantes = [[], [], []] # Dans cette liste il y a lst_rectangle_restant, lst_c_tuiles_restante, lst_coordonnee_tuile_restante
        h = [0,0,0,0]
        abscisse_rectangle = [[15, 50], [810, 845], [15, 50], [810, 845]]
        

        nb_malus = [0, 0, 0, 0]
        
        while Fin_de_manche == False:
            
            if lst_rec_c_xy[0] == [] and lst_rec_c_xy[1] == [] and lst_rec_c_xy[2] == [] and lst_rec_c_xy_restantes[0] == [] and lst_rec_c_xy_restantes[1] == [] and lst_rec_c_xy_restantes[2] == []:
                    break

            t1 = texte(100,5,"Joueur 1 joue",'red','nw',"Purisa",15)

            zoneclic, x, y = zone_clic(lst_rec_c_xy, lst_rec_c_xy_restantes, False)

            if zoneclic == True: ### clic dans les fabrique

                couleur, nb_carre, lst_c_non_selec, lst_rec_c_xy = efface_rectangle(lst_rec_c_xy, lst_rec_c_xy_restantes, x, y, zoneclic)

                abs, abs1, ord, ord1, lst_rec_c_xy_restantes = tuile_restante(lst_c_non_selec, abs, abs1, ord, ord1, lst_rec_c_xy_restantes)

                if couleur  == "#ed4b6f":
                    p = "Pink"
                    couleur_choisi1 = texte(100,25,p,"black","nw", "Purisa",15)
                else:
                    couleur_choisi1 = texte(100,25,couleur,"black","nw", "Purisa",15)
                                    
                    

            if zoneclic == False: ### clic dans la zone du millieu 

                couleur, nb_carre, lst_c_non_selec, lst_rec_c_xy_restantes = efface_rectangle(lst_rec_c_xy, lst_rec_c_xy_restantes, x, y, zoneclic)

                abs, abs1, ord, ord1, lst_rec_c_xy_restantes = tuile_restante(lst_c_non_selec, abs, abs1, ord, ord1, lst_rec_c_xy_restantes)
            
                if couleur  == "#ed4b6f":
                    p = "Pink"
                    couleur_choisi1 = texte(100,25,p,"black","nw", "Purisa",15)
                else:
                    couleur_choisi1 = texte(100,25,couleur,"black","nw", "Purisa",15)
            
            nombre_tuile_choisi1 = texte(170,25,nb_carre,"black","nw", "Purisa",15)

            h[0], abscisse_rectangle[0][0], abscisse_rectangle[0][1], lst_couleur_esc[0], lst_compte[0], lst_des_tours_de_rangement, nb_malus[0] = transposition_rectangle2(0, couleur, nb_carre, coordonnee_escalier[0], h[0], abscisse_rectangle[0][0], abscisse_rectangle[0][1], lst_couleur_esc[0], lst_compte[0], lst_des_tours_de_rangement, lst_des_coordonne_des_plancher, nb_malus[0], False)
            
            efface(t1)
            efface(couleur_choisi1)
            efface(nombre_tuile_choisi1)
            if lst_rec_c_xy[0] == [] and lst_rec_c_xy[1] == [] and lst_rec_c_xy[2] == [] and lst_rec_c_xy_restantes[0] == [] and lst_rec_c_xy_restantes[1] == [] and lst_rec_c_xy_restantes[2] == []:
                break
            
            
            for i in range(1,4):

                lst_rec_c_xy, lst_rec_c_xy_restantes, abs, abs1, ord, ord1, h[i], lst_couleur_esc[i], lst_compte[i], abscisse_rectangle[i][0], abscisse_rectangle[i][1], nb_malus[i] = bot(i,lst_rec_c_xy, lst_rec_c_xy_restantes, abs, abs1, ord, ord1, h[i], abscisse_rectangle[i][1], abscisse_rectangle[i][1], lst_couleur_esc[i], lst_compte[i], lst_des_tours_de_rangement, lst_des_coordonne_des_plancher, coordonnee_escalier[i], nb_malus[i])
                print(i, nb_malus)
                if lst_rec_c_xy[0] == [] and lst_rec_c_xy[1] == [] and lst_rec_c_xy[2] == [] and lst_rec_c_xy_restantes[0] == [] and lst_rec_c_xy_restantes[1] == [] and lst_rec_c_xy_restantes[2] == []:
                    break
        
        lst_des_tours_de_rangement, lst_couleur_esc, lst_compte, lst_comptage, score, tuile_visites_tous = mur_de_rangement(lst_dictionnaire_2mur, lst_couleur_esc, lst_des_tours_de_rangement, lst_compte, lst_comptage, score, tuile_visites_tous)
        

        if nb_malus[0] > 7:

            nb_malus[0] = 7

        if nb_malus[1] > 7:

            nb_malus[1] = 7

        if nb_malus[0] != 0:

            nb_malus[0] -= 1

        if nb_malus[1] != 0:

            nb_malus[1] -= 1

        if nb_malus[2] > 7:

            nb_malus[2] = 7

        if nb_malus[3] > 7:

            nb_malus[3] = 7

        if nb_malus[2] != 0:

            nb_malus[2] -= 1

        if nb_malus[3] != 0:

            nb_malus[3] -= 1
        
        score[0] = score[0] - lst_point_malus[nb_malus[0]]
        score[1] = score[1] - lst_point_malus[nb_malus[1]]
        score[2] = score[2] - lst_point_malus[nb_malus[2]]
        score[3] = score[3] - lst_point_malus[nb_malus[3]]

        efface(score_joueur1)
        efface(score_joueur2)
        efface(score_joueur3)
        efface(score_joueur4)

        score_joueur1 = texte(100,260,score[0],"Yellow","nw", "Impact",15)
        score_joueur2 = texte(895,260,score[1],"Yellow","nw", "Impact",15)
        score_joueur3 = texte(100,610,score[2],"Yellow","nw", "Impact",15)
        score_joueur4 = texte(895,610,score[3],"Yellow","nw", "Impact",15)

        partie_finie = verification(lst_comptage)
        if partie_finie == True:
            efface(score_joueur1)
            efface(score_joueur2)
            efface(score_joueur3)
            efface(score_joueur4)

    score, lst_ligne_remplie = comptage_final(lst_comptage, score)
    efface(score_joueur1)
    efface(score_joueur2)
    efface(score_joueur3)
    efface(score_joueur4)
    score_joueur1 = texte(100,260,score[0],"Yellow","nw", "Impact",15)
    score_joueur2 = texte(895,260,score[1],"Yellow","nw", "Impact",15)
    score_joueur3 = texte(100,610,score[2],"Yellow","nw", "Impact",15)
    score_joueur4 = texte(895,610,score[3],"Yellow","nw", "Impact",15)

    a = False
    if score[0] > score[1]:
        if score[0] > score[2]:
            if score[0] > score[3]:
                a = True
                texte(465,175,"Joueur 1 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)

    if score[1] > score[0]:
        if score[1] > score[2]:
            if score[1] > score[3]:
                a = True
                texte(465,175,"Joueur 2 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)

    if score[2] > score[0]:
        if score[2] > score[1]:
            if score[2] > score[3]:
                a = True
                texte(465,175,"Joueur 3 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)
    if score[3] > score[0]:
        if score[3] > score[1]:
            if score[3] > score[2]:
                a = True
                texte(465,175,"Joueur 4 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)

    if a == False:
        if lst_ligne_remplie[0] > lst_ligne_remplie[1]:
            if lst_ligne_remplie[0] > lst_ligne_remplie[2]:
                if lst_ligne_remplie[0] > lst_ligne_remplie[3]:
                    a = True 
                    texte(465,175,"Joueur 1 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)

        if lst_ligne_remplie[1] < lst_ligne_remplie[0]:
            if lst_ligne_remplie[1] > lst_ligne_remplie[2]:
                if lst_ligne_remplie[1] > lst_ligne_remplie[3]:
                    a = True
                    texte(465,175,"Joueur 2 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)

        if lst_ligne_remplie[2] > lst_ligne_remplie[0]:
            if lst_ligne_remplie[2] > lst_ligne_remplie[1]:
                if lst_ligne_remplie[2] > lst_ligne_remplie[3]:
                    a = True
                    texte(465,175,"Joueur 3 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)

        if lst_ligne_remplie[3] > lst_ligne_remplie[0]:
            if lst_ligne_remplie[3] > lst_ligne_remplie[1]:
                if lst_ligne_remplie[3] > lst_ligne_remplie[2]:
                    a = True
                    texte(465,175,"Joueur 4 à gagner ! Bravo à toi !","Yellow","nw", "Impact",20)

        if a == False:
            texte(450,175,"Tout les Joueur ont gagner ! Bravo à vous !","Yellow","nw", "Impact",20)



        
    attente_clic()
    
    ferme_fenetre()

##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################

def comptage_score(lst_des_tours_de_rangement, lst_comptage, score, tuiles_visites, s):
    
    l = lst_des_tours_de_rangement
    
    
    lst_couleur = [
                    ['Blue', 'Yellow', 'Orange', 'Black', '#ed4b6f'], 
                    ['Yellow', 'Orange', 'Black', '#ed4b6f', 'Blue'],
                    ['Orange', 'Black', '#ed4b6f', 'Blue', 'Yellow'],
                    ['Black', '#ed4b6f', 'Blue', 'Yellow', 'Orange'], 
                    ['#ed4b6f', 'Blue', 'Yellow', 'Orange', 'Black']
                    ]

    
    for i in range(len(l[s])):
        
        for j in range(len(l[s][i])):
            if not ((i,j) in tuiles_visites):
                
                for x in range(len(lst_couleur[i])):
                    if l[s][i][j] == lst_couleur[i][x]:

                        
                        lst_comptage[i][x] = lst_couleur[i][x]

                        tuiles_visites.add((i,j))
                        
                        score = comptage_tout(lst_comptage, i, x, score)
    
    return lst_comptage, tuiles_visites, score

def comptage_tout(lst_comptage, i, j, score):

    score += 1
    k = j
    c = j
    p = i
    g = i
    
    
    while k < 4:

        if lst_comptage[i][k+1] != None:
            score += 1
        else: 
            break 
        k += 1
        if k == 4:
            break
    
    while c > 0:

        if lst_comptage[i][c-1] != None:
            score += 1
        else: 
            break 
        c -= 1
        if c == 0:
            break
    
    while p < 4:
        
        if lst_comptage[p+1][j] != None:
            score += 1
        else: 
            break 
        p += 1
        if p == 4:
            break
    
    while g > 0:

        if lst_comptage[g-1][j] != None:
            
            score += 1
            
        else: 
            break 
        g -= 1
        if g == 0:
            break
    
    return score

def verification(lst_comptage):

    partie_finie = False
    for j in range(len(lst_comptage)):
        
        if partie_finie == True:
            break
        for l in range(len(lst_comptage[j])):
            
            if not  (None in lst_comptage[j][l]):
                
                partie_finie = True
                break
    
    return partie_finie
    
def comptage_final(lst_comptage, score):
    
    lst_ligne_remplie = [ [0], [0], [0], [0]]

    for j in range(len(lst_comptage)):
        
        for l in range(len(lst_comptage[j])):
            
            if not  (None in lst_comptage[j][l]):
                
                score[j] += 2
                lst_ligne_remplie[j][0] += 1
            compte_colonne = 0

        for i in range(5):
            
            for c in range(5):
                
                if lst_comptage[j][0+c][i] != None:
                    
                    compte_colonne += 1

        if compte_colonne == 5:
            
            score[j] += 7
    
    liste_des_couleurs = ['Blue','Yellow','Orange','#ed4b6f','Black']
    for j in range(len(lst_comptage)):

        for i in liste_des_couleurs:
            nb_couleur = 0
            
            for l in range(len(lst_comptage[j])):

                if i in lst_comptage[j][l]:

                    nb_couleur += 1
            if nb_couleur == 5:
                
                score[j] += 10
    
    return score, lst_ligne_remplie

if __name__ == "__main__":
    
    


    #partie_avec_trois_bot()
    #partie_avec_un_bot()
    partie_joueur_contre_joueur()
    




        