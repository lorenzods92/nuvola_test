import numpy as np
import matplotlib.pyplot as plt
import random

def crea_punti():
    num_righe = 5
    num_colonne = 5
    random.seed(11)
    
    y_min, y_max = 0, 100
    lun_righe_min, lun_righe_max  = 20, 30
    x_0_min, x_0_max = 0, 0
    z_min, z_max = 20, 20
    
    
    #y_righe = [random.randint(y_min, y_max) for _ in range(num_righe)]
    y_righe = random.sample(range(y_min, y_max), num_righe)
    y_righe = [0, 10, 20, 30, 40]
    y_righe.sort()
    
    lun_righe = [random.randint(lun_righe_min, lun_righe_max) for _ in range(num_righe)]
    lun_righe = [20 for _ in range(num_righe)]
    
    x_0 =  [random.randint(x_0_min, x_0_max) for _ in range(num_righe)]
    
    print("y_righe: ", y_righe)
    print("len_righe: ", lun_righe)
    print("x_0: ", x_0)
    
    X =[]
    
    for i, x_inizio in enumerate(x_0):
        X.append([x for x in np.linspace(x_inizio, x_inizio + lun_righe[i], num_righe, endpoint = True)])
    
    
    print("X", X)
    
    Points = []
    
    for i, y in enumerate(y_righe):
        for x in X[i]:
            z = random.randint(z_min, z_max)
            Points.append([x, y, z])
            
    
    print("points")
    for point in Points:
        print(point)
            
        
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    for point in Points:
        x = point[0]
        y = point[1]
        z = point[2]
        ax.scatter(x, y, z, marker='o')
        
        
    plt.show()
    
    points = np.array([np.array(p) for p in Points])
    
    Base = []
    for point in Points:
        Base.append([point[0], point[1], 0])
        
    base = np.array([np.array(p) for p in Base])
    
    all_points = np.concatenate((points, base), axis=0)
    
    return all_points