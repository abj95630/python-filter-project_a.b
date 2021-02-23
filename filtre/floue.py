# Importation de bibliotheques
import cv2
import os
import log


def en_floue(image, sortie, flo=3):
    """
    # Parcoure les images du dossier "img" pour filtrer en flou les images
    # qui seront classés dans le dossier "output"
    """
    # La variable "ficher" va contenir les éléments du dossier "img"
    fichier = os.listdir(image)
    for photo in fichier:
        try:
            chemin = f"{image}/{photo}"
            traitement = cv2.imread(chemin)
            dst = cv2.GaussianBlur(traitement, (flo, flo), cv2.BORDER_DEFAULT)
            cv2.imwrite(f"{sortie}/{photo}", dst)
            log.msg_filter(photo, 'floue')
        except cv2.error as e:
            print(e)