from upemtk import *

def fond_du_jeu():

    rectangle(0,0,3000,3000,couleur="#01743d",remplissage="#01743d")


def cercle_fabrique(n):
    "Dessine les fabriques"
    if n == 2:
        t = 5
    else:
        t = 9
    abscisse = 100
    for i in range(t):  
        cercle(abscisse,100,50,'black',epaisseur=4)
        if n == 2:
            abscisse += 275
        else:
            abscisse += 130

def plateau_des_joueurs(n):
    "Dessine les plateaux des joueurs"
    
    rectangle(10,250,465,550,'White','#920018',epaisseur=2)
    texte(400, 560, 'Joueur 1', "Yellow",'nw', 'Impact', 15)
    texte(805, 560, 'Joueur 2', "Yellow",'nw', 'Impact', 15)
    rectangle(805,250,1260,550,'White','#920018',epaisseur=2)
    if n != 2:
        rectangle(10,600,465,900,'White','#920018',epaisseur=2)
        texte(400,910, 'Joueur 3', 'Yellow','nw', 'Impact',15)
        texte(805,910, 'Joueur 4', 'Yellow','nw', 'Impact',15)
        rectangle(805,600,1260,900,'White','#920018',epaisseur=2)

def tour_de_rangement(n):
    "Dessine les tours de rangement"

    lst_dictionnaire_2mur = []
    lst_dictionnaire_mur1 = []
    lst_dictionnaire_mur2 = []
    lst_dictionnaire_mur3 = []
    lst_dictionnaire_mur4 = []

    lst_couleur = [
                   ['Blue', 'Yellow', 'Orange', 'Black', '#ed4b6f'], 
                   ['Yellow', 'Orange', 'Black', '#ed4b6f', 'Blue'],
                   ['Orange', 'Black', '#ed4b6f', 'Blue', 'Yellow'],
                   ['Black', '#ed4b6f', 'Blue', 'Yellow', 'Orange'], 
                   ['#ed4b6f', 'Blue', 'Yellow', 'Orange', 'Black']
                   ]

    abscisse_plateau_joueur = 435
    abscisse_plateau_joueur0 = 460
    abscisse = abscisse_plateau_joueur
    abscisse1 = abscisse_plateau_joueur0
    ordonne = 260
    ordonne1 = 290
    for x in range(n):
        if x == 0 or x == 1:
            ordonne = 260
            ordonne1 = 290
            
        else:
            ordonne = 610
            ordonne1 = 640
        if x == 0 or x == 2:
                abscisse = 435
                abscisse1 = 460
                abscisse_plateau_joueur = abscisse
                abscisse_plateau_joueur0 = abscisse1
        else:
            abscisse = 1230 
            abscisse1 = 1255
            abscisse_plateau_joueur = abscisse
            abscisse_plateau_joueur0 = abscisse1
        for i in range(5):
            a = dict()
            b = dict()
            c = dict()
            d = dict()
            lst = []
            for j in range(5):
                
                rectangle(abscisse,ordonne,abscisse1,ordonne1,lst_couleur[i][j],remplissage='#b4bcc8',epaisseur=3)

                if x == 0:
                    a[lst_couleur[i][j]] = [(abscisse, ordonne), (abscisse1, ordonne1)]
                
                if x == 1:
                    
                    b[lst_couleur[i][j]] = [(abscisse, ordonne), (abscisse1, ordonne1)]
                
                if x == 2:
                    c[lst_couleur[i][j]] = [(abscisse, ordonne), (abscisse1, ordonne1)]
                
                if x == 3:
                    d[lst_couleur[i][j]] = [(abscisse, ordonne), (abscisse1, ordonne1)]
                    
                abscisse -= 35
                abscisse1 -= 35

            ordonne += 50
            ordonne1 += 50
            
            abscisse = abscisse_plateau_joueur
            abscisse1 = abscisse_plateau_joueur0

            if x == 0:
                lst.append(a)
                lst_dictionnaire_mur1.append(lst)
            if x == 1:
                lst.append(b)
                lst_dictionnaire_mur2.append(lst)
            if x == 2:
                lst.append(c)
                lst_dictionnaire_mur3.append(lst)
            if x == 3:
                lst.append(d)
                lst_dictionnaire_mur4.append(lst)
        

    lst_dictionnaire_2mur.append(lst_dictionnaire_mur1)
    lst_dictionnaire_2mur.append(lst_dictionnaire_mur2)

    if n != 2:
        lst_dictionnaire_2mur.append(lst_dictionnaire_mur3)
        lst_dictionnaire_2mur.append(lst_dictionnaire_mur4)
   
    return lst_dictionnaire_2mur
    
    
def fleche_ligne(n):
    "Dessine les flêches près des tours de rangement"

    ordonne = 265   
    ordonne1 = 285
    for i in range(5):
        ligne(275,ordonne,275,ordonne1,'blue',2)
        ligne(1070,ordonne,1070,ordonne1,'blue',2)
        ordonne += 50
        ordonne1 += 50
    
    ordonne = 265
    ordonne1 = 285
    ordonne2 = 275
    for j in range(5):
        ligne(275,ordonne,285,ordonne2,'blue',2)
        ligne(275,ordonne1,285,ordonne2,'blue',2)
        ligne(1070,ordonne,1080,ordonne2,'blue',2)
        ligne(1070,ordonne1,1080,ordonne2,'blue',2)
        ordonne += 50 
        ordonne1 += 50 
        ordonne2 += 50
    if n != 2:
        ordonne = 615  
        ordonne1 = 635
        for i in range(5):
            ligne(275,ordonne,275,ordonne1,'blue',2)
            ligne(1070,ordonne,1070,ordonne1,'blue',2)
            ordonne += 50
            ordonne1 += 50

        ordonne = 615
        ordonne1 = 635
        ordonne2 = 625
        for j in range(5):
            ligne(275,ordonne,285,ordonne2,'blue',2)
            ligne(275,ordonne1,285,ordonne2,'blue',2)
            ligne(1070,ordonne,1080,ordonne2,'blue',2)
            ligne(1070,ordonne1,1080,ordonne2,'blue',2)
            ordonne += 50 
            ordonne1 += 50 
            ordonne2 += 50


def escaliers(x):
    "Dessine les cases pour placer les tuiles dans le plateau des joueurs"

    abscisse = 255
    abscisse1 = 220
    ordonne = 260
    ordonne1 = 290

    abscisse2 = 1050
    abscisse3 = 1015

    ordonne2 = 610
    ordonne3 = 640

    lst_coordonnee_escalier = [[],[],[],[],[]]
    lst_coordonnee_escalier2 = [[],[],[],[],[]]
    lst_coordonnee_escalier3 = [[],[],[],[],[]]
    lst_coordonnee_escalier4 = [[],[],[],[],[]]

    n = 0
    c = -1
    for i in range(5):
        n += 1
        c += 1
        for j in range(n):

           
            rectangle(abscisse,ordonne,abscisse1,ordonne1,'white','white')
            rectangle(abscisse2,ordonne,abscisse3,ordonne1,'white','white')

            if x == 4:
                rectangle(abscisse, ordonne2, abscisse1, ordonne3, 'white', 'white')
                rectangle(abscisse2, ordonne2, abscisse3, ordonne3, 'white', 'white')

                coordonnee2 = (abscisse,ordonne2)
                coordonnee3 = (abscisse1,ordonne3)

                lst = []

                lst.append(coordonnee2)
                lst.append(coordonnee3)

                lst_coordonnee_escalier3[c].append(lst)

                coordonnee2 = (abscisse2,ordonne2)
                coordonnee3 = (abscisse3,ordonne3)

                lst = []

                lst.append(coordonnee2)
                lst.append(coordonnee3)

                lst_coordonnee_escalier4[c].append(lst)


            coordonnee = (abscisse,ordonne)
            coordonnee1 = (abscisse1,ordonne1)

            lst = []
            
            lst.append(coordonnee)
            lst.append(coordonnee1)

#########################################################################

            lst_coordonnee_escalier[c].append(lst)
            
            coordonnee = (abscisse2, ordonne)
            coordonnee1 = (abscisse3, ordonne1)

            lst = []

            lst.append(coordonnee)
            lst.append(coordonnee1)
            
            lst_coordonnee_escalier2[c].append(lst)
            
            abscisse -= 45
            abscisse1 -= 45
            abscisse2 -= 45
            abscisse3 -= 45

        ordonne += 50
        ordonne1 += 50
        ordonne2 += 50
        ordonne3 += 50
        abscisse = 255
        abscisse1 = 220
        abscisse2 = 1050
        abscisse3 = 1015
    
    if x == 4:
        lst_tout_escalier = []
        
        lst_tout_escalier.append(lst_coordonnee_escalier)
        lst_tout_escalier.append(lst_coordonnee_escalier2)
        lst_tout_escalier.append(lst_coordonnee_escalier3)
        lst_tout_escalier.append(lst_coordonnee_escalier4)
        return lst_tout_escalier
    
    return lst_coordonnee_escalier, lst_coordonnee_escalier2

def ligne_plancher(n):
    "Dessine la ligne des planchers pour les excédant"

    abscisse_rectangle = 285
    abscisse_rectangle1 = 320

    abscisse_rectangle2 = 1080
    abscisse_rectangle3 = 1115

    abscisse_cercle = 303
    abscisse_cercle1 = 1098

    lst_des_coordonne_des_planchers = []
    lst_coordonne_plancher = []
    lst_coordonne_plancher2 = []
    lst_coordonne_plancher3 = []
    lst_coordonne_plancher4 = []

    for i in range(7):
        lst = []
        lst1 = []
        rectangle(abscisse_rectangle,510,abscisse_rectangle1,540,'white','white')
        rectangle(abscisse_rectangle2,510,abscisse_rectangle3,540,'white','white')
        if n == 4:
            rectangle(abscisse_rectangle, 860, abscisse_rectangle1, 890, 'white', 'white')
            rectangle(abscisse_rectangle2, 860, abscisse_rectangle3, 890, 'white', 'white')

            coordonne = (abscisse_rectangle, 860)
            coordonne1 = (abscisse_rectangle1, 860)
            lst.append(coordonne)
            lst.append(coordonne1)
            lst1.append(lst)

            lst_coordonne_plancher3.append(lst1)

            lst = []
            lst1 = []

            coordonne = (abscisse_rectangle2, 860)
            coordonne1 = (abscisse_rectangle3, 890)
            lst.append(coordonne)
            lst.append(coordonne1)
            lst1.append(lst)

            lst_coordonne_plancher4.append(lst1)

            cercle(abscisse_cercle,860,10,'white','white')
            cercle(abscisse_cercle1,860,10,'white','white')

        lst = []
        lst1 = []

        coordonne = (abscisse_rectangle, 510) 
        coordonne1 = (abscisse_rectangle1, 540)
        lst.append(coordonne)
        lst.append(coordonne1)
        lst1.append(lst)

        lst_coordonne_plancher.append(lst1)

#####################################################################

        lst = []
        lst1 = []

        coordonne = (abscisse_rectangle2, 510) 
        coordonne1 = (abscisse_rectangle3, 540)
        lst.append(coordonne)
        lst.append(coordonne1)
        lst1.append(lst)

        lst_coordonne_plancher2.append(lst1)


        cercle(abscisse_cercle,510,10,'white','white')
        cercle(abscisse_cercle1,510,10,'white','white')
        
        abscisse_rectangle -= 45
        abscisse_rectangle1 -= 45

        abscisse_rectangle2 -= 45
        abscisse_rectangle3 -= 45

        abscisse_cercle -= 45
        abscisse_cercle1 -= 45
    
    lst_des_coordonne_des_planchers.append(lst_coordonne_plancher)
    lst_des_coordonne_des_planchers.append(lst_coordonne_plancher2)
    if n == 4:
        lst_des_coordonne_des_planchers.append(lst_coordonne_plancher3)
        lst_des_coordonne_des_planchers.append(lst_coordonne_plancher4)
    texte_ligne_plancher(n)
    
    return lst_des_coordonne_des_planchers

def texte_ligne_plancher(n):
    "Ecris les chiffres de perte de points dans la ligne de plancher"

    abscisse_texte = 300
    abscisse_texte1 = 1095
    for i in range(2):
        texte(abscisse_texte,500,-3,'Red','nw',"Purisa",8)
        texte(abscisse_texte1,500,-3,'Red','nw',"Purisa",8)
        if n == 4: 
            texte(abscisse_texte,850,-3,'Red','nw',"Purisa",8)
            texte(abscisse_texte1,850,-3,'Red','nw',"Purisa",8)
        abscisse_texte -= 45
        abscisse_texte1 -= 45

    for j in range(3):
            texte(abscisse_texte,500,-2,'Red','nw',"Purisa",8)
            texte(abscisse_texte1,500,-2,'Red','nw',"Purisa",8)
            if n == 4:
                texte(abscisse_texte,850,-2,'Red','nw',"Purisa",8)
                texte(abscisse_texte1,850,-2,'Red','nw',"Purisa",8)
            abscisse_texte -= 45
            abscisse_texte1 -= 45

    for k in range(2):
        texte(abscisse_texte,500,-1,'Red','nw',"Purisa",8)
        texte(abscisse_texte1,500,-1,'Red','nw',"Purisa",8)
        if n == 4:
            texte(abscisse_texte,850,-1,'Red','nw',"Purisa",8)
            texte(abscisse_texte1,850,-1,'Red','nw',"Purisa",8)
        abscisse_texte -= 45
        abscisse_texte1 -= 45

def score_joueur(n):
    texte(40,260,"Score" ,'yellow','nw',"Impact",14)
    texte(835,260,"Score",'yellow','nw',"Impact",14)
    if n == 4:
        texte(40,610,"Score" ,'yellow','nw',"Impact",14)
        texte(835,610,"Score",'yellow','nw',"Impact",14)

    
def plateau_entier(n):
    "Prend toute les fonction de ce programme"
    
    fond_du_jeu()
    plateau_des_joueurs(n)
    cercle_fabrique(n)
    fleche_ligne(n)
    escaliers(n)
    score_joueur(n)
    
if __name__ == "__main__":

    cree_fenetre(1300, 1000,)
    plateau_entier(4)
    a = tour_de_rangement(4)
    
    ligne_plancher(4)
    attente_clic()
    ferme_fenetre()
    
    #def zone_tuile_restante():
    
        #rectangle(475,250,795,550)
