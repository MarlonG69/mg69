import streamlit as st

st.header('Introducción')

st.markdown('Teorema de Pitágoras: sea un triángulo rectángulo de catetos a y b e hipotenusa h (el lado opuesto al ángulo recto). Entonces, el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos:')

st.image('https://www.matesfacil.com/pitagoras/teorema-Pitagoras.png', caption='Llopis,J.')

st.markdown('''
Recordemos que:

El triángulo es rectángulo porque tiene un ángulo recto, es decir, un ángulo de 90 grados ó π/2 radianes

La hipotenusa es el lado opuesto al ángulo recto

Las 3 últimas fórmulas anteriores se obtienen de la primera (haciendo la raíz cuadrada en ambos lados)

Nota: h siempre es mayor que los dos catetos, es decir, h > a y h > b.
''')

st.header('Veamos un ejemplo')
st.subheader('Problema 1')
st.markdown('Queremos medir la altura de un árbol. A cierta hora del día, notamos que la sombra del árbol en el suelo mide 2,5 metros. Además, medimos la distancia desde la punta del árbol hasta el final de la sombra en el suelo, y esa distancia es de 4 metros. ¿Cuál es la altura aproximada del árbol?')

st.subheader('Solución')
st.markdown('Para calcular la altura del árbol, podemos usar el teorema de Pitágoras. En este caso, debemos identificar qué lados del triángulo rectángulo formado por la sombra, el árbol y la distancia que une sus puntas tenemos. Desde ahora, nos permitimos asumir que el árbol es perfectamente recto si no, el triángulo ya no sería rectángulo y no podríamos utilizar el teorema de Pitágoras. La altura del árbol y la longitud de la sombra son los catetos del triángulo rectángulo y la distancia entre el punto más alto del árbol y la sombra sería la hipotenusa.')

c1, c2 = st.columns(2, vertical_alignment='center')

with c1:
    st.image('https://www.smartick.es/blog/wp-content/uploads/2024/02/ejercicio-teorema-de-Pitagonas-castellano.jpg',caption='Aguilera,C. (2024)')

with c2:
    st.markdown('''
                c2=a2+b2

                42=a2+(2,5)2

                a2=42-(2,5)2

                a=3,12
                ''')






st.subheader('Referencias')
st.markdown('''
Llopis,J. Teorema de Pitágoras. Matesfacil. https://www.matesfacil.com/pitagoras/problemas-resueltos-pitagoras.html

Aguilera, C. (2024). Teorema de Pitágoras: Qué es, algunas demostraciones y ejemplo de aplicación práctica. https://www.smartick.es/blog/matematicas/geometria/teorema-de-pitagoras/

''')