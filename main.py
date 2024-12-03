import streamlit as st

h = st.Page('paginas/historia.py', title='Historia', icon=':material/patient_list:', default=True)
e = st.Page('paginas/ejemplos.py', title='Ejemplos',icon=':material/cheer:')
p = st.Page('paginas/practica.py', title='Practica',icon=':material/notifications_active:')
g = st.Page('paginas/graficas.py', title='Graficas',icon=':material/smart_toy:')

pg= st.navigation([h,e,p,g])

pg.run()

