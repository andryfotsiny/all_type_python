import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
data = pd.read_csv('dsanfran.xls', parse_dates=['Date'], index_col='Date')

# Tracer les données
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Pluie_mm'])
plt.title('Précipitations mensuelles à San Francisco')
plt.xlabel('Date')
plt.ylabel('Précipitations (mm)')
plt.grid(True)
plt.show()

