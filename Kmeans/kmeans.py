import numpy as np
#import matplotlib.pyplot as plt
#from sklearn.datasets import make_blobs

k = 3

clusters = {}

for idx in range(k):
    center = np.random.rand(1,4)
    print(str(center))
    points = []
    cluster = {
        'center' : center,
        'points' : []
    }
    
    clusters[idx] = cluster
    
clusters