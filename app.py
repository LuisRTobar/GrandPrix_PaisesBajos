from numpy import char
import pandas as pd
import streamlit as st 
from PIL import Image 

# linea de encabezado
st.header('Graficas utilizando Pandas', divider='rainbow')
# linea de titulo
st.title('Resultados del Grand Prix de Países Bajos')

# importando imagen
image= Image.open('george-russell-williams-fw43b-.jpg')
st.image(image, caption='Max Verstappen')

st.text_input("¿Cuál es tú nombre? ", key="name")
st.session_state.name
st.text('¡Hola !'+st.session_state.name+' !')
'Hola cómo estás? ', st.session_state.name

# importando archivo cvs
df = pd.read_csv('GrandPrix_PaisesBajos.csv')

# mostrando DataFrame
if st.checkbox('Mostrar dataframe'):
  df


option = st.selectbox(
  'Selecciona tu corredor favorito: ',
  df['DRIVER'])
'Tu seleccion: ',  option

# imprimiendo Fila
df.loc[df['DRIVER'] == option]

# creando grafica
st.line_chart(
  df,
  x= 'AVG SPEED',
  y = 'LAP'
)
