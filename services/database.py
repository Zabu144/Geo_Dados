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
  CREATE TABLE IF NOT EXISTS dados (
    id SERIAL PRIMARY KEY,
    numOriginal INTEGER NOT NULL,
    furo VARCHAR(25) NOT NULL,
    geometalurgico BOOLEAN,
    status VARCHAR(20) NOT NULL,
    tipoMaterial VARCHAR(20) NOT NULL
  );
  
  CREATE TABLE IF NOT EXISTS ref_furos (
    id SERIAL PRIMARY KEY,
    location_i INTERGER NOT NULL,
    status VARCHAR(20) NOT NULL,
    location_x VARCHAR(25),
    location_y VARCHAR(25),
    length VARCHAR(25),
    fase VARCHAR(3) NOT NULL,
    banco VARCHAR(3) NOT NULL,
    poligono VARCHAR(8) NOT NULL
  )
                 """)
  connection.commit()
  connection.close()
  