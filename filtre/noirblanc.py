# Importation de bibliotheques
import cv2
import os
import log


def n_b(image, sortie):
    """
    Fonction qui transforme les images en noir et blanc
    """
# La variable "ficher" va contenir les elements du dossier "img"
    fichier = os.listdir(image)
    try:
        for photo in fichier:
            chemin = image+"/"+photo
            a_traiter = cv2.imread(chemin)
            gris = cv2.cvtColor(a_traiter, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(str(sortie)+'/'+str(photo), gris)
            log.msg_filter(photo, "noir et blanc")
    except cv2.error as e:
        print(e)