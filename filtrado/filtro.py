import numpy as np
import csv
from scipy.signal import lfilter

archivos = ['boxcox', 'estandarizados', 'normalizados', 'Z-score', 'muestra4s',
            'ICA_boxcox', 'ICA_estandarizados', 'ICA_normalizados', 'ICA_Z-score',
            'ICA_muestra4s']
archDim3 = ['PCA3_boxcox', 'PCA3_estandarizados', 'PCA3_normalizados', 
            'PCA3_Z-score', 'PCA3_muestra4s']
archDim2 = ['PCA2_boxcox', 'PCA2_estandarizados', 'PCA2_normalizados', 
            'PCA2_Z-score', 'PCA2_muestra4s']

n = 15  # the larger n is, the smoother curve will be
a = 1

for tipo in archivos:
    id = []
    sensor1 = []
    sensor2 = []
    sensor3 = []
    sensor4 = []

    with open("../datos/"+tipo+".csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile)
        for row in csvreader:
            id.append(row[0])
            sensor1.append(float(row[1]))
            sensor2.append(float(row[2])) 
            sensor3.append(float(row[3])) 
            sensor4.append(float(row[4]))

    b = [1.0 / n] * n
    f_sen1 = lfilter(b, a, sensor1)
    print(f_sen1[1])
    f_sen2 = lfilter(b, a, sensor2)
    f_sen3 = lfilter(b, a, sensor3)
    f_sen4 = lfilter(b, a, sensor4)

    headers = ["id","sensor1","sensor2","sensor3","sensor4"]
    filtrocsv = [headers]

    aurora = 0
    for row in id:
        datos = [id[aurora], f_sen1[aurora], f_sen2[aurora], f_sen3[aurora], f_sen4[aurora]]
        filtrocsv.append(datos)
        aurora = aurora + 1

    with open('../datos/filtrado_'+tipo+'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(filtrocsv)

for tipo in archDim3:
    id = []
    sensor1 = []
    sensor2 = []
    sensor3 = []

    with open("../datos/"+tipo+".csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile)
        for row in csvreader:
            id.append(row[0])
            sensor1.append(float(row[1]))
            sensor2.append(float(row[2])) 
            sensor3.append(float(row[3])) 

    b = [1.0 / n] * n
    f_sen1 = lfilter(b, a, sensor1)
    print(f_sen1[1])
    f_sen2 = lfilter(b, a, sensor2)
    f_sen3 = lfilter(b, a, sensor3)

    headers = ["id","sensor1","sensor2","sensor3"]
    filtrocsv = [headers]

    aurora = 0
    for row in id:
        datos = [id[aurora], f_sen1[aurora], f_sen2[aurora], f_sen3[aurora]]
        filtrocsv.append(datos)
        aurora = aurora + 1

    with open('../datos/filtrado_'+tipo+'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(filtrocsv)

for tipo in archDim2:
    id = []
    sensor1 = []
    sensor2 = []

    with open("../datos/"+tipo+".csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile)
        for row in csvreader:
            id.append(row[0])
            sensor1.append(float(row[1]))
            sensor2.append(float(row[2])) 

    b = [1.0 / n] * n
    f_sen1 = lfilter(b, a, sensor1)
    f_sen2 = lfilter(b, a, sensor2)

    headers = ["id","sensor1","sensor2"]
    filtrocsv = [headers]

    aurora = 0
    for row in id:
        datos = [id[aurora], f_sen1[aurora], f_sen2[aurora]]
        filtrocsv.append(datos)
        aurora = aurora + 1

    with open('../datos/filtrado_'+tipo+'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(filtrocsv)
