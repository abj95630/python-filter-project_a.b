# Importation de bibliothèque
from datetime import datetime


def msg_filter(msg, filtre):
    """
    Rapporte les opérations effectués lors de l'exécution dans le fichier filter.log
    :param filtre: Le filtre qui est utilisé
    :param msg: Le nom du fichier parcouru
    """
    with open('../filter.log', 'a') as log:
        log.write(f"{datetime.now()} - Filtration en {filtre} {msg}\n")