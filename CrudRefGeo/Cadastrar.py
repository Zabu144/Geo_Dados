# pylint: disable=all
import streamlit as st
import psycopg2
import services.database as db
import Controllers.RefGeoController as refGeoController
import models.RefGeo as refGeo

def cadastrar():
    db.create_table()
    st.title("Registro Tabela de referência")
    
    location_i = st.number_input("Location_I:", min_value=0, placeholder="0")
    
    status = st.selectbox(
        "Status:",
        ("Não Amostrar", "Executado"),
        index=None,
        placeholder="Selecione uma opção",
    )
    
    location_x = st.number_input("Location_X: ", placeholder="0.00")
    st.write('Número completo → ', location_x)
    
    location_y = st.number_input("location_Y: ", placeholder="0.00")
    st.write('Número completo → ', location_y)
    
    location_z = st.number_input("location_Z: ", placeholder="0.00")
    st.write('Número completo → ', location_z)
    
    fase = st.selectbox(
        "Fase:",
        ("F02", "F03", "F04", "F05"),
        index=None,
        placeholder="F0..."
    )
    
    banco = st.text_input("Banco: ")
    poligono = st.text_input("Poligono: ")
    
    if st.button("Cadastrar"):
        if location_i and status and location_x and location_y and location_z and fase and banco and poligono:
            refGeo.location_i = location_i
            refGeo.status = status
            refGeo.location_x = location_x
            refGeo.location_y = location_y
            refGeo.location_z = location_z
            refGeo.fase = fase
            refGeo.banco = banco
            refGeo.poligono = poligono
            
            refGeoController.createRefGeo(refGeo.RefGeo(0, location_i, status, location_x, location_y, location_z, fase, banco, poligono))
            st.success("Dados cadastrados com sucesso!")
        else:
            st.error("Preencha todos os campos!")