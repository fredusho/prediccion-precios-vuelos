# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w_oOi4qpHcIYmcnM-QQ4eAZ3nNb2BcCw
"""

import pandas as pd
import numpy as np

def calidad_datos(df):
    # Inicializa el resumen base
    resumen = pd.DataFrame(index=df.columns)
    resumen['tipo_dato'] = df.dtypes.astype(str)
    resumen['nulos'] = df.isnull().sum()
    resumen['porcentaje_nulos'] = df.isnull().mean() * 100
    resumen['valores_unicos'] = df.nunique()

    # Cálculo de ceros solo para columnas numéricas
    columnas_numericas = df.select_dtypes(include=[np.number]).columns
    resumen['ceros'] = 0
    resumen.loc[columnas_numericas, 'ceros'] = (df[columnas_numericas] == 0).sum()
    resumen['porcentaje_ceros'] = 0.0
    resumen.loc[columnas_numericas, 'porcentaje_ceros'] = (df[columnas_numericas] == 0).mean() * 100

    # Outliers con regla del IQR
    outliers = {}
    for col in columnas_numericas:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lim_inf = Q1 - 1.5 * IQR
        lim_sup = Q3 + 1.5 * IQR
        outliers[col] = ((df[col] < lim_inf) | (df[col] > lim_sup)).sum()
    resumen['outliers'] = resumen.index.to_series().map(outliers).fillna(0).astype(int)

    # Estadísticas adicionales solo para columnas numéricas
    resumen['media'] = df[columnas_numericas].mean()
    resumen['desviacion_std'] = df[columnas_numericas].std()
    resumen['coef_variacion'] = (df[columnas_numericas].std() / df[columnas_numericas].mean()).replace([np.inf, -np.inf], np.nan)
    resumen['asimetria'] = df[columnas_numericas].skew()
    resumen['curtosis'] = df[columnas_numericas].kurtosis()

    # Calcular moda para todas las columnas
    try:
        resumen['moda'] = df.mode().iloc[0]
    except Exception:
        resumen['moda'] = np.nan

    # Asegura orden por porcentaje de nulos, pero sin errores por tipo
    resumen = resumen.sort_values(by='porcentaje_nulos', ascending=False)

    return resumen