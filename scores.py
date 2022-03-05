import matplotlib.pyplot as plt
import numpy as np
import math as m


names = ['Achats responsables', 'Durée de vie et fin de vie', 'Gouvernance', 'Postes de travail', 'Téléphonie',
         'impressions', 'Outils et usages', 'Logiciels', 'Services numériques', 'Centres informatiques', 'Réseau']
domaines = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

# moyennes bench fictives
moyennes_bench = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
notes_matu = [10, 9, 11, 10.5, 8, 9.5, 11, 10.05, 10, 9, 12]

# choix des niveaux
levels = [m.copysign(1, notes_matu[k]/v-1)*abs(notes_matu[k]/v*100-100) for (k, v) in enumerate(moyennes_bench)]
fig, ax = plt.subplots()
ax.set(title="Maturité")

# annotate lines an create arrow
for d, l, r in zip(domaines, levels, names):
    ax.annotate(f"+{l:.0f}" if l > 0 else f"-{l:.0f}",
                xy=(d, l+2 if l > 0 else l-2),
                xytext=(-3, np.sign(l)*3),
                textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top",
                color="green" if l > 0 else "red")
    ax.annotate(f"{d}.",
                xy=(d, -1 if l > 0 else 1),
                verticalalignment="top" if l > 0 else "bottom",
                color="black")

    # Otherwise an arrow will still be created at y=0.
    if l == 0:
        continue

    ax.arrow(x=int(d)-1, y=0, dx=0, dy=l,
             color="green" if l > 0 else "red",
             width=0.01,
             head_width=0.15,
             head_length=0.5,
             length_includes_head=False,
             overhang=2,
             head_starts_at_zero=False)

# The vertical stems
# ax.vlines(domaines,
#          [level for level in levels],
#          0,
#          color=["green" if level > 0 else "red" for level in levels])

ax.plot(domaines,
        np.zeros_like(domaines),
        "-o",
        color="k",
        markerfacecolor="w")  # Baseline and markers on it.

# remove y,x axis and subplot frame
plt.axis('off')
plt.box(on=None)

plt.show()
