import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.title('Evaluemos lo aprendido')

st.markdown('''
1) Encuentre la hipotenusa de un tiangulo rectángulo de catetos 8 y 6.
''')

x = [0, 8, 0, 0]
y = [0, 0, 6, 0]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim([-1, 9])
ax.set_ylim([-1, 7])
ax.text(-0.5, 3, "6", size=15)
ax.text(3.5, -0.5, "8", size=15)
ax.text(4, 3.2, "h", size=15)

st.pyplot(fig)

rta= st.number_input('Escribe la respuesta correcta',min_value=0,value=0, max_value=15)
if rta==10:
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
ax.set_xlim([-2, 18])
ax.set_ylim([-2, 14])
ax.text(0.5, 3, "12", size=15)
ax.text(3.5, -0.5, "c1", size=15)
ax.text(4, 3.2, "20", size=15)

st.pyplot(fig)

rt= st.number_input('Escribe la respuesta correcta',min_value=0,value=0, max_value=20)
if rt==10:
    st.success('Correcto')
    st.latex(r'h = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10')
elif rt==0:
    st.error('')
else:
    st.error('Incorrecto')