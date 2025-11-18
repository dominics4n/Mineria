import numpy as np
import csv
import scipy.stats as stats

archivos = 'muestra4s'
archDim3 = 'PCA3_muestra4s'
archDim2 = 'PCA2_muestra4s'

id = []
sensor1 = []
sensor2 = []
sensor3 = []
sensor4 = []

with open("../datos/"+archivos+".csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvfile)
    for row in csvreader:
        sensor1.append(float(row[1]))
        sensor2.append(float(row[2])) 
        sensor3.append(float(row[3])) 
        sensor4.append(float(row[4]))

wilc12 = stats.wilcoxon(sensor1, sensor2)
print('Sensor 1 + 2: ' + str(wilc12))
wilc13 = stats.wilcoxon(sensor1, sensor3)
print('Sensor 1 + 3: ' + str(wilc13))
wilc14 = stats.wilcoxon(sensor1, sensor4)
print('Sensor 1 + 4: ' + str(wilc14))
wilc23 = stats.wilcoxon(sensor2, sensor3)
print('Sensor 2 + 3: ' + str(wilc23))
wilc24 = stats.wilcoxon(sensor2, sensor4)
print('Sensor 2 + 4: ' + str(wilc24))
wilc34 = stats.wilcoxon(sensor3, sensor4)
print('Sensor 3 + 4: ' + str(wilc34))
