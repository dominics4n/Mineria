# stats.zscore() method  
import numpy as np
from scipy import stats
from sklearn.preprocessing import MinMaxScaler
import csv

sensor1= []
sensor2= []
sensor3= []
sensor4= []

with open("../muestra4s.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvfile)
    for row in csvreader:
        sensor1.append(float(row[1]))
        sensor2.append(float(row[2]))
        sensor3.append(float(row[3]))
        sensor4.append(float(row[4]))

zscore1 = stats.zscore(sensor1)
print(zscore1[1])
zscore2 = stats.zscore(sensor2)
zscore3 = stats.zscore(sensor3)
zscore4 = stats.zscore(sensor4)
i=0

scaler = MinMaxScaler()

# Fit and transform the data
normSens1 = scaler.fit_transform(sensor1)

headers = ["sensor1","sensor2","sensor3","sensor4"]
zscore = [headers]
normal = [headers]
for x in sensor1:
    Dzscore = [zscore1[i] ,zscore2[i] , zscore3[i] , zscore4[i]]
    Dnorm = [normSens1[i] ,normSens2[i] , normSens3[i] , normSens4[i]]
    zscore.append(Dzscore)
    normal.append(Dnorm)
    i=i+1

with open('Z-score.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(zscore)

with open('normalizados.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(normal)
