# Importation de bibliotheques
import cv2
import os
import log

# Variable pour contenir le chemin au images
image = '../data/img'
# La variable "ficher" va contenir les elements du dossier "img"
fichier = os.listdir(image)


def n_b():
    """
    Fonction qui transforme les images en noir et blanc
    """
    try:
        for photo in fichier:
            chemin = f"{image}/{photo}"
            a_traiter = cv2.imread(chemin)
            gris = cv2.cvtColor(a_traiter, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f'../data/output/{photo}', gris)
            log.msg_filter(photo, "noir et blanc")
    except cv2.error as e:
        print(e)

# Affichage de la fonction du filtre noir et blanc
n_b()
