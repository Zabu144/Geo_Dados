# pylint: disable=all
import streamlit as st
import psycopg2
import services.database as db
import pandas as pd
import Controllers.RefGeoController as refGeoController

refGeoList = []

def consultar():
    refGeoList.clear()
    for item in refGeoController.readRefGeo():
        refGeoList.append([item.location_i, item.status, item.location_x, item.location_y, item.location_z, item.fase, item.banco, item.poligono])

    df = pd.DataFrame(
    refGeoList,
    columns=['Location_i', 'status', 'location_x', 'location_y', 'location_z', 'fase', 'banco', 'poligono'] 
    )

    st.data_editor(df)