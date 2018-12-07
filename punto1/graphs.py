import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

files = ["dist_0.txt","dist_1.txt","dist_2.txt","dist_3.txt","dist_4.txt","dist_5.txt","dist_6.txt","dist_7.txt"]

data = np.zeros((8,1000))

for i in range(len(files)):
    f = open(file,"r")
    d = f.read().split(",")
    d.pop(-1)
    for j in range(len(d)):
        data[i,j] = float(d[j])
        
plt.figure(figsize=[16,28])
i = 1
for d in data:
    plt.subplot(4, 2, i)
    plt.hist(d,density=True)
    x = np.linspace(-3, 3, 100)
    plt.plot(x, mlab.normpdf(x, 0, 1))
    plt.title('Distribución de cadena ' + str(i))
    i = i + 1
plt.savefig("Histograms.png")

it = np.linspace(1, 1000, 1000, dtype=np.int16)
Vs = np.zeros(len(it))

for i in range(len(it)):
    m = it[i]
    means = np.zeros(len(data))
    variances = np.zeros(len(data))
    for j in range(len(data)):
        means[j] = np.mean(data[j][:m])
        variances[j] = np.var(data[j][:m])
    overall_mean = np.mean(means)

    B = m/7 * np.sum((means - overall_mean)**2)
    W = 1/8 * np.sum(variances)
    V = (m - 1)/it[i] * W + 9/(8 * m) * B
    
    Vs[i] = V
    
plt.figure(figsize=[16,12])
plt.plot(it,Vs)
plt.xlabel("Número de Iteraciones")
plt.ylabel("Gelman-Rubin")
plt.savefig("Gelman_Rubin.png")