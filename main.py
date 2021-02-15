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
    filtre_flo = re.findall('\d+', pipe)[0]
    filtre_dil = re.findall('\d+', pipe)[1]
    autres.verif_dossier(sortie)
    autres.verif_fichier(arg[2])
    if arg[2]:
        autres.pipeline(entree, sortie, int(filtre_flo), int(filtre_dil))
    else:
        print("Vous ne tapez pas le bon filtre :(")
else:
    print("Erreur, Vous ne tapez pas la bonne option :(")
