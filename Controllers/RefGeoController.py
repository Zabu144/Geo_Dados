# pylint: disable=all

import streamlit as st
import pandas as pd
import psycopg2
import io
import base64
import models.RefGeo as refGeo

def create_connection():
    connection = psycopg2.connect(
        database="geodb",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    return connection

def createRefGeo(refGeo):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO refGeo 
    (location_i,
    status,
    location_x,
    location_y,
    location_z,
    fase,
    banco,
    poligono) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", 
    (refGeo.location_i, refGeo.status, refGeo.location_x, refGeo.location_y, refGeo.location_z, refGeo.fase, refGeo.banco, refGeo.poligono))
    connection.commit()
    connection.close()



def SelecionarById(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * refGeo WHERE id = %s", id)
    refGeoList = []
    
    for row in cursor.fetchall():
        refGeoList.append(refGeo.RefGeo(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        
    return refGeoList


def updateRefGeo(refGeo):
    connection = create_connection()
    cursor = connection.cursor()
    print("Alterando...")
    count = cursor.execute("""
    UPDATE refGep
    SET location_i = %s,
    status = %s,
    location_x = %s,
    location_y = %s,
    location_z = %s,
    fase = %s,
    banco = %s,
    poligono = %s
    WHERE id = %s                
    """,
    refGeo.location_i, refGeo.status, refGeo.location_x, refGeo.location_y, refGeo.location_z, refGeo.fase, refGeo.banco, refGeo.poligono, refGeo.id).rowcount
    connection.commit()
    connection.close()
    

def readRefGeo():
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM refGeo")
    refGeoList = []
    
    for row in cursor.fetchall():
        refGeoList.append(refGeo.RefGeo(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
    
    return refGeoList