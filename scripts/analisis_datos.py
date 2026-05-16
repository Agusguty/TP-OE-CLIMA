import pandas as pd
import matplotlib.pyplot as plt
import os

def analizar_clima():
    print("Iniciando el análisis de datos climáticos...")
    
    # 1. Importar el archivo CSV usando rutas relativas
    ruta_datos = os.path.join('datos', 'global-temp.csv')
    df = pd.read_csv(ruta_datos)
    
    # Filtramos para usar una de las fuentes del archivo (GISTEMP de la NASA)
    df_gis = df[df['Source'] == 'GISTEMP'].copy()
    
    # 2. Calcular los indicadores clave que pide la cátedra [cite: 120, 121, 123]
    temp_promedio = df_gis['Mean'].mean()
    temp_maxima = df_gis['Mean'].max()
    temp_minima = df_gis['Mean'].min()
    
    print("\n--- RESULTADOS DEL ANÁLISIS ---")
    print(f"Temperatura promedio histórica (Anomalía): {temp_promedio:.4f} °C")
    print(f"Temperatura máxima registrada: {temp_maxima} °C")
    print(f"Temperatura mínima registrada: {temp_minima} °C")
    
    # 3. Generar el gráfico de evolución temporal [cite: 125]
    plt.figure(figsize=(10, 5))
    df_gis_sorted = df_gis.iloc[::-1] # Invertimos para que vaya de pasado a presente
    
    # CORRECCIÓN: Usamos 'Year' en lugar de 'Date' que es como viene en este dataset
    plt.plot(df_gis_sorted['Year'], df_gis_sorted['Mean'], color='crimson', label='Anomalía de Temp (°C)')
    plt.title('EVOLUCIÓN DE LA TEMPERATURA GLOBAL (GISTEMP)', fontsize=12, fontweight='bold')
    plt.xlabel('Año / Período', fontsize=10)
    plt.ylabel('Desviación de Temperatura (°C)', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    # Espaciamos las etiquetas del eje X para que sea legible
    plt.xticks(df_gis_sorted['Year'].values[::120], rotation=45)
    plt.tight_layout()
    
    # 4. Guardar el gráfico en la carpeta /resultados usando rutas relativas [cite: 89, 127]
    ruta_grafico = os.path.join('resultados', 'grafico_resultados.png')
    plt.savefig(ruta_grafico)
    plt.close()
    print(f"\n¡Éxito! El gráfico se guardó correctamente en: {ruta_grafico}")

if __name__ == '__main__':
    analizar_clima()
