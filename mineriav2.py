import math
fila = []
import csv
with open("muestra4s.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        datos = [row[1], row[2], row[3], row[4]]
        fila.append(datos)

del fila[0]
kys = 0
for rowv2 in fila:
    fila[kys][0]=float(fila[kys][0])
    fila[kys][1]=float(fila[kys][1])
    fila[kys][2]=float(fila[kys][2])
    fila[kys][3]=float(fila[kys][3])
    kys=kys + 1
print(fila[0])

class SOM:
    def winner(self, weights, sample):
        D0 = 0
        D1 = 0
        D2 = 0

        for i in range(len(sample)):
            D0 += math.pow((sample[i] - weights[0][i]), 2)
            D1 += math.pow((sample[i] - weights[1][i]), 2)
            D2 += math.pow((sample[i] - weights[2][i]), 2)
            
            if D0 < D1:
                if D0 < D2:
                    return 0
                else:
                    return 2
            else:
                if D1 < D2:
                    return 1
                else: 
                    return 2
        return 0 if D0 < D1 else 1
        
    def update(self, weights, sample, J, alpha):
        for i in range(len(weights[0])):
            weights[J][i] = weights[J][i] + alpha * (sample[i] - weights[J][i])

        return weights

def main():
    # T = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]
    T = fila
    m, n = len(T), len(T[0])
    print("n: "+str(n))
    print("m: "+str(m))
    weights = [[0.2, 0.6, 0.5, 0.9], [0.8, 0.4, 0.7, 0.3], [0.3, 0.7, 0.1, 0.2]]
    ob = SOM()
    epochs = 3
    alpha = 0.5

    # Inside the "main" function
    for i in range(epochs):
        for j in range(m):
            sample = T[j]
            J = ob.winner(weights, sample)
            weights = ob.update(weights, sample, J, alpha)
    

    # Inside the "Main" function
    s = [0, 0, 0, 1]
    J = ob.winner(weights, s)

    print("Test Sample s belongs to Cluster: ", J)
    print("Trained weights: ", weights)

if __name__ == "__main__":
    main()