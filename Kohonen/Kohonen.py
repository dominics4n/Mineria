from sklearn.metrics import silhouette_score
import math
import random
import os, shutil
import csv
import matplotlib.pyplot as plt

folder = './Clusters_'
minSilhouette = 0.5
archivos = ['boxcox', 'estandarizados', 'normalizados', 'Z-score', 'muestra4s',
            'ICA_boxcox', 'ICA_estandarizados', 'ICA_normalizados', 'ICA_Z-score',
            'ICA_muestra4s']
archDim3 = ['PCA3_boxcox', 'PCA3_estandarizados', 'PCA3_normalizados', 
            'PCA3_Z-score', 'PCA3_muestra4s']
archDim2 = ['PCA2_boxcox', 'PCA2_estandarizados', 'PCA2_normalizados', 
            'PCA2_Z-score', 'PCA2_muestra4s']
n_cluster = 3       # cambiar para obtener x numero de clusters
semilla = 'LindaLindaLinda'    # cambiar para obtener nuevas pesas aleatorias

class SOM:
    def winner(self, weights, sample):
        D=[]
        for x in range(n_cluster):
            D.append(0)
        for i in range(len(sample)):
            for x in range(n_cluster):
                D[x] += math.pow((sample[i] - weights[x][i]), 2)
            
            mini = min(D)
            for x in range(n_cluster):
                if mini == D[x]:
                    #print(str(x))
                    return x
        
    def update(self, weights, sample, J, alpha):
        for i in range(len(weights[0])):
            weights[J][i] = weights[J][i] + alpha * (sample[i] - weights[J][i])

        return weights

def main():
    for tipo in archivos:

        DatosEntrenamiento = []
        DatosAgrupar = []
        Clusters=[]
        ClusterList = []
        for x in range(n_cluster):
            Clusters.append([])

        with open("../datos/"+tipo+".csv", 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvfile)
            for row in csvreader:
                datos1 = [float(row[1]), float(row[2]), float(row[3]), float(row[4])]
                datos2 = [row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4])]
                DatosEntrenamiento.append(datos1)
                DatosAgrupar.append(datos2)

        # for filename in os.listdir(folder+tipo):
        #     file_path = os.path.join(folder+tipo, filename)
        #     try:
        #         if os.path.isfile(file_path) or os.path.islink(file_path):
        #             os.unlink(file_path)
        #         elif os.path.isdir(file_path):
        #             shutil.rmtree(file_path)
        #     except Exception as e:
        #         print('Failed to delete %s. Reason: %s' % (file_path, e))

        # T = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]
        T = DatosEntrenamiento
        m, n = len(T), len(T[0])
        random.seed(semilla)
        weights = []
        for x in range(n_cluster):
            datos = [random.random(), random.random(), random.random(), random.random()]
            weights.append(datos)
        #print("Initial weights: "+str(weights))
        ob = SOM()
        epochs = 17
        alpha = 0.5

        # Inside the "main" function
        for i in range(epochs):
            for j in range(m):
                sample = T[j]
                J = ob.winner(weights, sample)
                weights = ob.update(weights, sample, J, alpha)
        #print("******************************************************")
        mitski = 0
        for fila in DatosEntrenamiento:
            f = ob.winner(weights, fila)
            ClusterList.append(f)
            Clusters[f].append(DatosAgrupar[mitski])
            mitski +=  1
        
        #print (tipo + ' Kohonen:')
        silhouette = silhouette_score(DatosEntrenamiento, ClusterList)
        if silhouette > minSilhouette:
            print(tipo + ' Kohonen: ' + str(silhouette))
            
        # for x in range(n_cluster):
        #     if Clusters[x]:
        #         with open(folder+tipo+'/Cluster0'+str(x)+'.csv', 'w', newline='') as csvfile:
        #             writer = csv.writer(csvfile)
        #             writer.writerows(Clusters[x])

        #print("Trained weights: ", weights)
    for tipo in archDim3:
        DatosEntrenamiento = []
        DatosAgrupar = []
        sen1 = []
        sen2 = []
        sen3 = []
        Clusters=[]
        ClusterList = []
        for x in range(n_cluster):
            Clusters.append([])

        with open("../datos/"+tipo+".csv", 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvfile)
            for row in csvreader:
                datos1 = [float(row[1]), float(row[2]), float(row[3])]
                datos2 = [row[0], float(row[1]), float(row[2]), float(row[3])]
                DatosEntrenamiento.append(datos1)
                DatosAgrupar.append(datos2)
                sen1.append(float(row[1]))
                sen2.append(float(row[2]))
                sen3.append(float(row[3]))

        # for filename in os.listdir(folder+tipo):
        #     file_path = os.path.join(folder+tipo, filename)
        #     try:
        #         if os.path.isfile(file_path) or os.path.islink(file_path):
        #             os.unlink(file_path)
        #         elif os.path.isdir(file_path):
        #             shutil.rmtree(file_path)
        #     except Exception as e:
        #         print('Failed to delete %s. Reason: %s' % (file_path, e))

        # T = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]
        T = DatosEntrenamiento
        m, n = len(T), len(T[0])
        random.seed(semilla)
        weights = []
        for x in range(n_cluster):
            datos = [random.random(), random.random(), random.random()]
            weights.append(datos)
        #print("Initial weights: "+str(weights))
        ob = SOM()
        epochs = 17
        alpha = 0.5

        # Inside the "main" function
        for i in range(epochs):
            for j in range(m):
                sample = T[j]
                J = ob.winner(weights, sample)
                weights = ob.update(weights, sample, J, alpha)
        #print("******************************************************")
        mitski = 0
        for fila in DatosEntrenamiento:
            f = ob.winner(weights, fila)
            ClusterList.append(f)
            Clusters[f].append(DatosAgrupar[mitski])
            mitski +=  1
        
        #print (tipo + ' Kohonen:')
        silhouette = silhouette_score(DatosEntrenamiento, ClusterList)
        if silhouette > minSilhouette:
            print(tipo + ' Kohonen: ' + str(silhouette))
            fig = plt.figure()
            ax = fig.add_subplot(projection='3d')
            ax.scatter(sen1, sen2, sen3, c=ClusterList)
            plt.show()

        # for x in range(n_cluster):
        #     if Clusters[x]:
        #         with open(folder+tipo+'/Cluster0'+str(x)+'.csv', 'w', newline='') as csvfile:
        #             writer = csv.writer(csvfile)
        #             writer.writerows(Clusters[x])

        #print("Trained weights: ", weights)
    
    for tipo in archDim2:
        DatosEntrenamiento = []
        DatosAgrupar = []
        Clusters=[]
        ClusterList = []
        sen1 = []
        sen2 = []
        
        for x in range(n_cluster):
            Clusters.append([])

        with open("../datos/"+tipo+".csv", 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvfile)
            for row in csvreader:
                datos1 = [float(row[1]), float(row[2])]
                datos2 = [row[0], float(row[1]), float(row[2])]
                DatosEntrenamiento.append(datos1)
                DatosAgrupar.append(datos2)
                sen1.append(float(row[1]))
                sen2.append(float(row[2]))

        # for filename in os.listdir(folder+tipo):
        #     file_path = os.path.join(folder+tipo, filename)
        #     try:
        #         if os.path.isfile(file_path) or os.path.islink(file_path):
        #             os.unlink(file_path)
        #         elif os.path.isdir(file_path):
        #             shutil.rmtree(file_path)
        #     except Exception as e:
        #         print('Failed to delete %s. Reason: %s' % (file_path, e))

        # T = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]
        T = DatosEntrenamiento
        m, n = len(T), len(T[0])
        random.seed(semilla)
        weights = []
        for x in range(n_cluster):
            datos = [random.random(), random.random()]
            weights.append(datos)
        #print("Initial weights: "+str(weights))
        ob = SOM()
        epochs = 17
        alpha = 0.5

        # Inside the "main" function
        for i in range(epochs):
            for j in range(m):
                sample = T[j]
                J = ob.winner(weights, sample)
                weights = ob.update(weights, sample, J, alpha)
        #print("******************************************************")
        mitski = 0
        for fila in DatosEntrenamiento:
            f = ob.winner(weights, fila)
            ClusterList.append(f)
            Clusters[f].append(DatosAgrupar[mitski])
            mitski +=  1
        
        #print (tipo + ' Kohonen:')
        silhouette = silhouette_score(DatosEntrenamiento, ClusterList)
        if silhouette > minSilhouette:
            print(tipo + ' Kohonen: ' + str(silhouette))
            plt.scatter(sen1, sen2, c=ClusterList)
            plt.show()

        # for x in range(n_cluster):
        #     if Clusters[x]:
        #         with open(folder+tipo+'/Cluster0'+str(x)+'.csv', 'w', newline='') as csvfile:
        #             writer = csv.writer(csvfile)
        #             writer.writerows(Clusters[x])

        #print("Trained weights: ", weights)

if __name__ == "__main__":
    main()