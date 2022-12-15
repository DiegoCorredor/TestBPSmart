import requests as rq
import pandas as pd
import json
import os 
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv('URL')
rta = rq.get(API_URL)
data = rta.text #Def dataset
lower = data.lower() #Dataset a minúsculas
no_spaces = lower.replace(' ','') #Quitar espacios
tojson1 = json.loads(no_spaces) #En tojson1 se encuentra todo el dataset con las primeras modificaciones

#listas necesarias
id_conv = []
num_conv = []
year_conv = []
ano_convo = []
idstart = []
idnum = []
nme_clase_pd = []
nme_tipo_medicion_pd = []
nme_tipologia_pd = []
id_tipo_pd_med = []
nme_categoria_pd = []
fcreacion_pd = []
nme_producto_pd = []
cod_grupo_gr = []
nme_grupo_gr = []
id_persona_pd = []
#columnas innecesarias: nme_convocatoria, id_producto_pd
aux1=""

for i in tojson1:
    #separación de valores de la convocatoria
    aux1 = i['nme_convocatoria']
    num_conv.append(aux1[12:15])
    year_conv.append(aux1[17:22])
    #separación de valores del id del producto
    aux1 = i['id_producto_pd']
    sp = aux1.split('-')
    idstart.append(sp[0])
    idnum.append(sp[1]+'-'+sp[2])
    #relleno por columna de cada lista
    aux1 = i['id_convocatoria']
    id_conv.append(aux1)
    aux1 = i['ano_convo']
    ano_convo.append(aux1)
    aux1 = i['nme_clase_pd']
    nme_clase_pd.append(aux1)
    aux1 = i['nme_tipo_medicion_pd']
    nme_tipo_medicion_pd.append(aux1)
    aux1 = i['nme_tipologia_pd']
    nme_tipologia_pd.append(aux1)
    aux1 = i['nme_categoria_pd']
    nme_categoria_pd.append(aux1)
    aux1 = i['fcreacion_pd']
    fcreacion_pd.append(aux1)
    aux1 = i['nme_producto_pd']
    nme_producto_pd.append(aux1)
    aux1 = i['cod_grupo_gr']
    cod_grupo_gr.append(aux1)
    aux1 = i['nme_grupo_gr']
    nme_grupo_gr.append(aux1)
    aux1 = i['id_persona_pd']
    id_persona_pd.append(aux1)

#Json final
json_dt = {}
json_dt['exported'] = []

for i in range(len(tojson1)):
    array_json = {
        #todas las demas listas
        'id_conv': f'{id_conv[i]}',
        'num': f'{num_conv[i]}',
        'year': f'{year_conv[i]}',
        'ano_convo': f'{ano_convo[i]}',
        'id_pro_letra': f'{idstart[i]}',
        'id_pro_num': f'{idnum[i]}',
        'nme_clase_pd': f'{nme_clase_pd[i]}',
        'nme_tipo_medicion_pd': f'{nme_tipo_medicion_pd[i]}',
        'nme_tipologia_pd': f'{nme_tipologia_pd[i]}',
        'nme_categoria_pd': f'{nme_categoria_pd[i]}',
        'fcreacion_pd': f'{fcreacion_pd[i]}',
        'nme_producto_pd': f'{nme_producto_pd[i]}',
        'cod_grupo_gr': f'{cod_grupo_gr[i]}',
        'nme_grupo_gr': f'{nme_grupo_gr[i]}',
        'id_persona_pd': f'{id_persona_pd[i]}'
    }
    json_dt['exported'].append(array_json)
#exportar a archivo json
with open("test.json","w") as arch_json:
    arch_json.write(json.dumps(json_dt))
#convertir el json a dataframe
dfclean = pd.DataFrame(data=json_dt)
#los filtros no pude hacerlos, algo me fallo al exportar al dataframe y no pude colocar el nombre de cada columna


print("Json exportado con exito")