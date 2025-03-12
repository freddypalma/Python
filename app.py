import streamlit as st # importamos libreria streamlit
##st.write("Hello World") # Imprimie en pantalla
## llamamos el programa: streamlit run app.py
import pandas as pd
import numpy as np   
#dataframe = pd.DataFrame(
#    np.random.randn(10, 20), ## Creamos valores aleatorios
#    columns=('col %d' % i for i in range(20)) ## Llenamos columnas con los valores random
#    )
#st.dataframe(dataframe.style.highlight_max(axis=0))

#chart_data = pd.DataFrame(
#    np.random.randn(20, 3), # valores aleatorios
#    columns=['a', 'b', 'c'] # Genero las columnas
#    ) 
#st.write(chart_data)  #imprime en navegador
#st.line_chart(chart_data) ## Crear lineas aleatorias

#map_data = pd.DataFrame(
#    np.random.randn(1000, 2)/ [50, 50] + [6.25184, -75.56359], 
#    columns=['lat', 'lon']
#)
#st.map(map_data)

## widget 
x = st.slider('x') # this is a widget
st.write(x, 'squared is', x * x )  