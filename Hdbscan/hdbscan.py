import numpy as np
import csv
from sklearn.cluster import HDBSCAN
from sklearn.metrics import silhouette_score

minC = 7
minSilhouette = 0.3
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
    DejaVu = []
    Clusters = []

    with open("../datos/"+tipo+".csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile)
        for row in csvreader:
            id.append(row[0])
            datos = [float(row[1]),float(row[2]), float(row[3]), float(row[4])]
            DejaVu.append(datos)

    hdb = HDBSCAN(min_cluster_size=minC,
                            cluster_selection_method='eom',
                            metric='euclidean',
                            algorithm='auto',
                            leaf_size=30)
    #print (kmeans.fit_predict(kys))
    #print (tipo + ' HDBSCAN')
    hdb.fit(DejaVu)
    labels = hdb.labels_
    #print(labels)

    nplabel = np.unique(labels).tolist()

    if len(nplabel) > 1:
        #grupo = kmeans.predict(kys)
        silhouette = silhouette_score(DejaVu, labels)
        if silhouette > minSilhouette:
            print(tipo + ' HDBSCAN: '+ str(silhouette))
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
    DejaVu = []
    Clusters = []

    with open("../datos/"+tipo+".csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile)
        for row in csvreader:
            id.append(row[0])
            datos = [float(row[1]),float(row[2]), float(row[3])]
            DejaVu.append(datos)

    hdb = HDBSCAN(min_cluster_size=minC,
                            cluster_selection_method='eom',
                            metric='euclidean',
                            algorithm='auto',
                            leaf_size=30)
    #print (kmeans.fit_predict(kys))
    #print (tipo + ' HDBSCAN')
    hdb.fit(DejaVu)
    labels = hdb.labels_
    #print(labels)
    nplabel = np.unique(labels).tolist()

    if len(nplabel) > 1:
        #grupo = kmeans.predict(kys)
        silhouette = silhouette_score(DejaVu, labels)
        if silhouette > minSilhouette:
            print(tipo + ' HDBSCAN: '+ str(silhouette))
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
    DejaVu = []
    Clusters = []

    with open("../datos/"+tipo+".csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile)
        for row in csvreader:
            id.append(row[0])
            datos = [float(row[1]),float(row[2])]
            DejaVu.append(datos)

    hdb = HDBSCAN(min_cluster_size=minC,
                            cluster_selection_method='eom',
                            metric='euclidean',
                            algorithm='auto',
                            leaf_size=30)
    #print (kmeans.fit_predict(kys))
    #print (tipo + ' HDBSCAN')
    hdb.fit(DejaVu)
    labels = hdb.labels_
    #print(labels)
    nplabel = np.unique(labels).tolist()

    if len(nplabel) > 1:
        #grupo = kmeans.predict(kys)
        silhouette = silhouette_score(DejaVu, labels)
        if silhouette > minSilhouette:
            print(tipo + ' HDBSCAN: '+ str(silhouette))
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
