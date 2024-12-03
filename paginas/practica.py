import streamlit as st

st.title('Practica')

nombre= st.text_input('Escribe tu nombre')

st.markdown(f'Hola {nombre} vamos a realizar algunos ejericios usando el teorema de pitagoras')

st.subheader('Antes de iniciar recordemos algunos conceptos')
st.markdown('Si tenemos un triangulo rectangulo cuyos lados miden 5,7,4 ¿Cual es la hipotenusa?')

rta= st.number_input('Escribe la respuesta correcta',min_value=0,value=0, max_value=15)
if rta==7:
    st.success('Correcto')
elif rta==0:
    st.error('')
else:
    st.error('Incorrecto')

st.markdown('¿El teorema de pitagoas se puede usar para todos los triangulos?')

rsp= st.text_input('responde con si o no')
rsp=rsp.lower()
if rsp=='no':
    st.success('Correcto')
elif rsp=='':
    st.error('')
elif rsp=='si':
    st.error('Incorrecto, el teorema de pitagoas solo se puede para triangulos rectangulos')
else:
    st.error('No valido')






