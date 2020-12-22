# Importation des bibliothèques
import cv2
import os
from datetime import *

# Variable pour contenir le chemin au images
image = 'data/img'
# La variable "ficher" va contenir les éléments du dossier "img"
fichier = os.listdir(image)


def msg_filter(msg):
    """
    Rapporte les opérations effectués lors de l'exécution dans le fichier filter.log
    :param msg: Le nom du fichier parcouru
    """
    with open('filter.log', 'a') as log:
        log.write(f"{datetime.now()} - Filtration en floue {msg}\n")


# Parcourt les images du dossier "img" pour filtrer en flou les images
# qui seront classés dans le dossier "output"
for photo in fichier:
    try:
        chemin = f'{image}/{photo}'
        traitement = cv2.imread(chemin)
        dst = cv2.GaussianBlur(traitement, (41, 31), cv2.BORDER_DEFAULT)
        cv2.imwrite(f"data/output/{photo}", dst)
        msg_filter(photo)
    except cv2.error as e:
        print(e)
