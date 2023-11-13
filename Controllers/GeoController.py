# pylint: disable=all
import streamlit as st
import pandas as pd
import psycopg2
import io
import base64
import models.Geo as Geo

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