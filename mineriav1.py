fila = []
import csv
with open("muestra4s.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        fila.append(row)
print(fila)