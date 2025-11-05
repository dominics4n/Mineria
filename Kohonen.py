import math
DatosEntrenamiento = []
DatosAgrupar = []
Cluster00 = []
Cluster01 = []
Cluster02 = []

import csv
with open("muestra4s.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvfile)
    for row in csvreader:
        datos1 = [float(row[1]), float(row[2]), float(row[3]), float(row[4])]
        datos2 = [row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4])]
        DatosEntrenamiento.append(datos1)
        DatosAgrupar.append(datos2)

class SOM:
    def winner(self, weights, sample):
        D0 = 0
        D1 = 0
        D2 = 0
        
        for i in range(len(sample)):
            D0 += math.pow((sample[i] - weights[0][i]), 2)
            D1 += math.pow((sample[i] - weights[1][i]), 2)
            D2 += math.pow((sample[i] - weights[2][i]), 2)
            mini = min([D0, D1, D2])
            if mini == D0:
                return 0
            if mini == D1:
                return 1
            if mini == D2:
                return 2
        
    def update(self, weights, sample, J, alpha):
        for i in range(len(weights[0])):
            weights[J][i] = weights[J][i] + alpha * (sample[i] - weights[J][i])

        return weights

def main():
    # T = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]
    T = DatosEntrenamiento
    m, n = len(T), len(T[0])
    print("n: "+str(n))
    print("m: "+str(m))
    weights = [[0.2, 0.6, 0.5, 0.9], [0.8, 0.4, 0.7, 0.3], [0.3, 0.7, 0.1, 0.2]]
    ob = SOM()
    epochs = 5
    alpha = 0.5

    # Inside the "main" function
    for i in range(epochs):
        for j in range(m):
            sample = T[j]
            J = ob.winner(weights, sample)
            weights = ob.update(weights, sample, J, alpha)
    
    # Inside the "Main" function
    mitski = 0
    for fila in DatosEntrenamiento:
        f = ob.winner(weights, fila)
        if f == 0:
            Cluster00.append(DatosAgrupar[mitski])
        else:
            if f == 1:
                Cluster01.append(DatosAgrupar[mitski])
            else:
                if f == 2:
                    Cluster02.append(DatosAgrupar[mitski])
        mitski +=  1
    
    with open('Cluster00.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(Cluster00)

    with open('Cluster01.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(Cluster01)

    with open('Cluster02.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(Cluster02)

    print("Test Sample s belongs to Cluster: ", J)
    print("Trained weights: ", weights)

if __name__ == "__main__":
    main()