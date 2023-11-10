# pylint: disable=all
import streamlit as st
import psycopg2
import services.database as db
import Controllers.RefGeoController as refGeoController
import models.RefGeo as refGeo
import csv
import pandas as pd
from io import StringIO

def cadastrar():
    idAlteracao = st.experimental_get_query_params()
    st.experimental_set_query_params()
    dadoRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        dadoRecuperado = refGeoController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[dadoRecuperado.id]
        )
        st.title("Editar Tabela de referência")
    
    else:
        st.title("Registro Tabela de referência")
        
        
    db.create_table()
    
    listStatus = ["Nao Amostrar", "Executado"]
    listFase = ["F02", "F03", "F04", "F05"]
    
    if dadoRecuperado == None:
        location_i = st.number_input("Location_I:", min_value=0, placeholder="0")
    
        status = st.selectbox(
            "Status:",
            listStatus,
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
            listFase,
            index=None,
            placeholder="F0..."
        )
        
        banco = st.text_input("Banco: ")
        poligono = st.text_input("Poligono: ")
    else:
        location_i = st.number_input("Location_I:", min_value=0, placeholder="0", value=dadoRecuperado.location_i)
    
        status = st.selectbox(
            "Status:",
            listStatus,
            index=listStatus.index(dadoRecuperado.status),
            placeholder="Selecione uma opção",
        )
        
        location_x = st.number_input("Location_X: ", placeholder="0.00", value= dadoRecuperado.location_x)
        st.write('Número completo → ', location_x)
        
        location_y = st.number_input("location_Y: ", placeholder="0.00", value= dadoRecuperado.location_y)
        st.write('Número completo → ', location_y)
        
        location_z = st.number_input("location_Z: ", placeholder="0.00", value= dadoRecuperado.location_z)
        st.write('Número completo → ', location_z)
        
        fase = st.selectbox(
            "Fase:",
            listFase,
            index=listFase.index(dadoRecuperado.fase),
            placeholder="F0...",
        )
        
        banco = st.text_input("Banco: ", value= dadoRecuperado.banco)
        poligono = st.text_input("Poligono: ", value= dadoRecuperado.poligono)
    
    
    if st.button("Cadastrar"):
        if dadoRecuperado == None:
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
        else:
            if location_i and status and location_x and location_y and location_z and fase and banco and poligono:
                refGeo.location_i = location_i
                refGeo.status = status
                refGeo.location_x = location_x
                refGeo.location_y = location_y
                refGeo.location_z = location_z
                refGeo.fase = fase
                refGeo.banco = banco
                refGeo.poligono = poligono
                
                st.experimental_set_query_params()
                refGeoController.updateRefGeo(refGeo.RefGeo(dadoRecuperado.id ,location_i, status, location_x, location_y, location_z, fase, banco, poligono))
                st.success("Dados alterados com sucesso!")
            else:
                st.error("Preencha todos os campos!")
                
    uploaded_file = st.file_uploader("Selecione um arquivo CSV", type="csv")
    if st.button("Importar CSV"):
        if uploaded_file is not None:
           
            df = pd.read_csv(uploaded_file, sep=';')
            st.write(df)
            
            print(df.info())
            df['location_x'].to_string()
            df['location_y'].to_string()
            df['location_z'].to_string()
            
            connection = db.create_connection()
            cursor = connection.cursor()

            for index, row in df.iterrows():
                print(row)
                location_i = int(row["location_i"])
                status = row["status"]
                location_x = float(row["location_x"].replace('.', ''))
                location_y = float(row["location_y"].replace('.', ''))
                location_z = float(row["location_z"].replace('.', ''))
                fase = row["fase"]
                banco = row["banco"]
                poligono = row["poligono"]

                cursor.execute("""
                    INSERT INTO refGeo (location_i, status, location_x, location_y, location_z, fase, banco, poligono)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (location_i, status, location_x, location_y, location_z, fase, banco, poligono))
            connection.commit()
            connection.close()

            st.success("Dados importados com sucesso!")