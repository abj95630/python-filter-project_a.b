# Importation de bibiliothèques dont on aura besoin
import sys
import autres
import configparser
import re
from filtre import floue, dilatation, noirblanc

# On récupère la méthode "argv"
arg = sys.argv
# On définit une variable en provenance du module "configparser" pour des fichiers de paramètres
mon_conteneur = configparser.RawConfigParser()
# On lit le fichier passé en argument
mon_conteneur.read("config.ini")

# Ici, on définit les condiitions pour application de filtre
if arg[1] == '--filtrer':
    # On applique une pipeline de filtre à un dossier d'images
    if arg[2] == "-personnalisé":
        if arg[3] == '-i' and arg[5] == '-o':
            autres.verif_dossier(arg[6])
            autres.pipeline(arg[4], arg[6], int(arg[7]), int(arg[8]))
    else:
        # On applique un filtre unique pour un dossier d'images
        arg_filtre = arg[6]
        try:
            if arg[2] == "-i" and arg[4] == "-o":
                autres.verif_dossier(arg[5])
                if arg_filtre == "dilatation":
                    dilatation.en_dilatation(arg[3], arg[5])
                elif arg_filtre == "noir":
                    noirblanc.n_b(arg[3], arg[5])
                elif arg_filtre == "floue":
                    floue.en_floue(arg[3], arg[5])
                else:
                    print("Vous ne tapez pas l'un des filtrations correctes")
        except:
            print("Erreur")
        else:
            print("Vous devez tapez :\n'-i' pour l'élément source\n'-o' pour le dossier de destination ")
# L'option --aide pour aiguiller l'utilisateur sur le fonctionnement de l'application
elif arg[1] == "--aide":
    autres.aide()
# L'option --log pour lire le journal d'évènements
elif arg[1] == "--log":
    fichier = open("filtre.log", "r")
    print(fichier.read())
    fichier.close()
# L'option --config-fichier pour lire le fichier de paramètres
elif arg[1] == "--config-fichier":
    entree = mon_conteneur.get("Paramètres", "entrée")
    sortie = mon_conteneur.get("Paramètres", "sortie")
    pipe = mon_conteneur.get("Filtre", "pipeline")
    if arg[2]:
        autres.verif_dossier(sortie)
        autres.verif_fichier(arg[2])
        nb_filtre = len(pipe.split("|"))
        # On applique 1 filtre(s) a(ux) image(s)
        if nb_filtre == 1:
            mot = re.findall("[a-z ]", pipe)
            char = "".join(mot)
            try:
                if char == "dilatation":
                    val = re.findall("\d+", pipe)[0]
                    dilatation.en_dilatation(entree, sortie, int(val))
                if char == "noir et blanc":
                    noirblanc.n_b(entree, sortie)
                if char == "floue":
                    val = re.findall("\d+", pipe)[0]
                    floue.en_floue(entree, sortie, int(val))
            except:
                print("Vous devez appliquer de la force aux filtres 'dilatation' et 'floue'")
        # On applique 2 filtres a(ux) image(s)
        elif nb_filtre == 2:
            ind = pipe.find("|")
            mot_1 = pipe[0:ind]
            mot_2 = pipe[ind+1:]
            filtre_1 = re.findall("[a-z ]", mot_1)
            filtre_2 = re.findall("[a-z ]", mot_2)
            char_1, char_2 = "".join(filtre_1), "".join(filtre_2)
            try:
                if char_1 == "dilatation" and char_2 == "floue":
                    val_1 = re.findall("\d+", mot_1)[0]
                    val_2 = re.findall("\d+", mot_2)[0]
                    autres.dilate_floue(entree, sortie, int(val_1), int(val_2))
                elif char_1 == "dilatation" and char_2 == "noir et blanc":
                    val = re.findall("\d+", mot_1)[0]
                    autres.dilate_nb(entree, sortie, int(val))
                elif char_1 == "noir et blanc" and char_2 == "dilatation":
                    val = re.findall("\d+", mot_2)[0]
                    autres.dilate_nb(entree, sortie, int(val))
                elif char_1 == "noir et blanc" and char_2 == "floue":
                    val = re.findall("\d+", mot_2)[0]
                    autres.floue_nb(entree, sortie, int(val))
                elif char_1 == "floue" and char_2 == "noir et blanc":
                    val = re.findall("\d+", mot_1)[0]
                    autres.floue_nb(entree, sortie, int(val))
                elif char_1 == "floue" and char_2 == "dilatation":
                    val_1 = re.findall("\d+", mot_1)[0]
                    val_2 = re.findall("\d+", mot_2)[0]
                    autres.dilate_floue(entree, sortie, int(val_2), int(val_1))
            except:
                print("Il faut implémenter les filtres correctement")
        # On applique 2 filtres a(ux) image(s)
        elif nb_filtre == 3:
            ind = pipe.find("|")
            ind_1 = pipe.rfind("|")
            mot_1 = pipe[0:ind]
            mot_2 = pipe[ind+1:ind_1]
            mot_3 = pipe[ind_1+1:]
            filtre_1 = re.findall("[a-z ]", mot_1)
            filtre_2 = re.findall("[a-z ]", mot_2)
            filtre_3 = re.findall("[a-z ]", mot_3)
            char_1, char_2, char_3 = "".join(filtre_1), "".join(filtre_2), "".join(filtre_3)
            try:
                if char_1 == "dilatation" and char_2 == "floue" and char_3 == "noir et blanc":
                    val_1 = re.findall("\d+", mot_1)[0]
                    val_2 = re.findall("\d+", mot_2)[0]
                    autres.pipeline(entree, sortie, int(val_2), int(val_1))
                elif char_1 == "dilatation" and char_2 == "noir et blanc" and char_3 == "floue":
                    val_1 = re.findall( "\d+", mot_1)[0]
                    val_2 = re.findall( "\d+", mot_3)[0]
                    autres.pipeline(entree, sortie, int(val_2), int(val_1))
                elif char_1 == "noir et blanc" and char_2 == "dilatation" and char_3 == "floue":
                    val_1 = re.findall( "\d+", mot_2)[0]
                    val_2 = re.findall( "\d+", mot_3)[0]
                    autres.pipeline(entree, sortie, int(val_2), int(val_1))
                elif char_1 == "noir et blanc" and char_2 == "floue" and char_3 == "dilatation":
                    val_1 = re.findall( "\d+", mot_2)[0]
                    val_2 = re.findall( "\d+", mot_3)[0]
                    autres.pipeline(entree, sortie, int(val_1), int(val_2))
                elif char_1 == "floue" and char_2 == "noir et blanc" and char_3 == "dilatation":
                    val_1 = re.findall("\d+", mot_1)[0]
                    val_2 = re.findall("\d+", mot_3)[0]
                    autres.pipeline(entree, sortie, int(val_1), int(val_2))
                elif char_1 == "floue" and char_2 == "dilatation" and char_3 == "noir et blanc":
                    val_1 = re.findall("\d+", mot_1)[0]
                    val_2 = re.findall("\d+", mot_2)[0]
                    autres.pipeline(entree, sortie, int(val_1), int(val_2))
            except:
                print("Vous ne tapez pas le(s) bon(s) filtre(s) correct(s)")
        else:
            print("Vous avez 3 filres à votre disposition :")
            print("-Dilatation")
            print("-Floue")
            print("-Noir et blanc")
    else:
        print("Vous ne tapez pas la bonne pipeline :(")
else:
    print("Erreur, Vous ne tapez pas la bonne option :(")