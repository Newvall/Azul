from typing import overload
from upemtk import *
from Azul_Fonction_jeu import * 

def fond_du_menu():
    rectangle(0,0,2000,2000,couleur= "black", remplissage= "#01743d", epaisseur=5)

def titre_azul():
    texte(410,100,"A","blue","nw","Mv boli",50)
    texte(460,100,"Z","orange","nw","Mv boli",50)
    texte(510,100,"U","yellow","nw","Mv boli",50)
    texte(560,100,"L","pink","nw","Mv boli",50)

def mode_de_jeu():
    rectangle(200,430,350,300,remplissage="red",couleur="black",epaisseur=5)
    texte(245,330,"1vs1","black","nw","Purisa",20)
    texte(220,360,"contre joueur","black","nw","Purisa",15)

    rectangle(650,430,800,300,remplissage="red",couleur="black",epaisseur=5)
    texte(695,330,"1vs1","black","nw","Purisa",20)
    texte(680,360,"contre bot","black","nw","Purisa",15)

    rectangle(570,630,420,500,remplissage="red",couleur="black",epaisseur=5)
    texte(465,530,"1vs3","black","nw","Purisa",20)
    texte(450,560,"contre bots","black","nw","Purisa",15)

def lancer_menu():
    fond_du_menu()
    titre_azul()
    mode_de_jeu()
    
    


def clic_mode_jeu ():
    papier_toilette = False
    while papier_toilette == False:
        a = attente_clic()
        x = a[0]
        y = a[1]
        if 200 <= x <=350 and 300 <= y <= 430:
            return 1
        if 650 <= x <= 800 and 300 <= y <= 430:
            return 2
        if 420 <= x <= 570 and 500 <= y <= 630:
            return 3

if __name__ == "__main__":
    
    
    cree_fenetre(1000,700)
    lancer_menu()
    a = clic_mode_jeu()
    if a == 1 :
        ferme_fenetre()
        partie_joueur_contre_joueur()
    if a == 2:
        ferme_fenetre()
        partie_avec_un_bot()
    if a == 3:
        ferme_fenetre()
        partie_avec_trois_bot()