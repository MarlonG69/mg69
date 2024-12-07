import streamlit as st

st.subheader('Creador, Marlon Gómez')
st.markdown('''
Estudiante de matemáticas de la UIS, interesado en el aprendizaje continuo
de esta hermosa ciencia, con afinidad en Cálculo.
En mi tiempo libre disfruto ver series o peliculas, una buena plática y cocinar.
En mi paso por la materia de Programación1, aprendí conceptos basicos, diagramas de flujo y pseudocódigo,
hasta llegar a python, donde comencé con programas basicos, realizar graficos
y cálculos, conjuntos de datos y por ultimo esta página que espero disfruten y les sea util.
''')


st.divider()
st.title('**Historia del Teorema de Pitagoras**')


st.markdown('''
El teorema de Pitágoras era conocido por las culturas de China, Mesopotamia y Egipto, aunque no lo utilizaban formalmente; solo sabían que ciertos números cumplían propiedades geométricas en un triángulo. El teorema como tal fue descubierto alrededor del año 500 a.c. por Pitágoras y los pitagóricos, quienes dieron la primera demostración formal del mismo.

El teorema de Pitágoras se considera la base para la comprensión de diversos conceptos propios de las matemáticas, que tienen que ver con áreas como el álgebra, la trigonometría y la geometría analítica. Se usa para deducir la ecuación de la circunferencia, la distancia entre dos puntos en un plano coordenado y la definición de los números irracionales, entre muchas otras cosas.
''')

st.image('https://manuelfelipevargar.com/wp-content/uploads/2023/04/Manuelphilvar_Pythagoras_theorem_c6294d4f-8eaf-4aee-8333-5b2fa7607131.webp',caption="Vargas, M. (2023)")

st.markdown('Demostración del teorema de Pitágoras de Perigal. Al matemático inglés Henry Perigal (1801/1898), se le atribuye una ingeniosa comprobación del teorema de Pitágoras. «Sobre el mayor de los cuadrados construidos sobre los catetos se determina el centro y se trazan dos rectas paralela y perpendicular a la hipotenusa del triángulo. Con las cuatro piezas obtenidas más el cuadrado construido sobre el otro cateto podemos cubrir el cuadrado construido sobre la hipotenusa.»')

c1, c2 = st.columns(2, vertical_alignment='top')

with c1:
    st.subheader('Demostracion de Perigal')

    st.image('https://www.smartick.es/blog/wp-content/uploads/2024/02/teorema-de-Pitagoras-2-1024x825.png', caption="Aguilera,C. (2024)")
    

with c2:
    st.subheader('Video interactivo')

    st.caption('Realizado en Geogebra por Aguilera,C. (2024)')
    st.video('https://www.smartick.es/blog/wp-content/uploads/2024/02/Video-demostracion-Perigal.mp4?_=2')

st.subheader('Video explicativo (Extra)')
st.markdown('El matemático español Eduardo Sáenz de Cabezón, en su canal Derivando, explica en este breve video la importancia del teorema de pitagoras y algunas curiosidades sobre este, al que él considera el teorema más famoso de las matemáticas')

st.video('https://www.youtube.com/watch?v=4I6YIccTkcA')


st.subheader('Referencias')
st.markdown('''
Garcia, V. Universidad Autónoma Metropolitana. http://campusvirtual.cua.uam.mx/material/tallerm/27_Teorema_De_Pitagoras_html/index.html#

Vargas, M. (2023). Explorando el teorema de Pitágoras.https://manuelfelipevargar.com/explorando-el-teorema-de-pitagoras/

Aguilera, C. (2024). Teorema de Pitágoras: Qué es, algunas demostraciones y ejemplo de aplicación práctica. https://www.smartick.es/blog/matematicas/geometria/teorema-de-pitagoras/

Sáenz,E. (2021) ¿Por qué es tan importante el TEOREMA DE PITÁGORAS?. https://www.youtube.com/watch?v=4I6YIccTkcA
''')

