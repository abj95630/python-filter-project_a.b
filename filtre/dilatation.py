# Importation des bibliotheques
import cv2
import numpy
import os
import log


def en_dilatation(image, sortie, dil=3):
    """
    Fonction qui transforme les images en dilates dans le repertoire de sortie
    """
    # La variable "ficher" va contenir les elements du dossier "img"
    element = os.listdir(image)
    try:
        for photo in element:
            chemin = f"{image}/{photo}"
            kernel = numpy.ones((dil, dil), numpy.uint8)
            a_traiter = cv2.imread(chemin)
            img_dilatation = cv2.dilate(a_traiter, kernel, iterations=3)
            cv2.imwrite(f"{sortie}/{photo}", img_dilatation)
            log.msg_filter(photo, 'dilate')
    except cv2.error as e:
        print(e)