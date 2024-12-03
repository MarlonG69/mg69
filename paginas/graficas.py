import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.title('Espacio interactivo')

x1= st.number_input('Escribe las coordenadas de un punto x1',value=0, min_value=-10, max_value=10)
y1= st.number_input('Escribe las coordenadas de un punto y1',value=0, min_value=-10, max_value=10)
x2= st.number_input('Escribe las coordenadas de un punto x2',value=0, min_value=-10, max_value=10)
y2= st.number_input('Escribe las coordenadas de un punto y2',value=0, min_value=-10, max_value=10)


if y1>y2:
    y3=y2
    x3=x1
else:
    y3=y1
    x3=x2

# ------------------ st.divider() #crea una linea de division

puntos = pd.DataFrame({
    'x':[x1, x2, x3],
    'y':[y1, y2, y3],
})

#puntos = st.data_editor(puntos, hide_index=True)

pol = patches.Polygon(puntos, closed=True, fill=True, facecolor='azure', edgecolor='teal')

fig, ax = plt.subplots(ncols=2) 

ax[1].set_title('Viendolo como un tiángulo\nrectangulo')
ax[1].add_patch(pol) 
ax[1].set_xlim(puntos['x'].min()-1, puntos['x'].max()+1)
ax[1].set_ylim(puntos['y'].min()-1, puntos['y'].max()+1)
ax[1].set_aspect('equal')  #cambia tamaño de los cuadros


recta = pd.DataFrame({
    'x':[x1, x2],
    'y':[y1, y2],
})

#recta = st.data_editor(recta, hide_index=True)

pol = patches.Polygon(recta, closed=True, fill=True, facecolor='azure', edgecolor='teal')


ax[0].set_title('Viendolo como la gráfica \nde una función lineal')
ax[0].add_patch(pol) 
ax[0].set_xlim(puntos['x'].min()-1, recta['x'].max()+1)
ax[0].set_ylim(puntos['y'].min()-1, recta['y'].max()+1)
ax[0].set_aspect('equal')  #cambia tamaño de los cuadros

st.pyplot(fig)