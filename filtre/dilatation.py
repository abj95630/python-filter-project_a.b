# Importation des bibliotheques
import cv2
import numpy
import os
import log


# Variable pour contenir le chemin au images
image = '../data/img'
# La variable "ficher" va contenir les elements du dossier "img"
element = os.listdir(image)


def en_dilatation():
    """
    Fonction qui transforme les images en dilates dans le repertoire "output"
    """
    try:
        for photo in element:
            chemin = image+"/"+photo
            kernel = numpy.ones((5, 5), numpy.uint8)
            a_traiter = cv2.imread(chemin)
            img_dilatation = cv2.dilate(a_traiter, kernel, iterations=3)
            cv2.imwrite('../data/output/'+photo, img_dilatation)
            log.msg_filter(photo, 'dilate')
    except cv2.error as e:
        print(e)


# Affichage de la fonction du filtre noir et blanc
en_dilatation()
