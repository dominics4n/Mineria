import numpy as np
import csv
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

no_clusters = 3
folder = './Clusters_'
archivos = ['boxcox', 'estandarizados', 'normalizados', 'Z-score', 'muestra4s']

for tipo in archivos:
    id = []
    kys = []
    Clusters = [[],[],[]]

    with open("../datos/"+tipo+".csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile)
        for row in csvreader:
            id.append(row[0])
            datos = [float(row[1]),float(row[2]), float(row[3]), float(row[4])]
            kys.append(datos)

    kmeans = KMeans(n_clusters=no_clusters, random_state=42).fit(kys)
    print (tipo + ' kmeans')
    print(kmeans.cluster_centers_)

    grupo = kmeans.predict(kys)
    silhouette = silhouette_score(kys, kmeans.fit_predict(kys))
    print(silhouette)
    aurora = 0
    for num in grupo:
        datos = [id[aurora],kys[aurora][0], kys[aurora][1], kys[aurora][2], kys[aurora][3]]
        Clusters[num].append(datos)
        aurora = aurora + 1

    for x in range(no_clusters):
        if Clusters[x]:
            with open(folder+tipo+'/Cluster0'+str(x)+'.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(Clusters[x])
