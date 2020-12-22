# Importation de bibliothèques
import cv2
import os
import log


# Variable pour contenir le chemin au images
image = 'data/img'
# La variable "ficher" va contenir les éléments du dossier "img"
fichier = os.listdir(image)


# Parcourt les images du dossier "img" pour filtrer en flou les images
# qui seront classés dans le dossier "output"
for photo in fichier:
    try:
        chemin = f'{image}/{photo}'
        traitement = cv2.imread(chemin)
        dst = cv2.GaussianBlur(traitement, (41, 31), cv2.BORDER_DEFAULT)
        cv2.imwrite(f"data/output/{photo}", dst)
        log.msg_filter(photo, 'floue')
    except cv2.error as e:
        print(e)
