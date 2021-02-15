# Importation de bibliotèque
import os
import cv2
import numpy
import log
import configparser


def verif_dossier(dossier):
    """
    On vérifit si le dossier choisit en sortie, a été déja crée. Sinon,
    on le crée
    :param dossier: le dossier de sortie
    """
    try:
        os.mkdir(dossier)
    except OSError:
        if not os.path.isdir(dossier):
            raise


def verif_fichier(fichier_param):
    """
    On vérifit si un fichier de configuration existe ou non
    :param fichier_param: le fichier

    """
    try:
        if os.path.isfile(fichier_param) and fichier_param.endswith(".ini"):
            return None
        else:
            print("Le fichier n'existe pas ou n'est pas un fichier de configuration")
    except configparser.Error as e:
        print(e)


def aide():
    """
    Permet aider l'utilsateur à bien utiliser l'application

    """
    print("Pour mener à bien les opérations de filtration d'images, voici quelques règles :")
    print("Il faut taper l'option '--filtrer' pour l'application des filtres aux images")
    print("--filtrer -personnalisé pour appliquer une pipeline de filtres")
    print("-i pour le dossier source")
    print("-o pour le dossier de destination où on déposera les images")
    print("--log pour visualiser le journal d'événements")
    print("--config-fichier pour exécuter un fichier de configuration")


def pipeline(entree, sortie, v_floue, v_dilate):
    """

    :param entree: Le dossier source
    :param sortie: Le dossier de destination où seront déposé les images filtrées
    :param v_floue: la force du floue
    :param v_dilate: la force de la dilatation
    """
    fichier = os.listdir(entree)
    for photo in fichier:
        try:
            chemin = entree + "/" + photo
            traitement = cv2.imread(chemin)
            floue = cv2.GaussianBlur(traitement, (v_floue, v_floue), cv2.BORDER_DEFAULT)
            nb = cv2.cvtColor(floue, cv2.COLOR_BGR2GRAY)
            kernel = numpy.ones((v_dilate, v_dilate), numpy.uint8)
            dilate = cv2.dilate(nb, kernel, iterations=3)
            cv2.imwrite(str(sortie) + '/' + str(photo), dilate)
            log.msg_filter(photo, 'pipeline')
        except cv2.error as e:
            print(e)