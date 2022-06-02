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

# 2) NÚMERO DE MUNICIPIOS AFECTADOS
num_municipios = data['Nombre municipio'].value_counts().count()
print('*'*50)
print(f'Número de Municipios Afectados :\n{num_municipios}')

# 3) LISTA DE LOS MUNICIPIOS AFECTADOS (sin repetirlos)
municipios = data['Nombre municipio'].value_counts()
print('*'*50)
print(f'Municipios Afectados :\n{municipios}')

# 4) NÚMERO DE PERSONAS QUE SE ENCUENTRAN EN ATENCIÓN EN CASA
num_atencion_casa = data[data['Ubicación del caso'] == 'Casa'].shape[0]
print('*'*50)
print(f'Personas con atención en casa :\n{num_atencion_casa}')

# 5) NÚMERO DE PERSONAS QUE SE ENCUENTRAN RECUPERADAS
num_recuperados = data[data['Recuperado'] == 'Recuperado'].shape[0]
print('*'*50)
print(f'Personas recuperadas :\n{num_recuperados}')

# 6) NÚMERO DE PERSONAS QUE HAN FALLECIDO
num_fallecidos = data[data['Recuperado'] == 'Fallecido'].shape[0]
print('*'*50)
print(f'Personas fallecidas :\n{num_fallecidos}')

