# pylint: disable=all
import streamlit as st
import pandas as pd
import psycopg2
import io
import base64
import models.Geo as geo

def create_connection():
    connection = psycopg2.connect(
        database="geodb",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    return connection

def createGeo(geo):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO geo 
    (numOriginal,
    furo,
    geometalurgico,
    status,
    tipoMaterial,
    deCM,
    ateCM,
    profundidadePlanejada,
    alturaCone,
    profundidadeExecutada,
    presencaAgua,
    profundidadeAgua,
    tipoTerreno,
    deM,
    ateM,
    recuperacao,
    observacoes,
    data,
    turno,
    enviadoSGS) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
    (geo.numOriginal,
     geo.furo,
     geo.geometalurgico,
     geo.status,
     geo.tipoMaterial,
     geo.deCM,
     geo.ateCM,
     geo.profundidadePlanejada,
     geo.alturaCone,
     geo.profundidadeExecutada,
     geo.tipoTerreno,
     geo.deM,
     geo.ateM,
     geo.recuperacao,
     geo.observacoes,
     geo.data,
     geo.turno,
     geo.envadoSGS))
    connection.commit()
    connection.close()
    
def SelecionarById(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM geo WHERE id = %s", id)
    geoList = []
    
    for row in cursor.fetchall():
        geoList.append(geo.Geo(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], [18]))
        
    return geoList[0]

def deleteGeo(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM geo WHERE id = %s""", 
    (id))
    connection.commit()
    connection.close()
    
def updateGeo(geo):
    connection = create_connection()
    cursor = connection.cursor()
    print("Alterando...")
    count = cursor.execute("""
    UPDATE geo
    SET 
    numOriginal = %s,
    furo = %s,
    geometalurgico = %s,
    status = %s,
    tipoMaterial = %s,
    deCM = %s,
    ateCM = %s,
    profundidadePlanejada = %s,
    alturaCone = %s,
    profundidadeExecutada = %s,
    presencaAgua = %s,
    profundidadeAgua = %s,
    tipoTerreno = %s,
    deM = %s,
    ateM = %s,
    recuperacao = %s,
    observacoes = %s,
    data = %s,
    turno = %s,
    enviadoSGS = %s                
    """,
    (geo.numOriginal,
     geo.furo,
     geo.geometalurgico,
     geo.status,
     geo.tipoMaterial,
     geo.deCM,
     geo.ateCM,
     geo.profundidadePlanejada,
     geo.alturaCone,
     geo.profundidadeExecutada,
     geo.tipoTerreno,
     geo.deM,
     geo.ateM,
     geo.recuperacao,
     geo.observacoes,
     geo.data,
     geo.turno,
     geo.envadoSGS))
    connection.commit()
    connection.close()
    
    
def readGeo():
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM geo")
    geoList = []
    
    for row in cursor.fetchall():
        geoList.append(geo.Geo(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], [18]))
    
    return geoList


def exportToExcel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name="dados", index=False)
        
    output.seek(0)
    b64 = base64.b64encode(output.read()).decode()
    
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="Geo.xlsx">Geo.xlsx</a>'
    st.markdown(href, unsafe_allow_html=True)
    
    df.to_excel("Geo.xlsx", index=False)