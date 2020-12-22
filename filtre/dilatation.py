# Importation des bibliothèques
import cv2
import numpy
import os
import log

# Variable pour contenir le chemin au images
image = '../data/img'
# La variable "ficher" va contenir les éléments du dossier "img"
element = os.listdir(image)


def dilatation():
    """
    Fonction qui transforme les images en dilatés dans le répértoire "output"
    """
    for photo in element:
        chemin = f'{image}/{photo}'
        kernel = numpy.ones((5, 5), numpy.uint8)
        a_traiter = cv2.imread(chemin)
        img_dilatation = cv2.dilate(a_traiter, kernel, iterations=3)
        cv2.imwrite(f'../data/output/{photo}', img_dilatation)
        log.msg_filter(photo, 'dilaté')


# Affichage de la fonction du filtre noir et blanc
dilatation()
