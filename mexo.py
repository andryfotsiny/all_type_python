import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Charger les données
df = pd.read_excel('sanfran.xls')

# Préparation des données
df['Date'] = pd.to_datetime(df[['annee', 'mois']].assign(day=1))
df = df.set_index('Date')
df = df.resample('M').sum()  # Résumer les précipitations mensuelles

# 1. Tester la stationnarité
result = adfuller(df['pluie(mm)'])
print(f"ADF Statistic: {result[0]}")
print(f"p-value: {result[1]}")

# Si la série n'est pas stationnaire, appliquer une différenciation
if result[1] > 0.05:
    df_diff = df['pluie(mm)'].diff().dropna()
    result_diff = adfuller(df_diff)
    print(f"ADF Statistic after differencing: {result_diff[0]}")
    print(f"p-value after differencing: {result_diff[1]}")

    # Plot des données différenciées
    plt.figure(figsize=(10, 4))
    plt.plot(df_diff)
    plt.title('Differenced Monthly Precipitations in San Francisco')
    plt.show()

# 2. Proposer un modèle ARIMA
plot_acf(df_diff)
plot_pacf(df_diff)
plt.show()

# 3. Estimer le modèle SARIMA (2, 0, 0)x(0, 0, 0, 12)
sarima_model = SARIMAX(df['pluie(mm)'][:'1963-12'], order=(2, 0, 0), seasonal_order=(0, 0, 0, 12))
sarima_result = sarima_model.fit(disp=False)
print(sarima_result.summary())

# Résidus
residuals = sarima_result.resid
plt.figure(figsize=(10, 4))
plt.plot(residuals)
plt.title('SARIMA Residuals')
plt.show()

# 4. Prédiction pour 1964, 1965, 1966
forecast = sarima_result.get_forecast(steps=36)
forecast_index = pd.date_range(start='1964-01-01', end='1966-12-01', freq='MS')
forecast_series = pd.Series(forecast.predicted_mean, index=forecast_index)

# Affichage des prévisions et des valeurs réelles
plt.figure(figsize=(10, 6))
plt.plot(df['pluie(mm)'], label='Observed')
plt.plot(forecast_series, label='Forecast')
plt.title('Observed vs Forecasted Precipitations')
plt.legend()
plt.show()

# 5. Revenir au modèle AR(p) initial et faire la même chose
# Par exemple, on peut utiliser AR(2) si la PACF montrait un cut-off à lag 2
arima_model = SARIMAX(df['pluie(mm)'][:'1963-12'], order=(2, 0, 0))
arima_result = arima_model.fit(disp=False)
print(arima_result.summary())

# Prédiction avec ARIMA
arima_forecast = arima_result.get_forecast(steps=36)
arima_forecast_series = pd.Series(arima_forecast.predicted_mean, index=forecast_index)

# Affichage des prévisions ARIMA et des valeurs réelles
plt.figure(figsize=(10, 6))
plt.plot(df['pluie(mm)'], label='Observed')
plt.plot(arima_forecast_series, label='ARIMA Forecast')
plt.legend()
plt.title('Observed vs ARIMA Forecasted Precipitations')
plt.show()

# 6. Comparaison graphique des modèles
plt.figure(figsize=(10, 6))
plt.plot(df['pluie(mm)'], label='Observed')
plt.plot(forecast_series, label='SARIMA Forecast')
plt.plot(arima_forecast_series, label='ARIMA Forecast')
plt.legend()
plt.title('Comparison of SARIMA and ARIMA Models')
plt.show()
