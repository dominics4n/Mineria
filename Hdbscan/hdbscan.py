import numpy as np
import csv
from sklearn.cluster import HDBSCAN
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

minC = 2
minSilhouette = 0.5
eps = 0.09
folder = './Clusters_'
archivos = ['boxcox', 'estandarizados', 'normalizados', 'Z-score', 'muestra4s',
            'ICA_boxcox', 'ICA_estandarizados', 'ICA_normalizados', 'ICA_Z-score',
            'ICA_muestra4s', 'filtrado_boxcox', 'filtrado_estandarizados', 
            'filtrado_normalizados', 'filtrado_Z-score', 'filtrado_muestra4s',
            'filtrado_ICA_boxcox', 'filtrado_ICA_estandarizados', 
            'filtrado_ICA_normalizados', 'filtrado_ICA_Z-score',
            'filtrado_ICA_muestra4s']
archDim3 = ['PCA3_boxcox', 'PCA3_estandarizados', 'PCA3_normalizados', 
            'PCA3_Z-score', 'PCA3_muestra4s', 'filtrado_PCA3_boxcox', 
            'filtrado_PCA3_estandarizados', 'filtrado_PCA3_normalizados', 
            'filtrado_PCA3_Z-score', 'filtrado_PCA3_muestra4s']
archDim2 = ['PCA2_boxcox', 'PCA2_estandarizados', 'PCA2_normalizados', 
            'PCA2_Z-score', 'PCA2_muestra4s', 'filtrado_PCA2_boxcox', 
            'filtrado_PCA2_estandarizados', 'filtrado_PCA2_normalizados', 
            'filtrado_PCA2_Z-score', 'filtrado_PCA2_muestra4s']

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
                            cluster_selection_epsilon=eps,
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
            #print(nplabel)
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
    sen1 = []
    sen2 = []
    sen3 = []

    with open("../datos/"+tipo+".csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile)
        for row in csvreader:
            id.append(row[0])
            datos = [float(row[1]),float(row[2]), float(row[3])]
            DejaVu.append(datos)
            sen1.append(float(row[1]))
            sen2.append(float(row[2]))
            sen3.append(float(row[3]))

    hdb = HDBSCAN(min_cluster_size=minC,
                            cluster_selection_epsilon=eps,
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
            #print(nplabel)
            # fig = plt.figure()
            # ax = fig.add_subplot(projection='3d')
            # ax.scatter(sen1, sen2, sen3, c=labels)
            # plt.show()

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
    sen1 = []
    sen2 = []

    with open("../datos/"+tipo+".csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile)
        for row in csvreader:
            id.append(row[0])
            datos = [float(row[1]),float(row[2])]
            DejaVu.append(datos)
            sen1.append(float(row[1]))
            sen2.append(float(row[2]))

    hdb = HDBSCAN(min_cluster_size=minC,
                            cluster_selection_epsilon=eps,
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
            #print(nplabel)
            # plt.scatter(sen1, sen2, c=labels)
            # plt.show()

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
