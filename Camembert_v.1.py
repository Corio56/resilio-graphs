import matplotlib.pyplot as plt
import numpy as np

# make data
legend = []
data = [10, 10, 80]
labels = ['Fabrication', 'Utilisation', 'Fin de vie']
colours = {'Fabrication': '#52C78A',
           'Utilisation': '#FFDE55',
           'Fin de vie': '#EB5F1F'}

# plot
fig, (ax1, ax2) = plt.subplots(2)
ax1.pie(data, colors=[colours[key] for key in labels], radius=2, center=(4, 4), startangle=90)
for i, prc in enumerate(data):
    legend.append(f"{labels[i]} {prc}%")
    #print(legend)

ax2.axis([0, 10, 0, 10])
ax2.text(1.5, 4, legend[0], fontsize=15, bbox={'facecolor': '#52C78A', 'alpha': 1, 'pad': 7.5})
ax2.text(4.5, 4, legend[1], fontsize=15, bbox={'facecolor': '#FFDE55', 'alpha': 1, 'pad': 7.5})
ax2.text(7.5, 4, legend[2], fontsize=15, bbox={'facecolor': '#EB5F1F', 'alpha': 1, 'pad': 7.5})
plt.axis('off')
plt.show()
