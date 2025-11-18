import numpy as np
import csv
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

folder = './Clusters_'
archivos = ['muestra4s']

for tipo in archivos:
    id = []
    DejaVu = []
    Clusters = []
    Componentes = 2

    with open("../datos/"+tipo+".csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile)
        for row in csvreader:
            id.append(row[0])
            datos = [float(row[1]),float(row[2]), float(row[3]), float(row[4])]
            DejaVu.append(datos)

    pca = PCA(n_components=Componentes)
    pca.fit(DejaVu)
    Spca = pca.fit_transform(DejaVu)
    print(tipo+': ')
    print(Spca)
    headers = ["id","sensor1","sensor2","sensor3","sensor4"]
    icacsv = [headers]

    aurora = 0
    for row in Spca:
        datos = [id[aurora],Spca[aurora][0], Spca[aurora][1]]
        icacsv.append(datos)
        aurora = aurora + 1

    with open('../datos/PCA2_'+ tipo +'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(icacsv)
