# pylint: disable=all
import streamlit as st
import psycopg2
import services.database as db
import CrudRefGeo.Cadastrar as Cadastrar
import CrudRefGeo.Consultar as Consultar

db.create_connection()

st.sidebar.title('Menu')
refGeoCrud = st.sidebar.selectbox('CRUD', ['Cadastrar', 'Consultar', 'Editar/Excluir'])

if refGeoCrud == 'Cadastrar':
    Cadastrar.cadastrar()

if refGeoCrud == 'Consultar':
    Consultar.consultar()
    
if refGeoCrud == 'Editar/Excluir':
    ...