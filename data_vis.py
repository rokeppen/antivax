import matplotlib.pyplot as plt
import numpy as np
import math


t = np.arange(300, 1501, 300)
plt.plot(t, [473, 1118, 2060, 3423, 5028], 'rs', t, t**2/190, t, t*1.6)
plt.legend(['Algoritme', 'n²', 'n'])
plt.xlabel('Lengte n')
plt.ylabel('Tijd (ms)')
plt.show()


t2 = np.arange(500, 1501, 250)
plt.plot(t2, [1221, 1832, 2493, 3069, 3674], 'rs', t2, t2*2.44)
plt.legend(['Algoritme', 'm'])
plt.xlabel('Lengte m')
plt.ylabel('Tijd (ms)')
plt.show()
