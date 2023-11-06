# pylint: disable=all
import streamlit as st
import psycopg2
import services.database as db

st.sidebar.title('Menu')
geoCrud = st.sidebar.selectbox('CRUD', ['Cadastrar', 'Consultar', 'Editar/Excluir'])

if geoCrud == 'Cadastrar':
  st.title("Registro de Geometalúrgico")
  
  
      
if geoCrud == 'Consultar':
  ...

if geoCrud == 'Editar/Excluir':
  ...

  

# refGeoCrud = st.sidebar.selectbox('Tabela Ref. Geo', ['Cadastrar', 'Consultar', 'Editar/Excluir'])

# if refGeoCrud == 'Cadastrar':
#     st.title("Regitro Tabela de referência")

# if refGeoCrud == 'Consultar':
#     ...
    
# if refGeoCrud == 'Editar/Excluir':
#     ...