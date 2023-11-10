# pylint: disable=all
import psycopg2

def create_connection():
  connection = psycopg2.connect(
    database="geodb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
  )
  return connection

def create_table():
  connection = create_connection()
  cursor = connection.cursor()
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS geo (
    id SERIAL PRIMARY KEY,
    numOriginal INTEGER NOT NULL,
    furo VARCHAR(25) NOT NULL,
    geometalurgico BOOLEAN,
    status VARCHAR(20) NOT NULL,
    tipoMaterial VARCHAR(20) NOT NULL
  );
  
  CREATE TABLE IF NOT EXISTS refGeo (
    id SERIAL PRIMARY KEY,
    location_i INTEGER NOT NULL,
    status VARCHAR(20) NOT NULL,
    location_x DOUBLE PRECISION,
    location_y DOUBLE PRECISION,
    location_z DOUBLE PRECISION,
    fase VARCHAR(10) NOT NULL,
    banco VARCHAR(10) NOT NULL,
    poligono VARCHAR(20) NOT NULL
  )
                 """)
  connection.commit()
  connection.close()
  