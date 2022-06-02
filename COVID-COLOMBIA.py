"""
ESTUDIANTE: NATALIA TUIRAN QUINTERO
"""
import pandas as pd

#DATASETS
url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url)[:3000]

# ELIMINAMOS LAS COLUMNAS DEL DATASET 
data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Nombre del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)

# 1) NÚMERO DE CASOS DE CONTAGIADOS EN EL PAÍS
num_casos = data.shape[0]
print('*'*50)
print(f'Número de casos :\n{num_casos}')