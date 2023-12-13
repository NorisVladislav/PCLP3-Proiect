import pandas as pd
import matplotlib.pyplot as plt

# Citirea datelor din fișierul CSV
nume_fisier = 'data.csv'
date = pd.read_csv(nume_fisier)

# Plotează toate valorile
date.plot()
plt.title('Toate valorile')
plt.show()

# Plotează primele 9 valori
X = 9
date.head(X).plot()
plt.title(f'Primele {X} valori')
plt.show()

# Plotează ultimele 12 valori pentru coloanele Durata și Puls
Y = 12
date[['Durata', 'Puls']].tail(Y).plot()
plt.title(f'Ultimele {Y} valori pentru Durata și Puls')
plt.show()
