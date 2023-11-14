# pylint: disable=all
import streamlit as st
import psycopg2
import services.database as db
import Controllers.GeoController as geoController
import Controllers.RefGeoController as refGeoController
import models.Geo as geo
import csv
import pandas as pd
from io import StringIO

def cadastrar():
    idAlteracao = st.experimental_get_query_params()
    st.experimental_set_query_params()
    dadoRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        dadoRecuperado = geoController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id[dadoRecuperado.id]
        )
        st.title("Editar Tabela Geo")
        
    else:
        st.title("Registro Tabela Geo")
        
    db.create_table()
    
    listStatus = ["Amostrado", "Cancelado", "Planejado"]
    listTipoMaterial = ["Estéril", "Minério"]
    listTipoTerreno = ["Plano", "Irregular"]
    listTurno = ["A", "B", "C", "D"]
    
    if dadoRecuperado == None:
        numOriginal = st.number_input("Nº Original:", min_value=0, placeholder="0")
        
        refGeoValues = refGeoController.get_concatenated_values(2)
        if numOriginal:
            furo = f'{refGeoValues}-{numOriginal}'
        else:
            furo = ''
        
        furo = st.text_input('Furo: ', value=furo)
    