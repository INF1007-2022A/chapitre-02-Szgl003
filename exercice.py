#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
 nouveau_mot = " "
 for lettre in mot:

    if ord(lettre) >= 97:
        lettre_du_mot = chr(ord(lettre) - 32)

        nouveau_mot += lettre_du_mot

 return nouveau_mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)

