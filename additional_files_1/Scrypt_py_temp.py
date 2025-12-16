# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 11:17:44 2025

@author: Enzo
"""


import csv
import matplotlib.pyplot as plt
data = []
with open("Donnees.csv", newline= '') as csvfile :
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        data.append(row)
#print(data)
del(data[0])

#Ici, on importe notre fichier csv dans la liste data à laquelle
#on supprime la première ligne

alt = []
maxalt = 0
minalt = 1000000
for i in range(len(data)):
    alt.append(float(data[i][3]))
    #On importe donc la colonne 3 de la liste data dans la liste altitude
    if alt[i]>maxalt:
        maxalt = alt[i]
    if alt[i]<minalt:
        minalt = alt[i]
    #Puis nous calculons les valeurs minimales et maximales de l'altitude
print("L'altitude maximale mesurée est ", maxalt)
print("L'altitude minimale mesurée est ", minalt)
#print(alt)



tempext = []
maxext = 0
minext = 1000000
for i in range(len(data)):
    tempext.append(float(data[i][6]))
    #Ainsi, nous pouvons choisir de garder la colonne 6 (ici des floats) représentant
    #la température extérieure.
    if tempext[i]>maxext:
        maxext = tempext[i]
    if tempext[i]<minext:
        minext = tempext[i]
    #Puis nous calculons les valeurs minimales et maximales de la température extérieure
print("La température extérieure maximale mesurée est ", maxext)
print("La température extérieure minimale mesurée est ", minext)
#print(tempext)



tempint = []
maxint = 0
minint = 1000000
for i in range(len(data)):
    tempint.append(float(data[i][5]))
    #Nous utilisons ici, la colonne 5 représentant la température intérieure.
    if tempint[i]>maxint:
        maxint = tempint[i]
    if tempint[i]<minint:
        minint = tempint[i]
    #Puis nous calculons les valeurs minimales et maximales de la température intérieure
print("La température intérieure maximale mesurée est ", maxint)
print("La température intérieure minimale mesurée est ", minint)
#print(tempint)



plt.scatter(alt,tempext,s=4, c='b')
plt.xlabel("Altitude")
plt.ylabel('Température extérieure')
plt.title("Température extérieure en fonction de l'altitude")
#plt.grid()
#plt.show()

plt.scatter(alt,tempint,s=4, c='g')
plt.xlabel("Altitude")
plt.ylabel('Température intérieure')
plt.title("Température extérieure et intérieure en fonction de l'altitude")
plt.grid()
plt.show()