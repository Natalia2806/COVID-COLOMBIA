"""
ESTUDIANTE: NATALIA TUIRAN QUINTERO
"""
import pandas as pd
import matplotlib.pyplot as plt


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

# 7) ORDENAR DE MAYOR A MENOR POR TIPO DE CASO (Importado, en estudio, Relacionado)
tipo_contagio = data['Tipo de contagio'].sort_values().value_counts()
print('*'*50)
print(f'Tipo de contagio (Mayor a menor) :\n{tipo_contagio}')

# 8) NÚMERO DE DEPARTAMENTOS AFECTADOS
num_departamentos = data['Nombre departamento'].value_counts().count()
print('*'*50)
print(f'Número de departamentos afectados :\n{num_departamentos}')

# 9) LISTA DE LOS DEPARTAMENTOS AFECTADOS(sin repetirlos)
departamentos = data['Nombre departamento'].value_counts()
print('*'*50)
print(f'Departamentos afectados :\n{departamentos}')

# 10) ORDEN DE MAYOR A MENOR POR TIPO DE ATENCIÓN
tipo_recuperacion = data['Tipo de recuperación'].sort_values().value_counts()
print('*'*50)
print(f'Tipo de recuperación (Mayor a menor) :\n{tipo_recuperacion}')

# 11) LISTA DE MAYOR A MENOR LOS 10 DEPARTAMENTOS CON MAS CASOS DE CONTAGIADOS
departamentos_casos = data['Nombre departamento'].value_counts().head(10)
print('*'*50)
print(f'10 Departamentos con más casos de contagiados (Mayor a menor) :\n{departamentos_casos}')

# 12) LISTA DE MAYOR A MENOR LOS DEPARTAMENTOS CON MAS CASOS DE FALLECIDOS
aux_fallecidos_dep = data[data['Estado'] == 'Fallecido'].groupby('Nombre departamento')
fallecidos_dep = aux_fallecidos_dep.size().sort_values(ascending=False).head(10)
print('*'*50)
print(f'10 Departamentos con más casos casos de fallecidos (Mayor a menor) :\n{fallecidos_dep}')

# 13) LISTA DE MAYOR A MENOR LOS 10 DEPARTAMENTOS CON MAS CASOS DE RECUPERADOS
aux_recuperados_dep = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento')
recuperados_dep = aux_fallecidos_dep.size().sort_values(ascending=False).head(10)
print('*'*50)
print(f'10 Departamentos con más casos casos de recuperados (Mayor a menor) :\n{recuperados_dep}')

# 14) LISTA DE MAYOR A MENOR LOS 10 MUNICIPIOS CON MAS CASOS DE CONTAGIADOS
municipios_casos = data['Nombre municipio'].value_counts().head(10)
print('*'*50)
print(f'10 Municipios con más casos de contagiados (Mayor a menor) :\n{municipios_casos}')

# 15) LISTA DE MAYOR A MENOR LOS 10 MUNICIPIOS CON MAS CASOS DE FALLECIDOS
aux_fallecidos_mun = data[data['Estado'] == 'Fallecido'].groupby('Nombre municipio')
fallecidos_mun = aux_fallecidos_mun.size().sort_values(ascending=False).head(10)
print('*'*50)
print(f'10 Municipios con más casos casos de fallecidos (Mayor a menor) :\n{fallecidos_mun}')

# 16) LISTA DE MAYOR A MENOR LOS 10 MUNICIPIOS CON MAS CASOS DE RECUPERADOS
aux_recuperados_mun = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio')
recuperados_mun = aux_recuperados_mun.size().sort_values(ascending=False).head(10)
print('*'*50)
print(f'10 Municipios con más casos casos de recuperados (Mayor a menor) :\n{recuperados_mun}')

# 17) LISTA AGRUPADO POR DEPARTAMENTO Y EN ORDEN DE MAYOR A MENOR LAS CIUDADES CON MAS CASOS DE CONTAGIADOS
dep_ciud_contagios = data.groupby(['Nombre departamento', 'Nombre municipio']).size().sort_values(ascending=False)
print(f'Departamentos y sus ciudades con mas casos de contagios:\n{dep_ciud_contagios}')

# 18) NÚMERO DE MUJERES Y HOMBRES CONTAGIADOS POR CIUDAD POR DEPARTAMENTO
numero_h_m_contagiados = data.groupby(['Sexo', 'Nombre municipio', 'Nombre departamento']).size().sort_values(ascending=False)
print(f'Número de Mujeres y hombres contagiados por ciudad por departamento:\n{numero_h_m_contagiados}')

# 19) LISTA DEL PROMEDIO DE EDAD DE CONTAGIADOS POR HOMBRE Y MUJERES POR CIUDAD POR DEPARTAMENTO
promedio = data.groupby( ['Sexo', 'Nombre municipio', 'Nombre departamento']).Edad.mean()
print(f'{promedio}')

# 20) LISTA DE MAYOR A MENOR EL NÚMERO DE CONTAGIADOS POR DEPARTAMENTO DE PROCEDENCIA
departamento_procedencia = data['Nombre departamento'].value_counts()
print(f'Número de contagiados por departamento de procedencia: \n{departamento_procedencia}')

# 21) LISTA DE MAYOR A MENOR LAS FECHAS DONDE SE PRESENTARON MAS CONTAGIADOS
fechas_mas_contagios = data['Fecha de diagnóstico' ].value_counts().sort_values(ascending=False)
print(f'Fechas donde se presentaron mas contagios:\n{fechas_mas_contagios}')

# 22. DIGA CUAL ES LA TASA DE MORTALIDAD Y RECUPERACIÓN QUE TIENE TODA COLOMBIA
cantidad_muertes = data[data['Estado'] == 'Fallecido'].shape[0]
cantidad_recuperados = data[data['Recuperado'] == 'Recuperado'].shape[0]

tasa_mortalidad = cantidad_muertes / num_casos * 100
tasa_recuperacion = cantidad_recuperados / num_casos * 100

print(f'Tasa de mortalidad en Colombia: {tasa_mortalidad}')
print(f'Tasa de recuperacion en Colombia: {tasa_recuperacion}')

# 23) LISTA DE LA TASA DE MORTALIDAD Y RECUPERACIÓN QUE TIENE CADA DEPARTAMENTO
muertes_departamento = data[data['Estado'] == 'Fallecido'].groupby('Nombre departamento').size()
tasa_mortalidad_dpto = muertes_departamento /  num_casos * 100
print(f'Tasa de mortalidad de cada departamento:\n{tasa_mortalidad_dpto}')

recuperacion_departamento = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size()
tasa_recuperacion_dpto = recuperacion_departamento /  num_casos * 100
print(f'Tasa de recuperacion de cada departamento:\n{tasa_recuperacion_dpto}')

# 24) LISTA DE LA TASA DE MORTALIDAD Y RECUPERACIÓN QUE TIENE CADA CIUDAD
muertes_municipio = data[data['Estado'] == 'Fallecido'].groupby('Nombre municipio').size()
tasa_mortalidad_munic = muertes_municipio /  num_casos * 100
print(f'Tasa de mortalidad de cada municipio:\n{tasa_mortalidad_munic}')

recuperacion_municipio = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size()
tasa_recuperacion_munic = recuperacion_municipio /  num_casos * 100
print(f'Tasa de recuperacion de cada municipio:\n{tasa_recuperacion_munic}')

# 25.LISTA POR CADA CIUDAD LA CANTIDAD DE PERSONAS POR ATENCIÓN
cantidad_atencion = data.groupby(['Nombre municipio', 'Ubicación del caso']).size()
print(f'Cantidad de personas por atención:\n{cantidad_atencion}')

# 26) LISTA DEL PROMEDIO DE EDAD POR SEXO POR CADA CIUDAD DE CONTAGIADOS
promedio_edad_sexo = data.groupby(['Sexo', 'Nombre municipio']).Edad.mean()
print(f'Promedio de edad por sexo por cada ciudad de contagiados:\n{promedio_edad_sexo}')

# 27) GRAFIQUE LAS CURVAS DE CONTAGIO, MUERTE Y RECUPERACIÓN DE TODA COLOMBIA ACUMULADOS
data.loc[data['Sexo'] == 'm'] = 'M'
data.loc[data['Sexo'] == 'f'] = 'F'
data.loc[data['Estado'] == 'leve'] = 'Leve'
data.loc[data['Estado'] == 'LEVE'] = 'Leve'

contagios = data.groupby('Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
plt.show(contagios)
print('\nCurva de Contagios')


fallecidos = data[data['Estado'] == 'Fallecido'].groupby('Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
plt.show(fallecidos)
print('\nCurva de Fallecidos')

recuperados = data[data['Recuperado'] == 'Recuperado'].groupby('Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
plt.show(recuperados)
print('\nCurva de Recuperados')

# 28) GRAFICA DE LAS CURVAS DE CONTAGIO, MUERTE Y RECUPERACIÓN DE LOS 10 DEPARTAMENTOS CON MAS CASOS DE CONTAGIADOS ACUMULADOS
contagios_dpto = data.groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
plt.show(contagios_dpto)
print('\nCurva de los 10 departamentos con mas casos de contagiados')

fallecidos_dpto = data[data['Estado'] == 'Fallecido'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
plt.show(fallecidos_dpto)
print('\nCurva de los 10 departamentos con mas casos de fallecidos')

recuperados_dpto = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
plt.show(recuperados_dpto)
print('\nCurva de los 10 departamentos con mas casos de recuperados')

# 29) GRAFICA DE LAS CUERVAS DE CONTAGIO, MUERTE Y RECUPERACION DE LAS 10 CIUDADES CON MAS CASOS DE CONTAGIOS ACUMULADOS
contagios_municipio = data.groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
plt.show(contagios_municipio)
print('\nCurva de los 10 municipios con mas casos de contagiados')

fallecidos_municipio = data[data['Estado'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
plt.show(fallecidos_municipio)
print('\nCurva de los 10 municipios con mas casos de fallecidos')

recuperados_municipio = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
plt.show(recuperados_municipio)
print('\nCurva de los 10 municipios con mas casos de recuperados')

# 30) LISTA DE MAYOR A MENOR LA CANTIDAD DE FALLECIDOS POR EDAD EN TODA COLOMBIA.
fallecidos = data[data['Estado'] == 'Fallecido'].groupby('Edad').size().sort_values(ascending = False)
print(f'Cantidad de fallecidos por edad en toda Colombia:\n{fallecidos}')

# 31) LISTA DE EL PORCENTAJE DE PERSONAS POR ATENCIÓN DE TODA COLOMBIA
porcentaje_personas= ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)) / ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)).sum())) * 100
print(f'Porcentaje de personas por atención de toda Colombia\n {porcentaje_personas}')

# 32) HAGA UN GRÁFICO DE BARRAS POR ATENCIÓN DE TODA COLOMBIA
data.groupby(['Ubicación del caso']).size().sort_values(ascending = False).plot(kind='bar')
plt.ylabel('Cantidad de personas')
print('\n Gráfico de barras por atención de toda Colombia')

# 33) HAGA UN GRÁFICO DE BARRAS POR SEXO DE TODA COLOMBIA
data.groupby(['Sexo']).size().sort_values(ascending = False).plot(kind='bar')
print('\nGrafico de barras por sexo de toda Colombia')

# 34.Haga un gráfico de barras por tipo de toda Colombia
data.groupby(['Tipo de contagio']).size().sort_values(ascending = False).plot(kind='bar')
print('\nGrafico de barras por tipo de contagio de toda Colombia')


# 35. Haga un gráfico de barras del número de contagiados, recuperados y fallecidos por fecha de toda Colombia

data.groupby('Fecha de diagnóstico').size().plot(kind = 'bar')
Fallecidos = data[data['Ubicación del caso'] == 'Fallecido']
Fallecidos.groupby('Fecha de diagnóstico').size().plot(kind = 'bar')
Recuperado = data[data['Recuperado'] == 'Recuperado']
Recuperado.groupby('Fecha de diagnóstico').size().plot(kind = 'bar')
plt.legend(["Recuperados", "Fallecidos", "Contagiados"])