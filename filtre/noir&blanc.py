# Importation de bibliothèques
import cv2
import os
from filtre import log

# Variable pour contenir le chemin au images
image = '../data/img'
# La variable "ficher" va contenir les éléments du dossier "img"
fichier = os.listdir(image)


def noir_blanc():
    """
    Fonction qui transforme les images en noir et blanc
    """
    for photo in fichier:
        chemin = f"{image}/{photo}"
        a_traiter = cv2.imread(chemin)
        gris = cv2.cvtColor(a_traiter, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f'../data/output/{photo}', gris)
        log.msg_filter(photo, "noir et blanc")


# Affichage de la fonction du filtre noir et blanc
noir_blanc()
