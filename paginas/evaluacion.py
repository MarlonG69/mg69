import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.title('Evaluemos lo aprendido')

cal=0

st.markdown('''
1) Encuentre la hipotenusa de un tiangulo rectángulo de catetos 8 y 6.
''')

x = [0, 8, 0, 0]
y = [0, 0, 6, 0]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim([-1, 8])
ax.set_ylim([-1, 6])
ax.text(-0.5, 3, "6", size=15)
ax.text(3.5, -0.5, "8", size=15)
ax.text(4, 3.2, "h", size=15)

st.pyplot(fig)

rta= st.number_input('Escribe la respuesta correcta',min_value=0,value=0, max_value=15)
if rta==10:
    cal=cal+1
    st.success('Correcto')
    st.latex(r'h = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10')
elif rta==0:
    st.error('')
else:
    st.error('Incorrecto')

st.markdown('''
2) Encuentre el cateto faltante de un tiangulo rectángulo de hipotenusa 20 y cateto 12.
''')

x = [0, 16, 0, 0]
y = [0, 0, 12, 0]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim([-2, 16])
ax.set_ylim([-2, 12])
ax.text(-1.5, 5, "12", size=15)
ax.text(7, -1, "c1", size=15)
ax.text(9, 6, "20", size=15)

st.pyplot(fig)

rt= st.number_input('Escribe la respuesta correcta',min_value=0,value=0, max_value=20)
if rt==16:
    st.success('Correcto')
    cal=cal+1
    st.latex(r'h = \sqrt{20^2 - 12^2} = \sqrt{400 - 144} = \sqrt{256} = 16')
elif rt==0:
    st.error('')
else:
    st.error('Incorrecto')

st.divider()

st.image('https://i.ytimg.com/vi/6JrJvN3vR7Y/maxresdefault.jpg')

st.markdown('''
3) En la figura de la izquierda, si un francotirador se encuentra en la cima de un faro de 16 metros de altura
y un barco esta en el punto A, a una distancia de 63 metros de la base del faro ¿Cuantos metros debe recorrer 
bala para llegar hasta el barco?
''')

dbala= st.number_input('Escribe la respuesta correcta',min_value=0,value=0, max_value=100,key="j")
if dbala==65:
    cal=cal+1
    st.success('Correcto')
    st.latex(r'h = \sqrt{63^2 - 16^2} = \sqrt{3969 - 256} = \sqrt{4225} = 65')
elif dbala==0:
    st.error('')
else:
    st.error('Incorrecto')

st.markdown('''
4) En la figura de la derecha, una ardilla se encuentra en la cima del pino y salta hasta llegar al pico de la sombra recorriendo una distancia de 4 metros en linea recta, sí el pico de la sombra esta a 2.5 metros del tronco del pino, ¿cuanto mide el pino?
''')

pino= st.number_input('Escribe la respuesta correcta',min_value=0.0,value=0.0, max_value=4.0,key="l")
pino=round(pino,2)

if pino==3.12 or pino==3.1:
    cal=cal+1
    st.success('Correcto')
    st.latex(r'h = \sqrt{4^2 - 2.5^2} = \sqrt{16 - 6.25} = \sqrt{9.76} = 3.12')
elif pino==0:
    st.error('')
else:
    st.error('Incorrecto')

st.header(f'Tu puntaje es: {cal}/4')