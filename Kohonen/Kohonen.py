import math
import random
DatosEntrenamiento = []
DatosAgrupar = []
n_cluster = 6
Clusters=[[],[],[],[],[],[]]

import csv
with open("../muestra4s.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvfile)
    for row in csvreader:
        datos1 = [float(row[1]), float(row[2]), float(row[3]), float(row[4])]
        datos2 = [row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4])]
        DatosEntrenamiento.append(datos1)
        DatosAgrupar.append(datos2)

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
    # T = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]
    T = DatosEntrenamiento
    m, n = len(T), len(T[0])
    random.seed(1157)
    weights = []
    for x in range(n_cluster):
        datos = [random.random(), random.random(), random.random(), random.random()]
        weights.append(datos)
    print("Initial weights: "+str(weights))
    ob = SOM()
    epochs = 10
    alpha = 0.5

    # Inside the "main" function
    for i in range(epochs):
        for j in range(m):
            sample = T[j]
            J = ob.winner(weights, sample)
            weights = ob.update(weights, sample, J, alpha)
    print("******************************************************")
    # Inside the "Main" function
    mitski = 0
    for fila in DatosEntrenamiento:
        f = ob.winner(weights, fila)
        Clusters[f].append(DatosAgrupar[mitski])
        mitski +=  1
    
    
    for x in range(n_cluster):
        with open('Cluster0'+str(x)+'.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(Clusters[x])

    print("Trained weights: ", weights)

if __name__ == "__main__":
    main()