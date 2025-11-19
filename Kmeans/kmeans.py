import numpy as np
import csv
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

no_clusters = 2
minSilhouette = 0.5
folder = './Clusters_'
archivos = ['boxcox', 'estandarizados', 'normalizados', 'Z-score', 'muestra4s',
            'ICA_boxcox', 'ICA_estandarizados', 'ICA_normalizados', 'ICA_Z-score',
            'ICA_muestra4s']
archDim3 = ['PCA3_boxcox', 'PCA3_estandarizados', 'PCA3_normalizados', 
            'PCA3_Z-score', 'PCA3_muestra4s']
archDim2 = ['PCA2_boxcox', 'PCA2_estandarizados', 'PCA2_normalizados', 
            'PCA2_Z-score', 'PCA2_muestra4s']

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
    #print (kmeans.fit_predict(kys))
    #print (tipo + ' kmeans')
    #print(kmeans.cluster_centers_)

    grupo = kmeans.predict(kys)
    silhouette = silhouette_score(kys, kmeans.fit_predict(kys))
    if silhouette > minSilhouette:
        print(tipo + ' kmeans: ' + str(silhouette))
    aurora = 0
    # for num in grupo:
    #     datos = [id[aurora],kys[aurora][0], kys[aurora][1], kys[aurora][2], kys[aurora][3]]
    #     Clusters[num].append(datos)
    #     aurora = aurora + 1

    # for x in range(no_clusters):
    #     if Clusters[x]:
    #         with open(folder+tipo+'/Cluster0'+str(x)+'.csv', 'w', newline='') as csvfile:
    #             writer = csv.writer(csvfile)
    #             writer.writerows(Clusters[x])

for tipo in archDim3:
    id = []
    kys = []
    Clusters = [[],[],[]]
    sen1 = []
    sen2 = []
    sen3 = []

    with open("../datos/"+tipo+".csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile)
        for row in csvreader:
            id.append(row[0])
            datos = [float(row[1]),float(row[2]), float(row[3])]
            kys.append(datos)
            sen1.append(float(row[1]))
            sen2.append(float(row[2]))
            sen3.append(float(row[3]))

    kmeans = KMeans(n_clusters=no_clusters, random_state=42).fit(kys)
    #print (kmeans.fit_predict(kys))
    #print (tipo + ' kmeans')
    #print(kmeans.cluster_centers_)

    grupo = kmeans.predict(kys)
    silhouette = silhouette_score(kys, kmeans.fit_predict(kys))
    if silhouette > minSilhouette:
        print(tipo + ' kmeans: ' + str(silhouette))
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(sen1, sen2, sen3, c=grupo)
        plt.show()
    aurora = 0
    # for num in grupo:
    #     datos = [id[aurora],kys[aurora][0], kys[aurora][1], kys[aurora][2], kys[aurora][3]]
    #     Clusters[num].append(datos)
    #     aurora = aurora + 1

    # for x in range(no_clusters):
    #     if Clusters[x]:
    #         with open(folder+tipo+'/Cluster0'+str(x)+'.csv', 'w', newline='') as csvfile:
    #             writer = csv.writer(csvfile)
    #             writer.writerows(Clusters[x])

for tipo in archDim2:
    id = []
    kys = []
    Clusters = [[],[],[]]
    sen1 = []
    sen2 = []

    with open("../datos/"+tipo+".csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile)
        for row in csvreader:
            id.append(row[0])
            datos = [float(row[1]),float(row[2])]
            kys.append(datos)
            sen1.append(float(row[1]))
            sen2.append(float(row[2]))

    kmeans = KMeans(n_clusters=no_clusters, random_state=42).fit(kys)
    #print (kmeans.fit_predict(kys))
    #print (tipo + ' kmeans')
    #print(kmeans.cluster_centers_)

    grupo = kmeans.predict(kys)
    silhouette = silhouette_score(kys, kmeans.fit_predict(kys))
    if silhouette > minSilhouette:
        print(tipo + ' kmeans: ' + str(silhouette))
        plt.scatter(sen1, sen2, c=grupo)
        plt.show()

    aurora = 0
    # for num in grupo:
    #     datos = [id[aurora],kys[aurora][0], kys[aurora][1], kys[aurora][2], kys[aurora][3]]
    #     Clusters[num].append(datos)
    #     aurora = aurora + 1

    # for x in range(no_clusters):
    #     if Clusters[x]:
    #         with open(folder+tipo+'/Cluster0'+str(x)+'.csv', 'w', newline='') as csvfile:
    #             writer = csv.writer(csvfile)
    #             writer.writerows(Clusters[x])
