#!/usr/bin/env python
'''Bones pràctiques. Càlcul d'una divisió entera
Institut Icària
Programació - 1r Batxillerat - Curs 2023-24
El programa calculará el quocient i el residu d'una divisió entera.
Cal insertar el dividend i el divisor.
El programá finalment mostrará la divisió, el quocient i el residu.
'''
__author__ = "Andoni Baquero"
__email__ = "abaquero@instituticaria.cat"
__date__ = "2024/10/23"
D = int(input("Quin és es el dividend?: "))
d = int(input("Quin és el divisor: "))
resultat = D // d
residu = D-resultat*d
print(f"Divisió: {D}/{d}")
print(f"Quocient: {resultat}")
print(f"Residu: {residu}")
