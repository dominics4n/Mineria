from scipy import stats
import pandas as pd
import csv
archivo = 'muestra4s'
arch3D = 'PCA3_muestra4s'
arch2D = 'PCA2_muestra4s'

id = []
sensor1= []
sensor2= []
sensor3= []
sensor4= []

d3sensor1= []
d3sensor2= []
d3sensor3= []

d2sensor1= []
d2sensor2= []

with open("../datos/" + archivo + ".csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvfile)
    for row in csvreader:
        id.append(row[0])
        sensor1.append(float(row[1]))
        sensor2.append(float(row[2]))
        sensor3.append(float(row[3]))
        sensor4.append(float(row[4]))

with open("../datos/" + arch3D + ".csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvfile)
    for row in csvreader:
        d3sensor1.append(float(row[1]) + 0.35)
        d3sensor2.append(float(row[2]) + 0.34)
        d3sensor3.append(float(row[3]) + 0.37)

print(min(d3sensor1))
print(min(d3sensor2))
print(min(d3sensor3))

with open("../datos/" + arch2D + ".csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvfile)
    for row in csvreader:
        d2sensor1.append(float(row[1]) + 0.35)
        d2sensor2.append(float(row[2]) + 0.34)


print(min(d2sensor1))
print(min(d2sensor2))

transformed_data1, lambda_opt1 = stats.boxcox(sensor1)
transformed_data2, lambda_opt2 = stats.boxcox(sensor2)
transformed_data3, lambda_opt3 = stats.boxcox(sensor3)
transformed_data4, lambda_opt4 = stats.boxcox(sensor4)

d3transformed_data1, d3lambda_opt1 = stats.boxcox(d3sensor1)
d3transformed_data2, d3lambda_opt2 = stats.boxcox(d3sensor2)
d3transformed_data3, d3lambda_opt3 = stats.boxcox(d3sensor3)

d2transformed_data1, d2lambda_opt1 = stats.boxcox(d2sensor1)
d2transformed_data2, d2lambda_opt2 = stats.boxcox(d2sensor2)

df = pd.DataFrame({
    'id': id,
    'sensor1': sensor1,
    'sensor2': sensor2,
    'sensor3': sensor3,
    'sensor4': sensor4
})

d3df = pd.DataFrame({
    'id': id,
    'sensor1': d3sensor1,
    'sensor2': d3sensor2,
    'sensor3': d3sensor3
})

d2df = pd.DataFrame({
    'id': id,
    'sensor1': d2sensor1,
    'sensor2': d2sensor2
})


zscore1 = stats.zscore(sensor1)
zscore2 = stats.zscore(sensor2)
zscore3 = stats.zscore(sensor3)
zscore4 = stats.zscore(sensor4)

d3zscore1 = stats.zscore(d3sensor1)
d3zscore2 = stats.zscore(d3sensor2)
d3zscore3 = stats.zscore(d3sensor3)

d2zscore1 = stats.zscore(d2sensor1)
d2zscore2 = stats.zscore(d2sensor2)

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
print('desviacion sensor 1 ' + str(sen1des))
print('desviacion sensor 2 ' + str(sen2des))
print('desviacion sensor 3 ' + str(sen3des))
print('desviacion sensor 4 ' + str(sen4des))
print('promedio sensor 1 ' + str(sen1pro))
print('promedio sensor 2 ' + str(sen2pro))
print('promedio sensor 3 ' + str(sen3pro))
print('promedio sensor 4 ' + str(sen4pro))

d3sen1min = min(d3sensor1)
d3sen2min = min(d3sensor2)
d3sen3min = min(d3sensor3)
d3sen1max = max(d3sensor1)
d3sen2max = max(d3sensor2)
d3sen3max = max(d3sensor3)
d3sen1pro = d3df['sensor1'].mean()
d3sen2pro = d3df['sensor2'].mean()
d3sen3pro = d3df['sensor3'].mean()
d3sen1des = d3df['sensor1'].std()
d3sen2des = d3df['sensor2'].std()
d3sen3des = d3df['sensor3'].std()

d2sen1min = min(d2sensor1)
d2sen2min = min(d2sensor2)
d2sen1max = max(d2sensor1)
d2sen2max = max(d2sensor2)
d2sen1pro = d2df['sensor1'].mean()
d2sen2pro = d2df['sensor2'].mean()
d2sen1des = d2df['sensor1'].std()
d2sen2des = d2df['sensor2'].std()


df['sensor1'] = (df['sensor1'] - sen1pro) / sen1des
df['sensor2'] = (df['sensor2'] - sen2pro) / sen2des
df['sensor3'] = (df['sensor3'] - sen3pro) / sen3des
df['sensor4'] = (df['sensor4'] - sen4pro) / sen4des

d3df['sensor1'] = (d3df['sensor1'] - d3sen1pro) / d3sen1des
d3df['sensor2'] = (d3df['sensor2'] - d3sen2pro) / d3sen2des
d3df['sensor3'] = (d3df['sensor3'] - d3sen3pro) / d3sen3des

d2df['sensor1'] = (d2df['sensor1'] - d2sen1pro) / d2sen1des
d2df['sensor2'] = (d2df['sensor2'] - d2sen2pro) / d2sen2des

headers = ["id","sensor1","sensor2","sensor3","sensor4"]
d3headers = ["id","sensor1","sensor2","sensor3"]
d2headers = ["id","sensor1","sensor2"]
zscore = [headers]
normal = [headers]
Boxcox = [headers]
d3zscore = [d3headers]
d3normal = [d3headers]
d3Boxcox = [d3headers]
d2zscore = [d2headers]
d2normal = [d2headers]
d2Boxcox = [d2headers]
i=0
for x in sensor1:
    Dzscore = [id[i], zscore1[i] ,zscore2[i] , zscore3[i] , zscore4[i]]
    d3Dzscore = [id[i], d3zscore1[i] ,d3zscore2[i] , d3zscore3[i]]
    d2Dzscore = [id[i], d2zscore1[i] ,d2zscore2[i]]
    norms1 = (sensor1[i] - sen1min) / (sen1max - sen1min)
    norms2 = (sensor2[i] - sen2min) / (sen2max - sen2min)
    norms3 = (sensor3[i] - sen3min) / (sen3max - sen3min)
    norms4 = (sensor4[i] - sen4min) / (sen4max - sen4min)
    d3norms1 = (d3sensor1[i] - d3sen1min) / (d3sen1max - d3sen1min)
    d3norms2 = (d3sensor2[i] - d3sen2min) / (d3sen2max - d3sen2min)
    d3norms3 = (d3sensor3[i] - d3sen3min) / (d3sen3max - d3sen3min)
    d2norms1 = (d2sensor1[i] - d2sen1min) / (d2sen1max - d2sen1min)
    d2norms2 = (d2sensor2[i] - d2sen2min) / (d2sen2max - d2sen2min)

    Dnorm = [id[i], norms1 , norms2, norms3, norms4]
    DBCx = [id[i], transformed_data1[i],transformed_data2[i],transformed_data3[i],transformed_data4[i],]
    zscore.append(Dzscore)
    normal.append(Dnorm)
    Boxcox.append(DBCx)

    d3Dnorm = [id[i], d3norms1 , d3norms2, d3norms3]
    d3DBCx = [id[i], d3transformed_data1[i],d3transformed_data2[i],d3transformed_data3[i]]
    d3zscore.append(d3Dzscore)
    d3normal.append(d3Dnorm)
    d3Boxcox.append(d3DBCx)

    d2Dnorm = [id[i], d2norms1 , d2norms2]
    d2DBCx = [id[i], d2transformed_data1[i],d2transformed_data2[i]]
    d2zscore.append(d2Dzscore)
    d2normal.append(d2Dnorm)
    d2Boxcox.append(d2DBCx)

    i=i+1

with open('../datos/Z-score.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(zscore)
with open('../datos/PCA3_Z-score.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(d3zscore)
with open('../datos/PCA2_Z-score.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(d2zscore)

with open('../datos/normalizados.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(normal)
with open('../datos/PCA3_normalizados.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(d3normal)
with open('../datos/PCA2_normalizados.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(d2normal)

df.to_csv('../datos/estandarizados.csv', index=False)
d3df.to_csv('../datos/PCA3_estandarizados.csv', index=False)
d2df.to_csv('../datos/PCA2_estandarizados.csv', index=False)

# print(f"Optimal lambda sensor 1: {lambda_opt1}")
# print(f"Optimal lambda sensor 2: {lambda_opt2}")
# print(f"Optimal lambda sensor 3: {lambda_opt3}")
# print(f"Optimal lambda sensor 4: {lambda_opt4}")

with open('../datos/boxcox.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Boxcox)
with open('../datos/PCA3_boxcox.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(d3Boxcox)
with open('../datos/PCA2_boxcox.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(d2Boxcox)

