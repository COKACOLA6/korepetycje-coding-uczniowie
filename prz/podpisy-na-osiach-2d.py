import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.title('Wykres z podpisanymi osiami')
plt.show()




import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xticks([0, 2, 4, 6, 8, 10], ['zero', 'dwa', 'cztery', 'sześć', 'osiem', 'dziesięć'])
plt.yticks([-1, 0, 1], ['-jeden', 'zero', 'jeden'])
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.show()




'''
ax.set_xticks([0, 5, 10])
ax.set_xticklabels(['Start', 'Środek', 'Koniec'])

ax.set_xlabel('Oś X')
ax.set_ylabel('Oś Y')
ax.set_zlabel('Oś Z')
'''
