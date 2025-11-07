from scipy import stats
import pandas as pd
import csv

sensor1= []
sensor2= []
sensor3= []
sensor4= []

with open("../muestra4s.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvfile)
    for row in csvreader:
        sensor1.append(float(row[1]))
        sensor2.append(float(row[2]))
        sensor3.append(float(row[3]))
        sensor4.append(float(row[4]))

transformed_data1, lambda_opt1 = stats.boxcox(sensor1)
transformed_data2, lambda_opt2 = stats.boxcox(sensor2)
transformed_data3, lambda_opt3 = stats.boxcox(sensor3)
transformed_data4, lambda_opt4 = stats.boxcox(sensor4)

df = pd.DataFrame({
    'sensor1': sensor1,
    'sensor2': sensor2,
    'sensor3': sensor3,
    'sensor4': sensor4
})

zscore1 = stats.zscore(sensor1)
zscore2 = stats.zscore(sensor2)
zscore3 = stats.zscore(sensor3)
zscore4 = stats.zscore(sensor4)

sen1min = min(sensor1)
sen2min = min(sensor2)
sen3min = min(sensor3)
sen4min = min(sensor4)
sen1max = max(sensor1)
sen2max = max(sensor2)
sen3max = max(sensor3)
sen4max = max(sensor4)
sen1pro = df['sensor1'].mean()
sen2pro = df['sensor2'].mean()
sen3pro = df['sensor3'].mean()
sen4pro = df['sensor4'].mean()
sen1des = df['sensor1'].std()
sen2des = df['sensor2'].std()
sen3des = df['sensor3'].std()
sen4des = df['sensor4'].std()


df['sensor1'] = (df['sensor1'] - sen1pro) / sen1des
df['sensor2'] = (df['sensor2'] - sen2pro) / sen2des
df['sensor3'] = (df['sensor3'] - sen3pro) / sen3des
df['sensor4'] = (df['sensor4'] - sen4pro) / sen4des

headers = ["sensor1","sensor2","sensor3","sensor4"]
zscore = [headers]
normal = [headers]
Boxcox = [headers]
i=0
for x in sensor1:
    Dzscore = [zscore1[i] ,zscore2[i] , zscore3[i] , zscore4[i]]
    norms1 = (sensor1[i] - sen1min) / (sen1max - sen1min)
    norms2 = (sensor2[i] - sen2min) / (sen2max - sen2min)
    norms3 = (sensor3[i] - sen3min) / (sen3max - sen3min)
    norms4 = (sensor4[i] - sen4min) / (sen4max - sen4min)

    Dnorm = [norms1 , norms2, norms3, norms4]
    DBCx = [transformed_data1[i],transformed_data2[i],transformed_data3[i],transformed_data4[i],]
    zscore.append(Dzscore)
    normal.append(Dnorm)
    Boxcox.append(DBCx)
    i=i+1

with open('Z-score.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(zscore)

with open('normalizados.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(normal)

df.to_csv('estandarizados.csv', index=False)

print(f"Optimal lambda sensor 1: {lambda_opt1}")
print(f"Optimal lambda sensor 2: {lambda_opt2}")
print(f"Optimal lambda sensor 3: {lambda_opt3}")
print(f"Optimal lambda sensor 4: {lambda_opt4}")

with open('boxcox.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Boxcox)
