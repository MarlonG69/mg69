import streamlit as st

st.title('Marlon Gómez')
st.header('subtitulo')
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

