import streamlit as st

st.title('**Marlon Gómez**')

st.header('**subtitulo**')


st.slider('aaa')

st.subheader('sub-subtitulo')

st.markdown('''
Se puede poner un texo
**Negrilla**

*Italica*

***Ambas***

+ Item 1

+ Item 2

:red[Rojo Pasión], con mi negrita

''')

st. caption('Estudiante de la materia programaión')

st.latex('mx+b=y')

#imagenes o videos se copia el link
st.image('https://i.ytimg.com/vi/0VI05oJOhUY/maxresdefault.jpg')
st.video('https://www.youtube.com/watch?v=ULxjPNTiAZ8')

with st.container(border=True):
    st.caption('Estudiante de la materia programaión')
    st.latex('mx+b=y')

c1, c2 = st.columns(2, vertical_alignment='center')

with c1:
    st.markdown('pimera columna')
    

with c2:
    st.markdown('segunda columna')
