import cv2
import numpy
import os


def noir_blanc():
    image = '../data/img'
    fichier = os.listdir(image)

    for photo in fichier:
        chemin = f"{image}/{photo}"
        a_traiter = cv2.imread(chemin)
        gris = cv2.cvtColor(a_traiter, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f'../data/output/{photo}', gris)



noir_blanc()
