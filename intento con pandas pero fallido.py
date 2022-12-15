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
#Dataframe a partir de tojson1
dftemp = pd.DataFrame(data=tojson1)
#Creación del dataframe que contenga toda la información final
#dfcomplete = dftemp[['id_conv','num_conv','year_conv','ano_convo','idstart','idnum','nme_clase_pd','nme_tipo_medicion_pd','nme_tipologia_pd','id_tipo_pd_med','nme_categoria_pd','fcreacion_pd','nme_producto_pd','cod_producto_gr','nme_grupo_gr','id_persona_pd']]
dfcomplete = dftemp.loc[:, dftemp.columns]

for label,content in dftemp.items():
    dfcomplete.insert(int(dftemp.index),label,content)
    print(f'Label: {label}')
    print(f'Content: {content}')

print(dfcomplete)