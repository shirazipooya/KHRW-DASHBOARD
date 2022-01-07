import pandas as pd
import geopandas as gpd

import psycopg2
from sqlalchemy import *
from geoalchemy2 import Geometry, WKTElement


# Connect to layers DataBase
db_layers_url = "postgresql://postgres:1234@127.0.0.1:5432/layers"
engine = create_engine(db_layers_url, echo=False)


# # Enable PostGIS --------------------------------------------------------------
# conn = psycopg2.connect(
#    database="postgres",
#    user='postgres',
#    password='1333',
#    host='127.0.0.1',
#    port= '5432'
# )

# conn.autocommit = True

# cursor = conn.cursor()

# cursor.execute("CREATE EXTENSION postgis;")

# conn.close()
# # -----------------------------------------------------------------------------

# Load Layers:

# Wells:
wells = gpd.read_file('./Assets/GeoDatabase/GeoJson/Wells.geojson')
wells = wells.to_crs({'init': 'epsg:4326'})
COLs = ['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME']
wells[COLs] = wells[COLs].apply(lambda x: x.str.replace('ي','ی'))
wells[COLs] = wells[COLs].apply(lambda x: x.str.replace('ئ','ی'))
wells[COLs] = wells[COLs].apply(lambda x: x.str.replace('ك', 'ک'))

# Aquifers:
aquifers = gpd.read_file('./Assets/GeoDatabase/GeoJson/Aquifers.geojson')
aquifers = aquifers.to_crs({'init': 'epsg:4326'})
COLs = ['MAHDOUDE_NAME', 'AQUIFER_NAME']
aquifers[COLs] = aquifers[COLs].apply(lambda x: x.str.replace('ي','ی'))
aquifers[COLs] = aquifers[COLs].apply(lambda x: x.str.replace('ئ','ی'))
aquifers[COLs] = aquifers[COLs].apply(lambda x: x.str.replace('ك', 'ک'))

wells['geometry'] = wells['geometry'].apply(lambda x: WKTElement(x.wkt, srid = 4326))
aquifers['geometry'] = aquifers['geometry'].apply(lambda x: WKTElement(x.wkt, srid = 4326))




# Save to DataBase:

# Wells
wells.to_sql(
    'wells',
    engine,
    if_exists='replace',
    index=False,
    dtype={'geometry': Geometry(geometry_type='POINT', srid= 4326)}
)

# Aquifers
aquifers.to_sql(
    'aquifers',
    engine,
    if_exists='replace',
    index=False,
    dtype={'geometry': Geometry(geometry_type='MULTIPOLYGON', srid= 4326)}
)


# # -----------------------------------------------------------------------------
# # Create Servers and DataBase
# conn = psycopg2.connect(
#    database="postgres",
#    user='postgres',
#    password='1333',
#    host='127.0.0.1',
#    port= '5432'
# )

# conn.autocommit = True

# cursor = conn.cursor()

# sql = '''CREATE DATABASE layers''';

# cursor.execute(sql)

# print("Database layers Created Successfully........")

# conn.close()
# # -----------------------------------------------------------------------------

