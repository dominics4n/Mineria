import numpy as np
import csv
import scipy.stats as stats

archivos = 'muestra4s'
archDim3 = 'PCA3_muestra4s'
archDim2 = 'PCA2_muestra4s'

Pareidolia = []

sen12 = []
sen13 = []
sen14 = []
sen23 = []
sen24 = []
sen34 = []

with open("../datos/"+archivos+".csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvfile)
    for row in csvreader:
        sen12.append([float(row[1]), float(row[2])])
        sen13.append([float(row[1]), float(row[3])])
        sen14.append([float(row[1]), float(row[4])])
        sen23.append([float(row[2]), float(row[3])])
        sen24.append([float(row[2]), float(row[4])])
        sen34.append([float(row[3]), float(row[4])])
        Pareidolia.append([float(row[1]), float(row[2]), float(row[3]), float(row[4])])

shapiro12 = stats.shapiro(sen12)
print('Sensor 1 + 2: ' + str(shapiro12))
shapiro13 = stats.shapiro(sen13)
print('Sensor 1 + 3: ' + str(shapiro13))
shapiro14 = stats.shapiro(sen14)
print('Sensor 1 + 4: ' + str(shapiro14))
shapiro23 = stats.shapiro(sen23)
print('Sensor 2 + 3: ' + str(shapiro23))
shapiro24 = stats.shapiro(sen24)
print('Sensor 2 + 4: ' + str(shapiro24))
shapiro34 = stats.shapiro(sen34)
print('Sensor 3 + 4: ' + str(shapiro34))
shapirobase = stats.shapiro(Pareidolia)
print('Datos: ' + str(shapirobase))