# pylint: disable=all
import streamlit as st
import psycopg2
import services.database as db
import CrudGeo.Cadastrar as Cadastrar

st.sidebar.title('Menu')
geoCrud = st.sidebar.selectbox('CRUD', ['Cadastrar', 'Consultar', 'Editar/Excluir'])

if geoCrud == 'Cadastrar':
  st.experimental_set_query_params()
  Cadastrar.cadastrar()
  
if geoCrud == 'Consultar':
  ...

if geoCrud == 'Editar/Excluir':
  ...