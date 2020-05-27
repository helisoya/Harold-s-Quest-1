# Projet NSI : Jeu Interactif


# Importations
import tkinter
import time
from tkinter import simpledialog
from tkinter import messagebox
from math import *
import random

import pygame
from pygame import mixer
pygame.init()



# Création de la fenetre

fenetre = tkinter.Tk()
fenetre.title("Projet NSI : Jeu Interactif")
fenetre.iconbitmap(r"icone.ico")

# Création des Labels !!! Créer ici sinon ca risque de crash !!!

#----Decor/image-----
Decor = tkinter.Label(fenetre, text="Ceci est l'emplacement des images, \n utilisez votre imagination \n (°-°)\n \|/ \n/|", bg="grey")       #C'est l'endroit ou on met les images



#----Perso-----
NomPerso = tkinter.Label(fenetre, text="")   # C'est l'endroit ou on met les noms

# Noms random au cas ou on n'en entre pas

tabnom = ["Billy",
          "Figurant n°42",
          "Karl",
          "Rambo",
          "Joseph",
          "Le type qui n'a pas choisi de nom",
          "Moi",
          "Robin",
          "Alfred",
          "Hans"]


# Liste des couleurs des persos

# Joueur = blue
# Dragon = red
# Harold = green
# Chauve-Souris = brown
# Guarde de Disneyland = crimson
# Monstre du Marais = olive
# GARDE = burlywood
# Type Random = tan

#-------Dialogue------
Dialogue = tkinter.Label(fenetre, text="")     #C'est la ou on met les dialogues

Continuer1 = tkinter.Button(fenetre, text=">", bg="grey")          #Ce sont des boutons pour avoir des choix
Continuer2 = tkinter.Button(fenetre, text=">", bg="grey")
Continuer3 = tkinter.Button(fenetre, text=">", bg="grey")

#-----Menu------
NomJeu = tkinter.Label(fenetre, text="Ceci est le projet NSI portant sur un jeu interactif. \n \n Cliquez sur commencer")
Commencer = tkinter.Button(fenetre, text="Commencer", bg="grey")

#------FIN-------
FIN_Desc = tkinter.Label(fenetre, text="FIN")
FIN_Button = tkinter.Button(fenetre, text="Menu Principal", bg="grey")

#----Choix des chapitres-----
DescChoixChap = tkinter.Label(fenetre, text="Commmencez une nouvelle partie \n ou choisissez un chapitre individuellement")
NewGame = tkinter.Button(fenetre, text="Nouvelle Partie", bg="grey")

Chap1 = tkinter.Button(fenetre, text="Chapitre 1", bg="grey")
Chap1_1 = tkinter.Button(fenetre, text="Le Rève", bg="grey")
Chap1_2 = tkinter.Button(fenetre, text="Le Fou", bg="grey")
Chap1_3 = tkinter.Button(fenetre, text="La Maison", bg="grey")
Chap1_4 = tkinter.Button(fenetre, text="La Chambre", bg="grey")

Chap2 = tkinter.Button(fenetre, text="Chapitre 2", bg="grey")
Chap2_1 = tkinter.Button(fenetre, text="Exterieur", bg="grey")
Chap2_2 = tkinter.Button(fenetre, text="Disneyland", bg="grey")
Chap2_3 = tkinter.Button(fenetre, text="Le Marais", bg="grey")

Chap3 = tkinter.Button(fenetre, text="Chapitre 3", bg="grey")
Chap3_1 = tkinter.Button(fenetre, text="La Montagne", bg="grey")
Chap3_2 = tkinter.Button(fenetre, text="Le Château", bg="grey")
Chap3_3 = tkinter.Button(fenetre, text="Le Dragon", bg="grey")
Chap3_4 = tkinter.Button(fenetre, text="Moment Critique", bg="grey")

# Caractéristiques du Personage


# Montée de Niveau (C'est pour se souvenir ou c'est qu'on gagne des niveaux) :

# Meutre de Chauve Souris - (BATTRE LA CHAUVE SOURIS AU CHAPITRE 1) - 1 lv
# Sortir de chez Harold - (FINIR LE CHAPITRE 1) - 1 lv

# Lire un plan correctement - (REUSSIR LE TEST D'INTELLIGENCE 'REPAIRE' AU CHAPITRE 2) - 1 lv
# Fiole d'XP - (LA PRENDRE DANS "LE MARAIS" / "DISNEYLAND" AU CHAPITRE 2) - 1 lv
# Arriver à la montagne du Dragon - (FINIR LE CHAPITRE 2) - 1 lv

# Pacifier GARDE - (ENTRER DANS LE CHATEAU AU CHAPITRE 3) - 1 lv
# Potion magique - (TROUVER LA SALLE SECRETE AU CHAPITRE 3) - 1/2 lv
# Pacifier le Dragon - (BATTRE LE DRAGON AU CHAPITRE 3) - 1 lv


#Stats

nom = "Billy"

niveau = 1

agilite = 0
force = 0
intelligence = 0
charisme = 0

#Opérateurs logiques

Echec = False

Augmentation = False
ChambreHaroldOuverte = False

LockMarais = False
LockDisney = False

NbMauvaisesActions_Disney = 0
VolMarchand = False
MenacePassant = False
VolXP = False

ErreurMarais = 0

PassMarais = False
PassDisney = False
GARDE_Sympa = 0
GARDE_Hostille = 0
portedragon = 0
portebonus = 0
bonusobtenu = False

DragonTue = False
DragonCharme = False
DragonBlaze = False

#Objets

Epee = False
Flute = False
Partitions = False
Pistolet = False
Carte_Monopoly = False



#------------ Sons -----------

#BGM 

BGM_Menu = ("Musique\BGM\Menu.mp3")

BGM_Reve = ("Musique\BGM\Reve.mp3")
BGM_Harold = ("Musique\BGM\Harold.mp3")
BGM_Maison = ("Musique\BGM\Maison.mp3")
BGM_Tension = ("Musique\BGM\Tension.mp3")

BGM_Exterieur = ("Musique\BGM\Exterieur.mp3")
BGM_Marais = ("Musique\BGM\Marais.mp3")
BGM_Ogre = ("Musique\BGM\Ogre.mp3")
BGM_DisneyLand = ("Musique\BGM\DisneyLand.mp3")

BGM_GARDE = ("Musique\BGM\GARDE.mp3")
BGM_Chateau = ("Musique\BGM\Chateau.mp3")
BGM_Dragon = ("Musique\BGM\Dragon.mp3")
BGM_Fin = ("Musique\BGM\Fin.mp3")
BGM_Fuite = ("Musique\BGM\Fuite.mp3")


#SE

SE_Chute = pygame.mixer.Sound("Musique\SE\Chute.wav")
SE_Dragon_Cri = pygame.mixer.Sound("Musique\SE\Dragon_Cri.wav")
SE_Dragon_Feu = pygame.mixer.Sound("Musique\SE\Dragon_Feu.wav")
SE_Epee = pygame.mixer.Sound("Musique\SE\Epee.wav")
SE_Verre = pygame.mixer.Sound("Musique\SE\Verre.wav")
SE_Flute = pygame.mixer.Sound("Musique\SE\Flute.wav")
SE_Flute_EarRape = pygame.mixer.Sound("Musique\SE\Flute_EarRape.wav")
SE_Frappe = pygame.mixer.Sound("Musique\SE\Frappe.wav")
SE_LevelUp = pygame.mixer.Sound("Musique\SE\LevelUp.wav")
SE_Pistolet = pygame.mixer.Sound("Musique\SE\Pistolet.wav")
SE_Pistolet_Degainage = pygame.mixer.Sound("Musique\SE\Pistolet_Degainage.wav")
SE_Porte = pygame.mixer.Sound("Musique\SE\Porte.wav")
SE_Porte_Chateau = pygame.mixer.Sound("Musique\SE\Porte_Chateau.wav")
SE_Saut = pygame.mixer.Sound("Musique\SE\Saut.wav")
SE_Sonnerie = pygame.mixer.Sound("Musique\SE\Sonnerie.wav")
SE_Voiture = pygame.mixer.Sound("Musique\SE\Voiture.wav")
SE_RickRoll = pygame.mixer.Sound("Musique\SE\RickRoll.wav")

#-----------------------------



# Affichage (Il se fait par fonction)


#Les fonctions sont appelé par Chapitre/Partie/Nombre (Aa1 = Chapitre A/Partie a/1er tableau)


#----------------------------------------
#------------- Chapitre A ---------------
#----------- NOM DE CHAPITRE ------------
#----------------------------------------

#----------------------------------------
#-------------- Partie a ----------------
#-------------- LE REVE -----------------
#----------------------------------------


#----------------------------------------
#----------- Sous Partie 1 --------------
#------------- LE COULOIR ---------------
#----------------------------------------


def Aa1(event):
    pygame.mixer.music.load(BGM_Reve)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    #---------------------------
    Chap1.pack_forget()
    Chap2.pack_forget()
    Chap3.pack_forget()
    NewGame.pack_forget()
    Chap1_1.pack_forget()
    Chap1_2.pack_forget()
    Chap1_3.pack_forget()
    Chap1_4.pack_forget()
    DescChoixChap.pack_forget()
    #--------------------------
    Decor.pack(padx=10, pady=10)
    NomPerso.pack(padx=10, pady=10)
    Dialogue.pack(padx=10, pady=10)
    Continuer1.pack(padx=10, pady=10)
    NomPerso.config(text="")
    Dialogue.config(text="J’ouvre les yeux.")
    Continuer1.config(text=">")
    Continuer1.bind("<Button-1>", Aa2)

def Aa2(event):
    Dialogue.config(text="Devant moi se dresse un couloir.")
    Continuer1.bind("<Button-1>", Aa3)

def Aa3(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Ou suis-je ?")
    Continuer1.bind("<Button-1>", Aa4)

def Aa4(event):
    Dialogue.config(text="Je devrais avancer,\n cela répondra peu être à ma question.")
    Continuer1.bind("<Button-1>", Aa5)

def Aa5(event):
    NomPerso.config(text="")
    Dialogue.config(text="J’avance…")
    Continuer1.bind("<Button-1>", Aa6)

def Aa6(event):
    Dialogue.config(text="Le couloir est plutôt long.")
    Continuer1.bind("<Button-1>", Aa7)

def Aa7(event):
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Aa8)

def Aa8(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Oh ?")
    Continuer1.bind("<Button-1>", Aa9)

def Aa9(event):
    NomPerso.config(text="")
    Dialogue.config(text="Il y a une porte juste devant moi.")
    Continuer1.bind("<Button-1>", Aa10)

def Aa10(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Ça doit être la sortie.")
    Continuer1.bind("<Button-1>", Aa11)


def Aa11(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je prend mon courage à deux mains \n et j’ouvre la porte.")
    Continuer1.bind("<Button-1>", Aa12)


#----------------------------------------
#----------- Sous Partie 2 --------------
#------------ LA SALLE ------------------
#----------------------------------------


def Aa12(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Qu’est ce qu’il y a ici ?")
    Continuer1.bind("<Button-1>", Aa13)

def Aa13(event):
    NomPerso.config(text="")
    Dialogue.config(text="La salle semble vide, mais…")
    Continuer1.bind("<Button-1>", Aa14)

def Aa14(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Oh ?")
    Continuer1.bind("<Button-1>", Aa15)

def Aa15(event):
    Dialogue.config(text="Un trésor !")
    Continuer1.bind("<Button-1>", Aa16)

def Aa16(event):
    Dialogue.config(text="Je suis riche !")
    Continuer1.bind("<Button-1>", Aa17)

def Aa17(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je m’avance pour prendre l’or.")
    Continuer1.bind("<Button-1>", Aa18)

def Aa18(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Il faut tout prendre !")
    Continuer1.bind("<Button-1>", Aa19)

def Aa19(event):
    NomPerso.config(text="")
    Dialogue.config(text="J’empoigne une pièce mais…")
    Continuer1.bind("<Button-1>", Aa20)

def Aa20(event):
    SE_Dragon_Cri.play()
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Grr!")
    Continuer1.bind("<Button-1>", Aa21)

def Aa21(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Hein ?")
    Continuer1.bind("<Button-1>", Aa22)

def Aa22(event):
    NomPerso.config(text="")
    Dialogue.config(text="J’ai entendu du bruit, \n je me tourne vers celui-ci et…")
    Continuer1.bind("<Button-1>", Aa23)

def Aa23(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Tension)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Euh…")
    Continuer1.bind("<Button-1>", Aa24)

def Aa24(event):
    Dialogue.config(text="Ah…")
    Continuer1.bind("<Button-1>", Aa25)

def Aa25(event):
    Dialogue.config(text="Tu partages le trésor ?")
    Continuer1.bind("<Button-1>", Aa26)

def Aa26(event):
    SE_Dragon_Cri.play()
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Grr!")
    Continuer1.bind("<Button-1>", Aa27)

def Aa27(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Je vois...")
    Continuer1.bind("<Button-1>", Aa28)

#----------------------------------------
#----------- Sous Partie 3 --------------
#----------- LE DRAGON ------------------
#----------------------------------------


def Aa28(event):
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Grr!")
    Continuer1.bind("<Button-1>", Aa29)

def Aa29(event):
    NomPerso.config(text="")
    Dialogue.config(text="Le dragon se prépare à attaquer.")
    Continuer1.bind("<Button-1>", Aa30)

def Aa30(event):
    Dialogue.config(text="Il va essayer de m’écraser avec sa queue !")
    Continuer1.bind("<Button-1>", Aa31)

def Aa31(event):
    Dialogue.config(text="Je décide…")
    Continuer1.config(text="...d’esquiver son attaque (Agilité 8)")
    Continuer2.config(text="...de contre-attaquer (Force 9)")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.bind("<Button-1>", Aa32a)
    Continuer2.bind("<Button-1>", Aa32b)

#------ Choix A (Agilité)---------

def Aa32a(event):
    global Echec, agilite
    if agilite < 8:
        Echec = True
    Dialogue.config(text="Vite, je peut encore esquiver son attaque.")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer1.bind("<Button-1>", Aa33a)

def Aa33a(event):
    Dialogue.config(text="Je décide donc de sauter par dessus sa queue.")
    Continuer1.bind("<Button-1>", Aa34a)

def Aa34a(event):
    SE_Saut.play()
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Aa35a)

def Aa35a(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Ah !")
    Continuer1.bind("<Button-1>", Aa36a)

def Aa36a(event):
    global Echec
    NomPerso.config(text="")
    if Echec == True:
        SE_Chute.play()
        Dialogue.config(text="Ça n’a pas marché…")
    else:
        Dialogue.config(text="Ça a marché")
    Continuer1.bind("<Button-1>", Aa37a)

def Aa37a(event):
    global Echec
    if Echec == True:
        Dialogue.config(text="Le dragon est trop rapide.")
    else:
        Dialogue.config(text="Mais le dragon est bien trop rapide pour moi.")
    Continuer1.bind("<Button-1>", Aa38)


#-------------------------



#-------- Choix B (force)--------

def Aa32b(event):
    global Echec
    if force < 9:
        Echec = True
    else:
        Echec = False
    Dialogue.config(text="Vite, je doit attaquer avant lui !")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer1.bind("<Button-1>", Aa33b)

def Aa33b(event):
    Dialogue.config(text="Je décide de frapper le dragon de toute mes forces.")
    Continuer1.bind("<Button-1>", Aa34b)

def Aa34b(event):
    SE_Frappe.play()
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Ah !")
    Continuer1.bind("<Button-1>", Aa35b)

def Aa35b(event):
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Aa36b)

def Aa36b(event):
    global Echec
    NomPerso.config(text="Dragon", fg="red")
    if Echec == True:
        Dialogue.config(text="...")
    else:
        Dialogue.config(text="GRR!")
    Continuer1.bind("<Button-1>", Aa37b)

def Aa37b(event):
    global Echec
    NomPerso.config(text="")
    if Echec == True:
        Dialogue.config(text="Ça n’a pas marché, le dragon est résistant")
    else:
        Dialogue.config(text="Ça a marché, mais je crois\n que le dragon est énervé maintenant.")
    Continuer1.bind("<Button-1>", Aa38)

#-------------------------

def Aa38(event):
    SE_Dragon_Cri.play()
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Grr!")
    Continuer1.bind("<Button-1>", Aa39)

def Aa39(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Euh…")
    Continuer1.bind("<Button-1>", Aa40)

def Aa40(event):
    Dialogue.config(text="On peu faire une trêve ?")
    Continuer1.bind("<Button-1>", Aa41)

def Aa41(event):
    NomPerso.config(text="")
    Dialogue.config(text="Le Dragon se prépare à me cracher du feu dessus.")
    Continuer1.bind("<Button-1>", Aa42)

def Aa42(event):
    SE_Dragon_Feu.play()
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="AH!")
    Continuer1.bind("<Button-1>", Aa43)

def Aa43(event):
    pygame.mixer.music.fadeout(400)
    NomPerso.config(text="")
    Dialogue.config(text="Je me réveille dans une tout autre pièce.")
    Continuer1.bind("<Button-1>", Aa44)

def Aa44(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Ou suis-je ?")
    Continuer1.bind("<Button-1>", Ab1)


#----------------------------------------
#-------------- Partie b ----------------
#-------------- LE FOU ------------------
#----------------------------------------


#----------------------------------------
#----------- Sous Partie 1 --------------
#----------- PRE-DIALOGUE ---------------
#----------------------------------------

def Ab1(event):
    #---------------------------
    Chap1.pack_forget()
    NewGame.pack_forget()
    Chap1_1.pack_forget()
    Chap1_2.pack_forget()
    Chap1_3.pack_forget()
    Chap1_4.pack_forget()
    DescChoixChap.pack_forget()
    #--------------------------
    Decor.pack(padx=10, pady=10)
    NomPerso.pack(padx=10, pady=10)
    Dialogue.pack(padx=10, pady=10)
    Continuer1.pack(padx=10, pady=10)
    Continuer1.config(text=">")
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ab2)

def Ab2(event):
    Dialogue.config(text="Je ne sais pas ou je suis, \n mais je peu dire que cet endroit est moche.")
    Continuer1.bind("<Button-1>", Ab3)

def Ab3(event):
    Dialogue.config(text="Bon, au moins il n’y a pas \n de dragon qui essaye de me tuer.")
    Continuer1.bind("<Button-1>", Ab4)

def Ab4(event):
    NomPerso.config(text="")
    Dialogue.config(text="J’entend des bruits de pas en dehors de la pièce")
    Continuer1.bind("<Button-1>", Ab5)

def Ab5(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Qu’est ce que…")
    Continuer1.bind("<Button-1>", Ab6)

def Ab6(event):
    SE_Porte.play()
    NomPerso.config(text="")
    Dialogue.config(text="Tout à coup, la porte s’ouvre \n et un homme rentre dans la pièce.")
    Continuer1.bind("<Button-1>", Ab7)

#----------------------------------------
#----------- Sous Partie 2 --------------
#--------- DIALOGUE PARTIE 1 ------------
#----------------------------------------

def Ab7(event):
    pygame.mixer.music.load(BGM_Harold)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Ah !")
    Continuer1.bind("<Button-1>", Ab8)

def Ab8(event):
    NomPerso.config(text="Vieux Monsieur", fg="green")
    Dialogue.config(text="Ah !")
    Continuer1.bind("<Button-1>", Ab9)

def Ab9(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Qui est-vous ? \n C’est vous qui m’avez kidnappé ?")
    Continuer1.bind("<Button-1>", Ab10)

def Ab10(event):
    NomPerso.config(text="Vieux Monsieur", fg="green")
    Dialogue.config(text="Moi ? Non,\n je n’aurais jamais fais ça !")
    Continuer1.bind("<Button-1>", Ab11)

def Ab11(event):
    Dialogue.config(text="Mais qui êtes vous ? \n Et que faites vous chez moi ?")
    Continuer1.bind("<Button-1>", Ab12)

def Ab12(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Chez vous ? Je ne sais pas.")
    Continuer1.bind("<Button-1>", Ab13)

def Ab13(event):
    Dialogue.config(text="Je me suis réveillé ici.")
    Continuer1.bind("<Button-1>", Ab14)

def Ab14(event):
    NomPerso.config(text="Vieux Monsieur", fg="green")
    Dialogue.config(text="Vraiment ?")
    Continuer1.bind("<Button-1>", Ab15)

def Ab15(event):
    Dialogue.config(text="Mais alors...")
    Continuer1.bind("<Button-1>", Ab16)

#----------------------------------------
#----------- Sous Partie 3 --------------
#--------- DIALOGUE PARTIE 2 ------------
#----------------------------------------

def Ab16(event):
    Dialogue.config(text="J’ai compris !")
    Continuer1.bind("<Button-1>", Ab17)

def Ab17(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Quoi ?")
    Continuer1.bind("<Button-1>", Ab18)

def Ab18(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Je m’appelle Harold, \n c’est moi qui vous ai invoqué !")
    Continuer1.bind("<Button-1>", Ab19)

def Ab19(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Pardon ?")
    Continuer1.bind("<Button-1>", Ab20)

def Ab20(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Oui, je vous ai invoqué, vous, le puissant guerrier, \n afin de m’aider à réaliser une tache difficile !")
    Continuer1.bind("<Button-1>", Ab21)

def Ab21(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Euh...")
    Continuer1.bind("<Button-1>", Ab22)

def Ab22(event):
    NomPerso.config(text="")
    Dialogue.config(text="Il a peu être pris de la drogue.")
    Continuer1.bind("<Button-1>", Ab23)

def Ab23(event):
    NomPerso.config(text="")
    Dialogue.config(text="Cela expliquerai certaines choses.")
    Continuer1.bind("<Button-1>", Ab24)

#----------------------------------------
#----------- Sous Partie 4 --------------
#--------- DIALOGUE PARTIE 3 ------------
#----------------------------------------

def Ab24(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Écoutez, je ne pense pas que je suis votre «guerrier», \n vous devez vous tromper.")
    Continuer1.bind("<Button-1>", Ab25)

def Ab25(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Non, j’en suis sur, c’est bien vous. \n Je vais le prouver.")
    Continuer1.bind("<Button-1>", Ab26)

def Ab26(event):
    global force
    if force < 5:
        Dialogue.config(text="Vous êtes un guerrier médiocre.")
    elif force > 5:
        Dialogue.config(text="Vous êtes un puissant guerrier.")
    else:
        Dialogue.config(text="Vous êtes un guerrier moyen.")
    Continuer1.bind("<Button-1>", Ab27)

def Ab27(event):
    global agilite
    if agilite < 5:
        Dialogue.config(text="Vous n'etes pas agile.")
    elif agilite > 5:
        Dialogue.config(text="Vous êtes très agile.")
    else:
        Dialogue.config(text="Vous êtes moyennement agile.")
    Continuer1.bind("<Button-1>", Ab28)

def Ab28(event):
    global charisme
    if charisme < 5:
        Dialogue.config(text="Vous n'etes pas très charismatique.")
    elif charisme > 5:
        Dialogue.config(text="Vous êtes très charismatique.")
    else:
        Dialogue.config(text="Vous êtes moyennement charismatique.")
    Continuer1.bind("<Button-1>", Ab29)

def Ab29(event):
    global intelligence
    if intelligence < 5:
        Dialogue.config(text="Vous n'etes pas très intelligent.")
    elif intelligence > 5:
        Dialogue.config(text="Vous êtes très intelligent.")
    else:
        Dialogue.config(text="Vous êtes moyennement intelligent.")
    Continuer1.bind("<Button-1>", Ab30)

def Ab30(event):
    NomPerso.config(text="")
    Dialogue.config(text="... \n Tout ceci est vrai.")
    Continuer1.bind("<Button-1>", Ab31)

def Ab31(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Alors, vous acceptez de m’aider ?")
    Continuer1.bind("<Button-1>", Ab32)

def Ab32(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Je n’ai pas vraiment envie de vous aider, \n je ne vous connais pas et…")
    Continuer1.bind("<Button-1>", Ab33)

def Ab33(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Attendez, si je vous paye, \n vous acceptez de m’aider ?")
    Continuer1.bind("<Button-1>", Ab34)

def Ab34(event):
    NomPerso.config(text="")
    Dialogue.config(text="Il veut me payer pour ça ? \n Ça change tout.")
    Continuer1.bind("<Button-1>", Ab35)

def Ab35(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Bon , je pourrai vous aider \n si vous me donner de l’argent.")
    Continuer1.bind("<Button-1>", Ab36)

#----------------------------------------
#----------- Sous Partie 5 --------------
#--------- DIALOGUE PARTIE 4 ------------
#----------------------------------------

def Ab36(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Formidable, je vais tout vous expliquer.")
    Continuer1.bind("<Button-1>", Ab37)

def Ab37(event):
    Dialogue.config(text="Non loin de la, il y a le repère \n du terrible dragon de la province.")
    Continuer1.bind("<Button-1>", Ab38)

def Ab38(event):
    NomPerso.config(text="")
    Dialogue.config(text="Euh...")
    Continuer1.bind("<Button-1>", Ab39)

def Ab39(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je n’ai plus trop envie d’y aller d’un coup.")
    Continuer1.bind("<Button-1>", Ab40)

def Ab40(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Vous êtes sur que c’est dans mes capacités ?")
    Continuer1.bind("<Button-1>", Ab41)

def Ab41(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Bien sur !")
    Continuer1.bind("<Button-1>", Ab42)

def Ab42(event):
    Dialogue.config(text="Je vous demande simplement d’aller \n dans son repère, puis de voler son trésor.")
    Continuer1.bind("<Button-1>", Ab43)

def Ab43(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Je doit voler tout son trésor ? \n Ça va être long.")
    Continuer1.bind("<Button-1>", Ab44)

def Ab44(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Quoi ? Ah non, \n il ne faut pas tout prendre.")
    Continuer1.bind("<Button-1>", Ab45)

def Ab45(event):
    Dialogue.config(text="Je recherche seulement \n le trésor le plus précieux du dragon.")
    Continuer1.bind("<Button-1>", Ab46)

def Ab46(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Qui est ?")
    Continuer1.bind("<Button-1>", Ab47)

def Ab47(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Vous le verrez quand vous le trouverez.")
    Continuer1.bind("<Button-1>", Ab48)

def Ab48(event):
    NomPerso.config(text="")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ab49)

def Ab49(event):
    Dialogue.config(text="Il me cache quelque chose.")
    Continuer1.bind("<Button-1>", Ab50)

def Ab50(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Mais ne vous inquiétez pas, \n vous pourrez prendre de l’or au passage.")
    Continuer1.bind("<Button-1>", Ab51)


#----------------------------------------
#----------- Sous Partie 6 --------------
#--------- DIALOGUE PARTIE 5 ------------
#----------------------------------------

def Ab51(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Vraiment ?")
    Continuer1.bind("<Button-1>", Ab52)

def Ab52(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Oui, bien sur.")
    Continuer1.bind("<Button-1>", Ab53)

def Ab53(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Et si vous tuez le dragon,\n vous aurez droit à un bonus.")
    Continuer1.bind("<Button-1>", Ab54)

def Ab54(event):
    NomPerso.config(text="")
    Dialogue.config(text="Ça, ça m’intéresse, mais…")
    Continuer1.config(text="...Je n’ai pas d’arme")
    Continuer2.config(text="...Il ne me paye pas assez (Charisme 6)")
    Continuer3.config(text="...Ça me va en fait")
    Continuer2.pack(padx=10, pady=10)
    Continuer3.pack(padx=10, pady=10)
    Continuer1.bind("<Button-1>", Ab55a)
    Continuer2.bind("<Button-1>", Ab55b)
    Continuer3.bind("<Button-1>", Ab55c)

#-----------Choix A (Arme)----------

def Ab55a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Hmm…")
    Continuer1.bind("<Button-1>", Ab56a)

def Ab56a(event):
    Dialogue.config(text="Comment je bat le dragon sans arme ?")
    Continuer1.bind("<Button-1>", Ab57a)

def Ab57a(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Quoi ?")
    Continuer1.bind("<Button-1>", Ab58a)

def Ab58a(event):
    Dialogue.config(text="Euh…")
    Continuer1.bind("<Button-1>", Ab59a)

def Ab59a(event):
    global Epee
    Epee = True
    print()
    print("Vous avez obtenu une Epee")
    print()
    Dialogue.config(text="Prenez cette épée pour le tuer.")
    Continuer1.bind("<Button-1>", Ab60)

#----------------------------

#---------Choix B (Paye)------------

def Ab55b(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    global Echec, charisme
    if charisme < 6:
        Echec = True
    else:
        Echec = False
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Combien pensez vous me payez pour cela?")
    Continuer1.bind("<Button-1>", Ab56b)

def Ab56b(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="10000 euros, pourquoi ?")
    Continuer1.bind("<Button-1>", Ab57b)

def Ab57b(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="10000 euros pour risquer ma vie ? \n C’est trop peu pour cette quête.")
    Continuer1.bind("<Button-1>", Ab58b)

def Ab58b(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="…")
    Continuer1.bind("<Button-1>", Ab59b)

def Ab59b(event):
    global Echec, Augmentation
    if Echec == True:
        Dialogue.config(text="Je ne vais pas changer mon prix !")
    else:
        Augmentation = True
        Dialogue.config(text="Très bien, je vous paye 1 millions d’euros.")
    Continuer1.bind("<Button-1>", Ab60)

#----------------------------

def Ab55c(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Ab60(event)

def Ab60(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...Très bien, j’accepte votre marché.")
    Continuer1.bind("<Button-1>", Ab61)

def Ab61(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Génial ! Bonne chance !")
    Continuer1.bind("<Button-1>", Ac1)

#----------------------------------------
#-------------- Partie c ----------------
#-------------- LA MASION ---------------
#----------------------------------------


#----------------------------------------
#----------- Sous Partie 1 --------------
#----------- MAGIE D'HAROLD -------------
#----------------------------------------


def Ac1(event):
    pygame.mixer.music.fadeout(400)
    #---------------------------
    Chap1.pack_forget()
    NewGame.pack_forget()
    Chap1_1.pack_forget()
    Chap1_2.pack_forget()
    Chap1_3.pack_forget()
    Chap1_4.pack_forget()
    DescChoixChap.pack_forget()
    #--------------------------
    Decor.pack(padx=10, pady=10)
    NomPerso.pack(padx=10, pady=10)
    Dialogue.pack(padx=10, pady=10)
    Continuer1.pack(padx=10, pady=10)
    Continuer1.config(text=">")
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Bien, je vais m’en aller alors.")
    Continuer1.bind("<Button-1>", Ac2)

def Ac2(event):
    Dialogue.config(text="Ou est la sortie \n de votre maison Harold ?")
    Continuer1.bind("<Button-1>", Ac3)

def Ac3(event):
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ac4)

def Ac4(event):
    Dialogue.config(text="Il a...disparu.")
    Continuer1.bind("<Button-1>", Ac5)

def Ac5(event):
    Dialogue.config(text="Je suppose que \n je vais sortir tout seul.")
    Continuer1.bind("<Button-1>", Ac6)

#----------------------------------------
#----------- Sous Partie 2 --------------
#------------- LA PORTE -----------------
#----------------------------------------

def Ac6(event):
    pygame.mixer.music.load(BGM_Maison)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    NomPerso.config(text="")
    Dialogue.config(text="Je sort de la pièce.")
    Continuer1.bind("<Button-1>", Ac7)

def Ac7(event):
    Dialogue.config(text="Arrivé dans un couloir,\n je décide de descendre les escaliers.")
    Continuer1.bind("<Button-1>", Ac8)

def Ac8(event):
    Dialogue.config(text="Arrivé en bas,\n je trouve la porte de sortie.")
    Continuer1.bind("<Button-1>", Ac9)

def Ac9(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Enfin !")
    Continuer1.bind("<Button-1>", Ac10)

def Ac10(event):
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ac11)

def Ac11(event):
    NomPerso.config(text="")
    Dialogue.config(text="La porte est verrouillée.")
    Continuer1.bind("<Button-1>", Ac12)

def Ac12(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Euh…")
    Continuer1.bind("<Button-1>", Ac13)

def Ac13(event):
    Dialogue.config(text="Pourquoi la porte \n est-elle fermée à clefs ?")
    Continuer1.bind("<Button-1>", Ac14)

def Ac14(event):
    Dialogue.config(text="On dirais que je vais devoir chercher les clefs, \n je ne peut pas crocheter cette serrure")
    Continuer1.bind("<Button-1>", Ac15)

#----------------------------------------
#----------- Sous Partie 3 --------------
#--------------- SALON ------------------
#----------------------------------------

def Ac15(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je commence par chercher dans le salon.")
    Continuer1.bind("<Button-1>", Ac16)

def Ac16(event):
    Dialogue.config(text="Le salon est bien rangée, je décide de…")
    Continuer1.config(text="...fouiller la table basse")
    Continuer2.config(text="...fouiller le meuble de télévision")
    Continuer3.config(text="...fouiller la bibliothèque")
    Continuer2.pack(padx=10, pady=10)
    Continuer3.pack(padx=10, pady=10)
    Continuer1.bind("<Button-1>", Ac17a)
    Continuer2.bind("<Button-1>", Ac17b)
    Continuer3.bind("<Button-1>", Ac17c)

#------------ Choix A (table basse) -----------

def Ac17a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je décide de fouiller la table basse.")
    Continuer1.bind("<Button-1>", Ac18a)

def Ac18a(event):
    Dialogue.config(text="Je ne trouve rien à part \n la télécommande de la télévision.")
    Continuer1.bind("<Button-1>", Ac19)

#--------------------------------

#------------ Choix B (meuble télévison)-----------

def Ac17b(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je décide de fouiller le meuble de télévision.")
    Continuer1.bind("<Button-1>", Ac18b)

def Ac18b(event):
    Dialogue.config(text="Je trouve différente cassettes, \n mais pas de clefs.")
    Continuer1.bind("<Button-1>", Ac19)

#--------------------------------

#------------ Choix C (biblioteque)-----------

def Ac17c(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je décide de fouiller la bibliothèque.")
    Continuer1.bind("<Button-1>", Ac18c)

def Ac18c(event):
    global Partitions
    Partitions = True
    print()
    print("Vous avez obtenu des Partitions")
    print()
    Dialogue.config(text="Je trouve des partitions étranges.")
    Continuer1.bind("<Button-1>", Ac19)

#--------------------------------

def Ac19(event):
    Dialogue.config(text="Je décide ensuite \n de fouiller le reste du salon.")
    Continuer1.bind("<Button-1>", Ac20)

def Ac20(event):
    Dialogue.config(text="Ne trouvant rien, \n je décide de fouiller la cuisine.")
    Continuer1.bind("<Button-1>", Ac21)

#----------------------------------------
#----------- Sous Partie 4 --------------
#----------- SALLE A MANGER -------------
#----------------------------------------

def Ac21(event):
    Dialogue.config(text="La cuisine, elle aussi, est bien rangée.")
    Continuer1.bind("<Button-1>", Ac22)

def Ac22(event):
    Dialogue.config(text="Je décide de…")
    Continuer1.config(text="...fouiller les placards de provisions")
    Continuer2.config(text="...fouiller la plaque de cuisson")
    Continuer3.config(text="...fouiller le meuble centrale")
    Continuer2.pack(padx=10, pady=10)
    Continuer3.pack(padx=10, pady=10)
    Continuer1.bind("<Button-1>", Ac23a)
    Continuer2.bind("<Button-1>", Ac23b)
    Continuer3.bind("<Button-1>", Ac23c)

#------------ Choix A (placards)-----------

def Ac23a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je décide de fouiller les placards.")
    Continuer1.bind("<Button-1>", Ac24a)

def Ac24a(event):
    Dialogue.config(text="Je ne trouve cependant rien d’intéressant.")
    Continuer1.bind("<Button-1>", Ac25)

#--------------------------------

#------------ Choix B (plaque de cuisson)-----------

def Ac23b(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je décide de regarder \n ce qui cuit sur la plaque de cuisson.")
    Continuer1.bind("<Button-1>", Ac24b)

def Ac24b(event):
    Dialogue.config(text="Evidement, il n’y a pas de clefs.")
    Continuer1.bind("<Button-1>", Ac25)

#--------------------------------

#------------ Choix C (meuble centrale)-----------

def Ac23c(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je décide de fouiller le meuble centrale.")
    Continuer1.bind("<Button-1>", Ac24c)

def Ac24c(event):
    global Flute
    Flute = True
    print()
    print("Vous avez obtenu une Flûte")
    print()
    Dialogue.config(text="Je trouve une étrange flûte.")
    Continuer1.bind("<Button-1>", Ac25)

#--------------------------------

def Ac25(event):
    Dialogue.config(text="Après avoir fouillé plus en détails la cuisine, \n je décide de fouiller la chambre d’Harold.")
    Continuer1.bind("<Button-1>", Ac26)

def Ac26(event):
    Dialogue.config(text="Je monte les escaliers \n et j’arrive devant la porte de sa chambre.")
    Continuer1.bind("<Button-1>", Ac27)

#----------------------------------------
#----------- Sous Partie 5 --------------
#-------- LA PORTE DE CHAMBRE -----------
#----------------------------------------

def Ac27(event):
    Dialogue.config(text="J’ouvre la porte et…")
    Continuer1.bind("<Button-1>", Ac28)

def Ac28(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ac29)

def Ac29(event):
    Dialogue.config(text="La porte...est verrouillée ?")
    Continuer1.bind("<Button-1>", Ac30)

def Ac30(event):
    Dialogue.config(text="Bon, je n’ai pas le choix.")
    Continuer1.bind("<Button-1>", Ac31)

def Ac31(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je décide…")
    Continuer1.config(text="...de crocheter la serrure (Intelligence 4)")
    Continuer2.config(text="...d’enfoncer la porte (Force 6)")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.bind("<Button-1>", Ac32a)
    Continuer2.bind("<Button-1>", Ac32b)

#------------ Choix A (crochetage)-----------

def Ac32a(event):
    global Echec, intelligence
    if intelligence < 4:
        Echec = True
    else:
        Echec = False
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je sort mon matériel de ma poche \n et je commence à crocheter.")
    Continuer1.bind("<Button-1>", Ac33a)

def Ac33a(event):
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ac34a)

def Ac34a(event):
    global Echec, ChambreHaroldOuverte
    if Echec == True:
        ChambreHaroldOuverte = False
        Dialogue.config(text="Je n'arrive pas à le faire.")
        Continuer1.bind("<Button-1>", Ae1)
    else:
        ChambreHaroldOuverte = True
        Dialogue.config(text="Fini.")
        Continuer1.bind("<Button-1>", Ac35)

#--------------------------------

#------------ Choix B (enfoncage)-----------

def Ac32b(event):
    global Echec, force
    if force < 6:
        Echec = True
    else:
        Echec = False
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je décide donc d’enfoncer la porte.")
    Continuer1.bind("<Button-1>", Ac33b)

def Ac33b(event):
    SE_Frappe.play()
    Dialogue.config(text="Je prend mon élan… \n ...et le fonce sur la porte.")
    Continuer1.bind("<Button-1>", Ac34b)

def Ac34b(event):
    global Echec, ChambreHaroldOuverte
    if Echec == True:
        ChambreHaroldOuverte = False
        Dialogue.config(text="Je m'écrase sur la porte sans la briser.")
        Continuer1.bind("<Button-1>", Ae1)
    else:
        ChambreHaroldOuverte = True
        Dialogue.config(text="La porte vole en éclat.")
        Continuer1.bind("<Button-1>", Ac35)

#--------------------------------

def Ac35(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Je peut enfin rentrer dans la chambre.")
    Continuer1.bind("<Button-1>", Ac36)

def Ac36(event):
    SE_Porte.play()
    NomPerso.config(text="")
    Dialogue.config(text="Disant ces mots, \n j’entre dans la chambre.")
    Continuer1.bind("<Button-1>", Ad1)

#----------------------------------------
#-------------- Partie d ----------------
#------------- LA CHAMBRE ---------------
#----------------------------------------

#----------------------------------------
#----------- Sous Partie 1 --------------
#------------ DESCRIPTION  --------------
#----------------------------------------

def Ad1(event):
    global ChambreHaroldOuverte
    ChambreHaroldOuverte = True
    #---------------------------
    Chap1.pack_forget()
    NewGame.pack_forget()
    Chap1_1.pack_forget()
    Chap1_2.pack_forget()
    Chap1_3.pack_forget()
    Chap1_4.pack_forget()
    DescChoixChap.pack_forget()
    #--------------------------
    Decor.pack(padx=10, pady=10)
    NomPerso.pack(padx=10, pady=10)
    Dialogue.pack(padx=10, pady=10)
    Continuer1.pack(padx=10, pady=10)
    Continuer1.config(text=">")
    NomPerso.config(text="")
    Dialogue.config(text="La chambre d’Harold est assez bien rangée.")
    Continuer1.bind("<Button-1>", Ad2)

def Ad2(event):
    Dialogue.config(text="Il y a un ordinateur sur le bureau du fond, \n et une arme posée à coté.")
    Continuer1.bind("<Button-1>", Ad3)

def Ad3(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Pourquoi...")
    Continuer1.bind("<Button-1>", Ad4)

def Ad4(event):
    NomPerso.config(text="???", fg="brown")
    Dialogue.config(text="Squwak !")
    Continuer1.bind("<Button-1>", Ad5)

def Ad5(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Hein ?")
    Continuer1.bind("<Button-1>", Ad6)

def Ad6(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je me tourne vers le bruit et…")
    Continuer1.bind("<Button-1>", Ad7)

def Ad7(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Tension)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Une chauve-souris ?")
    Continuer1.bind("<Button-1>", Ad8)

def Ad8(event):
    NomPerso.config(text="Chauve-Souris", fg="brown")
    Dialogue.config(text="Squwak !")
    Continuer1.bind("<Button-1>", Ad9)

#----------------------------------------
#----------- Sous Partie 2 --------------
#-------------- COMBAT ------------------
#----------------------------------------

def Ad9(event):
    NomPerso.config(text="")
    Dialogue.config(text="La chauve-souris essaye de m’attaquer.")
    Continuer1.bind("<Button-1>", Ad10)

def Ad10(event):
    Dialogue.config(text="J’ai le temps de riposter.")
    Continuer1.bind("<Button-1>", Ad11)

def Ad11(event):
    Dialogue.config(text="Je décide…")
    Continuer1.config(text="...de prendre l’arme et de lui tirer dessus")
    Continuer2.config(text="...de prendre la chaise du bureau \n pour lui jeter dessus")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.bind("<Button-1>", Ad12a)
    Continuer2.bind("<Button-1>", Ad12b)

#------------ Choix A (arme)-----------

def Ad12a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Rapidement, je me jette sur l’arme...")
    Continuer1.bind("<Button-1>", Ad13a)

def Ad13a(event):
    SE_Pistolet.play()
    global Pistolet
    Pistolet = True
    print()
    print("Vous avez obtenu un Pistolet")
    print()
    Dialogue.config(text="…et je tire sur la chauve-souris.")
    Continuer1.bind("<Button-1>", Ad14a)

def Ad14a(event):
    NomPerso.config(text="Chauve-Souris", fg="brown")
    Dialogue.config(text="Sqwiik !")
    Continuer1.bind("<Button-1>", Ad15)

#--------------------------------

#------------ Choix B (chaise)-----------

def Ad12b(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Rapidement, j’attrape la chaise de bureau…")
    Continuer1.bind("<Button-1>", Ad13b)

def Ad13b(event):
    Dialogue.config(text="...et je la jette sur la chauve-souris.")
    Continuer1.bind("<Button-1>", Ad14b)

def Ad14b(event):
    SE_Verre.play()
    Dialogue.config(text="La chauve-souris est propulsée par la fenêtre.")
    Continuer1.bind("<Button-1>", Ad15)

#--------------------------------

def Ad15(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Maison)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="C’est bon.")
    Continuer1.bind("<Button-1>", Ad16)
    LevelUp(event)

def Ad16(event):
    NomPerso.config(text="")
    Dialogue.config(text="Ne sachant ou chercher les clefs, \n je m’approche de l’ordinateur.")
    Continuer1.bind("<Button-1>", Ad17)

def Ad17(event):
    Dialogue.config(text="Étrangement, il est allumé.")
    Continuer1.bind("<Button-1>", Ad18)

#----------------------------------------
#----------- Sous Partie 3 --------------
#-------------- LE PC -------------------
#----------------------------------------

def Ad18(event):
    if Pistolet == False:
        Dialogue.config(text="Il y a toujours l'arme sur la table.")
        Continuer1.config(text="La prendre")
        Continuer2.config(text="La laisser")
        Continuer2.pack(padx=10, pady=10)
        Continuer1.bind("<Button-1>", Ad18a)
        Continuer2.bind("<Button-1>", Ad18b)
    else:
        Dialogue.config(text="Je regarde en détail l’écran.")
        Continuer1.bind("<Button-1>", Ad19)

#-----------Choix A (prendre)------------

def Ad18a(event):
    global Pistolet
    Pistolet = True
    print()
    print("Vous avez obtenu un Pistolet")
    print()
    Dialogue.config(text="Je prend le Pistolet et \n je regarde en détail l’écran...")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer1.bind("<Button-1>", Ad19)

#----------------------------------------

#-----------Choix B (laisser)------------

def Ad18b(event):
    Dialogue.config(text="Je laisse le Pistolet et \n je regarde en détail l’écran..")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer1.bind("<Button-1>", Ad19)

#----------------------------------------

def Ad19(event):
    Dialogue.config(text="Il y écrit qu’il faut \n que je clique sur le bouton \n pour trouver les clefs.")
    Continuer1.bind("<Button-1>", Ad20)

def Ad20(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Ça à l’air invraisemblable.")
    Continuer1.bind("<Button-1>", Ad21)

def Ad21(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je décide...")
    Continuer1.config(text="...de cliquer sur le bouton")
    Continuer2.config(text="...d'ignorer le bouton")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.bind("<Button-1>", Ad22a)
    Continuer2.bind("<Button-1>", Ad22b)

#------------ Choix A (cliquer)-----------

def Ad22a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="L’ordinateur sait ou sont les clefs ?")
    Continuer1.bind("<Button-1>", Ad23a)

def Ad23a(event):
    Dialogue.config(text="Voyons voir...")
    Continuer1.bind("<Button-1>", Ad24a)

def Ad24a(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je clique sur le bouton.")
    Continuer1.bind("<Button-1>", Ad25a)

def Ad25a(event):
    SE_RickRoll.play()
    Dialogue.config(text="Le PC joue une petite musique \n et un écran bleu apparait.")
    Continuer1.bind("<Button-1>", Ad26a)

def Ad26a(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ad27)

#--------------------------------

#------------ Choix B (partir)-----------

def Ad22b(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Ça à l’air suspect.")
    Continuer1.bind("<Button-1>", Ad23b)

def Ad23b(event):
    Dialogue.config(text="Je devrais chercher autre part...")
    Continuer1.bind("<Button-1>", Ad24b)

def Ad24b(event):
    Dialogue.config(text="...Au cas ou.")
    Continuer1.bind("<Button-1>", Ad27)

#--------------------------------

#----------------------------------------
#----------- Sous Partie 4 --------------
#-------------- LE NID ------------------
#----------------------------------------

def Ad27(event):
    NomPerso.config(text="")
    Dialogue.config(text="N’ayant rien trouvé,\n je décide de fouiller la pièce.")
    Continuer1.bind("<Button-1>", Ad28)

def Ad28(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Tien ?")
    Continuer1.bind("<Button-1>", Ad29)

def Ad29(event):
    NomPerso.config(text="")
    Dialogue.config(text="Il y a un nid dans la chambre.")
    Continuer1.bind("<Button-1>", Ad30)

def Ad30(event):
    Dialogue.config(text="Après avoir fouillé le nid, \n je trouve un papier.")
    Continuer1.bind("<Button-1>", Ad31)

def Ad31(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Cherche sous le tapis de la porte d'entrée.")
    Continuer1.bind("<Button-1>", Ad32)

def Ad32(event):
    NomPerso.config(text="")
    Dialogue.config(text="C'est ce qui est marqué sur le papier.")
    Continuer1.bind("<Button-1>", Ad33)

def Ad33(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="A l’entrée ?")
    Continuer1.bind("<Button-1>", Ae1)


#----------------------------------------
#-------------- Partie e ----------------
#-------------- LA SORTIE ---------------
#----------------------------------------

def Ae1(event):
    if ChambreHaroldOuverte == True:
        NomPerso.config(text="")
        Dialogue.config(text="N’ayant pas d’autre piste, \n je me dirige vers l’entrée.")
    else:
        NomPerso.config(text=nom, fg="blue")
        Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ae2)

def Ae2(event):
    if ChambreHaroldOuverte == True:
        Dialogue.config(text="Je trouve facilement le tapis.")
    else:
        Dialogue.config(text="Je suppose que je vais retourner à l'entrée.")
    Continuer1.bind("<Button-1>", Ae3)

def Ae3(event):
    if ChambreHaroldOuverte == True:
        Dialogue.config(text="...")
    else:
        NomPerso.config(text="")
        Dialogue.config(text="Je retourne à l'entrée.")
    Continuer1.bind("<Button-1>", Ae4)

def Ae4(event):
    if ChambreHaroldOuverte == True:
        NomPerso.config(text=nom, fg="blue")
        Dialogue.config(text="Trouvé !")
    else:
        NomPerso.config(text="???", fg="green")
        Dialogue.config(text="J'ai déverrouillé la porte d'entrée !")
    Continuer1.bind("<Button-1>", Ae5)

def Ae5(event):
    if ChambreHaroldOuverte == True:
        Dialogue.config(text="Enfin !")
    else:
        NomPerso.config(text=nom, fg="blue")
        Dialogue.config(text="Euh...Merci.")
    Continuer1.bind("<Button-1>", Ae6)

def Ae6(event):
    SE_Porte.play()
    if ChambreHaroldOuverte == True:
        NomPerso.config(text="")
        Dialogue.config(text="J'ouvre la porte avec les clefs...")
    else:
        NomPerso.config(text="")
        Dialogue.config(text="J'ouvre la porte...")
    Continuer1.bind("<Button-1>", Ae7)

def Ae7(event):
    Dialogue.config(text="...et je sort enfin de la maison.")
    Continuer1.bind("<Button-1>", Ba1)
    LevelUp(event)








#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






#----------------------------------------
#------------- Chapitre B ---------------
#----------- NOM DE CHAPITRE ------------
#----------------------------------------

#----------------------------------------
#-------------- Partie a ----------------
#-------------- EXTERIEUR ---------------
#----------------------------------------


#----------------------------------------
#----------- Sous Partie 1 --------------
#-------------- SORTIE ------------------
#----------------------------------------


def Ba1(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Exterieur)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    #---------------------------
    Chap2.pack_forget()
    NewGame.pack_forget()
    Chap2_1.pack_forget()
    Chap2_2.pack_forget()
    Chap2_3.pack_forget()
    DescChoixChap.pack_forget()
    #--------------------------
    Decor.pack(padx=10, pady=10)
    NomPerso.pack(padx=10, pady=10)
    Dialogue.pack(padx=10, pady=10)
    Continuer1.pack(padx=10, pady=10)
    Continuer1.config(text=">")
    NomPerso.config(text="")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ba2)

def Ba2(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Enfin libre !")
    Continuer1.bind("<Button-1>", Ba3)

def Ba3(event):
    Dialogue.config(text="Bon, j'ai un dragon à tuer.")
    Continuer1.bind("<Button-1>", Ba4)

def Ba4(event):
    Dialogue.config(text="Et je ne sais pas ou le trouver.")
    Continuer1.bind("<Button-1>", Ba5)

def Ba5(event):
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ba6)

def Ba6(event):
    Dialogue.config(text="Il a un repaire dans la région, non ?")
    Continuer1.bind("<Button-1>", Ba7)

def Ba7(event):
    Dialogue.config(text="Je devrais facilement le trouver.")
    Continuer1.bind("<Button-1>", Ba8)

def Ba8(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je regarde au alentour...")
    Continuer1.bind("<Button-1>", Ba9)

def Ba9(event):
    Dialogue.config(text="...mais pas de repaire.")
    Continuer1.bind("<Button-1>", Ba10)

def Ba10(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Mais ou se cache-t-il ?")
    Continuer1.bind("<Button-1>", Ba11)

#----------------------------------------
#----------- Sous Partie 2 --------------
#------------- VOITURE ------------------
#----------------------------------------

def Ba11(event):
    NomPerso.config(text="")
    Dialogue.config(text="Mon regard se pose sur une voiture.")
    Continuer1.bind("<Button-1>", Ba12)

def Ba12(event):
    Dialogue.config(text="Elle doit appartenir à Harold.")
    Continuer1.bind("<Button-1>", Ba13)

def Ba13(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Peu être que je pourrais la lui emprunter.")
    Continuer1.bind("<Button-1>", Ba14)

def Ba14(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je m'approche de la voiture pour l'ouvrir...")
    Continuer1.bind("<Button-1>", Ba15)

def Ba15(event):
    Dialogue.config(text="...mais elle est fermée a clef \n et je ne voit pas les clefs à l'interrieur.")
    Continuer1.bind("<Button-1>", Ba16)

def Ba16(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Dommage...")
    Continuer1.bind("<Button-1>", Ba17)

def Ba17(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je m'éloigne de la voiture pour me diriger \n vers la sortie de la propriété d'Harold.")
    Continuer1.bind("<Button-1>", Ba18)

#----------------------------------------
#----------- Sous Partie 3 --------------
#------------- PANNEAU ------------------
#----------------------------------------

def Ba18(event):
    Dialogue.config(text="Une fois sortis, je regarde autour de moi...")
    Continuer1.bind("<Button-1>", Ba19)

def Ba19(event):
    Dialogue.config(text="...pour remarquer un plan de la région \n sur un des cotés de la route.")
    Continuer1.bind("<Button-1>", Ba20)

def Ba20(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Parfait, un plan.")
    Continuer1.bind("<Button-1>", Ba21)

def Ba21(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je m'avance vers le plan.")
    Continuer1.bind("<Button-1>", Ba22)

def Ba22(event):
    Dialogue.config(text="Je décide de chercher...")
    Continuer1.config(text="...le mot 'Dragon' (Intelligence 4)")
    Continuer2.config(text="...le mot 'repaire' (Intelligence 6)")
    Continuer3.config(text="...le mot 'chateau' (Intelligence 3)")
    Continuer1.pack(padx=10, pady=10)
    Continuer2.pack(padx=10, pady=10)
    Continuer3.pack(padx=10, pady=10)
    Continuer1.bind("<Button-1>", Ba23a)
    Continuer2.bind("<Button-1>", Ba23b)
    Continuer3.bind("<Button-1>", Ba23c)

#------------ Choix A (Dragon)-----------

def Ba23a(event):
    global Echec
    if intelligence < 4:
        Echec = True
    else:
        Echec = False
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je décide de chercher le mot 'Dragon' sur le plan.")
    Continuer1.bind("<Button-1>", Ba24a)

def Ba24a(event):
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ba25a)

def Ba25a(event):
    if Echec == True:
        Dialogue.config(text="Le repaire du dragon semble s'appeller \n 'Sushi du Dragon Rouge'.")
    else:
        Dialogue.config(text="Je ne trouve qu'un restaurant asiatique sur la carte.")
    Continuer1.bind("<Button-1>", Ba26a)

def Ba26a(event):
    NomPerso.config(text=nom, fg="blue")
    if Echec == True:
        Dialogue.config(text="Ca doit être ça, \n mais je ne sait pas comment y aller.")
    else:
        Dialogue.config(text="Le plan n'indique pas ou se trouve le Dragon.")
    Continuer1.bind("<Button-1>", Ba27)


#--------------------------------

#------------ Choix B (Repaire)-----------

def Ba23b(event):
    global Echec
    if intelligence < 6:
        Echec = True
    else:
        Echec = False
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je décide de chercher le mot 'Repaire' sur le plan.")
    Continuer1.bind("<Button-1>", Ba24b)

def Ba24b(event):
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ba25b)

def Ba25b(event):
    if Echec == True:
        Dialogue.config(text="Je trouve le 'Repaire du marchand de tapis' \n sur le plan.")
    else:
        Dialogue.config(text="Le plan indique la position du \n 'Repaire du Seigneur Braise'.")
    Continuer1.bind("<Button-1>", Ba26b)

def Ba26b(event):
    NomPerso.config(text=nom, fg="blue")
    if Echec == True:
        Dialogue.config(text="Ca doit être ça, \n mais je ne sait pas ou c'est.")
    else:
        global LockMarais
        LockMarais = True
        Dialogue.config(text="Ca doit être ça, \n il faut que je me souvienne de la route.")
        LevelUp(event)
    Continuer1.bind("<Button-1>", Ba27)

#--------------------------------

#------------ Choix C (Chateau)-----------

def Ba23c(event):
    global Echec
    if intelligence < 3:
        Echec = True
    else:
        Echec = False
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je décide de chercher le mot 'Chateau' sur le plan.")
    Continuer1.bind("<Button-1>", Ba24c)

def Ba24c(event):
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ba25c)

def Ba25c(event):
    if Echec == True:
        Dialogue.config(text="Je trouve facilement le repaire du Dragon.")
    else:
        Dialogue.config(text="Je ne trouve qu'un lieu touristique sur la carte.")
    Continuer1.bind("<Button-1>", Ba26c)

def Ba26c(event):
    NomPerso.config(text=nom, fg="blue")
    if Echec == True:
        global LockDisney
        LockDisney = True
        Dialogue.config(text="'Chateau Disney', c'est la ou il se cache.")
    else:
        Dialogue.config(text="Le plan n'indique pas ou se trouve le Dragon.")
    Continuer1.bind("<Button-1>", Ba27)

#--------------------------------


def Ba27(event):
    NomPerso.config(text="")
    Dialogue.config(text="Après avoir retenu ce que j'avais appris, \n je continue ma route.")
    Continuer1.bind("<Button-1>", Ba28)


#----------------------------------------
#----------- Sous Partie 4 --------------
#----------- INTERSECTION ---------------
#----------------------------------------

def Ba28(event):
    Dialogue.config(text="Après 30 minutes de marche, \n j'arrive à une intersection.")
    Continuer1.bind("<Button-1>", Ba29)

def Ba29(event):
    Dialogue.config(text="A gauche, le chemin s'enfonce dans la foret.")
    Continuer1.bind("<Button-1>", Ba30)

def Ba30(event):
    Dialogue.config(text="A droite, le chemin va vers un magnifique chateau.")
    Continuer1.bind("<Button-1>", Ba31)

def Ba31(event):
    if LockMarais == True:
        Dialogue.config(text="Je sais déjà ou je doit aller, \n je doit aller à gauche.")
        Continuer1.bind("<Button-1>", Ba32a)
    elif LockDisney == True:
        Dialogue.config(text="Je sais déjà ou je doit aller, \n je doit aller à droite.")
        Continuer1.bind("<Button-1>", Ba32b)
    else:
        Dialogue.config(text="Je ne sais pas ou aller.")
        Continuer1.bind("<Button-1>", Ba32c)

#------------ Lock Marais -------------

def Ba32a(event):
    Dialogue.config(text="Je prend donc le chemin de gauche.")
    Continuer1.bind("<Button-1>", Bc1)

#----------- Lock Disney ------------

def Ba32b(event):
    Dialogue.config(text="Je prend donc le chemin de droite.")
    Continuer1.bind("<Button-1>", Bb1)

#----------- Chemin Normal -----------

def Ba32c(event):
    Dialogue.config(text="Je dois donc choisir entre la gauche et la droite.")
    Continuer1.bind("<Button-1>", Ba33)


def Ba33(event):
    Dialogue.config(text="Je décide donc d'aller...")
    Continuer1.config(text="...à gauche.")
    Continuer2.config(text="...à droite.")
    Continuer1.pack(padx=10, pady=10)
    Continuer2.pack(padx=10, pady=10)
    Continuer1.bind("<Button-1>", Ba34a)
    Continuer2.bind("<Button-1>", Ba34b)


#---------- Choix A (Gauche) ----------

def Ba34a(event):
    Dialogue.config(text="Je m'engoufre alors dans le chemin menant à la foret.")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer1.bind("<Button-1>", Bc1)

#--------------------------------------

#---------- Choix B (Droite) ----------

def Ba34b(event):
    Dialogue.config(text="Je m'avance alors vers le curieux chateau.")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer1.bind("<Button-1>", Bb1)

#--------------------------------------


#----------------------------------------
#-------------- Partie b ----------------
#--------------- DISNEY -----------------
#----------------------------------------


#----------------------------------------
#----------- Sous Partie 1 --------------
#------------- L'ENTREE -----------------
#----------------------------------------

def Bb1(event):
    #---------------------------
    Chap2.pack_forget()
    NewGame.pack_forget()
    Chap2_1.pack_forget()
    Chap2_2.pack_forget()
    Chap2_3.pack_forget()
    DescChoixChap.pack_forget()
    #--------------------------
    Decor.pack(padx=10, pady=10)
    NomPerso.pack(padx=10, pady=10)
    Dialogue.pack(padx=10, pady=10)
    Continuer1.pack(padx=10, pady=10)
    Continuer1.config(text=">")
    NomPerso.config(text="")
    Dialogue.config(text="J'arrive à l'entrée du chateau.")
    Continuer1.bind("<Button-1>", Bb2)

def Bb2(event):
    if LockDisney == True:
        Dialogue.config(text="Je sais que le Dragon se cache ici.")
        Continuer1.bind("<Button-1>", Bb3)
    else:
        Dialogue.config(text="J'ai toujours des doutes sur \n le fait que le Dragon se trouve ici.")
        Continuer2.pack(padx=10, pady=10)
        Continuer1.config(text="Continuer")
        Continuer2.config(text="Retourner à \n l'intersection")
        Continuer1.bind("<Button-1>", Bb3)
        Continuer2.bind("<Button-1>", Bb2a)

#--------- Choix Retour à l'intersection ---------

def Bb2a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je décide de retourner à l'intersection.")
    Continuer1.bind("<Button-1>", Ba32c)

#-------------------------------------------------

def Bb3(event):
    global PassMarais, PassDisney
    PassMarais = False
    PassDisney = True
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je m'avance vers l'entrée.")
    Continuer1.bind("<Button-1>", Bb4)

def Bb4(event):
    Dialogue.config(text="Le chateau est bizarrement coloré.")
    Continuer1.bind("<Button-1>", Bb5)

def Bb5(event):
    Dialogue.config(text="J'aperçois une personne étrange \n au niveau du pont levis permettant l'entrée au chateau.")
    Continuer1.bind("<Button-1>", Bb6)

def Bb6(event):
    Dialogue.config(text="Je décide de lui adresser la parole.")
    Continuer1.bind("<Button-1>", Bb7)


#----------------------------------------
#----------- Sous Partie 2 --------------
#-------------- VIGILE ------------------
#----------------------------------------

def Bb7(event):
    NomPerso.config(text=nom, fg="blue")
    if LockDisney == True:
        Dialogue.config(text="Bonjour, je sais que votre seigneur se cache ici, \n et je compte le terrasser.")
    else:
        Dialogue.config(text="Bonjour, j'aimerais entrer dans votre humble chateau.")
    Continuer1.bind("<Button-1>", Bb8)

def Bb8(event):
    NomPerso.config(text=nom, fg="blue")
    if LockDisney == True:
        Dialogue.config(text="Bonjour, je sais que votre seigneur se cache ici, \n et je compte le terrasser.")
    else:
        Dialogue.config(text="Bonjour, j'aimerais entrer dans votre humble chateau.")
    Continuer1.bind("<Button-1>", Bb9)

def Bb9(event):
    NomPerso.config(text="Homme étrange", fg="crimson")
    Dialogue.config(text="Hmm ?")
    Continuer1.bind("<Button-1>", Bb10)

def Bb10(event):
    NomPerso.config(text=nom, fg="blue")
    if LockDisney == True:
        Dialogue.config(text="Ne faites pas l'innocent, \n je n'hésiterais pas à vous tuer.")
    else:
        Dialogue.config(text="Il y a un problème ?")
    Continuer1.bind("<Button-1>", Bb11)

def Bb11(event):
    NomPerso.config(text="Homme très étrange", fg="crimson")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bb12)

def Bb12(event):
    if LockDisney == True:
        Dialogue.config(text="Faites attention à vous, \n je vous ai à l'oeil.")
    else:
        Dialogue.config(text="Non, mais ne semez pas \n la discorde à l'interieur.")
    Continuer1.bind("<Button-1>", Bb13)

def Bb13(event):
    SE_Pistolet_Degainage.play()
    Dialogue.config(text="Si je vous voit faire le zouave, \n je vous fait arrêter.")
    Continuer1.bind("<Button-1>", Bb14)

def Bb14(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bb15)

def Bb15(event):
    Dialogue.config(text="Oui Monsieur...")
    Continuer1.bind("<Button-1>", Bb16)

def Bb16(event):
    NomPerso.config(text="")
    Dialogue.config(text="Rapidement, j'entre dans l'enceinte du chateau.")
    Continuer1.bind("<Button-1>", Bb17)


#----------------------------------------
#----------- Sous Partie 3 --------------
#----------- ALLEE CENTRALE -------------
#----------------------------------------

def Bb17(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_DisneyLand)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bb18)

def Bb18(event):
    Dialogue.config(text="Ce type est effrayant.")
    Continuer1.bind("<Button-1>", Bb19)

def Bb19(event):
    if LockDisney == True:
        Dialogue.config(text="C'est la preuve que \n le dragon se cache ici.")
    else:
        Dialogue.config(text="Je devrais faire attention \n à ce que je fais.")
    Continuer1.bind("<Button-1>", Bb20)

def Bb20(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je regarde autour de moi.")
    Continuer1.bind("<Button-1>", Bb21)

def Bb21(event):
    Dialogue.config(text="Avant d'acceder au chateau lui-même, \n il faut passer par une grande allée.")
    Continuer1.bind("<Button-1>", Bb22)

def Bb22(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Ca m'a l'air simple.")
    Continuer1.bind("<Button-1>", Bb23)

def Bb23(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bb24)

def Bb24(event):
    NomPerso.config(text="")
    Dialogue.config(text="Il m'a semblé voir \n l'homme étrange de tout à l'heure.")
    Continuer1.bind("<Button-1>", Bb25)

def Bb25(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Je dois vraiment faire \n attention à ce que je fais.")
    Continuer1.bind("<Button-1>", Bb26)

def Bb26(event):
    Dialogue.config(text="Je décide alors de marcher vers le chateau.")
    Continuer1.bind("<Button-1>", Bb27)


#----------------------------------------
#----------- Sous Partie 4 --------------
#--------- MARCHAND ANTIQUE -------------
#----------------------------------------

def Bb27(event):
    Dialogue.config(text="Après quelques metres,  \n j'aperçois un étrange marchand.")
    Continuer1.bind("<Button-1>", Bb28)

def Bb28(event):
    Dialogue.config(text="Il a l'air de vendre des choses intéressantes.")
    Continuer1.bind("<Button-1>", Bb29)

def Bb29(event):
    Dialogue.config(text="Je décide...")
    Continuer1.config(text="...d'aller le voir.")
    Continuer2.config(text="...de continuer mon chemin.")
    Continuer1.pack(padx=10, pady=10)
    Continuer2.pack(padx=10, pady=10)
    Continuer1.bind("<Button-1>", Bb30)
    Continuer2.bind("<Button-1>", Bb29a)


#---------- Choix A (Passer son chemin) ----------

def Bb29a(event):
    Dialogue.config(text="Je n'ai pas besoin d'une distraction, \n je dois continuer mon chemin.")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer1.bind("<Button-1>", Bb51)

#--------------------------------------

#---------- Choix B (Aller voir le marchand) ----------

def Bb30(event):
    Dialogue.config(text="Je m'avance alors vers le marchand.")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer1.bind("<Button-1>", Bb31)

def Bb31(event):
    NomPerso.config(text=nom, fg="blue")
    if LockDisney == True:
        Dialogue.config(text="Bonjour paysan, qu'avez-vous à vendre ?")
    else:
        Dialogue.config(text="Bonjour, que vendez-vous ?")
    Continuer1.bind("<Button-1>", Bb32)

def Bb32(event):
    NomPerso.config(text="Marchand", fg="tan")
    Dialogue.config(text="Euh...")
    Continuer1.bind("<Button-1>", Bb33)

def Bb33(event):
    Dialogue.config(text="Je vend des objets rares \n et d'une extrême valeur.")
    Continuer1.bind("<Button-1>", Bb34)

def Bb34(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Que me proposez-vous alors ?")
    Continuer1.bind("<Button-1>", Bb35)

def Bb35(event):
    NomPerso.config(text="Marchand", fg="tan")
    Dialogue.config(text="Et bien...")
    Continuer1.bind("<Button-1>", Bb36)

def Bb36(event):
    Dialogue.config(text="Vous m'avez l'air d'un aventurier alors...")
    Continuer1.bind("<Button-1>", Bb37)

def Bb37(event):
    Dialogue.config(text="Je vous propose cette relique.")
    Continuer1.bind("<Button-1>", Bb38)

def Bb38(event):
    NomPerso.config(text="")
    Dialogue.config(text="Il me montre une carte Monopoly.")
    Continuer1.bind("<Button-1>", Bb39)

def Bb39(event):
    NomPerso.config(text="Marchand", fg="tan")
    Dialogue.config(text="Ceci vous permettra d'ignorer la police.")
    Continuer1.bind("<Button-1>", Bb40)

def Bb40(event):
    Dialogue.config(text="Elle est à vous pour 2 millions d'euros.")
    Continuer1.bind("<Button-1>", Bb41)

def Bb41(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bb42)

def Bb42(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je n'ai pas d'argent, que faire ?")
    Continuer1.config(text="Voler la carte (Agilité 4)")
    Continuer2.config(text="Convaincre le Marchand (Charisme 6)")
    Continuer3.config(text="Ne pas obtenir la carte")
    Continuer1.pack(padx=10, pady=10)
    Continuer2.pack(padx=10, pady=10)
    Continuer3.pack(padx=10, pady=10)
    Continuer1.bind("<Button-1>", Bb43a)
    Continuer2.bind("<Button-1>", Bb43b)
    Continuer3.bind("<Button-1>", Bb43c)


#---------- Choix A (Voler la carte) ---------

def Bb43a(event):
    global Echec, NbMauvaisesActions_Disney, VolMarchand
    NbMauvaisesActions_Disney = NbMauvaisesActions_Disney + 1
    VolMarchand = True
    if agilite < 4:
        Echec = True
    else:
        Echec = False
    Dialogue.config(text="Je vais voler cette carte.")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Continuer1.bind("<Button-1>", Bb44a)

def Bb44a(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Oh ? Qu'est ce que c'est ?")
    Continuer1.bind("<Button-1>", Bb45a)

def Bb45a(event):
    NomPerso.config(text="Marchand", fg="tan")
    Dialogue.config(text="De quoi?")
    Continuer1.bind("<Button-1>", Bb46a)

def Bb46a(event):
    NomPerso.config(text="")
    Dialogue.config(text="Rapidement, j'attrape la carte.")
    Continuer1.bind("<Button-1>", Bb47a)

def Bb47a(event):
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bb48a)

def Bb48a(event):
    if Echec == True:
        Dialogue.config(text="J'ai raté.")
    else:
        global Carte_Monopoly
        Carte_Monopoly = True
        print()
        print("Vous avez obtenu une Carte Monopoly")
        print()
        Dialogue.config(text="J'ai réussi.")
    Continuer1.bind("<Button-1>", Bb49a)

def Bb49a(event):
    NomPerso.config(text="Marchand", fg="tan")
    if Echec == True:
        Dialogue.config(text="Que faites vous ? \n Au voleur !")
    else:
        Dialogue.config(text="Je ne vois rien...")
    Continuer1.bind("<Button-1>", Bb50a)

def Bb50a(event):
    NomPerso.config(text="")
    if Echec == True:
        Dialogue.config(text="Je décide de prendre la fuite.")
    else:
        Dialogue.config(text="Je m'enfuis sans qu'il \n ne voit mon acte.")
    Continuer1.bind("<Button-1>", Bb51)

#---------------------------------------------


#------ Choix B (Convaincre le Marchand) -----

def Bb43b(event):
    global Echec
    if charisme < 6:
        Echec = True
    else:
        Echec = False
    Dialogue.config(text="Je vais essayer de le convaincre \n de me la donner gratuitement.")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Continuer1.bind("<Button-1>", Bb44b)

def Bb44b(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Vous savez, je suis un grand aventurier.")
    Continuer1.bind("<Button-1>", Bb45b)

def Bb45b(event):
    if LockDisney == True:
        Dialogue.config(text="Je vais vous débarrasser \n de votre seigneur néfaste.")
    else:
        Dialogue.config(text="Je vais terrasser le puissant \n Dragon de la province.")
    Continuer1.bind("<Button-1>", Bb46b)

def Bb46b(event):
    Dialogue.config(text="Vous vous devez de m'aider dans ma quête.")
    Continuer1.bind("<Button-1>", Bb47b)


def Bb47b(event):
    NomPerso.config(text="Marchand", fg="tan")
    if Echec == True:
        Dialogue.config(text="Je ne vais rien vous donner.")
    else:
        Dialogue.config(text="Très bien, pour vous aider, \n voici la carte.")
    Continuer1.bind("<Button-1>", Bb48b)

def Bb48b(event):
    if Echec == True:
        Dialogue.config(text="Si vous ne voulez pas payer, \n partez sur le champ.")
    else:
        global Carte_Monopoly
        Carte_Monopoly = True
        print()
        print("Vous avez obtenu une Carte Monopoly")
        print()
        NomPerso.config(text="")
        Dialogue.config(text="Il me donne la carte.")
    Continuer1.bind("<Button-1>", Bb49b)

def Bb49b(event):
    NomPerso.config(text=nom, fg="blue")
    if Echec == True:
        Dialogue.config(text="...")
    else:
        Dialogue.config(text="Merci Monsieur.")
    Continuer1.bind("<Button-1>", Bb50b)

def Bb50b(event):
    NomPerso.config(text="")
    Dialogue.config(text="Après ça, je m'éloigne \n de la boutique.")
    Continuer1.bind("<Button-1>", Bb51)

#---------------------------------------------


#------------- Choix C (Partir) --------------

def Bb43c(event):
    Dialogue.config(text="Je n'ai pas besoin de sa carte débile.")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Continuer1.bind("<Button-1>", Bb44c)

def Bb44c(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Désolé, vous ne ferez pas affaire avec moi.")
    Continuer1.bind("<Button-1>", Bb45c)

def Bb45c(event):
    NomPerso.config(text="Marchand", fg="tan")
    Dialogue.config(text="Dommage...")
    Continuer1.bind("<Button-1>", Bb46c)

def Bb46c(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Au revoir.")
    Continuer1.bind("<Button-1>", Bb47c)

def Bb47c(event):
    NomPerso.config(text="")
    Dialogue.config(text="Disant ces mots, \n je m'en vais.")
    Continuer1.bind("<Button-1>", Bb51)

#---------------------------------------------

#--------------------------------------

#----------------------------------------
#----------- Sous Partie 5 --------------
#------------ LE VISITEUR ---------------
#----------------------------------------


def Bb51(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je continue ensuite ma route vers le chateau.")
    Continuer1.bind("<Button-1>", Bb52)

def Bb52(event):
    Dialogue.config(text="Les ruelles sont peuplées.")
    Continuer1.bind("<Button-1>", Bb53)

def Bb53(event):
    Dialogue.config(text="Je pourrais demander des informations, \n j'aperçois un homme qui pourrais savoir des choses.")
    Continuer1.bind("<Button-1>", Bb54)

def Bb54(event):
    Dialogue.config(text="Je décide...")
    Continuer1.config(text="...de demander mon chemin.")
    Continuer2.config(text="...de ne pas demander mon chemin.")
    Continuer1.pack(padx=10, pady=10)
    Continuer2.pack(padx=10, pady=10)
    Continuer1.bind("<Button-1>", Bb55)
    Continuer2.bind("<Button-1>", Bb55a)

#---------- Choix A (ne pas le faire) -------

def Bb55a(event):
    Dialogue.config(text="Je n'ai pas besoin de demander mon chemin.")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer1.bind("<Button-1>", Bb56a)

def Bb56a(event):
    Dialogue.config(text="Je doit continuer vers le chateau.")
    Continuer1.bind("<Button-1>", Bb69)
#--------------------------------------------

#---------- Choix B (le faire) --------------

def Bb55(event):
    Dialogue.config(text="Je devrais demander mon chemin.")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer1.bind("<Button-1>", Bb56)

def Bb56(event):
    Dialogue.config(text="Je m'avance vers l'homme.")
    Continuer1.bind("<Button-1>", Bb57)

def Bb57(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Exusez-moi.")
    Continuer1.bind("<Button-1>", Bb58)

def Bb58(event):
    NomPerso.config(text="Homme", fg="tan")
    Dialogue.config(text="Hein ?")
    Continuer1.bind("<Button-1>", Bb59)

def Bb59(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Pouvez-vous m'aider ? \n Je recherche un Dragon.")
    Continuer1.bind("<Button-1>", Bb60)

def Bb60(event):
    NomPerso.config(text="Homme", fg="tan")
    Dialogue.config(text="...Un Dragon ?")
    Continuer1.bind("<Button-1>", Bb61)

def Bb61(event):
    Dialogue.config(text="Je...ne sais absolument pas \n de quoi vous parlez...")
    Continuer1.bind("<Button-1>", Bb61a)

def Bb61a(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bb62)

def Bb62(event):
    NomPerso.config(text="")
    Dialogue.config(text="Il cache quelque chose, \n que faire ?")
    Continuer1.config(text="Le menacer")
    Continuer2.config(text="Partir")
    Continuer1.pack(padx=10, pady=10)
    Continuer2.pack(padx=10, pady=10)
    Continuer1.bind("<Button-1>", Bb63a)
    Continuer2.bind("<Button-1>", Bb63b)

#------------ Choix A (Menace) ------------

def Bb63a(event):
    NomPerso.config(text="")
    Dialogue.config(text="Il cache quelque chose, \n je vais le faire parler.")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer1.bind("<Button-1>", Bb64a)

def Bb64a(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Tension)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    global NbMauvaisesActions_Disney, MenacePassant
    NbMauvaisesActions_Disney = NbMauvaisesActions_Disney + 1
    MenacePassant = True
    NomPerso.config(text=nom, fg="blue")
    if LockDisney == True:
        Dialogue.config(text="Je le savais tu est \n un de ses espions !")
    else:
        Dialogue.config(text="Que caches-tu ? Parle !")
    Continuer1.bind("<Button-1>", Bb65a)

def Bb65a(event):
    NomPerso.config(text="Homme", fg="tan")
    Dialogue.config(text="Je ne sais rien !")
    Continuer1.bind("<Button-1>", Bb66a)

def Bb66a(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bb67a)

def Bb67a(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_DisneyLand)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    NomPerso.config(text="")
    Dialogue.config(text="Il a fuit, \n je devrais faire de même.")
    Continuer1.bind("<Button-1>", Bb68a)

def Bb68a(event):
    NomPerso.config(text="")
    Dialogue.config(text="Disant ces mots, je m'en vais.")
    Continuer1.bind("<Button-1>", Bb69)

#------------------------------------------

#------------ Choix B (Partir) ------------

def Bb63b(event):
    NomPerso.config(text="")
    Dialogue.config(text="C'est sans doute une coincidence.")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer1.bind("<Button-1>", Bb64b)

def Bb64b(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Je vois, au revoir.")
    Continuer1.bind("<Button-1>", Bb65b)

def Bb65b(event):
    NomPerso.config(text="")
    Dialogue.config(text="Disant cela, je m'en vais.")
    Continuer1.bind("<Button-1>", Bb69)

#------------------------------------------

#--------------------------------------------

#----------------------------------------
#----------- Sous Partie 6 --------------
#------------ FIOLE A XP ----------------
#----------------------------------------

def Bb69(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je me retrouve une fois de plus \n en direction du chateau.")
    Continuer1.bind("<Button-1>", Bb70)

def Bb70(event):
    Dialogue.config(text="Après quelque temps, \n je me retrouve en face du chateau.")
    Continuer1.bind("<Button-1>", Bb71)

def Bb71(event):
    Dialogue.config(text="Sur un banc en face de moi, \n je remarque une fiole d'XP.")
    Continuer1.bind("<Button-1>", Bb72)

def Bb72(event):
    Dialogue.config(text="Elle me serais très utile.")
    Continuer1.bind("<Button-1>", Bb73)

def Bb73(event):
    Dialogue.config(text="Je décide...")
    Continuer1.config(text="...de la prendre.")
    Continuer2.config(text="...de la laisser.")
    Continuer1.pack(padx=10, pady=10)
    Continuer2.pack(padx=10, pady=10)
    Continuer1.bind("<Button-1>", Bb74a)
    Continuer2.bind("<Button-1>", Bb74b)

#-------------- Choix A (voler la fiole) -------

def Bb74a(event):
    Dialogue.config(text="Je vais prendre la fiole.")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer1.bind("<Button-1>", Bb75a)

def Bb75a(event):
    Dialogue.config(text="Personne n'en a besoin.")
    Continuer1.bind("<Button-1>", Bb76a)

def Bb76a(event):
    Dialogue.config(text="Je m'avance vers la fiole...")
    Continuer1.bind("<Button-1>", Bb77a)

def Bb77a(event):
    global VolXP, NbMauvaisesActions_Disney
    NbMauvaisesActions_Disney = NbMauvaisesActions_Disney +1
    VolXP = True
    Dialogue.config(text="...et je la prend.")
    Continuer1.bind("<Button-1>", Bb78a)

def Bb78a(event):
    Dialogue.config(text="Je la bois aussitôt.")
    Continuer1.bind("<Button-1>", Bb79a)
    LevelUp(event)

def Bb79a(event):
    NomPerso.config(text=nom, fg="blue")
    if niveau%2 != 0:
        Dialogue.config(text="Même pas de points supplémentaire.")
    else:
        Dialogue.config(text="Et un point en plus !")
    Continuer1.bind("<Button-1>", Bb80)

#-----------------------------------------------

#------------- Choix B (laisser la fiole) ------

def Bb74b(event):
    Dialogue.config(text="Je vais laisser la fiole.")
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer1.bind("<Button-1>", Bb75b)

def Bb75b(event):
    if LockDisney == True:
        Dialogue.config(text="Elle est forcément empoisonnée, \n vu qu'on est au chateau du Dragon.")
    else:
        Dialogue.config(text="C'est du vol ça.")
    Continuer1.bind("<Button-1>", Bb80)

#-----------------------------------------------

#----------------------------------------
#----------- Sous Partie 7 --------------
#------------- JUGEMENT -----------------
#----------------------------------------

def Bb80(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je me dirige alors vers le chateau.")
    Continuer1.bind("<Button-1>", Bb81)

def Bb81(event):
    Dialogue.config(text="Après avoir monté les escaliers \n menant au chateau, je trouve...")
    Continuer1.bind("<Button-1>", Bb82)

def Bb82(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="L'homme de l'entrée !")
    Continuer1.bind("<Button-1>", Bb83)

def Bb83(event):
    NomPerso.config(text="L'homme de l'entrée", fg="crimson")
    Dialogue.config(text="Et oui, c'est moi.")
    Continuer1.bind("<Button-1>", Bb84)

def Bb84(event):
    Dialogue.config(text="Je t'ai observé durant ton séjour.")
    Continuer1.bind("<Button-1>", Bb85)

def Bb85(event):
    if VolMarchand == True:
        Dialogue.config(text="Je t'ai vu voler le marchand.")
    else:
        Dialogue.config(text="Je t'ai vu vers le Marchand.")
    Continuer1.bind("<Button-1>", Bb86)

def Bb86(event):
    if MenacePassant == True:
        Dialogue.config(text="Je t'ai vu menacer un passant.")
    else:
        Dialogue.config(text="Je t'ai vu vers un passant.")
    Continuer1.bind("<Button-1>", Bb87)

def Bb87(event):
    if VolXP == True:
        Dialogue.config(text="Je t'ai vu voler la fiole d'XP.")
    else:
        Dialogue.config(text="Je t'ai vu regarder la fiole d'XP.")
    Continuer1.bind("<Button-1>", Bb88)

def Bb88(event):
    Dialogue.config(text="Au final, j'ai décidé que...")
    Continuer1.bind("<Button-1>", Bb89)

def Bb89(event):
    if NbMauvaisesActions_Disney > 1:
        Dialogue.config(text="...tu ne t'es pas bien comporté.")
    else:
        Dialogue.config(text="...tu t'es relativement bien comporté.")
    Continuer1.bind("<Button-1>", Bb90)

def Bb90(event):
    if NbMauvaisesActions_Disney > 1:
        Dialogue.config(text="Pour cela, tu va finir en prison.")
    else:
        Dialogue.config(text="Pour cela, je vais t'aider.")
    Continuer1.bind("<Button-1>", Bb91)

def Bb91(event):
    if NbMauvaisesActions_Disney > 1:
        Dialogue.config(text="Rend toi maintenant !")
    else:
        Dialogue.config(text="Le chateau du Dragon se trouve au Nord.")
    Continuer1.bind("<Button-1>", Bb92)

def Bb92(event):
    NomPerso.config(text=nom, fg="blue")
    if NbMauvaisesActions_Disney > 1:
        Dialogue.config(text="Quoi ?!")
    else:
        Dialogue.config(text="Oh, merci.")
    Continuer1.bind("<Button-1>", Bb93)

def Bb93(event):
    NomPerso.config(text="")
    if NbMauvaisesActions_Disney > 1:
        SE_Frappe.play()
        Dialogue.config(text="L'homme me fonce dessus \n et m'assomme.")
        Continuer1.bind("<Button-1>", FIN_Disney)
    else:
        Dialogue.config(text="L'homme m'explique alors en detail \n ou se trouve le dragon.")
        Continuer1.bind("<Button-1>", Bb94)

def Bb94(event):
    Dialogue.config(text="Après quoi, je me dirige vers le chateau du Dragon.")
    Continuer1.bind("<Button-1>", Ca1)


#----------------------------------------
#-------------- Partie c ----------------
#--------------- MARAIS -----------------
#----------------------------------------

#----------------------------------------
#----------- Sous Partie 1 --------------
#-------------- ARRIVEE -----------------
#----------------------------------------

def Bc1(event):
    #---------------------------
    Chap2.pack_forget()
    NewGame.pack_forget()
    Chap2_1.pack_forget()
    Chap2_2.pack_forget()
    Chap2_3.pack_forget()
    DescChoixChap.pack_forget()
    #--------------------------
    Decor.pack(padx=10, pady=10)
    NomPerso.pack(padx=10, pady=10)
    Dialogue.pack(padx=10, pady=10)
    Continuer1.pack(padx=10, pady=10)
    Continuer1.config(text=">")
    NomPerso.config(text="")
    Dialogue.config(text="J'arrive à la bordure de la forêt.")
    Continuer1.bind("<Button-1>", Bc2)

def Bc2(event):
    if LockMarais == True:
        Dialogue.config(text="Je sais que le repaire du Dragon \n se trouve au dela de la forêt.")
        Continuer1.bind("<Button-1>", Bc3)
    else:
        Dialogue.config(text="J'ai toujours des doutes sur \n le fait que le Dragon se trouve ici.")
        Continuer2.pack(padx=10, pady=10)
        Continuer1.config(text="Continuer")
        Continuer2.config(text="Retourner à \n l'intersection")
        Continuer1.bind("<Button-1>", Bc3)
        Continuer2.bind("<Button-1>", Bc2a)

#--------- Choix Retour à l'intersection ---------

def Bc2a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je décide de retourner à l'intersection.")
    Continuer1.bind("<Button-1>", Ba32c)

#-------------------------------------------------

def Bc3(event):
    global PassMarais, PassDisney
    PassMarais = True
    PassDisney = False
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je rentre dans la forêt.")
    Continuer1.bind("<Button-1>", Bc4)

def Bc4(event):
    if LockMarais == True:
        Dialogue.config(text="Je doit faire attention dans cette forêt.")
    else:
        Dialogue.config(text="Je ne sais pas à quoi m'attendre ici.")
    Continuer1.bind("<Button-1>", Bc5)

def Bc5(event):
    if LockMarais == True:
        Dialogue.config(text="Elle abrite un marais maudit.")
    else:
        Dialogue.config(text="Je doit rester sur vigilant.")
    Continuer1.bind("<Button-1>", Bc6)

def Bc6(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bc7)

def Bc7(event):
    NomPerso.config(text="")
    Dialogue.config(text="Au loin, dans les montagnes , \n je peut apercevoir un chateau.")
    Continuer1.bind("<Button-1>", Bc8)

def Bc8(event):
    NomPerso.config(text=nom, fg="blue")
    if LockMarais == True:
        Dialogue.config(text="C'est le chateau du Dragon.")
    else:
        Dialogue.config(text="C'est peut être l'endroit \n ou se cache le dragon.")
    Continuer1.bind("<Button-1>", Bc9)

def Bc9(event):
    Dialogue.config(text="Je doit y aller.")
    Continuer1.bind("<Button-1>", Bc10)

def Bc10(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je m'enfonce donc plus profondément dans la forêt.")
    Continuer1.bind("<Button-1>", Bc11)

#----------------------------------------
#----------- Sous Partie 2 --------------
#------------ LE MARAIS -----------------
#----------------------------------------

def Bc11(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Marais)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    Dialogue.config(text="Après quelque temps, \n j'arrive vers un marais.")
    Continuer1.bind("<Button-1>", Bc12)

def Bc12(event):
    NomPerso.config(text=nom, fg="blue")
    if LockMarais == True:
        Dialogue.config(text="C'est le marais maudit.")
    else:
        Dialogue.config(text="Un marais ?")
    Continuer1.bind("<Button-1>", Bc13)

def Bc13(event):
    NomPerso.config(text=nom, fg="blue")
    if LockMarais == True:
        Dialogue.config(text="On dit qu'il y a un monstre ici.")
    else:
        Dialogue.config(text="Il ne m'inspire pas confiance.")
    Continuer1.bind("<Button-1>", Bc14)

def Bc14(event):
    NomPerso.config(text="???", fg="olive")
    Dialogue.config(text="AH AH AH")
    Continuer1.bind("<Button-1>", Bc15)

def Bc15(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Hein ?")
    Continuer1.bind("<Button-1>", Bc16)

def Bc16(event):
    if LockMarais == True:
        Dialogue.config(text="C'est lui !")
    else:
        Dialogue.config(text="Il y a un monstre ici ?!")
    Continuer1.bind("<Button-1>", Bc17)

def Bc17(event):
    NomPerso.config(text="Monstre du Marais", fg="olive")
    Dialogue.config(text="OUI, ET JE VAIS TE TUER !")
    Continuer1.bind("<Button-1>", Bc18)

def Bc18(event):
    NomPerso.config(text="Monstre du Marais", fg="olive")
    Dialogue.config(text="ENFIN...QUAND JE T'AURAIS TROUVE !")
    Continuer1.bind("<Button-1>", Bc19)

def Bc19(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je n'ai pas le choix, \n je doit traverser le marais.")
    Continuer1.bind("<Button-1>", Bc20)

def Bc20(event):
    Dialogue.config(text="Je doit le faire discrètement.")
    Continuer1.bind("<Button-1>", Bc21)

#----------------------------------------
#----------- Sous Partie 3 --------------
#--------- 1ER CHECK AGILITE ------------
#----------------------------------------

def Bc21(event):
    Dialogue.config(text="Je doit faire très attention.")
    Continuer1.config(text="Avancer (Agilité 2)")
    Continuer1.bind("<Button-1>", Bc22)

def Bc22(event):
    global Echec
    if agilite < 2:
        Echec = True
    else:
        Echec = False
    Dialogue.config(text="J'avance donc discrètement \n entre les arbres.")
    Continuer1.config(text=">")
    Continuer1.bind("<Button-1>", Bc23)

def Bc23(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bc24)

def Bc24(event):
    NomPerso.config(text="")
    if Echec == True:
        global ErreurMarais
        ErreurMarais = ErreurMarais + 1
        SE_Chute.play()
        Dialogue.config(text="J'ai marché sur une branche.")
    else:
        Dialogue.config(text="J'ai réussit à passer inaperçu.")
    Continuer1.bind("<Button-1>", Bc25)

def Bc25(event):
    NomPerso.config(text="Monstre du Marais", fg="olive")
    if Echec == True:
        Dialogue.config(text="JE T'AI ENTENDU HUMAIN !")
    else:
        Dialogue.config(text="OU EST TU HUMAIN ?")
    Continuer1.bind("<Button-1>", Bc26)

def Bc26(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bc27)

def Bc27(event):
    NomPerso.config(text="")
    if Echec == True:
        Dialogue.config(text="Je m'enfuis aussi discrètement que possible.")
    else:
        Dialogue.config(text="Je continue ma route.")
    Continuer1.bind("<Button-1>", Bc28)

#----------------------------------------
#----------- Sous Partie 4 --------------
#------------- FIOLE D'XP ---------------
#----------------------------------------

def Bc28(event):
    Dialogue.config(text="Après quelque temps, \n j'arrive vers un rocher.")
    Continuer1.bind("<Button-1>", Bc29)

def Bc29(event):
    Dialogue.config(text="Sur le rocher se trouve une fiole d'XP.")
    Continuer1.bind("<Button-1>", Bc30)

def Bc30(event):
    Dialogue.config(text="Je pourais en avoir besoin.")
    Continuer1.bind("<Button-1>", Bc31)

def Bc31(event):
    Dialogue.config(text="Je décide...")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.config(text="...de la prendre.")
    Continuer2.config(text="...de la laisser.")
    Continuer1.bind("<Button-1>", Bc32a)
    Continuer2.bind("<Button-1>", Bc32b)

#--------- Choix A (La prendre) ---------

def Bc32a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je vais prendre la fiole.")
    Continuer1.bind("<Button-1>", Bc33a)

def Bc33a(event):
    Dialogue.config(text="Je m'approche...")
    Continuer1.bind("<Button-1>", Bc34a)

def Bc34a(event):
    Dialogue.config(text="...et je prend la fiole.")
    Continuer1.bind("<Button-1>", Bc35a)

def Bc35a(event):
    Dialogue.config(text="Je la bois aussitôt.")
    Continuer1.bind("<Button-1>", Bc36a)
    LevelUp(event)

def Bc36a(event):
    global ErreurMarais
    ErreurMarais = ErreurMarais + 1
    NomPerso.config(text="Monstre du Marais", fg="olive")
    Dialogue.config(text="JE TE RATTRAPE HUMAIN !")
    Continuer1.bind("<Button-1>", Bc37a)

def Bc37a(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bc38a)

def Bc38a(event):
    NomPerso.config(text="")
    Dialogue.config(text="J'ai perdu du temps.")
    Continuer1.bind("<Button-1>", Bc39)

#-------------------------------------------------

#--------- Choix B (La laisser) ---------

def Bc32b(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je n'ai pas besoin d'une distraction.")
    Continuer1.bind("<Button-1>", Bc39)

#-------------------------------------------------

def Bc39(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je reprend aussitôt ma route.")
    Continuer1.bind("<Button-1>", Bc40)


#----------------------------------------
#----------- Sous Partie 5 --------------
#-------- 2EME CHECK AGILITE ------------
#----------------------------------------

def Bc40(event):
    Dialogue.config(text="En route, j'arrive vers un ruisseau.")
    Continuer1.bind("<Button-1>", Bc41)

def Bc41(event):
    Dialogue.config(text="Je risque de faire du bruit \n si je le traverse a pied.")
    Continuer1.bind("<Button-1>", Bc42)

def Bc42(event):
    Dialogue.config(text="Je pourrais traverser en sautant sur des rochers.")
    Continuer1.bind("<Button-1>", Bc43)

def Bc43(event):
    Dialogue.config(text="Je décide...")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.config(text="...de passer par les rochers (Agilité 5).")
    Continuer2.config(text="...de traverser à pied.")
    Continuer1.bind("<Button-1>", Bc44a)
    Continuer2.bind("<Button-1>", Bc44b)

#--------- Choix A ( Passer par les rochers) ---------

def Bc44a(event):
    global Echec
    if agilite < 5:
        Echec = True
    else:
        Echec = False
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je me prépare à sauter sur les rochers.")
    Continuer1.bind("<Button-1>", Bc45a)

def Bc45a(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bc46a)

def Bc46a(event):
    NomPerso.config(text="")
    if Echec == True:
        global ErreurMarais
        ErreurMarais = ErreurMarais + 2
        SE_Chute.play()
        Dialogue.config(text="J'ai échoué \n et je suis tombé dans la rivière.")
    else:
        Dialogue.config(text="J'ai réussit \n et je suis de l'autre coté de la rivière.")
    Continuer1.bind("<Button-1>", Bc47a)

def Bc47a(event):
    NomPerso.config(text="Monstre du Marais", fg="olive")
    if Echec == True:
        Dialogue.config(text="ON TOMBE, HUMAIN ? \n LAISSE MOI T'AIDER !")
    else:
        Dialogue.config(text="JE TE SENT, HUMAIN !")
    Continuer1.bind("<Button-1>", Bc48)

#-----------------------------------------------------

#--------- Choix B (Traverser à pied) ----------------

def Bc44b(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je vais traverser à pied.")
    Continuer1.bind("<Button-1>", Bc45b)

def Bc45b(event):
    Dialogue.config(text="Tant pis pour le bruit.")
    Continuer1.bind("<Button-1>", Bc46b)

def Bc46b(event):
    global ErreurMarais
    ErreurMarais = ErreurMarais + 1
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bc47b)

def Bc47b(event):
    NomPerso.config(text="Monstre du Marais", fg="olive")
    Dialogue.config(text="JE T'AI ENTENDU, HUMAIN !")
    Continuer1.bind("<Button-1>", Bc48)

#----------------------------------------------------

def Bc48(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je m'enfuis aussitôt.")
    Continuer1.bind("<Button-1>", Bc49)

#----------------------------------------
#----------- Sous Partie 6 --------------
#------------- LE VIEUX -----------------
#----------------------------------------

def Bc49(event):
    Dialogue.config(text="Après quelque minutes, \n j'arrive enfin vers la sortie du marais.")
    Continuer1.bind("<Button-1>", Bc50)

def Bc50(event):
    Dialogue.config(text="Mon regard se pose sur \n un cadavre non loin de moi.")
    Continuer1.bind("<Button-1>", Bc51)

def Bc51(event):
    Dialogue.config(text="Il a peut etre des \n ressources utiles sur lui.")
    Continuer1.bind("<Button-1>", Bc52)

def Bc52(event):
    Dialogue.config(text="Je décide...")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.config(text="...de le fouiller.")
    Continuer2.config(text="...de l'ignorer.")
    Continuer1.bind("<Button-1>", Bc53)
    Continuer2.bind("<Button-1>", Bc52a)

#--------- Choix A (Le Fouiller) ---------

def Bc53(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je vais le fouiller.")
    Continuer1.bind("<Button-1>", Bc54)

def Bc54(event):
    Dialogue.config(text="Je m'approche du cadavre et...")
    Continuer1.bind("<Button-1>", Bc55)

def Bc55(event):
    NomPerso.config(text="Cadavre Vivant", fg="tan")
    Dialogue.config(text="Hein ?")
    Continuer1.bind("<Button-1>", Bc56)

def Bc56(event):
    NomPerso.config(text="Un Vieux", fg="tan")
    Dialogue.config(text="Enfin, des secours !")
    Continuer1.bind("<Button-1>", Bc57)

def Bc57(event):
    Dialogue.config(text="Je suis coincé ici depuis 10 ans !")
    Continuer1.bind("<Button-1>", Bc58)

def Bc58(event):
    NomPerso.config(text="")
    Dialogue.config(text="Il va attirer le monstre.")
    Continuer1.bind("<Button-1>", Bc59)

def Bc59(event):
    Dialogue.config(text="Je décide...")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.config(text="...de le faire taire.")
    Continuer2.config(text="...de fuir.")
    Continuer1.bind("<Button-1>", Bc60a)
    Continuer2.bind("<Button-1>", Bc60b)

#--------- Choix A (Le faire taire) ---------

def Bc60a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Écoutez moi, taisez vous ou...")
    Continuer1.bind("<Button-1>", Bc61a)

def Bc61a(event):
    NomPerso.config(text="Un Vieux", fg="tan")
    Dialogue.config(text="NON JAMAIS, JE NE VAIS PAS ME TAIRE !")
    Continuer1.bind("<Button-1>", Bc62a)

def Bc62a(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bc63a)

def Bc63a(event):
    global ErreurMarais
    ErreurMarais = ErreurMarais + 2
    NomPerso.config(text="Monstre du Marais", fg="olive")
    Dialogue.config(text="J'ARRIVE, HUMAIN !")
    Continuer1.bind("<Button-1>", Bc64a)

def Bc64a(event):
    NomPerso.config(text="")
    Dialogue.config(text="Rapidement, je prend la fuite.")
    Continuer1.bind("<Button-1>", Bc65)

#--------------------------------------------

#--------- Choix B (Fuir) ---------

def Bc60b(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Rapidement, je m'enfuis.")
    Continuer1.bind("<Button-1>", Bc61b)

def Bc61b(event):
    NomPerso.config(text="Un Vieux", fg="tan")
    Dialogue.config(text="Attendez ! \n Qui va me sauvez maintenant !?")
    Continuer1.bind("<Button-1>", Bc62b)

def Bc62b(event):
    global ErreurMarais
    ErreurMarais = ErreurMarais + 1
    NomPerso.config(text="Monstre du Marais", fg="olive")
    Dialogue.config(text="J'ARRIVE POUR VOUS, HUMAINS !")
    Continuer1.bind("<Button-1>", Bc63b)

def Bc63b(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je suis déjà loin.")
    Continuer1.bind("<Button-1>", Bc65)

#--------------------------------------------


#-----------------------------------------------------

#--------- Choix B (L'ignorer) ---------

def Bc52a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je vais l'ignorer.")
    Continuer1.bind("<Button-1>", Bc52b)

def Bc52b(event):
    Dialogue.config(text="Je ne veut pas perdre plus de temps.")
    Continuer1.bind("<Button-1>", Bc52c)

def Bc52c(event):
    Dialogue.config(text="Je continue donc ma route.")
    Continuer1.bind("<Button-1>", Bc65)

#-----------------------------------------------------

#----------------------------------------
#----------- Sous Partie 7 --------------
#------------- LA SORTIE ----------------
#----------------------------------------

def Bc65(event):
    NomPerso.config(text="")
    Dialogue.config(text="Après quelque temps, \n j'arrive au bout du marais.")
    Continuer1.bind("<Button-1>", Bc66)

def Bc66(event):
    Dialogue.config(text="Si je franchis le pont, \n je serais sauf.")
    Continuer1.bind("<Button-1>", Bc67)

def Bc67(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Ogre)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    NomPerso.config(text="Monstre du Marais", fg="olive")
    Dialogue.config(text="TE VOILA, HUMAIN !")
    Continuer1.bind("<Button-1>", Bc68)

def Bc68(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je me retourne \n pour voir le terrible monstre.")
    Continuer1.bind("<Button-1>", Bc69)

def Bc69(event):
    NomPerso.config(text="Monstre du Marais", fg="olive")
    Dialogue.config(text="JE VAIS TE TUER !")
    Continuer1.bind("<Button-1>", Bc70)

def Bc70(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Jamais !")
    Continuer1.bind("<Button-1>", Bc71)

def Bc71(event):
    NomPerso.config(text="")
    Dialogue.config(text="Disant ces mots, \n je commence à traverser le pont.")
    Continuer1.bind("<Button-1>", Bc72)

def Bc72(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bc73)

def Bc73(event):
    NomPerso.config(text="")
    if ErreurMarais > 3:
        Dialogue.config(text="Je n'arrive pas à le distancer.")
    else:
        Dialogue.config(text="J'arrive à le distancer.")
    Continuer1.bind("<Button-1>", Bc74)

def Bc74(event):
    NomPerso.config(text="Monstre du Marais", fg="olive")
    if ErreurMarais > 3:
        Dialogue.config(text="OUI ! ENFIN !")
    else:
        Dialogue.config(text="NON ! REVIENS !")
    Continuer1.bind("<Button-1>", Bc75)

def Bc75(event):
    NomPerso.config(text="")
    if ErreurMarais > 3:
        Dialogue.config(text="Le monstre m'attrape.")
    else:
        Dialogue.config(text="Je franchis le pont...")
    Continuer1.bind("<Button-1>", Bc76)

def Bc76(event):
    if ErreurMarais > 3:
        NomPerso.config(text="Monstre du Marais", fg="olive")
        Dialogue.config(text="AH ! JE VAIS ENFIN TE MANGER !")
    else:
        SE_Epee.play()
        NomPerso.config(text="")
        Dialogue.config(text="...et je coupe les cordes de soutien.")
    Continuer1.bind("<Button-1>", Bc77)

def Bc77(event):
    if ErreurMarais > 3:
        NomPerso.config(text="")
        Dialogue.config(text="Le monstre m'emmenène dans le marais.")
        Continuer1.bind("<Button-1>", FIN_Marais)
    else:
        NomPerso.config(text="")
        Dialogue.config(text="Le pont est destabilisé.")
        Continuer1.bind("<Button-1>", Bc78)

def Bc78(event):
    NomPerso.config(text="Monstre du Marais", fg="olive")
    Dialogue.config(text="NOOOOONNN !")
    Continuer1.bind("<Button-1>", Bc79)

def Bc79(event):
    pygame.mixer.music.fadeout(400)
    NomPerso.config(text="")
    Dialogue.config(text="Le monstre tombe avec le pont dans la rivière.")
    Continuer1.bind("<Button-1>", Bc80)

def Bc80(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Bc81)

def Bc81(event):
    Dialogue.config(text="Je peut enfin accéder au chateau du Dragon.")
    Continuer1.bind("<Button-1>", Bc82)

def Bc82(event):
    NomPerso.config(text="")
    Dialogue.config(text="Disant cela, \n je me dirige vers les montagnes.")
    Continuer1.bind("<Button-1>", Ca1)








#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------








#----------------------------------------
#------------- Chapitre C ---------------
#----------- NOM DE CHAPITRE ------------
#----------------------------------------

#----------------------------------------
#-------------- Partie a ----------------
#-------------- MONTAGNE ----------------
#----------------------------------------


#----------------------------------------
#----------- Sous Partie 1 --------------
#-------------- ARRIVEE -----------------
#----------------------------------------

def Ca1(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Exterieur)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    #---------------------------
    Chap3.pack_forget()
    NewGame.pack_forget()
    Chap3_1.pack_forget()
    Chap3_2.pack_forget()
    Chap3_3.pack_forget()
    Chap3_4.pack_forget()
    DescChoixChap.pack_forget()
    #--------------------------
    Decor.pack(padx=10, pady=10)
    NomPerso.pack(padx=10, pady=10)
    Dialogue.pack(padx=10, pady=10)
    Continuer1.pack(padx=10, pady=10)
    Continuer1.config(text=">")
    NomPerso.config(text="")
    Dialogue.config(text="Après une heure de marche, \n j'arrive à mon but.")
    Continuer1.bind("<Button-1>", Ca2)
    LevelUp(event)

def Ca2(event):
    Dialogue.config(text="Au sommet de la montagne se trouve \n le repaire du Dragon.")
    Continuer1.bind("<Button-1>", Ca3)

def Ca3(event):
    Dialogue.config(text="Je commence donc à gravir la montagne.")
    Continuer1.bind("<Button-1>", Ca4)

def Ca4(event):
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ca5)

def Ca5(event):
    Dialogue.config(text="Au bout d'un moment, je trouve un cadavre.")
    Continuer1.bind("<Button-1>", Ca6)

def Ca6(event):
    Dialogue.config(text="Je pourrais le fouiller.")
    Continuer1.bind("<Button-1>", Ca7)

def Ca7(event):
    Dialogue.config(text="Je décide...")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.config(text="...de le fouiller.")
    Continuer2.config(text="...de l'ignorer.")
    Continuer1.bind("<Button-1>", Ca8a)
    Continuer2.bind("<Button-1>", Ca8b)


#-------- Choix A (Le fouillier) ----------

def Ca8a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je vais le fouiller.")
    Continuer1.bind("<Button-1>", Ca9a)

def Ca9a(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ca10a)

def Ca10a(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Une épée !")
    Continuer1.bind("<Button-1>", Ca11a)

def Ca11a(event):
    global Epee
    if Epee == True:
        Dialogue.config(text="J'en ai déjà une, \n je n'ai pas besoin de celle-la.")
    else:
        Epee = True
        print()
        print("Vous avez obtenu une Epee")
        print()
        Dialogue.config(text="Ca tombe bien, \n je n'en avais pas.")
    Continuer1.bind("<Button-1>", Ca12)

#------------------------------

#-------- Choix B (L'ignorer) ----------

def Ca8b(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je vais l'ignorer.")
    Continuer1.bind("<Button-1>", Ca9b)

def Ca9b(event):
    Dialogue.config(text="Il a peut être quelque chose de contagieux.")
    Continuer1.bind("<Button-1>", Ca13)

#------------------------------

def Ca12(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je reprend ensuite mon chemin.")
    Continuer1.bind("<Button-1>", Ca13)

#----------------------------------------
#----------- Sous Partie 2 --------------
#-------------- ENTREE ------------------
#----------------------------------------

def Ca13(event):
    Dialogue.config(text="Après quelque temps, \n j'arrive à l'entrée du chateau.")
    Continuer1.bind("<Button-1>", Ca14)

def Ca14(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Le Dragon se cache à l'interieur.")
    Continuer1.bind("<Button-1>", Ca15)

def Ca15(event):
    NomPerso.config(text="")
    Dialogue.config(text="Mais...")
    Continuer1.bind("<Button-1>", Ca16)

def Ca16(event):
    NomPerso.config(text="")
    Dialogue.config(text="Aie-je vraiment envie d'y aller ?")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.config(text="Oui, bien sur")
    Continuer2.config(text="Euh...")
    Continuer1.bind("<Button-1>", Ca17)
    Continuer2.bind("<Button-1>", Ca16a)


#-------- Choix FUITE ----------

def Ca16a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Euh, en fait...")
    Continuer1.bind("<Button-1>", Ca16b)

def Ca16b(event):
    Dialogue.config(text="Désolé Harold, mais...")
    Continuer1.bind("<Button-1>", Ca16c)

def Ca16c(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je prend la fuite, \n cette quête n'est pas faite pour moi.")
    Continuer1.bind("<Button-1>", FIN_Fuite)

#----------------------------------------

def Ca17(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Je doit y aller.")
    Continuer1.bind("<Button-1>", Ca18)

def Ca18(event):
    Dialogue.config(text="Il y a de l'argent en jeu !")
    Continuer1.bind("<Button-1>", Ca19)

def Ca19(event):
    NomPerso.config(text="")
    Dialogue.config(text="Disant cela, je m'avance \n vers la porte d'entrée.")
    Continuer1.bind("<Button-1>", Ca20)

def Ca20(event):
    Dialogue.config(text="Elle est fermée.")
    Continuer1.bind("<Button-1>", Ca21)

def Ca21(event):
    Dialogue.config(text="Je décide...")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.config(text="...de frapper à la porte.")
    Continuer2.config(text="...d'escalader le mur.")
    Continuer1.bind("<Button-1>", Ca22)
    Continuer2.bind("<Button-1>", Ca21a)

#-------- Choix  Escalader le mur ------------

def Ca21a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je m'avance vers le mur.")
    Continuer1.bind("<Button-1>", Ca21b)

def Ca21b(event):
    Dialogue.config(text="J'essaie de grimper...")
    Continuer1.bind("<Button-1>", Ca21c)

def Ca21c(event):
    Dialogue.config(text="...mais je tombe avec bruit.")
    Continuer1.bind("<Button-1>", Ca24)

#------------------------------------------------

def Ca22(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je m'avance vers la porte...")
    Continuer1.bind("<Button-1>", Ca23)

def Ca23(event):
    Dialogue.config(text="...et je frappe.")
    Continuer1.bind("<Button-1>", Ca24)

def Ca24(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ca25)

def Ca25(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_GARDE)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    NomPerso.config(text="???", fg="burlywood")
    Dialogue.config(text="Qui va la ?")
    Continuer1.bind("<Button-1>", Ca26)

def Ca26(event):
    NomPerso.config(text="")
    Dialogue.config(text="Un homme montre sa tête \n du haut des remparts.")
    Continuer1.bind("<Button-1>", Ca27)

def Ca27(event):
    NomPerso.config(text=nom, fg="blue")
    if LockDisney == True and MenacePassant == True:
        Dialogue.config(text="Vous êtes l'espion du Dragon !")
    elif MenacePassant == True:
        Dialogue.config(text="Vous êtes le type chelou \n de l'autre château !")
    elif PassDisney == True and MenacePassant == False:
        Dialogue.config(text="Vous êtes le type \n de l'autre château !")
    else:
        Dialogue.config(text="Qui êtes-vous ?")
    Continuer1.bind("<Button-1>", Ca28)

def Ca28(event):
    NomPerso.config(text="GARDE", fg="burlywood")
    Dialogue.config(text="Je suis GARDE...parce que \n c'est mon nom de fonction.")
    Continuer1.bind("<Button-1>", Ca29)

def Ca29(event):
    if PassDisney == True:
        Dialogue.config(text="Je ne vous félicite pas pour \n vous être trompé de château.")
    elif PassMarais == True:
        Dialogue.config(text="Vous avez survécu au marais ? \n Intéressant.")
    else:
        Dialogue.config(text="Je ne sais pas d'ou vous venez, étranger.")
    Continuer1.bind("<Button-1>", Ca30)

#----------------------------------------
#----------- Sous Partie 3 --------------
#-------------- GUARDE ------------------
#----------------------------------------

def Ca30(event):
    Dialogue.config(text="Que venez-vous faire ici ?")
    Continuer1.bind("<Button-1>", Ca31)

def Ca31(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Euh.")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.config(text="Mentir")
    Continuer2.config(text="Dire la vérité")
    Continuer1.bind("<Button-1>", Ca32a)
    Continuer2.bind("<Button-1>", Ca32b)

#---------- Choix A (Mentir) -----------

def Ca32a(event):
    global GARDE_Sympa
    GARDE_Sympa = GARDE_Sympa + 1
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je viens rendre visite \n à votre seigneur.")
    Continuer1.bind("<Button-1>", Ca33)

#---------------------------------------

#---------- Choix B (Verité) -----------

def Ca32b(event):
    global GARDE_Hostille
    GARDE_Hostille = GARDE_Hostille + 2
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je viens terrasser votre seigneur.")
    Continuer1.bind("<Button-1>", Ca33)

#---------------------------------------

def Ca33(event):
    NomPerso.config(text="GARDE", fg="burlywood")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ca34)

def Ca34(event):
    Dialogue.config(text="Et pourquoi ?")
    Continuer1.bind("<Button-1>", Ca35)

def Ca35(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Euh.")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.config(text="Aider un ami")
    Continuer2.config(text="Voler le Trésor")
    Continuer1.bind("<Button-1>", Ca36a)
    Continuer2.bind("<Button-1>", Ca36b)

#---------- Choix A (Ami) -----------

def Ca36a(event):
    global GARDE_Sympa
    GARDE_Sympa = GARDE_Sympa + 1
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="C'est pour aider un de mes amis.")
    Continuer1.bind("<Button-1>", Ca37)

#---------------------------------------

#---------- Choix B (Trésor) -----------

def Ca36b(event):
    global GARDE_Hostille
    GARDE_Hostille = GARDE_Hostille + 1
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je viens voler votre trésor.")
    Continuer1.bind("<Button-1>", Ca37)

#---------------------------------------

def Ca37(event):
    NomPerso.config(text="GARDE", fg="burlywood")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ca38)

def Ca38(event):
    Dialogue.config(text="Je dois vous posez quelques questions supplémentaires, \n simple protocole de sécurité.")
    Continuer1.bind("<Button-1>", Ca39)

def Ca39(event):
    Dialogue.config(text="Quel est le nom de notre seigneur, \n garant de la paix et de la liberté ?")
    Continuer1.bind("<Button-1>", Ca40)

def Ca40(event):
    NomPerso.config(text=nom, fg="blue")
    if LockMarais == True:
        Dialogue.config(text="Son nom est 'Seigneur Braise'.")
        global GARDE_Sympa
        GARDE_Sympa = GARDE_Sympa + 1
        Continuer1.bind("<Button-1>", Ca42)
    else:
        Dialogue.config(text="Euh.")
        Continuer2.pack(padx=10, pady=10)
        Continuer1.config(text="Seigneur Dragon ?")
        Continuer2.config(text="Tyranus ?")
        Continuer1.bind("<Button-1>", Ca41a)
        Continuer2.bind("<Button-1>", Ca41b)

#---------- Choix A (Seigneur Dragon) -----------

def Ca41a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je l'ignore, \n je le connais uniquement sous le nom de \n 'Seigneur Dragon'.")
    Continuer1.bind("<Button-1>", Ca42)

#---------------------------------------

#---------- Choix B (Tyranus) -----------

def Ca41b(event):
    global GARDE_Hostille
    GARDE_Hostille = GARDE_Hostille + 1
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Il s'appèle 'Tyranus', non ?")
    Continuer1.bind("<Button-1>", Ca42)

#---------------------------------------

def Ca42(event):
    NomPerso.config(text="GARDE", fg="burlywood")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ca43)

def Ca43(event):
    Dialogue.config(text="Comment le trouvez-vous ?")
    Continuer1.bind("<Button-1>", Ca44)

def Ca44(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Euh.")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.config(text="Il est sympa.")
    Continuer2.config(text="Il est méchant.")
    Continuer1.bind("<Button-1>", Ca45a)
    Continuer2.bind("<Button-1>", Ca45b)

#---------- Choix A (Cool) -----------

def Ca45a(event):
    global GARDE_Sympa
    GARDE_Sympa = GARDE_Sympa + 1
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je trouve que Monseigneur est bon.")
    Continuer1.bind("<Button-1>", Ca46)

#---------------------------------------

#---------- Choix B (Méchant) -----------

def Ca45b(event):
    global GARDE_Hostille
    GARDE_Hostille = GARDE_Hostille + 1
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je trouve qu'il est horrible.")
    Continuer1.bind("<Button-1>", Ca46)

#---------------------------------------

def Ca46(event):
    NomPerso.config(text="GARDE", fg="burlywood")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ca47)

def Ca47(event):
    Dialogue.config(text="Dernière question.")
    Continuer1.bind("<Button-1>", Ca48)

def Ca48(event):
    Dialogue.config(text="Qui est le plus grand et le plus beau \n garde de la région ?")
    Continuer1.bind("<Button-1>", Ca49)

def Ca49(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Euh.")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.config(text="C'est vous.")
    Continuer2.config(text="C'est moi.")
    Continuer1.bind("<Button-1>", Ca50a)
    Continuer2.bind("<Button-1>", Ca50b)

#---------- Choix A (Vous) -----------

def Ca50a(event):
    global GARDE_Sympa
    GARDE_Sympa = GARDE_Sympa + 2
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="C'est vous, bien évidemment.")
    Continuer1.bind("<Button-1>", Ca51)

#---------------------------------------

#---------- Choix B (Moi) -----------

def Ca50b(event):
    global GARDE_Hostille
    GARDE_Hostille = GARDE_Hostille + 3
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Facile, Moi.")
    Continuer1.bind("<Button-1>", Ca51)

#---------------------------------------

def Ca51(event):
    NomPerso.config(text="GARDE", fg="burlywood")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ca52)

def Ca52(event):
    if GARDE_Hostille <= GARDE_Sympa:
        Dialogue.config(text="C'est bon, vous pouvez entrer.")
        Continuer1.bind("<Button-1>", Ca53)
    else:
        Dialogue.config(text="Désolé, je vais devoir vous tuer.")
        Continuer1.bind("<Button-1>", Ca52a)

#-------------- ROUTE - FIN GUARDE --------------

def Ca52a(event):
    SE_Pistolet_Degainage.play()
    NomPerso.config(text="")
    Dialogue.config(text="GARDE me pointe une arme dessus.")
    Continuer1.bind("<Button-1>", Ca52b)

def Ca52b(event):
    SE_Pistolet.play()
    if Pistolet == True:
        Dialogue.config(text="Mais rapidement, \n je lui tire dessus avec la mienne.")
        Continuer1.bind("<Button-1>", Ca52c)
    else:
        Dialogue.config(text="Il me tire dessus.")
        Continuer1.bind("<Button-1>", FIN_GARDE)

def Ca52c(event):
    NomPerso.config(text="GARDE", fg="burlywood")
    Dialogue.config(text="AH !")
    Continuer1.bind("<Button-1>", Ca52d)

def Ca52d(event):
    NomPerso.config(text="")
    Dialogue.config(text="Il tombe du haut des remparts \n juste à coté de moi.")
    Continuer1.bind("<Button-1>", Ca52e)

def Ca52e(event):
    Dialogue.config(text="Et d'un coup, la porte s'ouvre.")
    Continuer1.bind("<Button-1>", Ca53)
#------------------------------------------------

def Ca53(event):
    pygame.mixer.music.fadeout(400)
    NomPerso.config(text="")
    Dialogue.config(text="Je pénètre donc dans le château.")
    Continuer1.bind("<Button-1>", Cb1)
    LevelUp(event)

#----------------------------------------
#-------------- Partie b ----------------
#------------- LE CHATEAU ---------------
#----------------------------------------

#----------------------------------------
#----------- Sous Partie 1 --------------
#------------ LABYRINTHE ----------------
#----------------------------------------

def Cb1(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Chateau)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    #---------------------------
    Chap3.pack_forget()
    NewGame.pack_forget()
    Chap3_1.pack_forget()
    Chap3_2.pack_forget()
    Chap3_3.pack_forget()
    Chap3_4.pack_forget()
    DescChoixChap.pack_forget()
    #--------------------------
    Decor.pack(padx=10, pady=10)
    NomPerso.pack(padx=10, pady=10)
    Dialogue.pack(padx=10, pady=10)
    Continuer1.pack(padx=10, pady=10)
    Continuer1.config(text=">")
    NomPerso.config(text="")
    Dialogue.config(text="Le château est un immense \n labyrinthe à l'interieur.")
    Continuer1.bind("<Button-1>", Cb2)

def Cb2(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Il doit avoir un grand trésor \n pour avoir un château comme ça.")
    Continuer1.bind("<Button-1>", Cb3)

def Cb3(event):
    SE_Porte_Chateau.play()
    NomPerso.config(text="")
    Dialogue.config(text="Soudainement, la porte d'entrée se referme.")
    Continuer1.bind("<Button-1>", Cb4)

def Cb4(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Cb5)

def Cb5(event):
    Dialogue.config(text="Je n'ai plus le choix \n que d'avancer au hasard.")
    Continuer1.bind("<Button-1>", Cb6)

def Cb6(event):
    Porterandom()
    NomPerso.config(text="")
    Dialogue.config(text="Devant moi se dresse 3 portes.")
    Continuer1.bind("<Button-1>", Cb7)

def Cb7(event):
    Dialogue.config(text="Je prend celle....")
    Continuer2.pack(padx=10, pady=10)
    Continuer3.pack(padx=10, pady=10)
    Continuer1.config(text="...de gauche.")
    Continuer2.config(text="...du haut.")
    Continuer3.config(text="...de droite.")
    Continuer1.bind("<Button-1>", Cb7a)
    Continuer2.bind("<Button-1>", Cb7b)
    Continuer3.bind("<Button-1>", Cb7c)

#---------- Choix A (Gauche) -----------

def Cb7a(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je prend la porte de gauche.")
    if portedragon == 1:
        Continuer1.bind("<Button-1>", Cb8)
    elif portebonus == 1:
        Continuer1.bind("<Button-1>", Cb8a)
    else:
        Continuer1.bind("<Button-1>", Cb6)

#---------------------------------------

#---------- Choix B (Haut) -----------

def Cb7b(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je prend la porte du haut")
    if portedragon == 2:
        Continuer1.bind("<Button-1>", Cb8)
    elif portebonus == 2:
        Continuer1.bind("<Button-1>", Cb8a)
    else:
        Continuer1.bind("<Button-1>", Cb6)

#---------------------------------------

#---------- Choix C (Droite) -----------

def Cb7c(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je prend la porte de droite.")
    if portedragon == 3:
        Continuer1.bind("<Button-1>", Cb8)
    elif portebonus == 3:
        Continuer1.bind("<Button-1>", Cb8a)
    else:
        Continuer1.bind("<Button-1>", Cb6)

#---------------------------------------


#--------------- BONUS -------------------

def Cb8a(event):
    global bonusobtenu
    bonusobtenu = True
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="J'arrive dans une salle étrange.")
    Continuer1.bind("<Button-1>", Cb8b)

def Cb8b(event):
    Dialogue.config(text="Il y a sur une table une potion.")
    Continuer1.bind("<Button-1>", Cb8c)

def Cb8c(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="C'est...une potion magique ?")
    Continuer1.bind("<Button-1>", Cb8d)

def Cb8d(event):
    Dialogue.config(text="Il me la faut !")
    Continuer1.bind("<Button-1>", Cb8e)

def Cb8e(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je prend la potion et la boit.")
    if niveau%2 == 0:
        LevelUp(event)
        LevelUp(event)
    else:
        LevelUp(event)
    Continuer1.bind("<Button-1>", Cb8f)

def Cb8f(event):
    Dialogue.config(text="Après cela, \n je sort de la pièce.")
    Continuer1.bind("<Button-1>", Cb6)
#-----------------------------------------


def Cb8(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="J'arrive dans un couloir.")
    Continuer1.bind("<Button-1>", Cb9)

def Cb9(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Enfin...")
    Continuer1.bind("<Button-1>", Cb10)

#----------------------------------------
#----------- Sous Partie 2 --------------
#----------- GARDE PARTIE 2 -------------
#----------------------------------------

def Cb10(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_GARDE)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    NomPerso.config(text="???", fg="burlywood")
    Dialogue.config(text="PAS SI VITE !")
    Continuer1.bind("<Button-1>", Cb10a)

def Cb10a(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Hein ?")
    Continuer1.bind("<Button-1>", Cb11)

def Cb11(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je me retourne et...")
    Continuer1.bind("<Button-1>", Cb12)

def Cb12(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Vous ?")
    Continuer1.bind("<Button-1>", Cb13)

def Cb13(event):
    NomPerso.config(text="GARDE", fg="burlywood")
    if GARDE_Hostille <= GARDE_Sympa:
        Dialogue.config(text="Oui, c'est moi.")
    else:
        Dialogue.config(text="J'ai survécu !")
    Continuer1.bind("<Button-1>", Cb14)

def Cb14(event):
    NomPerso.config(text="GARDE", fg="burlywood")
    if GARDE_Hostille <= GARDE_Sympa:
        Dialogue.config(text="J'ai l'impression que vous allez causer des problèmes.")
    else:
        Dialogue.config(text="Vous allez payer pour ça !")
    Continuer1.bind("<Button-1>", Cb15)

def Cb15(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Attendez ! \n Je peut expliquer !")
    Continuer1.bind("<Button-1>", Cb16)

def Cb16(event):
    NomPerso.config(text="GARDE", fg="burlywood")
    Dialogue.config(text="Allez-y...")
    Continuer1.bind("<Button-1>", Cb17)

def Cb17(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Et bien...")
    Continuer2.pack(padx=10, pady=10)
    Continuer3.pack(padx=10, pady=10)
    Continuer1.config(text="Le convaincre (Charisme 5)")
    Continuer2.config(text="Reflexes Ninja (Force 6)")
    Continuer3.config(text="Être sincère")
    Continuer1.bind("<Button-1>", Cb18a)
    Continuer2.bind("<Button-1>", Cb18b)
    Continuer3.bind("<Button-1>", Cb18c)


#------------ Choix A (le convaincre) ------------

def Cb18a(event):
    global Echec
    if charisme < 5:
        Echec = True
    else:
        Echec = False
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Écoutez, vous devez me laisser passer.")
    Continuer1.bind("<Button-1>", Cb19a)

def Cb19a(event):
    Dialogue.config(text="Le Dragon doit être arrêté, \n je n'ai pas le choix.")
    Continuer1.bind("<Button-1>", Cb20a)

def Cb20a(event):
    NomPerso.config(text="GARDE", fg="burlywood")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Cb21a)

def Cb21a(event):
    if Echec == True:
        Dialogue.config(text="Oui, mais il paye bien, \n et j'ai un château gratuit.")
    else:
        Dialogue.config(text="Vous avez raison, \n il faut l'arreter.")
    Continuer1.bind("<Button-1>", Cb22a)

def Cb22a(event):
    if Echec == True:
        Dialogue.config(text="Vous allez le lui dire en personne \n qu'il est néfaste.")
    else:
        Dialogue.config(text="Je vous laisse.")
    Continuer1.bind("<Button-1>", Cb23a)

def Cb23a(event):
    Dialogue.config(text="Allez-y.")
    Continuer1.bind("<Button-1>", Cb24a)

def Cb24a(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Très bien...")
    Continuer1.bind("<Button-1>", Cb25)

#-------------------------------------------------

#------------ Choix B (Reflexes ninja) -----------

def Cb18b(event):
    global Echec
    if force < 6:
        Echec = True
    else:
        Echec = False
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="JAMAIS !")
    Continuer1.bind("<Button-1>", Cb19b)

def Cb19b(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je lui fonce dessus \n afin de l'éliminer.")
    Continuer1.bind("<Button-1>", Cb20b)

def Cb20b(event):
    if Echec == True:
        SE_Pistolet.play()
        Dialogue.config(text="Mais il est plus rapide, \n et il me tire dessus avant.")
        Continuer1.bind("<Button-1>", FIN_GARDE_NINJA)
    else:
        Dialogue.config(text="Je réussit à le \n faire tomber par terre.")
        Continuer1.bind("<Button-1>", Cb21b)

def Cb21b(event):
    Dialogue.config(text="Je l'élimine rapidement.")
    Continuer1.bind("<Button-1>", Cb22b)

def Cb22b(event):
    Dialogue.config(text="Il n'y a plus d'obstacles \n entre moi et le Dragon.")
    Continuer1.bind("<Button-1>", Cb25)
#-------------------------------------------------

#------------ Choix C (Etre sincère) -------------

def Cb18c(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je suis obligé, \n je dois aider un ami.")
    Continuer1.bind("<Button-1>", Cb19c)

def Cb19c(event):
    Dialogue.config(text="Ne voulez-vous pas aussi \n aider vos amis ?")
    Continuer1.bind("<Button-1>", Cb20c)

def Cb20c(event):
    NomPerso.config(text="GARDE", fg="burlywood")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Cb21c)

def Cb21c(event):
    Dialogue.config(text="Bon, je vais vous laissez.")
    Continuer1.bind("<Button-1>", Cb22c)

def Cb22c(event):
    Dialogue.config(text="Mais pas de grabuge, compris ?")
    Continuer1.bind("<Button-1>", Cb23c)

def Cb23c(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Oui, merci.")
    Continuer1.bind("<Button-1>", Cb25)

#-------------------------------------------------

def Cb25(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Chateau)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    NomPerso.config(text="")
    Dialogue.config(text="Je continue alors ma route \n dans le couloir.")
    Continuer1.bind("<Button-1>", Cb26)

def Cb26(event):
    Dialogue.config(text="Au bout, il y a une immense porte")
    Continuer1.bind("<Button-1>", Cb27)

def Cb27(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Ca doit être la salle de trône du Dragon.")
    Continuer1.bind("<Button-1>", Cb28)

def Cb28(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je reprend mon souffle...")
    Continuer1.bind("<Button-1>", Cb29)

def Cb29(event):
    Dialogue.config(text="...et je rentre dans la salle.")
    Continuer1.bind("<Button-1>", Cc1)



#----------------------------------------
#-------------- Partie c ----------------
#------------- LE DRAGON ---------------
#----------------------------------------

#----------------------------------------
#----------- Sous Partie 1 --------------
#------------- DIALOGUE -----------------
#----------------------------------------

def Cc1(event):
    #---------------------------
    Chap3.pack_forget()
    NewGame.pack_forget()
    Chap3_1.pack_forget()
    Chap3_2.pack_forget()
    Chap3_3.pack_forget()
    Chap3_4.pack_forget()
    DescChoixChap.pack_forget()
    #--------------------------
    Decor.pack(padx=10, pady=10)
    NomPerso.pack(padx=10, pady=10)
    Dialogue.pack(padx=10, pady=10)
    Continuer1.pack(padx=10, pady=10)
    Continuer1.config(text=">")
    NomPerso.config(text="")
    Dialogue.config(text="La salle est immense.")
    Continuer1.bind("<Button-1>", Cc2)

def Cc2(event):
    Dialogue.config(text="Au centre, il y a un trône.")
    Continuer1.bind("<Button-1>", Cc3)

def Cc3(event):
    Dialogue.config(text="Et sur ce trône...")
    Continuer1.bind("<Button-1>", Cc4)

def Cc4(event):
    SE_Dragon_Cri.play()
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Tient donc.")
    Continuer1.bind("<Button-1>", Cc5)

def Cc5(event):
    if PassMarais == True:
        Dialogue.config(text="Le survivant du marais.")
    elif PassDisney == True:
        Dialogue.config(text="L'homme qui à confondu \n mon château avec celui de Disney.")
    else:
        Dialogue.config(text="L'homme qui à commencé au Chapitre 3, \n vaurien.")
    Continuer1.bind("<Button-1>", Cc6)

def Cc6(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="C'est moi.")
    Continuer1.bind("<Button-1>", Cc7)

def Cc7(event):
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Comment est-tu entré ?\n GARDE était supposé ne laisser\npersonne entrer dans mon repaire !")
    Continuer1.bind("<Button-1>", Cc8)

def Cc8(event):
    Dialogue.config(text="Peut importe ! \n Que vient-tu faire ici ?")
    Continuer1.bind("<Button-1>", Cc9)

def Cc9(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Je viens vous voler \n votre plus grand trésor.")
    Continuer1.bind("<Button-1>", Cc10)

def Cc10(event):
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Comment ?")
    Continuer1.bind("<Button-1>", Cc11)

def Cc11(event):
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Cc12)

def Cc12(event):
    Dialogue.config(text="C'est ce misérable Harold qui t'envoie ?")
    Continuer1.bind("<Button-1>", Cc13)

def Cc13(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Comment...")
    Continuer1.bind("<Button-1>", Cc14)

def Cc14(event):
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Je ne rendrais jamais ses clefs ! \n Elles sont à moi maintenant !")
    Continuer1.bind("<Button-1>", Cc15)

def Cc15(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Ses clefs ?")
    Continuer1.bind("<Button-1>", Cc16)

def Cc16(event):
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Il ne te l'avait pas dit ?")
    Continuer1.bind("<Button-1>", Cc17)

def Cc17(event):
    Dialogue.config(text="La semaine dernière, \n j'ai volé ses clefs de voiture.")
    Continuer1.bind("<Button-1>", Cc18)

def Cc18(event):
    Dialogue.config(text="Ca lui apprendra à ne pas se prosterner devant moi.")
    Continuer1.bind("<Button-1>", Cc19)

def Cc19(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Cc20)

def Cc20(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je fais ca...\n pour des clefs.")
    Continuer1.bind("<Button-1>", Cc21)

def Cc21(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Dragon)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Assez discuté !")
    Continuer1.bind("<Button-1>", Cc22)

def Cc22(event):
    Dialogue.config(text="Je vais te tuer !")
    Continuer1.bind("<Button-1>", Cc23)

#----------------------------------------
#----------- Sous Partie 2 --------------
#-------------- COMBAT ------------------
#----------------------------------------

def Cc23(event):
    NomPerso.config(text="")
    Dialogue.config(text="Le Dragon se prépare à me tuer.")
    Continuer1.bind("<Button-1>", Cc24)

def Cc24(event):
    Dialogue.config(text="Je décide...")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.config(text="...de l'attaquer")
    Continuer2.config(text="...de le convaincre (Charisme 10)")
    Continuer1.bind("<Button-1>", Dragon_attaque1)
    Continuer2.bind("<Button-1>", Dragon_conv1)
    if Flute == True:
        Continuer3.pack(padx=10, pady=10)
        Continuer3.config(text="...de le charmer avec la flute")
        Continuer3.bind("<Button-1>", Dragon_flute1)


#------------ Attaque ------------------

def Dragon_attaque1(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je vais l'attaquer.")
    Continuer1.bind("<Button-1>", Dragon_attaque2)

def Dragon_attaque2(event):
    Dialogue.config(text="Mais avec quoi ?")
    if Epee == True:
        Continuer1.config(text="Avec l'épée (Force 7)")
        Continuer1.bind("<Button-1>", Dragon_attaque3a)
    if Pistolet == True:
        Continuer2.pack(padx=10, pady=10)
        Continuer2.config(text="Avec le pistolet")
        Continuer2.bind("<Button-1>", Dragon_attaque3b)
    if Epee == False and Pistolet == False:
        Continuer1.config(text="AVEC RIEN !")
        Continuer1.bind("<Button-1>", Dragon_attaque3c)

#------------- Epée ----------------

def Dragon_attaque3a(event):
    global Echec
    if force < 7:
        Echec = True
    else:
        Echec = False
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je vais l'attaquer \n avec mon épée.")
    Continuer1.bind("<Button-1>", Dragon_attaque4a)

def Dragon_attaque4a(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Meurt Dragon !")
    Continuer1.bind("<Button-1>", Dragon_attaque5a)

def Dragon_attaque5a(event):
    SE_Epee.play()
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Dragon_attaque6a)

def Dragon_attaque6a(event):
    NomPerso.config(text="")
    if Echec == False:
        Dialogue.config(text="J'ai salement amoché le Dragon.")
    else:
        Dialogue.config(text="Je n'ai pas réussi à lui faire mal.")
    Continuer1.bind("<Button-1>", Dragon_attaque7a)

def Dragon_attaque7a(event):
    NomPerso.config(text="Dragon", fg="red")
    if Echec == False:
        Dialogue.config(text="AH ! \n Ca fait mal ça !")
    else:
        Dialogue.config(text="Pathétique.")
    Continuer1.bind("<Button-1>", Dragon_attaque8a)

def Dragon_attaque8a(event):
    if Echec == False:
        Dialogue.config(text="Je te hais, humain !")
    else:
        Dialogue.config(text="Une dernière volonté ?")
    Continuer1.bind("<Button-1>", Dragon_attaque9a)

def Dragon_attaque9a(event):
    NomPerso.config(text=nom, fg="blue")
    if Echec == False:
        Dialogue.config(text="Une dernière volonté ?")
    else:
        Dialogue.config(text="Euh...")
    Continuer1.bind("<Button-1>", Dragon_attaque10a)

def Dragon_attaque10a(event):
    NomPerso.config(text="Dragon", fg="red")
    if Echec == False:
        Dialogue.config(text="Va mourir !")
    else:
        Dialogue.config(text="Je suis d'accord, \n je vais te tuer maintenant.")
    Continuer1.bind("<Button-1>", Dragon_attaque11a)

def Dragon_attaque11a(event):
    NomPerso.config(text="")
    if Echec == False:
        SE_Epee.play()
        global DragonTue
        DragonTue = True
        Dialogue.config(text="J'achève le Dragon de mon épée.")
        Continuer1.bind("<Button-1>", Dragon_attaque12a)
    else:
        SE_Dragon_Feu.play()
        Dialogue.config(text="Le Dragon me crache du feu dessus.")
        Continuer1.bind("<Button-1>", FIN_Dragon_Epee)

def Dragon_attaque12a(event):
    pygame.mixer.music.fadeout(400)
    Dialogue.config(text="J'ai gagné le combat.")
    Continuer1.bind("<Button-1>", Cc25)


#------------------------------------

#------------ Pistolet --------------

def Dragon_attaque3b(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je vais l'attaquer \n avec mon pistolet.")
    Continuer1.bind("<Button-1>", Dragon_attaque4b)

def Dragon_attaque4b(event):
    SE_Pistolet_Degainage.play()
    Dialogue.config(text="Je le dégaine...")
    Continuer1.bind("<Button-1>", Dragon_attaque5b)

def Dragon_attaque5b(event):
    SE_Pistolet.play()
    Dialogue.config(text="...et je tire.")
    Continuer1.bind("<Button-1>", Dragon_attaque6b)

def Dragon_attaque6b(event):
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Ah ! \n C'est de la triche !.")
    Continuer1.bind("<Button-1>", Dragon_attaque7b)

def Dragon_attaque7b(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Non.")
    Continuer1.bind("<Button-1>", Dragon_attaque8b)

def Dragon_attaque8b(event):
    NomPerso.config(text="")
    global DragonTue
    DragonTue = True
    Dialogue.config(text="Le Dragon s'enfondre, mort.")
    Continuer1.bind("<Button-1>", Dragon_attaque9b)

def Dragon_attaque9b(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="J'ai gagné.")
    Continuer1.bind("<Button-1>", Cc25)

#------------------------------------

#------------ Main Nu --------------

def Dragon_attaque3c(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Dialogue.config(text="Je vais l'attaquer \n à main nu.")
    Continuer1.bind("<Button-1>", Dragon_attaque4c)

def Dragon_attaque4c(event):
    Dialogue.config(text="Je fonce en direction du Dragon.")
    Continuer1.bind("<Button-1>", Dragon_attaque5c)

def Dragon_attaque5c(event):
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Pathétique.")
    Continuer1.bind("<Button-1>", Dragon_attaque6c)

def Dragon_attaque6c(event):
    NomPerso.config(text="")
    SE_Dragon_Feu.play()
    Dialogue.config(text="Le Dragon m'incinère de \n son souffle ardent.")
    Continuer1.bind("<Button-1>", FIN_Dragon_Rien)

#------------------------------------

#---------------------------------------

#-------------- Convaincre -------------

def Dragon_conv1(event):
    global Echec
    if charisme < 10:
        Echec = True
    else:
        Echec = False
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je vais essayer de le convaincre \n de ne pas me tuer.")
    Continuer1.bind("<Button-1>", Dragon_conv2)

def Dragon_conv2(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Attendez !")
    Continuer1.bind("<Button-1>", Dragon_conv3)

def Dragon_conv3(event):
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Quoi ?")
    Continuer1.bind("<Button-1>", Dragon_conv4)

def Dragon_conv4(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Vous êtes sur de vouloir me tuer ?")
    Continuer1.bind("<Button-1>", Dragon_conv5)

def Dragon_conv5(event):
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Oui, pourquoi ?")
    Continuer1.bind("<Button-1>", Dragon_conv6)

def Dragon_conv6(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Vous ne pouvez me tuer, \n je suis innocent !")
    Continuer1.bind("<Button-1>", Dragon_conv7)

def Dragon_conv7(event):
    NomPerso.config(text="Dragon", fg="red")
    Dialogue.config(text="Quoi ?")
    Continuer1.bind("<Button-1>", Dragon_conv8)

def Dragon_conv8(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Si vous me tuer, \n vous faites un meurtre.")
    Continuer1.bind("<Button-1>", Dragon_conv9)

def Dragon_conv9(event):
    Dialogue.config(text="Et les meurtriers se font arrêter.")
    Continuer1.bind("<Button-1>", Dragon_conv10)

def Dragon_conv10(event):
    NomPerso.config(text="Dragon", fg="red")
    if Echec == True:
        Dialogue.config(text="Tais-toi !")
    else:
        Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Dragon_conv11)

def Dragon_conv11(event):
    if Echec == True:
        SE_Dragon_Feu.play()
        NomPerso.config(text="")
        Dialogue.config(text="Le dragon me crache du feu dessus.")
        Continuer1.bind("<Button-1>", FIN_Dragon_Charisme)
    else:
        Dialogue.config(text="Tu as raison.")
        Continuer1.bind("<Button-1>", Dragon_conv12)

def Dragon_conv12(event):
    Dialogue.config(text="Je n'y avais jamais pensé.")
    Continuer1.bind("<Button-1>", Dragon_conv13)

def Dragon_conv13(event):
    global DragonBlaze
    DragonBlaze = True
    Dialogue.config(text="Comment je fais faire le mal \n maintenant ?")
    Continuer1.bind("<Button-1>", Dragon_conv14)

def Dragon_conv14(event):
    Dialogue.config(text="Bon, tu peu t'en aller humain, \n reprend les clefs.")
    Continuer1.bind("<Button-1>", Dragon_conv15)

def Dragon_conv15(event):
    pygame.mixer.music.fadeout(400)
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Merci.")
    Continuer1.bind("<Button-1>", Cc25)

#---------------------------------------

#-------------- Charmer -------------

def Dragon_flute1(event):
    Continuer1.config(text=">")
    Continuer2.pack_forget()
    Continuer3.pack_forget()
    Dialogue.config(text="Je vais essayer de le \n charmer avec ma flûte.")
    Continuer1.bind("<Button-1>", Dragon_flute2)

def Dragon_flute2(event):
    pygame.mixer.music.fadeout(400)
    Dialogue.config(text="Je la sort et \n je commence à jouer.")
    Continuer1.bind("<Button-1>", Dragon_flute3)

def Dragon_flute3(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Dragon_flute4)

def Dragon_flute4(event):
    NomPerso.config(text="")
    if Partitions == False:
        SE_Flute_EarRape.play()
        Dialogue.config(text="Sans les partitions, \n je fais n'importe quoi.")
    else:
        SE_Flute.play()
        Dialogue.config(text="Avec les partitions, \n je joue la mélodie.")
    Continuer1.bind("<Button-1>", Dragon_flute5)

def Dragon_flute5(event):
    NomPerso.config(text="Dragon", fg="red")
    if Partitions == False:
        Dialogue.config(text="Quelle est cette mélodie infâme ? \n Arrête ça tout de suite !")
    else:
        Dialogue.config(text="Que...Quelle est cette mélodie ?")
    Continuer1.bind("<Button-1>", Dragon_flute6)

def Dragon_flute6(event):
    if Partitions == False:
        NomPerso.config(text="")
        SE_Dragon_Feu.play()
        Dialogue.config(text="Le Dragon m'incinère sur place.")
        Continuer1.bind("<Button-1>", FIN_Dragon_Flute)
    else:
        global DragonCharme
        DragonCharme = True
        Dialogue.config(text="Je...Je...\n suis à votre disposition...maitre.")
        Continuer1.bind("<Button-1>", Dragon_flute7)

def Dragon_flute7(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Excellent.")
    Continuer1.bind("<Button-1>", Cc25)


#---------------------------------------


#----------------------------------------
#----------- Sous Partie 3 --------------
#-------------- TRESOR ------------------
#----------------------------------------


def Cc25(event):
    NomPerso.config(text="")
    Dialogue.config(text="La confrontation gagnée, \n je cherche les clefs.")
    Continuer1.bind("<Button-1>", Cc26)
    LevelUp(event)

def Cc26(event):
    if DragonCharme == True:
        Dialogue.config(text="Je les trouve facilement \n avec l'aide du Dragon.")
    else:
        Dialogue.config(text="Je les trouve avec un peu de mal.")
    Continuer1.bind("<Button-1>", Cc27)

def Cc27(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Les clefs de la voiture d'Harold.")
    Continuer1.bind("<Button-1>", Cc28)

def Cc28(event):
    Dialogue.config(text="Il faut les lui rendre maintenant.")
    Continuer1.bind("<Button-1>", Cc29)

def Cc29(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je commence alors mon \n long chemin du retour.")
    Continuer1.bind("<Button-1>", Cc30)

def Cc30(event):
    Dialogue.config(text="Au bout de ce chemin, \n il y a mon retour chez moi.")
    Continuer1.bind("<Button-1>", Cd1)


#----------------------------------------
#-------------- Partie d ----------------
#---------- MOMENT CRITIQUE -------------
#----------------------------------------


def Cd1(event):
    #---------------------------
    Chap3.pack_forget()
    NewGame.pack_forget()
    Chap3_1.pack_forget()
    Chap3_2.pack_forget()
    Chap3_3.pack_forget()
    Chap3_4.pack_forget()
    DescChoixChap.pack_forget()
    #--------------------------
    Decor.pack(padx=10, pady=10)
    NomPerso.pack(padx=10, pady=10)
    Dialogue.pack(padx=10, pady=10)
    Continuer1.pack(padx=10, pady=10)
    Continuer1.config(text=">")
    NomPerso.config(text="")
    if DragonCharme == True:
        Dialogue.config(text="Avec l'aide du Dragon, \n j'arrive rapidement chez Harold.")
    else:
        Dialogue.config(text="Le trajet fut long et pénible, \n mais je suis enfin arrivé chez Harold.")
    Continuer1.bind("<Button-1>", Cd2)

def Cd2(event):
    Dialogue.config(text="Je vais enfin pouvoir lui rendre \n les clefs de sa voiture.")
    Continuer1.bind("<Button-1>", Cd3)

def Cd3(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Cd4)

def Cd4(event):
    NomPerso.config(text="")
    Dialogue.config(text="Aie-je vraiment \n envie de le faire ?")
    Continuer1.bind("<Button-1>", Cd5)

def Cd5(event):
    Dialogue.config(text="Tout ça... \n pour des clefs.")
    Continuer1.bind("<Button-1>", Cd6)

def Cd6(event):
    Dialogue.config(text="Harold s'est clairement joué de moi.")
    Continuer1.bind("<Button-1>", Cd7)

def Cd7(event):
    Dialogue.config(text="Que faire ?")
    Continuer2.pack(padx=10, pady=10)
    Continuer1.config(text="Les rendre")
    Continuer2.config(text="Voler la voiture")
    Continuer1.bind("<Button-1>", Cd8a)
    Continuer2.bind("<Button-1>", Cd8b)

#----------- Choix A (les rendre) -------


def Cd8a(event):
    Continuer2.pack_forget()
    Continuer1.config(text=">")
    Dialogue.config(text="Je vais les rendre.")
    Continuer1.bind("<Button-1>", Cd9a)

def Cd9a(event):
    Dialogue.config(text="Lui seul sait comment \n me renvoyer chez moi.")
    Continuer1.bind("<Button-1>", Cd10a)

def Cd10a(event):
    Dialogue.config(text="Je m'avance donc vers \n la porte d'entrée de la maison.")
    Continuer1.bind("<Button-1>", Ce1)


#----------------------------------------

#----------- Choix B (voler la voiture) -------


def Cd8b(event):
    Continuer2.pack_forget()
    Continuer1.config(text=">")
    Dialogue.config(text="Je vais voler sa voiture.")
    Continuer1.bind("<Button-1>", Cd9b)

def Cd9b(event):
    Dialogue.config(text="Ca lui apprendra à \n m'utiliser de la sorte.")
    Continuer1.bind("<Button-1>", Cd10b)

def Cd9b(event):
    Dialogue.config(text="Je m'avance donc vers la voiture d'Harold.")
    Continuer1.bind("<Button-1>", Cf1)

#----------------------------------------


#----------------------------------------
#-------------- Partie e ----------------
#--------------- ADIEUX -----------------
#----------------------------------------

def Ce1(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Fin)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    Dialogue.config(text="Arrivé, je sonne.")
    Continuer1.bind("<Button-1>", Ce2)

def Ce2(event):
    SE_Sonnerie.play()
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ce3)

def Ce3(event):
    SE_Porte.play()
    Dialogue.config(text="Après quelques secondes, \n la porte s'ouvre.")
    Continuer1.bind("<Button-1>", Ce4)

def Ce4(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Guerrier ? C'est bien vous ?")
    Continuer1.bind("<Button-1>", Ce5)

def Ce5(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Oui, c'est moi. \n J'ai réussi.")
    Continuer1.bind("<Button-1>", Ce6)

def Ce6(event):
    if DragonCharme == True:
        Dialogue.config(text="J'ai charmé le Dragon avec ma flûte.")
    elif DragonTue == True:
        Dialogue.config(text="J'ai tué le Dragon.")
    elif DragonBlaze == True:
        Dialogue.config(text="J'ai convaincu le Dragon \n d'arreter son règne de Terreur.")
    else:
        Dialogue.config(text="Mais je n'ai pas vu de Dragon.")
    Continuer1.bind("<Button-1>", Ce7)

def Ce7(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Vraiment ? \n Merci beaucoup !")
    Continuer1.bind("<Button-1>", Ce8)

def Ce8(event):
    Dialogue.config(text="Je pensais  ne jamais revoir mes clefs.")
    Continuer1.bind("<Button-1>", Ce9)

def Ce9(event):
    Dialogue.config(text="Excusez-moi de vous avoir caché cela, \n c'était trop embarrassant à dire.")
    Continuer1.bind("<Button-1>", Ce10)

def Ce10(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Ce n'est pas grave.")
    Continuer1.bind("<Button-1>", Ce11)

def Ce11(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Ah, avant que je ne l'oublie.")
    Continuer1.bind("<Button-1>", Ce12)

def Ce12(event):
    if Augmentation == True:
        Dialogue.config(text="Voici votre million pour m'avoir aidé.")
    else:
        Dialogue.config(text="Voici 10 miles euros pour vous remercier.")
    Continuer1.bind("<Button-1>", Ce13)

def Ce13(event):
    NomPerso.config(text="")
    Dialogue.config(text="Il me tend les billets.")
    Continuer1.bind("<Button-1>", Ce14)

def Ce14(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Merci.")
    Continuer1.bind("<Button-1>", Ce15)

def Ce15(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Maintenant, je pense que \n vous voulez retourner chez vous.")
    Continuer1.bind("<Button-1>", Ce16)

def Ce16(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="En effet.")
    Continuer1.bind("<Button-1>", Ce17)

def Ce17(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="C'est simple, \n vous allez voir.")
    Continuer1.bind("<Button-1>", Ce18)

def Ce18(event):
    Dialogue.config(text="Buvez ceci.")
    Continuer1.bind("<Button-1>", Ce19)

def Ce19(event):
    NomPerso.config(text="")
    Dialogue.config(text="Il me tend un bol remplit \n d'un étrange liquide.")
    Continuer1.bind("<Button-1>", Ce20)

def Ce20(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Cette potion vous ramènera chez vous.")
    Continuer1.bind("<Button-1>", Ce21)

def Ce21(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Très bien.")
    Continuer1.bind("<Button-1>", Ce22)

def Ce22(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Adieu, Guerrier.")
    Continuer1.bind("<Button-1>", Ce23)

def Ce23(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Adieu, Harold.")
    Continuer1.bind("<Button-1>", Ce24)

def Ce24(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je boit le liquide.")
    Continuer1.bind("<Button-1>", Ce25)

def Ce25(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Ce26)

def Ce26(event):
    NomPerso.config(text="")
    Dialogue.config(text="Je perd aussitôt connaissance.")
    Continuer1.bind("<Button-1>", Ce27)

def Ce27(event):
    Dialogue.config(text="Mais...")
    Continuer1.bind("<Button-1>", Ce28)

def Ce28(event):
    Dialogue.config(text="...je me reveille dans une clairière.")
    Continuer1.bind("<Button-1>", Ce29)

def Ce29(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Je suis enfin de retour.")
    Continuer1.bind("<Button-1>", Ce30)

def Ce30(event):
    Dialogue.config(text="C'est la fin de cette aventure.")
    Continuer1.bind("<Button-1>", FIN_Harold)

#----------------------------------------
#-------------- Partie f ----------------
#--------------- CAVALE -----------------
#----------------------------------------

def Cf1(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Fuite)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.15)
    Dialogue.config(text="Arrivé, j'ouvre la voiture.")
    Continuer1.bind("<Button-1>", Cf2)

def Cf2(event):
    SE_Voiture.play()
    Dialogue.config(text="Puis je la démarre.")
    Continuer1.bind("<Button-1>", Cf3)

def Cf3(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Qu'est ce qu'il se passe ici ?")
    Continuer1.bind("<Button-1>", Cf4)

def Cf4(event):
    NomPerso.config(text="")
    Dialogue.config(text="Harold sort de sa maison.")
    Continuer1.bind("<Button-1>", Cf5)

def Cf5(event):
    NomPerso.config(text="Harold", fg="green")
    Dialogue.config(text="Que faites vous ? \n AU VOLEUR !")
    Continuer1.bind("<Button-1>", Cf6)

def Cf6(event):
    NomPerso.config(text="")
    if DragonCharme == True:
        SE_Dragon_Feu.play()
        Dialogue.config(text="Le Dragon lui crache du feu dessus, \n sécurisant ma fuite.")
    else:
        Dialogue.config(text="Je ne l'écoute pas, \n et je m'enfuis avec la voiture.")
    Continuer1.bind("<Button-1>", Cf7)

def Cf7(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Cf8)

def Cf8(event):
    NomPerso.config(text="")
    Dialogue.config(text="Ne connaissant pas ce monde, \n je roule au hasard.")
    Continuer1.bind("<Button-1>", Cf9)

def Cf9(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="Hein ?")
    Continuer1.bind("<Button-1>", Cf10)

def Cf10(event):
    NomPerso.config(text="")
    Dialogue.config(text="La police me poursuit.")
    Continuer1.bind("<Button-1>", Cf11)

def Cf11(event):
    if DragonCharme == True:
        Dialogue.config(text="J'ai le Dragon pour m'aider.")
    else:
        Dialogue.config(text="Je n'ai personne pour m'aider.")
    Continuer1.bind("<Button-1>", Cf12)

def Cf12(event):
    if DragonCharme == True:
        SE_Dragon_Feu.play()
        Dialogue.config(text="Le Dragon commence à cracher \n du feu sur les policiers.")
    else:
        Dialogue.config(text="Je dois les semer.")
    Continuer1.bind("<Button-1>", Cf13)

def Cf13(event):
    if DragonCharme == True:
        Dialogue.config(text="Les voitures explosent à cause du feu.")
    else:
        Dialogue.config(text="Les voitures se rapprochent.")
    Continuer1.bind("<Button-1>", Cf14)

def Cf14(event):
    if DragonCharme == True:
        Dialogue.config(text="Mais des hélicoptères arrivent.")
    else:
        Dialogue.config(text="Elles vont plus vite que moi.")
    Continuer1.bind("<Button-1>", Cf15)

def Cf15(event):
    if DragonCharme == True:
        Dialogue.config(text="Ils abattent le Dragon.")
    else:
        Dialogue.config(text="Ils vont essayer de me forcer à m'arreter.")
    Continuer1.bind("<Button-1>", Cf16)

def Cf16(event):
    if DragonCharme == True:
        Dialogue.config(text="Le Dragon s'écrase devant moi.")
    else:
        Dialogue.config(text="Une voiture me fait une queue de poisson.")
    Continuer1.bind("<Button-1>", Cf17)

def Cf17(event):
    Dialogue.config(text="Je suis obligé de m'arreter.")
    Continuer1.bind("<Button-1>", Cf18)

def Cf18(event):
    Dialogue.config(text="J'essaie de fuir à pied, mais...")
    Continuer1.bind("<Button-1>", Cf19)

def Cf19(event):
    NomPerso.config(text="Policier", fg="tan")
    Dialogue.config(text="On ne bouge plus !")
    Continuer1.bind("<Button-1>", Cf20)

def Cf20(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Cf21)

def Cf21(event):
    NomPerso.config(text="Policier", fg="tan")
    Dialogue.config(text="On vole des voitures ? \n Tu peut expliquer ?")
    Continuer1.bind("<Button-1>", Cf22)

def Cf22(event):
    NomPerso.config(text=nom, fg="blue")
    Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Cf23)

def Cf23(event):
    NomPerso.config(text="Policier", fg="tan")
    Dialogue.config(text="Je vois. \n Tu as gagné un allez à la case prison.")
    Continuer1.bind("<Button-1>", Cf24)

def Cf24(event):
    NomPerso.config(text=nom, fg="blue")
    if Carte_Monopoly == True:
        Dialogue.config(text="Pas si vite !")
    else:
        Dialogue.config(text="...")
    Continuer1.bind("<Button-1>", Cf25)

def Cf25(event):
    NomPerso.config(text="")
    if Carte_Monopoly == True:
        Dialogue.config(text="Je sort ma Carte Monopoly")
        Continuer1.bind("<Button-1>", Cf26)
    else:
        Dialogue.config(text="Le policier m'empoigne \n et me conduis en prison.")
        Continuer1.bind("<Button-1>", FIN_Prison)

def Cf26(event):
    NomPerso.config(text="Policier", fg="tan")
    Dialogue.config(text="Qu'est ce que ?")
    Continuer1.bind("<Button-1>", Cf27)

def Cf27(event):
    Dialogue.config(text="Désolé, je ne peut pas \n vous arrêter si vous avez ça.")
    Continuer1.bind("<Button-1>", Cf28)

def Cf28(event):
    Dialogue.config(text="Mes excuses, au revoir.")
    Continuer1.bind("<Button-1>", Cf29)

def Cf29(event):
    NomPerso.config(text="")
    Dialogue.config(text="Les policiers s'en vont, \n me laissant libre.")
    Continuer1.bind("<Button-1>", Cf30)

def Cf30(event):
    Dialogue.config(text="Je monte de nouveau dans la voiture, \n et je m'en vais.")
    Continuer1.bind("<Button-1>", FIN_Libre)

#--------------------------
#--------- Autres ---------
#--------------------------


#------------ Portes Chapitre 3 ------------


def Porterandom():
    global portedragon, portebonus
    portedragon = random.randint(1,3)
    if bonusobtenu == False:
        probabonus = random.randint(1,100)
        if probabonus < 25:
            portebonus = random.randint(1,3)
            while portebonus == portedragon:
                portebonus = random.randint(1,3)


#---------- Selection de Chapitre ------------
def ChoixCahpitre(event):
    NomJeu.pack_forget()
    Commencer.pack_forget()
    DescChoixChap.pack(padx=10, pady=10)
    NewGame.pack(padx=10, pady=10)
    Chap1.pack(padx=10, pady=10)
    Chap1.bind("<Button-1>", Chapitre1)
    Chap2.pack(padx=10, pady=10)
    Chap2.bind("<Button-1>", Chapitre2)
    Chap3.pack(padx=10, pady=10)
    Chap3.bind("<Button-1>", Chapitre3)
    NewGame.bind("<Button-1>", Aa1)


def Chapitre1(event):
    Chap1.pack_forget()
    Chap2.pack_forget()
    Chap3.pack_forget()
    NewGame.pack_forget()
    Chap1_1.pack(padx=10, pady=10)
    Chap1_2.pack(padx=10, pady=10)
    Chap1_3.pack(padx=10, pady=10)
    Chap1_4.pack(padx=10, pady=10)
    Chap1_1.bind("<Button-1>", Aa1)
    Chap1_2.bind("<Button-1>", ChapA_2)
    Chap1_3.bind("<Button-1>", Ac1)
    Chap1_4.bind("<Button-1>", ChapA_4)

def Chapitre2(event):
    Chap1.pack_forget()
    Chap2.pack_forget()
    Chap3.pack_forget()
    NewGame.pack_forget()
    Chap2_1.pack(padx=10, pady=10)
    Chap2_2.pack(padx=10, pady=10)
    Chap2_3.pack(padx=10, pady=10)
    Chap2_1.bind("<Button-1>", Ba1)
    Chap2_2.bind("<Button-1>", ChapB_2)
    Chap2_3.bind("<Button-1>", ChapB_3)

def Chapitre3(event):
    Chap1.pack_forget()
    Chap2.pack_forget()
    Chap3.pack_forget()
    NewGame.pack_forget()
    Chap3_1.pack(padx=10, pady=10)
    Chap3_2.pack(padx=10, pady=10)
    Chap3_3.pack(padx=10, pady=10)
    Chap3_4.pack(padx=10, pady=10)
    Chap3_1.bind("<Button-1>", Ca1)
    Chap3_2.bind("<Button-1>", Cb1)
    Chap3_3.bind("<Button-1>", ChapC_3)
    Chap3_4.bind("<Button-1>", ChapC_4)


#------------- Stats ----------------

def ExplicationRegles(event):
    global Epee, Flute, Partitions, Pistolet, Carte_Monopoly, ChambreHaroldOuverte, LockMarais, LockDisney, NbMauvaisesActions_Disney, VolMarchand, VolXP, MenacePassant, ErreurMarais, PassMarais, PassDisney, Augmentation, GARDE_Hostille, GARDE_Sympa, bonusobtenu, DragonTue, DragonCharme, DragonBlaze
    Epee = False
    Flute = False
    Partitions = False
    Pistolet = False
    Carte_Monopoly = False
    ChambreHaroldOuverte = False
    LockMarais = False
    LockDisney = False
    NbMauvaisesActions_Disney = 0
    VolMarchand = False
    VolXP = False
    MenacePassant = False
    ErreurMarais = 0
    PassMarais = False
    PassDisney = False
    Augmentation = False
    GARDE_Sympa = 0
    GARDE_Hostille = 0
    bonusobtenu = False
    DragonTue = False
    DragonCharme = False
    DragonBlaze = False
    print("----------------------------------------------------------------")
    print("Bienvenue sur le projet NSI portant sur l'histoire interactive")
    print("Pour avancer dans le jeu, cliquez sur les boutons '>'")
    print("Vous aurez de temps en temps des choix qui seront important pour la suite")
    print("Choisissez bien car vous pouvez perdre !")
    print()
    print("Vous possédez 4 types de statistiques qui vous permettrons de réussir certains choix")
    print("De temps en temps, vous allez gagner des niveaux")
    print("Tout les niveaux pairs, vous allez pouvoir améliorer vos statistiques")
    print()
    print("Amusez-vous bien !")
    print()
    print("----------------------------------------------------------------")
    print()
    creation_perso(event)

def creation_perso(event):
    global agilite, force, intelligence, charisme, nom, niveau
    nomchoisi = input("Entrez le nom du joueur ")
    if nomchoisi != "":
        nom = nomchoisi
    else:
        num = random.randint(0,len(tabnom)-1)
        nom = tabnom[num]
    niveau = 1
    print()
    print("Pour l'instant, les statistiques sont décidés au hasard")
    agilite = random.randint(1,10)
    force = random.randint(1,10)
    intelligence = random.randint(1,10)
    charisme = random.randint(1,10)
    print()
    print("Votre nom est : ",nom)
    print("Vous etes au niveau ",niveau)
    print("Votre force est de : ", force)
    print("Votre agilité est de : ", agilite)
    print("Votre intelligence est de : ", intelligence)
    print("Votre charisme est de : ", charisme)
    print()
    ChoixCahpitre(event)


def LevelUp(event):
    SE_LevelUp.play()
    global niveau, agilite, force, intelligence, charisme
    PointBienPlace = False
    niveau = niveau + 1
    print()
    print("Vous êtes passé au niveau ", niveau)
    print()
    if niveau%2 == 0 and agilite+force+intelligence+charisme < 40:
        print("Vous pouvez assigner 1 point supplémentaire dans une statistique au choix.")
        print("Vous ne pouvez pas excéder 10 points dans une statistique.")
        print("Votre force est de : ", force)
        print("Votre agilité est de : ", agilite)
        print("Votre intelligence est de : ", intelligence)
        print("Votre charisme est de : ", charisme)
        while PointBienPlace == False:
            print()
            rep = input("Choisissiez une de vos statistiques (F/A/I/C)")
            if rep == "F" or rep == "f":
                if force + 1 < 11:
                    force = force+1
                    PointBienPlace = True
                else:
                    print("Action Impossible, veuillez réessayer")
            elif rep == "A" or rep == "a":
                if agilite + 1 < 11:
                    agilite = agilite+1
                    PointBienPlace = True
                else:
                    print("Action Impossible, veuillez réessayer")
            elif rep == "I" or rep == "i":
                if intelligence + 1 < 11:
                    intelligence = intelligence+1
                    PointBienPlace = True
                else:
                    print("Action Impossible, veuillez réessayer")
            elif rep == "C" or rep == "c":
                if charisme + 1 < 11:
                    charisme = charisme+1
                    PointBienPlace = True
                else:
                    print("Action Impossible, veuillez réessayer")
            else:
                print("Action Impossible, veuillez réessayer")
        print()
        print("Action réussit")
        print()
        print("Votre force est de : ", force)
        print("Votre agilité est de : ", agilite)
        print("Votre intelligence est de : ", intelligence)
        print("Votre charisme est de : ", charisme)
        print()
    else:
        print("Vous ne pouvez pas attribuer de points supplémentaire pour ce niveau")
        print()


#------------ FINS ---------------

def FIN_Generic(event):
    pygame.mixer.music.fadeout(400)
    Decor.pack_forget()
    NomPerso.pack_forget()
    Dialogue.pack_forget()
    Continuer1.pack_forget()
    Continuer2.pack_forget()
    Continuer3.pack_forget()

    FIN_Desc.pack(padx=10, pady=10)
    FIN_Button.pack(padx=10, pady=10)
    FIN_Desc.config(text="FIN")
    FIN_Button.bind("<Button-1>", menu)

def FIN_Fuite(event):
    pygame.mixer.music.fadeout(400)
    Decor.pack_forget()
    NomPerso.pack_forget()
    Dialogue.pack_forget()
    Continuer1.pack_forget()
    Continuer2.pack_forget()
    Continuer3.pack_forget()

    FIN_Desc.pack(padx=10, pady=10)
    FIN_Button.pack(padx=10, pady=10)
    FIN_Desc.config(text="FIN \n \n Vous avez fuit, \n échouant ainsi votre quête. \n Ce Dragon étais vraiment terrible, \n enfin, vous ne l'avez pas vu...")
    FIN_Button.bind("<Button-1>", menu)

def FIN_Harold(event):
    pygame.mixer.music.fadeout(400)
    Decor.pack_forget()
    NomPerso.pack_forget()
    Dialogue.pack_forget()
    Continuer1.pack_forget()
    Continuer2.pack_forget()
    Continuer3.pack_forget()

    FIN_Desc.pack(padx=10, pady=10)
    FIN_Button.pack(padx=10, pady=10)
    FIN_Desc.config(text="FIN \n \n Vous avez réussit votre quête, \n félicitations.")
    FIN_Button.bind("<Button-1>", menu)

def FIN_Prison(event):
    pygame.mixer.music.fadeout(400)
    Decor.pack_forget()
    NomPerso.pack_forget()
    Dialogue.pack_forget()
    Continuer1.pack_forget()
    Continuer2.pack_forget()
    Continuer3.pack_forget()

    FIN_Desc.pack(padx=10, pady=10)
    FIN_Button.pack(padx=10, pady=10)
    FIN_Desc.config(text="FIN \n \n Vous avez fini en prison, \n le crime ne paye pas. \n Harold à retrouvé sa voiture \n 'grace' à vous.")
    FIN_Button.bind("<Button-1>", menu)

def FIN_Libre(event):
    pygame.mixer.music.fadeout(400)
    Decor.pack_forget()
    NomPerso.pack_forget()
    Dialogue.pack_forget()
    Continuer1.pack_forget()
    Continuer2.pack_forget()
    Continuer3.pack_forget()

    FIN_Desc.pack(padx=10, pady=10)
    FIN_Button.pack(padx=10, pady=10)
    FIN_Desc.config(text="FIN \n \n Vous avez réussi à fuir la police, \n vous érrez maintenant \n dans un monde inconnu. \n (Avec votre voiture)")
    FIN_Button.bind("<Button-1>", menu)

def FIN_Dragon_Rien(event):
    pygame.mixer.music.fadeout(400)
    Decor.pack_forget()
    NomPerso.pack_forget()
    Dialogue.pack_forget()
    Continuer1.pack_forget()
    Continuer2.pack_forget()
    Continuer3.pack_forget()

    FIN_Desc.pack(padx=10, pady=10)
    FIN_Button.pack(padx=10, pady=10)
    FIN_Desc.config(text="FIN \n \n Vous êtes mort, \n franchement, \n je ne comprend pas pourquoi \n vous l'avez attaqué à main nu.")
    FIN_Button.bind("<Button-1>", menu)

def FIN_Dragon_Epee(event):
    pygame.mixer.music.fadeout(400)
    Decor.pack_forget()
    NomPerso.pack_forget()
    Dialogue.pack_forget()
    Continuer1.pack_forget()
    Continuer2.pack_forget()
    Continuer3.pack_forget()

    FIN_Desc.pack(padx=10, pady=10)
    FIN_Button.pack(padx=10, pady=10)
    FIN_Desc.config(text="FIN \n \n Vous êtes mort, \n vous devriez vous \n entrainer d'avantage \n à l'épée.")
    FIN_Button.bind("<Button-1>", menu)

def FIN_Dragon_Charisme(event):
    pygame.mixer.music.fadeout(400)
    Decor.pack_forget()
    NomPerso.pack_forget()
    Dialogue.pack_forget()
    Continuer1.pack_forget()
    Continuer2.pack_forget()
    Continuer3.pack_forget()

    FIN_Desc.pack(padx=10, pady=10)
    FIN_Button.pack(padx=10, pady=10)
    FIN_Desc.config(text="FIN \n \n Vous êtes mort, \n il n'a pas cru à votre discours \n apparament, incompréhensible...")
    FIN_Button.bind("<Button-1>", menu)

def FIN_Dragon_Flute(event):
    pygame.mixer.music.fadeout(400)
    Decor.pack_forget()
    NomPerso.pack_forget()
    Dialogue.pack_forget()
    Continuer1.pack_forget()
    Continuer2.pack_forget()
    Continuer3.pack_forget()

    FIN_Desc.pack(padx=10, pady=10)
    FIN_Button.pack(padx=10, pady=10)
    FIN_Desc.config(text="FIN \n \n Vous êtes mort, \n une flûte sans partitions, \n c'est pas très utile...")
    FIN_Button.bind("<Button-1>", menu)

def FIN_GARDE_NINJA(event):
    pygame.mixer.music.fadeout(400)
    Decor.pack_forget()
    NomPerso.pack_forget()
    Dialogue.pack_forget()
    Continuer1.pack_forget()
    Continuer2.pack_forget()
    Continuer3.pack_forget()

    FIN_Desc.pack(padx=10, pady=10)
    FIN_Button.pack(padx=10, pady=10)
    FIN_Desc.config(text="FIN \n \n Franchement, \n ce garde mérite une promotion. \n Tuer avec tant de rapidité...")
    FIN_Button.bind("<Button-1>", menu)

def FIN_GARDE(event):
    pygame.mixer.music.fadeout(400)
    Decor.pack_forget()
    NomPerso.pack_forget()
    Dialogue.pack_forget()
    Continuer1.pack_forget()
    Continuer2.pack_forget()
    Continuer3.pack_forget()

    FIN_Desc.pack(padx=10, pady=10)
    FIN_Button.pack(padx=10, pady=10)
    FIN_Desc.config(text="FIN \n \n Vous êtes mort, \n la prochaine fois, \n évitez de vexer celui qui a une arme.")
    FIN_Button.bind("<Button-1>", menu)

def FIN_Disney(event):
    pygame.mixer.music.fadeout(400)
    Decor.pack_forget()
    NomPerso.pack_forget()
    Dialogue.pack_forget()
    Continuer1.pack_forget()
    Continuer2.pack_forget()
    Continuer3.pack_forget()

    FIN_Desc.pack(padx=10, pady=10)
    FIN_Button.pack(padx=10, pady=10)
    FIN_Desc.config(text="FIN \n \n Attention, l'homme étrange va vous arreter \n si vous faites plus d'une mauvaise action.")
    FIN_Button.bind("<Button-1>", menu)

def FIN_Marais(event):
    pygame.mixer.music.fadeout(400)
    Decor.pack_forget()
    NomPerso.pack_forget()
    Dialogue.pack_forget()
    Continuer1.pack_forget()
    Continuer2.pack_forget()
    Continuer3.pack_forget()

    FIN_Desc.pack(padx=10, pady=10)
    FIN_Button.pack(padx=10, pady=10)
    FIN_Desc.config(text="FIN \n \n Attention, le monstre va vous attraper \n si vous faites plus de trois erreurs. \n Certaines en valent deux.")
    FIN_Button.bind("<Button-1>", menu)

def menu(event):
    pygame.mixer.music.load(BGM_Menu)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    FIN_Desc.pack_forget()
    FIN_Button.pack_forget()
    NomJeu.pack(padx=10, pady=10)
    Commencer.pack(padx=10, pady=10)
    Commencer.bind("<Button-1>", ExplicationRegles)



# Chapitres avec sons :

def ChapA_2(event):
    pygame.mixer.music.fadeout(400)
    Ab1(event)

def ChapA_4(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Maison)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    Ad1(event)

def ChapB_2(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Exterieur)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    Bb1(event)

def ChapB_3(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Exterieur)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    Bc1(event)

def ChapC_3(event):
    pygame.mixer.music.fadeout(400)
    pygame.mixer.music.load(BGM_Chateau)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    Cc1(event)

def ChapC_4(event):
    pygame.mixer.music.fadeout(400)
    Cd1(event)


#----------------------------
#-------- Inventaire --------
#----------------------------

def INVENTAIRE(event):
    feninv = tkinter.Tk()
    feninv.title("Inventaire")

    def NOINVENTAIRE(event):
        feninv.destroy()
        fenetre.bind("<Button-3>", INVENTAIRE)


    #Labels

    inv_nom = tkinter.Label(feninv, text="Nom : " + nom)
    inv_niveau = tkinter.Label(feninv, text="Niveau : " + str(niveau))
    inv_force = tkinter.Label(feninv, text="Force : " + str(force))
    inv_agilite = tkinter.Label(feninv, text="Agilité : " + str(agilite))
    inv_intelligence = tkinter.Label(feninv, text="Intelligence : " + str(intelligence))
    inv_Charisme = tkinter.Label(feninv, text="Charisme : " + str(charisme))
    

    inv_text = "\n Vous avez :"
    if Epee == True:
        inv_text = inv_text + "\n -Une Epée"
    if Pistolet == True:
        inv_text = inv_text + "\n -Un Pistolet"
    if Flute == True:
        inv_text = inv_text + "\n -Une Flute"
    if Partitions == True:
        inv_text = inv_text + "\n -Des Partitions"
    if Carte_Monopoly == True:
        inv_text = inv_text + "\n -Une Carte Monopoly"
    if Carte_Monopoly == False and Partitions == False and Flute == False and Pistolet == False and Epee == False:
        inv_text = inv_text + "\n Rien =)"
    inv_label = tkinter.Label(feninv, text=inv_text)
    
    #Boutons
    inv_stats_bouton = tkinter.Button(feninv, text="Statistiques")
    inv_inv_bouton = tkinter.Button(feninv, text="Inventaire")

    inv_stats_bouton.grid(column=1,row=0)
    inv_inv_bouton.grid(column=3,row=0)


    
    # Statistiques
    def Inv_Stats(event):
        inv_label.grid_forget()
        inv_stats_bouton.unbind("<Button-1>")
        
        inv_nom.grid(column=2,row=1)
        inv_niveau.grid(column=2,row=2)
        inv_force.grid(column=2,row=3)
        inv_agilite.grid(column=2,row=4)
        inv_intelligence.grid(column=2,row=5)
        inv_Charisme.grid(column=2,row=6)
        inv_inv_bouton.bind("<Button-1>", Inv_inv)

    #Inventaire
    
    def Inv_inv(event):
        inv_nom.grid_forget()
        inv_niveau.grid_forget()
        inv_force.grid_forget()
        inv_agilite.grid_forget()
        inv_intelligence.grid_forget()
        inv_Charisme.grid_forget()
        inv_inv_bouton.unbind("<Button-1>")

        inv_label.grid(column=2,row=1)
        inv_stats_bouton.bind("<Button-1>", Inv_Stats)


    inv_inv_bouton.bind("<Button-1>", Inv_inv)
    inv_stats_bouton.bind("<Button-1>", Inv_Stats)   
    feninv.bind("<Button-3>", NOINVENTAIRE)
    fenetre.bind("<Button-3>", NOINVENTAIRE)
    feninv.mainloop()
    

fenetre.bind("<Button-3>", INVENTAIRE)

#----------------------------
#-------- Menu DEBUG --------
#----------------------------


def DEBUGMENU(event):
    fendebug = tkinter.Tk()
    fendebug.title("DEBUG")

    def NODEBUGMENU(event):
        fendebug.destroy()
        fenetre.bind("<Insert>", DEBUGMENU)

    def Debug_ShowStats():
        print()
        print("---------------------------------")
        print("------------ DEBUG --------------")
        print("---------------------------------")
        print("Votre nom est : ",nom)
        print("Vous etes au niveau ",niveau)
        print("Votre force est de : ", force)
        print("Votre agilité est de : ", agilite)
        print("Votre intelligence est de : ", intelligence)
        print("Votre charisme est de : ", charisme)
        print("---------------------------------")
        print()

    def Debug_ShowItems():
        print()
        print("---------------------------------")
        print("------------ DEBUG --------------")
        print("---------------------------------")
        print("Epee : ",Epee)
        print("Flute : ",Flute)
        print("Partitions : ", Partitions)
        print("Pistolet : ", Pistolet)
        print("Carte_Monopoly : ", Carte_Monopoly)
        print("---------------------------------")
        print()

    def Debug_Stats_OP():
        global agilite, force, intelligence, charisme
        agilite = 10
        force = 10
        intelligence = 10
        charisme = 10

    def Debug_Stats_NUL():
        global agilite, force, intelligence, charisme
        agilite = 0
        force = 0
        intelligence = 0
        charisme = 0

    def Debug_GiveItems():
        global Epee, Flute, Partitions, Pistolet, Carte_Monopoly
        Epee = True
        Flute = True
        Partitions = True
        Pistolet = True
        Carte_Monopoly = True

    def Debug_LockMarais():
        global LockMarais, LockDisney, PassMarais, PassDisney
        LockMarais = True
        LockDisney = False
        PassMarais = True
        PassDisney = False

    def Debug_LockDisney():
        global LockMarais, LockDisney, PassMarais, PassDisney
        LockMarais = False
        LockDisney = True
        PassMarais = False
        PassDisney = True


    Debug_Stats = tkinter.Button(fendebug, text="Montrer Stats", command=Debug_ShowStats)
    Debug_Objets = tkinter.Button(fendebug, text="Montrer Objets", command=Debug_ShowItems)
    Debug_OP = tkinter.Button(fendebug, text="Stats OP", command=Debug_Stats_OP)
    Debug_NUL = tkinter.Button(fendebug, text="Stats Nuls", command=Debug_Stats_NUL)
    Debug_GiveItems_Button = tkinter.Button(fendebug, text="Gagner tout les objets", command=Debug_GiveItems)
    Debug_LockMarais_Button = tkinter.Button(fendebug, text="Passer par le marais", command=Debug_LockMarais)
    Debug_LockDisney_Button = tkinter.Button(fendebug, text="Passer par Disneyland", command=Debug_LockDisney)
    Debug_Niveau = tkinter.Button(fendebug, text="Gagner un niveau")
    Debug_Niveau.bind("<Button-1>", LevelUp)

    Debug_Stats.pack(padx=10, pady=10)
    Debug_Objets.pack(padx=10, pady=10)
    Debug_OP.pack(padx=10, pady=10)
    Debug_NUL.pack(padx=10, pady=10)
    Debug_GiveItems_Button.pack(padx=10, pady=10)
    Debug_LockMarais_Button.pack(padx=10, pady=10)
    Debug_LockDisney_Button.pack(padx=10, pady=10)
    Debug_Niveau.pack(padx=10, pady=10)
    fendebug.bind("<Insert>", NODEBUGMENU)
    fenetre.bind("<Insert>", NODEBUGMENU)
    fendebug.mainloop()


fenetre.bind("<Insert>", DEBUGMENU)

#----Menu Principal(doit etre en dernier)------
pygame.mixer.music.load(BGM_Menu)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
NomJeu.pack(padx=10, pady=10)
Commencer.pack(padx=10, pady=10)
Commencer.bind("<Button-1>", ExplicationRegles)


#Lancement du jeu
fenetre.mainloop()




