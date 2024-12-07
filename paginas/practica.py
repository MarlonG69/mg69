import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.title('Practica')

nombre= st.text_input('Escribe tu nombre')

st.markdown(f'Hola {nombre} vamos a realizar algunos ejericios usando el teorema de pitagoras')

st.subheader('Antes de iniciar recordemos algunos conceptos')
st.markdown('Si tenemos un triangulo rectángulo cuyos lados miden 5,7,4 ¿Cual es la hipotenusa?')

rta= st.number_input('Escribe la respuesta correcta',min_value=0,value=0, max_value=15)
if rta==7:
    st.success('Correcto, la hipotenusa es el lado más largo.')
elif rta==0:
    st.error('')
else:
    st.error('Incorrecto')

st.markdown('¿El teorema de pitagoas se puede usar para todos los triangulos?')

rsp= st.text_input('responde con si o no')
rsp=rsp.lower()
if rsp=='no':
    st.success('Correcto, solo se puede usar para triangulos rectangulos.')
elif rsp=='':
    st.error('')
elif rsp=='si':
    st.error('Incorrecto, el teorema de pitagoas solo se puede para triangulos rectangulos')
else:
    st.error('No valido')

st.markdown('''
Desde el cálculo de la diagonal de una pantalla de TV hasta la determinación de la longitud de una escalera necesaria
para alcanzar cierta altura, el teorema es aplicable en una gran variedad de escenarios.
Incluso determinar la distancia entre dos puntos de un plano de coordenadas implica el uso del Teorema de Pitágoras.

En este apartado podremos ver como relacionamos la distancia entre dos puntos del plano y la diagonal de un rectángulo.
''')

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

st. markdown('''
Podemos notar que la distancia entre esos dos puntos esta dada por la hipotenusa del triangulo,
por lo tanto procederemos a encontrarla

Los catetos los hallamos con la diferencia entre las coordenadas. Tanto para X, como para Y, así:
''')
c1, c2 = st.columns(2, vertical_alignment='center')

with c1:

    st.latex(r'|x_2 - x_1| = \Delta x')
    st.latex(r'|y_2 - y_1| = \Delta y')
    
with c2:
    st.latex(r'\Delta x = ' + str(abs(x2-x1)))
    st.latex(r'\Delta y = ' + str(abs(y2-y1)))

st.markdown('Por consiguiente la distancia entre los dos puntos sera:')

dh= round(((x2-x1)**2 + (y2-y1)**2)**0.5, 3)
st.latex(fr'\sqrt{{(\Delta_x)^2 + (\Delta_y)^2}} = \sqrt{{ {abs(x2-x1)} ^2 + {abs(y2-y1)} ^2  }} = {dh}') 

st.markdown(' - Usando el ejericio anterior, varia las coordenadas hasta crear un triangulo con hipotenusa 5.')

if dh==5 and x1!=x2 and y1!=y2:
    st.success('Correcto, bien hecho!')
elif x1==x2 and y1==y2 and dh==0:
    st.error('')
elif x1==5 or x2==5 or y1==5 or y2==5 or x1==-5 or x2==-5 or y1==-5 or y2==-5:
    st.error('Incorrecto, aunque la distancia es 5, es una linea recta, no un triangulo.')
else:
    st.error('Incorrecto, intenta nuevamente')



