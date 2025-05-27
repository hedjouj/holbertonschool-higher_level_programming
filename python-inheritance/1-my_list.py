#!/usr/bin/python3
"""Module contenant une classe MyList qui hérite de list."""


class MyList(list):
    """Classe héritée de list avec une méthode pour imprimer triée."""

    def print_sorted(self):
        """
        Affiche la liste triée en ordre croissant.
        Ne modifie pas la liste originale.
        """
        print(sorted(self))
