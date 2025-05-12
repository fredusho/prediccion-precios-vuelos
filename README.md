# Predicción del Precio de Vuelos ✈️

## 🧠 Objetivo del Proyecto
El objetivo de este proyecto es **predecir el precio de boletos de avión** a partir de distintas características como la aerolínea, ciudad de origen y destino, duración del vuelo, número de escalas, clase del pasaje y día de la semana. Esto permite ayudar a consumidores o plataformas de viaje a estimar precios y tomar mejores decisiones.

---

## 📊 Dataset
El dataset contiene información sobre vuelos domésticos en la India. Las principales variables utilizadas son:

- `airline`: Nombre de la aerolínea
- `from` y `to`: Ciudad de origen y destino
- `date`: Fecha del vuelo
- `duration_min`: Duración del vuelo en minutos
- `stop_clean`: Número de escalas
- `class`: Clase (económica o ejecutiva)
- `price`: Precio del boleto (variable objetivo)

---

## 🔍 Metodología
Se siguieron los pasos típicos de un pipeline de ciencia de datos:

1. **Exploración y limpieza de datos**
   - Conversión de fechas
   - Eliminación de outliers
   - Ingeniería de variables (como el día de la semana)

2. **Análisis exploratorio (EDA)**
   - Análisis del comportamiento del precio según aerolínea, día, escalas, etc.
   - Visualización de la distribución de la variable objetivo

3. **Modelado predictivo**
   - Se probaron tres modelos:
     - Regresión Lineal
     - Árbol de Decisión
     - Random Forest
   - Se seleccionó Random Forest por su mejor desempeño.
   - Se aplicó optimización de hiperparámetros con `GridSearchCV`.

4. **Evaluación**
   - Métricas utilizadas: MAE, RMSE y R²
   - Comparación con baseline (modelo más simple)
   - Se guardó el mejor modelo (`random_forest_optimized.pkl`)

---

## 📈 Resultados
Modelo final seleccionado: **Random Forest optimizado**  
Métricas sobre el conjunto de prueba:
- MAE: 2301.05
- RMSE: 3681.38
- R²: 0.9736

---

## 💡 Conclusiones
- El modelo desarrollado permite estimar precios de vuelos con alta precisión.
- Variables como la duración, aerolínea, clase y número de escalas fueron determinantes.
- Este tipo de modelo puede ser útil para integrarse en comparadores de vuelos o apps de viajes.

---

## 📦 Archivos del proyecto
- `Prueba_Predicción_del_precio_de_vuelos_Freddy_Gonzalez.ipynb`: Notebook principal con todo el análisis.
- `random_forest_optimized.pkl`: Modelo entrenado y listo para usar.
- `README.md`: Este archivo.

---

## 🚀 Próximos pasos
- Probar otros algoritmos como XGBoost o LightGBM.
- Incorporar más variables como horarios de salida o promociones.
- Desplegar el modelo como API para uso real.

---

👨‍💻 Autor: Freddy González  
📅 Fecha: Mayo 2025
