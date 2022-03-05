import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

legend = []
colours = {'Fabrication': '#52C78A',
           'Utilisation': '#FFDE55',
           'Fin de vie': '#EB5F1F'}
data = [30, 30, 40]
labels = ['Fabrication', 'Utilisation', 'Fin de vie']
for i, prc in enumerate(data):
    legend.append(f"{labels[i]} {prc}%")

wedges, texts = ax.pie(data, colors=[colours[key] for key in labels] , startangle=90)

bbox_props = dict(boxstyle="square,pad=1", fc="w", ec="k", lw=2)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=10, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(legend[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw, fontsize=15)

plt.show()