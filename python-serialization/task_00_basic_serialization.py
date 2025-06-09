#!/usr/bin/env python3
"""
Module de sérialisation de base utilisant JSON
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python vers un fichier JSON
    
    Args:
        data: Dictionnaire Python à sérialiser
        filename: Nom du fichier JSON de sortie
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    """
    Charge et désérialise des données depuis un fichier JSON
    
    Args:
        filename: Nom du fichier JSON d'entrée
        
    Returns:
        dict: Dictionnaire Python désérialisé
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
