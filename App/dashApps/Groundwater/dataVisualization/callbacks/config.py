import base64
import io
import string
import re
import pandas as pd
import numpy as np
import geopandas as gpd
from itertools import compress
# from srtm import Srtm1HeightMapCollection
import statistics
import Assets.jalali as jalali
import json
import sqlite3
from dash.dependencies import Input, Output, State

import dash_leaflet.express as dlx
import geojson

import plotly.graph_objects as go
import plotly.express as px

from dash import html
from dash import dcc
from dash import dash_table

import psycopg2
from sqlalchemy import *

# -----------------------------------------------------------------------------
# MAPBOX TOKEN
# -----------------------------------------------------------------------------
PATH_MAPBOX_TOKEN = "./Assets/Files/.mapbox_token"
MAPBOX_TOKEN = open(PATH_MAPBOX_TOKEN).read()


# -----------------------------------------------------------------------------
# DATABASE
# -----------------------------------------------------------------------------
PATH_DB_GROUNDWATER = './Assets/Database/groundwater.db'
DB_GROUNDWATER = sqlite3.connect(PATH_DB_GROUNDWATER, check_same_thread=False)



# Load GeoDatabase
# -----------------------------------------------------------------------------
url_db_layers = "postgresql://postgres:1333@127.0.0.1:5432/layers"
engine_db_layers = create_engine(url_db_layers, echo=False)

url_db_hydrograph = "postgresql://postgres:1333@127.0.0.1:5432/hydrograph"
engine_db_hydrograph = create_engine(url_db_hydrograph, echo=False)

def read_data_from_postgis(table, engine, geom_col='geometry', modify_cols=None):
    sql = f"select * from {table}"
    df = gpd.GeoDataFrame.from_postgis(sql, engine, geom_col=geom_col)
    if modify_cols is not None:
        df[modify_cols] = df[modify_cols].apply(lambda x: x.str.rstrip())
        df[modify_cols] = df[modify_cols].apply(lambda x: x.str.lstrip())
        df[modify_cols] = df[modify_cols].apply(lambda x: x.str.replace('ي','ی'))
        df[modify_cols] = df[modify_cols].apply(lambda x: x.str.replace('ئ','ی'))
        df[modify_cols] = df[modify_cols].apply(lambda x: x.str.replace('ك', 'ک'))
    return df



# -----------------------------------------------------------------------------
# NO MATCHING DATA FOUND TEMPLATE
# -----------------------------------------------------------------------------

NO_MATCHING_DATA_FOUND = {
    "layout": {
        "xaxis": {"visible": False},
        "yaxis": {"visible": False},
        "annotations": [
            {
                "text": "No Data Found ...",
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": {"size": 36}
            }
        ]
    }
}

NO_MATCHING_MAP_FOUND = {
    "layout": {
        "xaxis": {"visible": False},
        "yaxis": {"visible": False},
        "annotations": [
            {
                "text": "No Map Found ...",
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": {"size": 36}
            }
        ]
    }
}

NO_MATCHING_GRAPH_FOUND = {
    "layout": {
        "xaxis": {"visible": False},
        "yaxis": {"visible": False},
        "annotations": [
            {
                "text": "No Graph Found ...",
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": {"size": 36}
            }
        ]
    }
}



# -----------------------------------------------------------------------------
# BASE MAP
# -----------------------------------------------------------------------------
BASE_MAP = go.Figure(
    go.Scattermapbox(
        lat=[36.25],
        lon=[59.55],
        mode='markers',
        marker=go.scattermapbox.Marker(size=9),
        text="شهر مشهد"
    )
)

BASE_MAP.update_layout(
    mapbox={
        'style': "stamen-terrain",
        'center': {
            'lon': 59.55,
            'lat': 36.25
        },
        'zoom': 5.5
    },
    showlegend=False,
    hovermode='closest',
    margin={'l':0, 'r':0, 'b':0, 't':0},
    autosize=False
)



# -----------------------------------------------------------------------------
# GEOJSON LOCATION
# -----------------------------------------------------------------------------
# GEOJSON_LOCATION = {
#     "COUNTRY" : {
#         "url": "./Assets/GeoJson/Country.geojson",
#         "data": dlx.geojson_to_geobuf(geojson.load(open("./Assets/GeoDatabase/GeoJson/Country.geojson"))),
#         "options": {
#             "weight": "1",
#             # "dashArray": "10, 10",
#             # "dashOffset": "10",
#             "color": "black",
#             "opacity": "1",
#             "fillColor": "black",
#             "fillOpacity": "0.01",
#         }
#     },
#     "PROVINCE" : {
#         "url": "./Assets/GeoJson/Province.geojson",
#         "data": dlx.geojson_to_geobuf(geojson.load(open("./Assets/GeoDatabase/GeoJson/Province.geojson"))),
#         "options": {
#             "weight": "1",
#             # "dashArray": "10, 10",
#             # "dashOffset": "10",
#             "color": "black",
#             "opacity": "1",
#             "fillColor": "black",
#             "fillOpacity": "0.01",
#         }
#     },
#     "COUNTY" : {
#         "url": "./Assets/GeoJson/County.geojson",
#         "data": dlx.geojson_to_geobuf(geojson.load(open("./Assets/GeoDatabase/GeoJson/County.geojson"))),
#         "options": {
#             "weight": "1",
#             # "dashArray": "10, 10",
#             # "dashOffset": "10",
#             "color": "black",
#             "opacity": "1",
#             "fillColor": "black",
#             "fillOpacity": "0.01",
#         }
#     },
#     "DISTRICT" : {
#         "url": "./Assets/GeoJson/District.geojson",
#         "data": dlx.geojson_to_geobuf(geojson.load(open("./Assets/GeoDatabase/GeoJson/District.geojson"))),
#         "options": {
#             "weight": "1",
#             # "dashArray": "10, 10",
#             # "dashOffset": "10",
#             "color": "black",
#             "opacity": "1",
#             "fillColor": "black",
#             "fillOpacity": "0.01",
#         }
#     },
#     "BASIN1" : {
#         "url": "./Assets/GeoJson/Basin1.geojson",
#         "data": dlx.geojson_to_geobuf(geojson.load(open("./Assets/GeoDatabase/GeoJson/Basin1.geojson"))),
#         "options": {
#             "weight": "5",
#             # "dashArray": "10, 10",
#             # "dashOffset": "10",
#             "color": "blue",
#             "opacity": "1",
#             "fillColor": "blue",
#             "fillOpacity": "0.01",
#         }
#     },
#     "BASIN2" : {
#         "url": "./Assets/GeoJson/Basin2.geojson",
#         "data": dlx.geojson_to_geobuf(geojson.load(open("./Assets/GeoDatabase/GeoJson/Basin2.geojson"))),
#         "options": {
#             "weight": "5",
#             # "dashArray": "10, 10",
#             # "dashOffset": "10",
#             "color": "blue",
#             "opacity": "1",
#             "fillColor": "blue",
#             "fillOpacity": "0.01",
#         }
#     },
#     "MAHDOUDE" : {
#         "url": "./Assets/GeoJson/Mahdoude.geojson",
#         "data": dlx.geojson_to_geobuf(geojson.load(open("./Assets/GeoDatabase/GeoJson/Mahdoude.geojson"))),
#         "options": {
#             "weight": "5",
#             # "dashArray": "10, 10",
#             # "dashOffset": "10",
#             "color": "blue",
#             "opacity": "1",
#             "fillColor": "blue",
#             "fillOpacity": "0.01",
#         }
#     },
#     "AQUIFER" : {
#         "url": "./Assets/GeoJson/Aquifer.geojson",
#         "data": dlx.geojson_to_geobuf(geojson.load(open("./Assets/GeoDatabase/GeoJson/Aquifer.geojson"))),
#         "options": {
#             "weight": "5",
#             # "dashArray": "10, 10",
#             # "dashOffset": "10",
#             "color": "blue",
#             "opacity": "1",
#             "fillColor": "blue",
#             "fillOpacity": "0.01",
#         }
#     }
# }



# -----------------------------------------------------------------------------
# IMAGE LOCATION
# -----------------------------------------------------------------------------

# ATTRIBUTION
ATTRIBUTION = '&copy; <a href="http://www.khrw.ir/">Khorasan Regional Water Company</a>'


# BASE MAP SELECTED STYLE
BASE_MAP_SELECTED_STYLE = {
    "background-color": "#337ab7",
    "color":"#fff"
}


# NONE BASE MAP
NONEBASEMAP = base64.b64encode(
    open("./App/static/images/base_map/None.png", 'rb').read()
).decode()

NONEBASEMAP_URL = ""


# IMAGERY BASE MAP
IMAGERY = base64.b64encode(
    open("./App/static/images/base_map/Imagery.png", 'rb').read()
).decode()

IMAGERY_URL = "http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}"


# OPEN STREET MAP
STREETS = base64.b64encode(
    open("./App/static/images/base_map/Streets.png", 'rb').read()
).decode()

STREETS_URL = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"


# TERRAIN BASE MAP
TERRAIN = base64.b64encode(
    open("./App/static/images/base_map/Terrain.png", 'rb').read()
).decode()

TERRAIN_URL = "https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png"


# TOPOGRAPHIC BASE MAP
TOPOGRAPHIC = base64.b64encode(
    open("./App/static/images/base_map/Topographic.png", 'rb').read()
).decode()

TOPOGRAPHIC_URL = 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png'


# DARK BASE MAP
DARK = base64.b64encode(
    open("./App/static/images/base_map/Dark.png", 'rb').read()
).decode()

DARK_URL = 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png'

# KHRW LOGO
KHRW_LOGO = base64.b64encode(
    open("./App/static/images/logo/Khrw_Logo.png", 'rb').read()
).decode()

# DATABASE LOGO
DATABASE_LOGO = base64.b64encode(
    open("./App/static/images/logo/Database_Logo.png", 'rb').read()
).decode()

# DATA CLEANSING LOGO
DATACLEANSING_LOGO = base64.b64encode(
    open("./App/static/images/logo/DataCleansing_Logo.png", 'rb').read()
).decode()

# DATABASE CONNECTION LOGO
DATABASE_CONNECTION_LOGO = base64.b64encode(
    open("./App/static/images/logo/Database_Connection_Logo.png", 'rb').read()
).decode()

# CALCULATE LOGO
CALCULATE_LOGO = base64.b64encode(
    open("./App/static/images/logo/Calculate_Logo.png", 'rb').read()
).decode()

# MENU LOGO
MENU_LOGO = base64.b64encode(
    open("./App/static/images/logo/Menu.png", 'rb').read()
).decode()





# -----------------------------------------------------------------------------
# WATER YEAR - DIFF - CUMSUM
# -----------------------------------------------------------------------------
# Column 1: Persian Year (YYYY) - سال
# Column 2: Persian Month (MM) - ماه
# Column 3: Value -پارامتر

def waterYear(df):
    if df["ماه"] >= 7 and df["ماه"] <= 12:
        WY = str(int(df["سال"])) + "-" + str(int(df["سال"]) + 1)[2:4]
        WM = int(df["ماه"]) - 6
    elif df["ماه"] >= 1 and df["ماه"] <= 6:
        WY = str(int(df["سال"]) - 1) + "-" + str(int(df["سال"]))[2:4]
        WM = int(df["ماه"]) + 6
    else:
        WY = None
        WM = None
    return [WY, WM]


def resultTable(df):
    df["پارامتر"] = df["پارامتر"].round(2)    
    df["WATER_YEAR"] = df.apply(waterYear, axis=1)
    df[['سال آبی','ماه آبی']] = pd.DataFrame(df.WATER_YEAR.tolist(), index= df.index)
    df.drop('WATER_YEAR', inplace=True, axis=1)
    df = df.sort_values(['سال', 'ماه'])
    df["اختلاف ماه"] = df["پارامتر"].diff()
    df["اختلاف ماه"] = df["اختلاف ماه"].round(2)
    df = df.sort_values(['ماه', 'سال'])
    result = pd.DataFrame()
    for m in range(1,13):
        d = df[df["ماه"] == m]
        d["اختلاف ماه سال"] = d["پارامتر"].diff()
        result = pd.concat([result, d])
    result = result.sort_values(['سال', 'ماه'])
    print(result)
    result["اختلاف ماه سال"] = result["اختلاف ماه سال"].round(2)
    
    return result

def resultTableAquifer(df):
    df["هد"] = df["هد"].round(2)   
    df["مساحت"] = df["مساحت"].round(2)   
    df["ضریب"] = df["ضریب"].round(2)
    df["WATER_YEAR"] = df.apply(waterYear, axis=1)
    df[['سال آبی','ماه آبی']] = pd.DataFrame(df.WATER_YEAR.tolist(), index= df.index)
    df.drop('WATER_YEAR', inplace=True, axis=1)
    df["اختلاف ماه"] = df["هد"].diff()
    df["اختلاف ماه"] = df["اختلاف ماه"].round(2)
    
    df = df.sort_values(['ماه', 'سال'])
    result = pd.DataFrame()
    for m in range(1,13):
        d = df[df["ماه"] == m]
        d["اختلاف ماه سال"] = d["هد"].diff()
        result = pd.concat([result, d])
    result = result.sort_values(['سال', 'ماه'])
    result["اختلاف ماه سال"] = result["اختلاف ماه سال"].round(2)
    
    return result