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


import pandas as pd

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


# -----------------------------------------------------------------------------
# ALL ENGLISH CHARECTER
# -----------------------------------------------------------------------------
EN_CHAR = list(string.ascii_lowercase) +\
    list(string.ascii_uppercase) +\
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_"]



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


# table_name = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", db)


# try:
#     if table_name['name'].str.contains('RawDATA').any():
#         RawDATA = pd.read_sql_query(sql="SELECT * FROM RawDATA", con=db)
#         GeoInfoData = extract_geo_info_dataset(RawDATA)
#     else:
#         print("ERROR: RawDATA TABLE NOT EXIST")
# except:
#     print("ERROR: DATABASE NOT EXIST")

# try:
#     if table_name['name'].str.contains('AquiferDATA').any():
#         AquiferDATA = pd.read_sql_query(sql="SELECT * FROM AquiferDATA", con=db)
#     else:
#         print("ERROR: AquiferDATA TABLE NOT EXIST")
# except:
#     print("ERROR: DATABASE NOT EXIST")


# -----------------------------------------------------------------------------
# COLUMNS "HydrographDataSample.xlsx"
# -----------------------------------------------------------------------------
HydrographDataSample = pd.ExcelFile('./Assets/Files/Groundwater/HydrographData_Template.xlsx')
HydrographDataSample_DataColumns = pd.read_excel(HydrographDataSample, sheet_name='Data').columns
HydrographDataSample_GeoInfoColumns = pd.read_excel(HydrographDataSample, sheet_name='GeoInfo').columns



# -----------------------------------------------------------------------------
# CONVERT TO DAY 15
# -----------------------------------------------------------------------------
def convert_to_day_15(data, method, date_type="persian"):
    
    data = data.reset_index(drop=True)
            
    df = data[["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME"]]
    
    if date_type == "gregorian":
        df["DATE_GREGORIAN"] = data.DATE_GREGORIAN_RAW.apply(pd.to_datetime)
        df["DATE_PERSIAN"] = list(
            map(
                lambda i: jalali.Gregorian(i.date()).persian_string(),
                df["DATE_GREGORIAN"]
            )
        )
        
    elif date_type == "persian":
        df["DATE_PERSIAN"] = data.DATE_PERSIAN_RAW
        df["DATE_GREGORIAN"] = list(
            map(
                lambda i: jalali.Persian(i).gregorian_string(),
                df["DATE_PERSIAN"]
            )
        )
        df["DATE_GREGORIAN"] = df["DATE_GREGORIAN"].apply(pd.to_datetime)
        
    else:
        pass
    
    df["VALUE"] = data.WATER_TABLE_MODIFY 

    df["DELTA_DAY"] = df["DATE_GREGORIAN"].diff().dt.days
    
    df["DATE_PERSIAN_NEW"] = list(
        map(
            lambda i: f"{int(i.split('-')[0])}-{int(i.split('-')[1])}-{method}",
            df["DATE_PERSIAN"]
        )
    )
    
    df["DATE_GREGORIAN_NEW"] = list(
        map(
            lambda i: jalali.Persian(i).gregorian_string(),
            df["DATE_PERSIAN_NEW"]
        )
    )
    
    df["DATE_GREGORIAN_NEW"] = df["DATE_GREGORIAN_NEW"].apply(pd.to_datetime)
    
    df["VALUE_NEW"] = df["VALUE"]
    
    A = []
    
    A.append(df["VALUE"][0])
    
    for i in range(1, len(df) - 1):
        if int(df["DATE_PERSIAN"][i].split('-')[2]) >= method:
            NEW_VALUE = df["VALUE"][i-1] + ((((df["DATE_GREGORIAN_NEW"][i] - df["DATE_GREGORIAN"][i-1]).days) / ((df["DATE_GREGORIAN"][i] - df["DATE_GREGORIAN"][i-1]).days)) * (df["VALUE"][i] - df["VALUE"][i-1]))
            A.append(NEW_VALUE)
        else:
            NEW_VALUE = df["VALUE"][i] + ((((df["DATE_GREGORIAN_NEW"][i] - df["DATE_GREGORIAN"][i]).days) / ((df["DATE_GREGORIAN"][i+1] - df["DATE_GREGORIAN"][i]).days)) * (df["VALUE"][i+1] - df["VALUE"][i]))
            A.append(NEW_VALUE)
    
    A.append(df["VALUE"][len(df) - 1])
            
    df["VALUE_NEW"] = A
        
    return df

# # -----------------------------------------------------------------------------
# # Gap Filling
# # -----------------------------------------------------------------------------
# def create_date_day15(min, max):
#     """[summary]

#     Args:
#         min ([type]): [description]
#         max ([type]): [description]

#     Returns:
#         [type]: [description]
#     """
#     result = []
#     min_list = list(map(lambda x: int(x), min.split("-")))
#     max_list = list(map(lambda x: int(x), max.split("-")))
#     for y in range(min_list[0], max_list[0] + 1):
#         for m in range(1, 13):
#             result.append(f"{y}-{m}-15")

#     result = pd.DataFrame(
#         {"DATE_PERSIAN" : result}
#     )
#     result['DATE_GREGORIAN'] = result.apply(
#         lambda x: jalali.Persian(x["DATE_PERSIAN"]).gregorian_string(), 
#         axis=1
#     )
#     result["DATE_GREGORIAN"] = result["DATE_GREGORIAN"].apply(pd.to_datetime)
#     result = result[result["DATE_GREGORIAN"] >= pd.to_datetime(jalali.Persian(min).gregorian_string())]
#     result = result[result["DATE_GREGORIAN"] <= pd.to_datetime(jalali.Persian(max).gregorian_string())]
#     result["DATE_GREGORIAN"] = result["DATE_GREGORIAN"].apply(pd.to_datetime)  
#     return result


# -----------------------------------------------------------------------------
# GEOINFO TABLE
# -----------------------------------------------------------------------------
def create___geoinfo_table___spreadsheet_database(
    data,
    con,
    name,
    column,
    if_exists
):
    data = data[column]
    COLs = ['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME']
    data[COLs] = data[COLs].apply(lambda x: x.str.rstrip())
    data[COLs] = data[COLs].apply(lambda x: x.str.lstrip())
    data[COLs] = data[COLs].apply(lambda x: x.str.replace('ي','ی'))
    data[COLs] = data[COLs].apply(lambda x: x.str.replace('ئ','ی'))
    data[COLs] = data[COLs].apply(lambda x: x.str.replace('ك', 'ک'))
    
    data.to_sql(
        name=name,
        con=con,
        if_exists=if_exists
    )
    

# -----------------------------------------------------------------------------
# GROUNDWATER RAW DATA TABLE
# -----------------------------------------------------------------------------
def create___groundwater_raw_data_table___spreadsheet_database(
    data,
    con,
    raw_table_name,
    cleansing_table_name,
    interpolated_table_name,
    syncdate_table_name,
    column,
    date_type,
    if_exists,
):
    data = data[column]
    COLs = ['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME']
    data[COLs] = data[COLs].apply(lambda x: x.str.rstrip())
    data[COLs] = data[COLs].apply(lambda x: x.str.lstrip())
    data[COLs] = data[COLs].apply(lambda x: x.str.replace('ي','ی'))
    data[COLs] = data[COLs].apply(lambda x: x.str.replace('ئ','ی'))
    data[COLs] = data[COLs].apply(lambda x: x.str.replace('ك', 'ک'))

    
    # Convert Date
    # ---------------------------------
    if date_type == "persian_ymd":
        data["YEAR_PERSIAN"] = data["YEAR_PERSIAN"].astype(str).str.zfill(4)
        data["MONTH_PERSIAN"] = data["MONTH_PERSIAN"].astype(str).str.zfill(2)
        data["DAY_PERSIAN"] = data["DAY_PERSIAN"].astype(str).str.zfill(2)
        data['DATE_PERSIAN'] = data["YEAR_PERSIAN"] + "-" + data["MONTH_PERSIAN"] + "-" + data["DAY_PERSIAN"]
        data['DATE_GREGORIAN'] = data.apply(
            lambda x: jalali.Persian(x["DATE_PERSIAN"]).gregorian_string(), 
            axis=1
        )
        data[['YEAR_GREGORIAN', 'MONTH_GREGORIAN', 'DAY_GREGORIAN']] = data['DATE_GREGORIAN'].str.split('-', 2, expand=True)
        data["YEAR_GREGORIAN"] = data["YEAR_GREGORIAN"].str.zfill(4)
        data["MONTH_GREGORIAN"] = data["MONTH_GREGORIAN"].str.zfill(2)
        data["DAY_GREGORIAN"] = data["DAY_GREGORIAN"].str.zfill(2)
        data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
        
    elif date_type == "gregorian_ymd":
        data["YEAR_GREGORIAN"] = data["YEAR_GREGORIAN"].astype(str).str.zfill(4)
        data["MONTH_GREGORIAN"] = data["MONTH_GREGORIAN"].astype(str).str.zfill(2)
        data["DAY_GREGORIAN"] = data["DAY_GREGORIAN"].astype(str).str.zfill(2)
        data['DATE_GREGORIAN'] = data["YEAR_GREGORIAN"] + "-" + data["MONTH_GREGORIAN"] + "-" + data["DAY_GREGORIAN"]
        data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
        data['DATE_PERSIAN'] = data.apply(
            lambda x: jalali.Gregorian(x["DATE_GREGORIAN"].date()).persian_string(), 
            axis=1
        )
        data[['YEAR_PERSIAN', 'MONTH_PERSIAN', 'DAY_PERSIAN']] = data['DATE_PERSIAN'].str.split('-', 2, expand=True)
        data["YEAR_PERSIAN"] = data["YEAR_PERSIAN"].str.zfill(4)
        data["MONTH_PERSIAN"] = data["MONTH_PERSIAN"].str.zfill(2)
        data["DAY_PERSIAN"] = data["DAY_PERSIAN"].str.zfill(2)
    
    elif date_type == "persian_date":
        data[['YEAR_PERSIAN', 'MONTH_PERSIAN', 'DAY_PERSIAN']] = data['DATE_PERSIAN'].str.split('-', 2, expand=True)
        data["YEAR_PERSIAN"] = data["YEAR_PERSIAN"].str.zfill(4)
        data["MONTH_PERSIAN"] = data["MONTH_PERSIAN"].str.zfill(2)
        data["DAY_PERSIAN"] = data["DAY_PERSIAN"].str.zfill(2)
        data['DATE_PERSIAN'] = data["YEAR_PERSIAN"] + "-" + data["MONTH_PERSIAN"] + "-" + data["DAY_PERSIAN"]
        data['DATE_GREGORIAN'] = data.apply(
            lambda x: jalali.Persian(x["DATE_PERSIAN"]).gregorian_string(), 
            axis=1
        )
        data[['YEAR_GREGORIAN', 'MONTH_GREGORIAN', 'DAY_GREGORIAN']] = data['DATE_GREGORIAN'].str.split('-', 2, expand=True)
        data["YEAR_GREGORIAN"] = data["YEAR_GREGORIAN"].str.zfill(4)
        data["MONTH_GREGORIAN"] = data["MONTH_GREGORIAN"].str.zfill(2)
        data["DAY_GREGORIAN"] = data["DAY_GREGORIAN"].str.zfill(2)
        data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
    
    elif date_type == "gregorian_date":
        data[['YEAR_GREGORIAN', 'MONTH_GREGORIAN', 'DAY_GREGORIAN']] = data['DATE_GREGORIAN'].str.split('-', 2, expand=True)
        data["YEAR_GREGORIAN"] = data["YEAR_GREGORIAN"].str.zfill(4)
        data["MONTH_GREGORIAN"] = data["MONTH_GREGORIAN"].str.zfill(2)
        data["DAY_GREGORIAN"] = data["DAY_GREGORIAN"].str.zfill(2)
        data['DATE_GREGORIAN'] = data["YEAR_GREGORIAN"] + "-" + data["MONTH_GREGORIAN"] + "-" + data["DAY_GREGORIAN"]
        data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
        data['DATE_PERSIAN'] = data.apply(
            lambda x: jalali.Gregorian(x["DATE_GREGORIAN"].date()).persian_string(), 
            axis=1
        )
        data[['YEAR_PERSIAN', 'MONTH_PERSIAN', 'DAY_PERSIAN']] = data['DATE_PERSIAN'].str.split('-', 2, expand=True)
        data["YEAR_PERSIAN"] = data["YEAR_PERSIAN"].str.zfill(4)
        data["MONTH_PERSIAN"] = data["MONTH_PERSIAN"].str.zfill(2)
        data["DAY_PERSIAN"] = data["DAY_PERSIAN"].str.zfill(2)
    else:
        pass
    
    data.sort_values(
        by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"], 
        inplace=True
    )

    data = data.sort_values(
        by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
    ).reset_index(drop=True)  

    data.to_sql(
        name=raw_table_name,
        con=con,
        if_exists=if_exists
    )
    
    data.to_sql(
        name=cleansing_table_name,
        con=con,
        if_exists=if_exists
    )
    
    data["WATER_TABLE"] = np.nan
    
    data.to_sql(
        name=interpolated_table_name,
        con=con,
        if_exists=if_exists
    )

    data["DATE_GREGORIAN_RAW"] = data["DATE_GREGORIAN"]
    
    data.to_sql(
        name=syncdate_table_name,
        con=con,
        if_exists=if_exists
    )


def f_interpolate(x, method, order, limit):
    
    persian_date_min = x["DATE_PERSIAN"].min().split("-")
    persian_date_max = x["DATE_PERSIAN"].max().split("-")
    
    year = list(range(int(persian_date_min[0]), int(persian_date_max[0]) + 1))
    month = list(range(1, 13))
    
    dt = pd.DataFrame(
        {
            "YEAR_PERSIAN": np.repeat(year, 12, axis=0),
            "MONTH_PERSIAN": month * len(year)
        }
    )
    
    dt["YEAR_PERSIAN"] = dt["YEAR_PERSIAN"].astype(str).str.zfill(4)
    dt["MONTH_PERSIAN"] = dt["MONTH_PERSIAN"].astype(str).str.zfill(2)
    
    x = pd.merge(left=x, right=dt, on=["YEAR_PERSIAN", "MONTH_PERSIAN"], how="outer").reset_index(drop=True)
    

    
    x["MAHDOUDE_NAME"] = x["MAHDOUDE_NAME"].interpolate(method="pad")
    x["AQUIFER_NAME"] = x["AQUIFER_NAME"].interpolate(method="pad")
    x["LOCATION_NAME"] = x["LOCATION_NAME"].interpolate(method="pad")
    x["DAY_PERSIAN"] = x["DAY_PERSIAN"].interpolate(method="pad")
    
    x["YEAR_PERSIAN"] = x["YEAR_PERSIAN"].astype(str).str.zfill(4)
    x["MONTH_PERSIAN"] = x["MONTH_PERSIAN"].astype(str).str.zfill(2)
    x["DAY_PERSIAN"] = x["DAY_PERSIAN"].astype(str).str.zfill(2)
    x['DATE_PERSIAN'] = x["YEAR_PERSIAN"] + "-" + x["MONTH_PERSIAN"] + "-" + x["DAY_PERSIAN"]
    x['DATE_GREGORIAN'] = x.apply(
        lambda x: jalali.Persian(x["DATE_PERSIAN"]).gregorian_string(), 
        axis=1
    )
    x[['YEAR_GREGORIAN', 'MONTH_GREGORIAN', 'DAY_GREGORIAN']] = x['DATE_GREGORIAN'].str.split('-', 2, expand=True)
    x["YEAR_GREGORIAN"] = x["YEAR_GREGORIAN"].str.zfill(4)
    x["MONTH_GREGORIAN"] = x["MONTH_GREGORIAN"].str.zfill(2)
    x["DAY_GREGORIAN"] = x["DAY_GREGORIAN"].str.zfill(2)
    x["DATE_GREGORIAN"] = x["DATE_GREGORIAN"].apply(pd.to_datetime)
    
    x = x.sort_values(
        by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DAY_PERSIAN"]
    ).reset_index(drop=True) 

    
    if method in ["polynomial", "spline"]:
        try:
            if limit == 0:
                x["WATER_TABLE"] = x["WATER_TABLE"].interpolate(method=method, order=order)
            else:
                x["WATER_TABLE"] = x["WATER_TABLE"].interpolate(method=method, order=order, limit=limit)
        except:
            pass
    else:
        try:
            if limit == 0:
                x["WATER_TABLE"] = x["WATER_TABLE"].interpolate(method=method)
            else:
                x["WATER_TABLE"] = x["WATER_TABLE"].interpolate(method=method, limit=limit)
        except:
            pass
    
    return x



def f_syncdate(x, method):
    
    try:   
        x = x.drop_duplicates(
            subset=['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME', 'DATE_GREGORIAN'],
            keep='last'
        )
        
        x.dropna(
            subset=["WATER_TABLE"],
            inplace=True
        )

        x.reset_index(
            drop=True,
            inplace=True
        )

        x["DAY_PERSIAN_NEW"] = method
            
        x["YEAR_PERSIAN_NEW"] = x["YEAR_PERSIAN"].astype(str).str.zfill(4)
        x["MONTH_PERSIAN_NEW"] = x["MONTH_PERSIAN"].astype(str).str.zfill(2)
        x["DAY_PERSIAN_NEW"] = x["DAY_PERSIAN_NEW"].astype(str).str.zfill(2)
        x['DATE_PERSIAN_NEW'] = x["YEAR_PERSIAN_NEW"] + "-" + x["MONTH_PERSIAN_NEW"] + "-" + x["DAY_PERSIAN_NEW"]
        x['DATE_GREGORIAN_NEW'] = x.apply(
            lambda x: jalali.Persian(x["DATE_PERSIAN_NEW"]).gregorian_string(), 
            axis=1
        )
        x[['YEAR_GREGORIAN_NEW', 'MONTH_GREGORIAN_NEW', 'DAY_GREGORIAN_NEW']] = x['DATE_GREGORIAN_NEW'].str.split('-', 2, expand=True)
        x["YEAR_GREGORIAN_NEW"] = x["YEAR_GREGORIAN_NEW"].str.zfill(4)
        x["MONTH_GREGORIAN_NEW"] = x["MONTH_GREGORIAN_NEW"].str.zfill(2)
        x["DAY_GREGORIAN_NEW"] = x["DAY_GREGORIAN_NEW"].str.zfill(2)
        x["DATE_GREGORIAN_NEW"] = x["DATE_GREGORIAN_NEW"].apply(pd.to_datetime)
        x["DATE_GREGORIAN"] = x["DATE_GREGORIAN"].apply(pd.to_datetime)

        x["WATER_TABLE_NEW"] = x["WATER_TABLE"]
            
        A = []

        A.append(x["WATER_TABLE"][0])

        for i in range(1, len(x) - 1):

            if pd.isna(x["WATER_TABLE"][i-1]) or pd.isna(x["WATER_TABLE"][i]):
                NEW_VALUE = np.nan
                A.append(NEW_VALUE)
            else:
                if int(x["DAY_PERSIAN"][i]) >= method:
                    NEW_VALUE = x["WATER_TABLE"][i-1] + ((((x["DATE_GREGORIAN_NEW"][i] - x["DATE_GREGORIAN"][i-1]).days) / ((x["DATE_GREGORIAN"][i] - x["DATE_GREGORIAN"][i-1]).days)) * (x["WATER_TABLE"][i] - x["WATER_TABLE"][i-1]))
                    A.append(NEW_VALUE)
                else:
                    NEW_VALUE = x["WATER_TABLE"][i] + ((((x["DATE_GREGORIAN_NEW"][i] - x["DATE_GREGORIAN"][i]).days) / ((x["DATE_GREGORIAN"][i+1] - x["DATE_GREGORIAN"][i]).days)) * (x["WATER_TABLE"][i+1] - x["WATER_TABLE"][i]))
                    A.append(NEW_VALUE)

        A.append(x["WATER_TABLE"][len(x) - 1])
                
        x["WATER_TABLE_NEW"] = A
            
        return x
    except:
        pass

    
def synchronize_date(
    data_interpolated,
    method,
    how_modify
):
    if how_modify == 0:
        data_interpolated = data_interpolated.groupby(by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME"]).apply(lambda x: f_syncdate(x, method)).reset_index(drop=True)
                
        data_interpolated.sort_values(
            by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
        ).reset_index(drop=True)
        
        data_interpolated["DAY_PERSIAN"] = data_interpolated["DAY_PERSIAN_NEW"]
        data_interpolated["MONTH_PERSIAN"] = data_interpolated["MONTH_PERSIAN_NEW"]
        data_interpolated["YEAR_PERSIAN"] = data_interpolated["YEAR_PERSIAN_NEW"]
        data_interpolated["DATE_PERSIAN"] = data_interpolated["DATE_PERSIAN_NEW"]
        
        data_interpolated["DATE_GREGORIAN_RAW"] = data_interpolated["DATE_GREGORIAN"]
        data_interpolated["DAY_GREGORIAN"] = data_interpolated["DAY_GREGORIAN_NEW"]
        data_interpolated["MONTH_GREGORIAN"] = data_interpolated["MONTH_GREGORIAN_NEW"]
        data_interpolated["YEAR_GREGORIAN"] = data_interpolated["YEAR_GREGORIAN_NEW"]
        data_interpolated["DATE_GREGORIAN"] = data_interpolated["DATE_GREGORIAN_NEW"]

        data_interpolated["WATER_TABLE"] = data_interpolated["WATER_TABLE_NEW"]

        data_interpolated.drop(
            ['DAY_PERSIAN_NEW', 'MONTH_PERSIAN_NEW', 'YEAR_PERSIAN_NEW', 'DATE_PERSIAN_NEW', 'DAY_GREGORIAN_NEW', 'MONTH_GREGORIAN_NEW', 'YEAR_GREGORIAN_NEW', 'DATE_GREGORIAN_NEW'],
            axis=1,
            inplace=True
        )
        
        data_interpolated.drop_duplicates(
            subset=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_PERSIAN"],
            keep='last',
            inplace=True
        )

        data_interpolated.to_sql(
            name="GROUNDWATER_SYNCDATE_DATA",
            con=DB_GROUNDWATER,
            if_exists="replace"
        )

    else:
        pass



def interpolate___missingData(
    data_interpolated,
    data_cleansing,
    method,
    order,
    limit,
    study_area,
    aquifer,
    well,
    how_modify
):
    if how_modify == 0:
        
        data_cleansing = data_cleansing.groupby(by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME"]).apply(lambda x: f_interpolate(x, method, order, limit)).reset_index(drop=True)
               
        data_cleansing.sort_values(
            by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
        ).reset_index(drop=True) 
        
        data_cleansing.to_sql(
            name="GROUNDWATER_INTERPOLATED_DATA",
            con=DB_GROUNDWATER,
            if_exists="replace"
        )
        
    elif how_modify == 1:
        data_cleansing_well = data_cleansing[data_cleansing["MAHDOUDE_NAME"] == study_area]            
        data_cleansing_well = data_cleansing_well[data_cleansing_well["AQUIFER_NAME"] == aquifer]
        data_cleansing_well = data_cleansing_well[data_cleansing_well["LOCATION_NAME"] == well]            
        data_cleansing_well = data_cleansing_well.sort_values(
            by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
        ).reset_index(drop=True)
        data_cleansing_well = data_cleansing_well.groupby(by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME"]).apply(lambda x: f_interpolate(x, method, order, limit)).reset_index(drop=True)
        
        index_names = data_cleansing[(data_cleansing["MAHDOUDE_NAME"] == study_area) & (data_cleansing["AQUIFER_NAME"] == aquifer) & (data_cleansing["LOCATION_NAME"] == well)].index
        data_cleansing.drop(index_names, inplace=True)
        
        result = data_cleansing.append(data_cleansing_well, sort=False).reset_index(drop=True) 

        result = result.sort_values(
            by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
        )
        
        result['DATE_GREGORIAN'] = result["YEAR_GREGORIAN"] + "-" + result["MONTH_GREGORIAN"] + "-" + result["DAY_GREGORIAN"]
        result["DATE_GREGORIAN"] = result["DATE_GREGORIAN"].apply(pd.to_datetime)
                
        result.to_sql(
            name="GROUNDWATER_INTERPOLATED_DATA",
            con=DB_GROUNDWATER,
            if_exists="replace"
        )
        
    elif how_modify == 2:
        data_cleansing_well = data_cleansing[data_cleansing["MAHDOUDE_NAME"] == study_area]            
        data_cleansing_well = data_cleansing_well[data_cleansing_well["AQUIFER_NAME"] == aquifer]
        data_cleansing_well = data_cleansing_well.sort_values(
            by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
        ).reset_index(drop=True)
        data_cleansing_well = data_cleansing_well.groupby(by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME"]).apply(lambda x: f_interpolate(x, method, order, limit)).reset_index(drop=True)
        
        index_names = data_cleansing[(data_cleansing["MAHDOUDE_NAME"] == study_area) & (data_cleansing["AQUIFER_NAME"] == aquifer)].index
        data_cleansing.drop(index_names, inplace=True)
        
        result = data_cleansing.append(data_cleansing_well, sort=False).reset_index(drop=True) 

        result = result.sort_values(
            by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
        )
        
        result['DATE_GREGORIAN'] = result["YEAR_GREGORIAN"] + "-" + result["MONTH_GREGORIAN"] + "-" + result["DAY_GREGORIAN"]
        result["DATE_GREGORIAN"] = result["DATE_GREGORIAN"].apply(pd.to_datetime)
                
        result.to_sql(
            name="GROUNDWATER_INTERPOLATED_DATA",
            con=DB_GROUNDWATER,
            if_exists="replace"
        )
    elif how_modify == 3:
        data_cleansing_well = data_cleansing[data_cleansing["MAHDOUDE_NAME"] == study_area]            
        data_cleansing_well = data_cleansing_well.sort_values(
            by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
        ).reset_index(drop=True)
        data_cleansing_well = data_cleansing_well.groupby(by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME"]).apply(lambda x: f_interpolate(x, method, order, limit)).reset_index(drop=True)
        
        index_names = data_cleansing[(data_cleansing["MAHDOUDE_NAME"] == study_area)].index
        data_cleansing.drop(index_names, inplace=True)
        
        result = data_cleansing.append(data_cleansing_well, sort=False).reset_index(drop=True) 

        result = result.sort_values(
            by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
        )
        
        result['DATE_GREGORIAN'] = result["YEAR_GREGORIAN"] + "-" + result["MONTH_GREGORIAN"] + "-" + result["DAY_GREGORIAN"]
        result["DATE_GREGORIAN"] = result["DATE_GREGORIAN"].apply(pd.to_datetime)
                
        result.to_sql(
            name="GROUNDWATER_INTERPOLATED_DATA",
            con=DB_GROUNDWATER,
            if_exists="replace"
        )  
    else:
        pass
    
 

# -----------------------------------------------------------------------------
# CHECK USER INPUT
# -----------------------------------------------------------------------------
def check_user_input(x):
    try:
        x = int(x)
        return x
    except ValueError:
        try:
            x = float(x)
            return x
        except ValueError:
            return x



# -----------------------------------------------------------------------------
# READ CONNECTED SPREADSHEET File
# -----------------------------------------------------------------------------
# CASE-DEPENDENT
# WARNING : EXCEL FILE WITH SEVERAL SHEET
def read_spreadsheet(contents, filename):
    if '.xlsx' in filename or '.xls' in filename:
        data = {}
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        spreadsheet_file = pd.ExcelFile(io.BytesIO(decoded))
        if len(spreadsheet_file.sheet_names) >= 2:
            for sheet_name in spreadsheet_file.sheet_names:
                data[sheet_name] = spreadsheet_file.parse(sheet_name).to_dict()
            return data, spreadsheet_file.sheet_names
        else:
            return None, None


# -----------------------------------------------------------------------------
# EXTRACT GEOGRAPHICAL INFORMATION DATASET
# -----------------------------------------------------------------------------
# CASE-DEPENDENT
def extract_geo_info_dataset(data):
    columns = [
        "ID", "Mahdodeh_Name", "Mahdodeh_Code", "Aquifer_Name", "Well_Name",
        "X_Decimal", "Y_Decimal", "Final_Elevation"
    ]
    data = data[columns]
    data.drop_duplicates(keep="first", inplace=True)
    return data


# # -----------------------------------------------------------------------------
# # DATA CLEANSING
# # -----------------------------------------------------------------------------
# def convert_to_day_15(info, date, value, date_type="persian"):
#     df = info.copy()
#     if date_type == "gregorian":
#         df["DATE_GREGORIAN"] = date.apply(pd.to_datetime)
#         df["DATE_PERSIAN"] = list(
#             map(
#                 lambda i: jalali.Gregorian(i.date()).persian_string(),
#                 df["DATE_GREGORIAN"]
#             )
#         )
#     elif date_type == "persian":
#         df["DATE_PERSIAN"] = date
#         df["DATE_GREGORIAN"] = list(
#             map(
#                 lambda i: jalali.Persian(i).gregorian_string(),
#                 df["DATE_PERSIAN"]
#             )
#         )
#         df["DATE_GREGORIAN"] = df["DATE_GREGORIAN"].apply(pd.to_datetime)    
#     else:
#         pass
#     df["VALUE"] = value        
#     df["DELTA_DAY"] = df["DATE_GREGORIAN"].diff().dt.days
#     df["DATE_PERSIAN_NEW"] = list(
#         map(
#             lambda i: f"{int(i.split('-')[0])}-{int(i.split('-')[1])}-{15}",
#             df["DATE_PERSIAN"]
#         )
#     )
#     df["DATE_GREGORIAN_NEW"] = list(
#         map(
#             lambda i: jalali.Persian(i).gregorian_string(),
#             df["DATE_PERSIAN_NEW"]
#         )
#     )
#     df["DATE_GREGORIAN_NEW"] = df["DATE_GREGORIAN_NEW"].apply(pd.to_datetime)
#     df["VALUE_NEW"] = df["VALUE"]
#     A = []
#     A.append(df["VALUE"][0])
#     for i in range(1, len(df)):
#         if int(df["DATE_PERSIAN"][i].split('-')[2]) >= 15:
#             NEW_VALUE = df["VALUE"][i-1] + ((((df["DATE_GREGORIAN_NEW"][i] - df["DATE_GREGORIAN"][i-1]).days) / ((df["DATE_GREGORIAN"][i] - df["DATE_GREGORIAN"][i-1]).days)) * (df["VALUE"][i] - df["VALUE"][i-1]))
#             A.append(NEW_VALUE)
#         else:
#             NEW_VALUE = df["VALUE"][i] + ((((df["DATE_GREGORIAN_NEW"][i] - df["DATE_GREGORIAN"][i]).days) / ((df["DATE_GREGORIAN"][i+1] - df["DATE_GREGORIAN"][i]).days)) * (df["VALUE"][i+1] - df["VALUE"][i]))
#             A.append(NEW_VALUE)
#     df["VALUE_NEW"] = A
#     return df


# def create_date_day15(min, max):    
#     result = []
#     min_list = list(map(lambda x: int(x), min.split("-")))
#     max_list = list(map(lambda x: int(x), max.split("-")))
#     for y in range(min_list[0], max_list[0] + 1):
#         for m in range(1, 13):
#             result.append(f"{y}-{m}-15")

#     result = pd.DataFrame(
#         {"DATE_PERSIAN" : result}
#     )
#     result['DATE_GREGORIAN'] = result.apply(
#         lambda x: jalali.Persian(x["DATE_PERSIAN"]).gregorian_string(), 
#         axis=1
#     )
#     result["DATE_GREGORIAN"] = result["DATE_GREGORIAN"].apply(pd.to_datetime)
#     result = result[result["DATE_GREGORIAN"] >= pd.to_datetime(jalali.Persian(min).gregorian_string())]
#     result = result[result["DATE_GREGORIAN"] <= pd.to_datetime(jalali.Persian(max).gregorian_string())]
#     result["DATE_GREGORIAN"] = result["DATE_GREGORIAN"].apply(pd.to_datetime)  
#     return result


# def data_cleansing(
#     GeoInfo,
#     Data,
#     DateType,
#     InterpolateMethod,
#     Order,
#     Limit
# ):
#     """Data Cleansing

#     Args:
#         GeoInfo (str): Name of GeoInfo Table in Database
#         Data (str): Name of Data Table in Database

#     Returns:
#         [type]: [description]
#     """
    
#     # LOAD GeoInfo DATA
#     geoInfo = pd.read_sql_query(
#         sql=f"SELECT * FROM {GeoInfo}",
#         con=DB_GROUNDWATER
#     )
    
#     # LOAD DATA
#     data = pd.read_sql_query(
#         sql=f"SELECT * FROM {Data}",
#         con=DB_GROUNDWATER
#     )
    
#     # REMOVE ANY SPACE AT THE START AND END STRING
#     COLs = ['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME']
#     geoInfo[COLs] = geoInfo[COLs].apply(lambda x: x.str.rstrip())
#     geoInfo[COLs] = geoInfo[COLs].apply(lambda x: x.str.lstrip())
#     data[COLs] = data[COLs].apply(lambda x: x.str.rstrip())
#     data[COLs] = data[COLs].apply(lambda x: x.str.lstrip())
    
#     # CONVERT GREGORIAN DATE
#     data["DATE_GREGORIAN_RAW"] = data["DATE_GREGORIAN_RAW"].apply(pd.to_datetime)
    
#     # CREATE A DATE CHECK COLUMN
#     data['DATE_CHECK'] = np.where(
#         data["DATE_PERSIAN_RAW"].isna(),
#         np.where(
#             data["DATE_GREGORIAN_RAW"].isna(),
#             np.NaN,
#             "G"
#         ),
#         "P"  
#     )
    
#     # CONVERT DATE (PERSIAN <--> GREGORIAN)
#     data['DATE_PERSIAN_RAW'] = data.apply(
#         lambda x: jalali.Gregorian(x["DATE_GREGORIAN_RAW"].date()).persian_string() if x["DATE_CHECK"] == "G" else x["DATE_PERSIAN_RAW"], 
#         axis=1
#     )

#     data['DATE_GREGORIAN_RAW'] = data.apply(
#         lambda x: jalali.Persian(x["DATE_PERSIAN_RAW"]).gregorian_string() if x["DATE_CHECK"] == "P" else x["DATE_GREGORIAN_RAW"], 
#         axis=1
#     )

#     data["DATE_GREGORIAN_RAW"] = data["DATE_GREGORIAN_RAW"].apply(pd.to_datetime)
    
#     # REMOVE DATE CHECK COLUMN
#     data.drop(
#         ['DATE_CHECK'],
#         axis=1,
#         inplace=True
#     )
    
#     data.sort_values(
#         by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN_RAW"], 
#         inplace=True
#     )
    
#     # REMOVE NA ROW IN COLUMN "WATER_TABLE_RAW"
#     data.dropna(
#         subset=["WATER_TABLE_RAW"],
#         inplace=True
#     )

#     data.reset_index(
#         inplace=True,
#         drop=True
#     )
    
#     # CONVERT TO DAY 15
#     wt_date_converted = convert_to_day_15(
#         info=data[["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME"]],
#         date=data["DATE_PERSIAN_RAW"],
#         value=data["WATER_TABLE_RAW"],
#         date_type=DateType
#     )[["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_PERSIAN", "DATE_PERSIAN_NEW", "DATE_GREGORIAN", "DATE_GREGORIAN_NEW", "VALUE_NEW"]]

#     wt_date_converted.columns = ["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_PERSIAN_RAW", "DATE_PERSIAN", "DATE_GREGORIAN_RAW","DATE_GREGORIAN", "WATER_TABLE"]

#     data = data.merge(
#         right=wt_date_converted,
#         how="left",
#         on=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_PERSIAN_RAW", "DATE_GREGORIAN_RAW"]
#     )
    
#     # FILL MISSING DAY 15
#     tmp = pd.DataFrame()

#     for mn in list(data["MAHDOUDE_NAME"].unique()):
#         for an in list(data["AQUIFER_NAME"].unique()):
#             for ln in list(data["LOCATION_NAME"].unique()):
#                 df = data[(data["MAHDOUDE_NAME"] == mn) & (data["MAHDOUDE_NAME"] == an) & (data["LOCATION_NAME"] == ln)]
#                 date = create_date_day15(
#                     min = df.DATE_PERSIAN.min(),
#                     max = df.DATE_PERSIAN.max()
#                 )
#                 df = date.merge(
#                     df,
#                     how="left",
#                     on=["DATE_PERSIAN", "DATE_GREGORIAN"]
#                 )
                
#                 if InterpolateMethod in ["polynomial", "spline"]:
#                     if Limit == 0:
#                         df["WATER_TABLE_INTERPOLATED"] = df["WATER_TABLE"].interpolate(
#                             method=InterpolateMethod,
#                             order=Order,
#                             limit=None
#                         )
#                     else:
#                         df["WATER_TABLE_INTERPOLATED"] = df["WATER_TABLE"].interpolate(
#                             method=InterpolateMethod,
#                             order=Order,
#                             limit=Limit
#                         )
#                 else:
#                     if Limit == 0:
#                         df["WATER_TABLE_INTERPOLATED"] = df["WATER_TABLE"].interpolate(
#                             method=InterpolateMethod,
#                             limit=None
#                         )
#                     else:
#                         df["WATER_TABLE_INTERPOLATED"] = df["WATER_TABLE"].interpolate(
#                             method=InterpolateMethod,
#                             limit=Limit
#                         )
#                 df["WATER_TABLE_INTERPOLATED"] = df["WATER_TABLE_INTERPOLATED"].interpolate(method='ffill')
#                 df["WATER_TABLE_INTERPOLATED"] = df["WATER_TABLE_INTERPOLATED"].interpolate(method='bfill')
#                 df["MAHDOUDE_NAME"] = mn
#                 df["MAHDOUDE_CODE"] = int(df["MAHDOUDE_CODE"].unique()[0])
#                 df["AQUIFER_NAME"] = an
#                 df["LOCATION_NAME"] = ln
#                 df["DATA_STATE"] = df["DATA_STATE"].fillna("M")
#                 df["STORAGE_COEFFICIENT_LOCATION"] = df["STORAGE_COEFFICIENT_LOCATION"].unique()[0]
#                 df = df[[
#                     "MAHDOUDE_NAME", "MAHDOUDE_CODE", "AQUIFER_NAME", "LOCATION_NAME",
#                     "DATE_GREGORIAN", "DATE_PERSIAN",
#                     "WATER_TABLE", "WATER_TABLE_INTERPOLATED", "STORAGE_COEFFICIENT_LOCATION", "THISSEN_LOCATION", "THISSEN_AQUIFER",
#                     "DATA_STATE", "NO_MEASURE_CODE", "INFO",
#                     "DATE_GREGORIAN_RAW", "DATE_PERSIAN_RAW", "WATER_TABLE_RAW"	
#                 ]]

#                 tmp = pd.concat([tmp, df], axis=0)
    
#     data_cleaned = tmp.copy() 
    
#     return geoInfo, data_cleaned
    







# def data_cleansing(well_info_data_all, dtw_data_all, thiessen_data_all, sc_data_all, threshold=0.5):
#     result = pd.DataFrame()
#     result_aquifer = pd.DataFrame()

#     for aquifer in well_info_data_all['Aquifer_Name'].unique():
#         well_info_data = well_info_data_all[well_info_data_all['Aquifer_Name'] == aquifer]
#         dtw_data = dtw_data_all[dtw_data_all['Aquifer_Name'] == aquifer]
#         thiessen_data = thiessen_data_all[thiessen_data_all['Aquifer_Name'] == aquifer]
#         sc_data = sc_data_all[sc_data_all['Aquifer_Name'] == aquifer]

#         # Well Info Data:------------------------------------------------------
#         Columns_Info = list(compress(well_info_data.columns.tolist(),
#                                      list(map(lambda x: isinstance(x, str),
#                                               well_info_data.columns.tolist()))))

#         Well_Info = well_info_data[Columns_Info]

#         Well_Info['Aquifer_Name'] = Well_Info['Aquifer_Name'].apply(lambda x: x.rstrip())
#         Well_Info['Aquifer_Name'] = Well_Info['Aquifer_Name'].apply(lambda x: x.lstrip())
#         Well_Info['Well_Name'] = Well_Info['Well_Name'].apply(lambda x: x.rstrip())
#         Well_Info['Well_Name'] = Well_Info['Well_Name'].apply(lambda x: x.lstrip())

#         # Depth to Water (DTW) Data:--------------------------------------------

#         # Extract Dates From Columns Name
#         id_vars = list(compress(dtw_data.columns.tolist(),
#                                 list(map(lambda x: isinstance(x, str),
#                                          dtw_data.columns.tolist()))))

#         dtw_data['Aquifer_Name'] = dtw_data['Aquifer_Name'].apply(lambda x: x.rstrip())
#         dtw_data['Aquifer_Name'] = dtw_data['Aquifer_Name'].apply(lambda x: x.lstrip())
#         dtw_data['Well_Name'] = dtw_data['Well_Name'].apply(lambda x: x.rstrip())
#         dtw_data['Well_Name'] = dtw_data['Well_Name'].apply(lambda x: x.lstrip())

#         # Convert DTW Data to Wide Format
#         DTW_Wide = pd.melt(frame=dtw_data,
#                            id_vars=id_vars,
#                            var_name="Date",
#                            value_name="Depth_To_Water").pivot(index='Date',
#                                                               columns='ID',
#                                                               values='Depth_To_Water').reset_index()

#         # Modify Columns Name
#         DTW_Wide.columns = [col for col in DTW_Wide.columns]

#         # Modified Date - Add Gregorian Date
#         DTW_Wide["Date_Gregorian"] = list(map(lambda i: pd.to_datetime(i - 2, unit='D', origin='1900-01-01').date(),
#                                               DTW_Wide["Date"]))

#         # Modified Date - Add Persian Date
#         DTW_Wide["Date_Persian"] = list(map(lambda i: jalali.Gregorian(i).persian_string(),
#                                             DTW_Wide["Date_Gregorian"]))

#         # Reorder Columns
#         DTW_Wide = DTW_Wide.reindex(columns=(['Date', 'Date_Gregorian', 'Date_Persian'] + list(
#             [a for a in DTW_Wide.columns if a not in ['Date', 'Date_Gregorian', 'Date_Persian']])))

#         # Convert DTW_Wide Data Into A Tidy Format
#         DTW = pd.melt(frame=DTW_Wide,
#                       id_vars=['Date_Gregorian', 'Date', 'Date_Persian'],
#                       value_name='Depth_To_Water',
#                       var_name='ID').sort_values(['ID', 'Date_Gregorian']).drop('Date', axis=1)
#         DTW = DTW[['ID', 'Date_Gregorian', 'Date_Persian', 'Depth_To_Water']]

#         # Thiessen Weights Data:----------------------------------------------

#         # Extract Dates From Columns Name
#         id_vars = list(compress(thiessen_data.columns.tolist(),
#                                 list(map(lambda x: isinstance(x, str),
#                                          thiessen_data.columns.tolist()))))

#         thiessen_data['Aquifer_Name'] = thiessen_data['Aquifer_Name'].apply(lambda x: x.rstrip())
#         thiessen_data['Aquifer_Name'] = thiessen_data['Aquifer_Name'].apply(lambda x: x.lstrip())
#         thiessen_data['Well_Name'] = thiessen_data['Well_Name'].apply(lambda x: x.rstrip())
#         thiessen_data['Well_Name'] = thiessen_data['Well_Name'].apply(lambda x: x.lstrip())

#         # Convert Thiessen Data to Wide Format
#         Thiessen_Wide = pd.melt(frame=thiessen_data,
#                                 id_vars=id_vars,
#                                 var_name="Date",
#                                 value_name="Area").pivot(index='Date',
#                                                          columns='ID',
#                                                          values='Area').reset_index()

#         # Modify Columns Name
#         Thiessen_Wide.columns = [col for col in Thiessen_Wide.columns]

#         # Modified Date - Add Gregorian Date
#         Thiessen_Wide["Date_Gregorian"] = list(map(lambda i: pd.to_datetime(i - 2, unit='D', origin='1900-01-01').date(),
#                                                    Thiessen_Wide["Date"]))

#         # Modified Date - Add Persian Date
#         Thiessen_Wide["Date_Persian"] = list(map(lambda i: jalali.Gregorian(i).persian_string(),
#                                                  Thiessen_Wide["Date_Gregorian"]))

#         # Reorder Columns
#         Thiessen_Wide = Thiessen_Wide.reindex(columns=(['Date', 'Date_Gregorian', 'Date_Persian'] + list(
#             [a for a in Thiessen_Wide.columns if a not in ['Date', 'Date_Gregorian', 'Date_Persian']])))

#         # Convert DTW_Wide Data Into A Tidy Format
#         Thiessen = pd.melt(frame=Thiessen_Wide,
#                            id_vars=['Date_Gregorian', 'Date', 'Date_Persian'],
#                            value_name='Area',
#                            var_name='ID').sort_values(['ID', 'Date_Gregorian']).drop('Date', axis=1)
#         Thiessen = Thiessen[['ID', 'Date_Gregorian', 'Date_Persian', 'Area']]

#         # Sum Thiessen for Each Month (Area Aquifer)
#         Thiessen = pd.merge(left=Thiessen,
#                             right=Thiessen.groupby(by='Date_Gregorian').sum().reset_index().rename(
#                                 columns={'Area': 'Aquifer_Area'}),
#                             how='outer',
#                             on='Date_Gregorian').sort_values(['ID', 'Date_Gregorian'])

#         # Storage Coefficient Data:------------------------------------------

#         # Extract Dates From Columns Name
#         id_vars = list(compress(sc_data.columns.tolist(),
#                                 list(map(lambda x: isinstance(x, str),
#                                          sc_data.columns.tolist()))))

#         sc_data['Aquifer_Name'] = sc_data['Aquifer_Name'].apply(lambda x: x.rstrip())
#         sc_data['Aquifer_Name'] = sc_data['Aquifer_Name'].apply(lambda x: x.lstrip())
#         sc_data['Well_Name'] = sc_data['Well_Name'].apply(lambda x: x.rstrip())
#         sc_data['Well_Name'] = sc_data['Well_Name'].apply(lambda x: x.lstrip())

#         # Convert Storage Coefficient Data to Wide Format
#         Storage_Coefficient_Wide = pd.melt(frame=sc_data,
#                                            id_vars=id_vars,
#                                            var_name="Date",
#                                            value_name="Storage_Coefficient").pivot(index='Date',
#                                                                                    columns='ID',
#                                                                                    values='Storage_Coefficient').reset_index()

#         # Modify Columns Name
#         Storage_Coefficient_Wide.columns = [col for col in Storage_Coefficient_Wide.columns]

#         # Modified Date - Add Gregorian Date
#         Storage_Coefficient_Wide["Date_Gregorian"] = list(
#             map(lambda i: pd.to_datetime(i - 2, unit='D', origin='1900-01-01').date(),
#                 Storage_Coefficient_Wide["Date"]))

#         # Modified Date - Add Persian Date
#         Storage_Coefficient_Wide["Date_Persian"] = list(map(lambda i: jalali.Gregorian(i).persian_string(),
#                                                             Storage_Coefficient_Wide["Date_Gregorian"]))

#         # Reorder Columns
#         Storage_Coefficient_Wide = Storage_Coefficient_Wide.reindex(columns=(
#                     ['Date', 'Date_Gregorian', 'Date_Persian'] + list(
#                 [a for a in Storage_Coefficient_Wide.columns if a not in ['Date', 'Date_Gregorian', 'Date_Persian']])))

#         # Convert Storage_Coefficient_Wide Data Into A Tidy Format
#         Storage_Coefficient = pd.melt(frame=Storage_Coefficient_Wide,
#                                       id_vars=['Date_Gregorian', 'Date', 'Date_Persian'],
#                                       value_name='Storage_Coefficient',
#                                       var_name='ID').sort_values(['ID', 'Date_Gregorian']).drop('Date', axis=1)
#         Storage_Coefficient = Storage_Coefficient[['ID', 'Date_Gregorian', 'Date_Persian', 'Storage_Coefficient']]

#         # Surface Elevation of Observation Well:----------------------------
#         # Extract Surface Elevation of Observation Well From NASA Shuttle Radar Topography Mission (SRTM) Version 3.0
#         # srtm1_data = Srtm1HeightMapCollection()

#         # Well_Info["G.S.L_DEM_SRTM1"] = list(
#         #     map(lambda LonLat: srtm1_data.get_altitude(longitude=LonLat[0], latitude=LonLat[1]),
#         #         zip(Well_Info.X_Decimal, Well_Info.Y_Decimal)))

#         Well_Info["G.S.L_DEM_SRTM1"] = Well_Info["Final_Elevation"]

#         Elevation = Well_Info[['ID', 'G.S.L_M.S.L', 'Final_Elevation', 'G.S.L_DEM_SRTM1']]
#         # Elevation = Well_Info[['ID', 'G.S.L_M.S.L', 'Final_Elevation']]

#         Elevation.columns = ['ID', 'MSL_Elevation', 'Final_Elevation', 'Elevation']
#         # Elevation.columns = ['ID', 'MSL_Elevation', 'Final_Elevation']

#         # Combine Data:-----------------------------------------------------
#         data = pd.merge(left=DTW,
#                         right=Elevation,
#                         how='outer',
#                         on=['ID']).merge(right=Thiessen,
#                                          how='outer',
#                                          on=['ID', 'Date_Gregorian', 'Date_Persian']).merge(right=Storage_Coefficient,
#                                                                                             how='outer',
#                                                                                             on=['ID', 'Date_Gregorian',
#                                                                                                 'Date_Persian']).sort_values(
#             ['ID', 'Date_Gregorian'])

#         data.to_csv(f"{aquifer}.csv")

#         # Calculate Aquifer Storage Coefficient:------------------------------------
#         data['Unit_Aquifer_Storage_Coefficient'] = (data['Storage_Coefficient'] * data['Area']) / data['Aquifer_Area']

#         # Sum Aquifer Storage Coefficient for Each Month (Aquifer Storage Coefficient)
#         df = data.groupby(by=['Date_Gregorian', 'Date_Persian']).sum().reset_index()[
#             ['Date_Gregorian', 'Date_Persian', 'Unit_Aquifer_Storage_Coefficient']].rename(
#             columns={'Unit_Aquifer_Storage_Coefficient': 'Aquifer_Storage_Coefficient'})

#         data = data.merge(right=df,
#                           how='outer',
#                           on=['Date_Gregorian', 'Date_Persian']).sort_values(['ID', 'Date_Gregorian'])

#         #  Calculate Well Head:----------------------------------------------
#         data['Well_Head'] = data['Final_Elevation'] - data['Depth_To_Water']

#         # Calculate Aquifer Head:--------------------------------------------
#         data['Unit_Aquifer_Head'] = (data['Well_Head'] * data['Area']) / data['Aquifer_Area']

#         # Sum Units Aquifer Head for Each Month (Aquifer_Head)
#         df = data.groupby(by=['Date_Gregorian', 'Date_Persian']).sum().reset_index()[
#             ['Date_Gregorian', 'Date_Persian', 'Unit_Aquifer_Head']].rename(columns={'Unit_Aquifer_Head': 'Aquifer_Head'})

#         data = data.merge(right=df,
#                           how='outer',
#                           on=['Date_Gregorian', 'Date_Persian']).sort_values(['ID', 'Date_Gregorian'])

#         df = data[['Date_Gregorian', 'Date_Persian', 'Well_Head']].groupby(by=['Date_Gregorian', 'Date_Persian']).agg({
#             'Well_Head': [statistics.mean, statistics.geometric_mean, statistics.harmonic_mean]
#         }).reset_index()

#         df.columns = [col for col in df.columns]

#         df.columns = ['Date_Gregorian', 'Date_Persian', 'Aquifer_Head_Arithmetic_Mean', 'Aquifer_Head_Geometric_Mean', 'Aquifer_Head_Harmonic_Mean']

#         data = data.merge(right=df,
#                           how='outer',
#                           on=['Date_Gregorian', 'Date_Persian']).sort_values(['ID', 'Date_Gregorian'])
        
        

#         # Add Name Well
#         data = data.merge(right=Well_Info[
#             ['Mahdodeh_Name', 'Mahdodeh_Code', 'Aquifer_Name', 'Well_Name', 'ID', 'X_UTM', 'Y_UTM', 'X_Decimal',
#              'Y_Decimal']],
#                           how='outer',
#                           left_on=['ID'],
#                           right_on=['ID']).sort_values(['ID', 'Date_Gregorian'])
        
#         result = result.append(data)
        


#         # ADJUSMENT AQUIFER HEAD
#         data_aquifer = data.drop_duplicates(subset=['Date_Gregorian', 'Date_Persian'], keep='last').reset_index()
        
#         data_aquifer = data_aquifer[[
#             "Date_Gregorian", "Date_Persian",
#             "Aquifer_Area", "Aquifer_Storage_Coefficient", "Aquifer_Head",
#             "Aquifer_Head_Arithmetic_Mean", "Aquifer_Head_Geometric_Mean", "Aquifer_Head_Harmonic_Mean",
#             "Mahdodeh_Name", 'Mahdodeh_Code', "Aquifer_Name"
#         ]]

#         data_aquifer.replace(0, np.nan, inplace=True)
#         data_aquifer['Delta'] = data_aquifer['Aquifer_Head'].diff().fillna(0)
#         data_aquifer['Index'] = abs(data_aquifer['Delta']).apply(lambda x: 1 if x >= threshold else 0)
#         data_aquifer['Adjusted_Aquifer_Head'] = data_aquifer['Aquifer_Head']
        

#         n = data_aquifer.index[data_aquifer['Index'] == True].tolist()
        
        
#         if len(n) > 0:
#             while len(n) != 0:
#                 delta = data_aquifer['Delta'][n[0]]
#                 data_aquifer['Temp_Aquifer_Head'] = data_aquifer['Adjusted_Aquifer_Head']
#                 for i in range(n[0]):
#                     data_aquifer['Temp_Aquifer_Head'][i] = data_aquifer['Adjusted_Aquifer_Head'][i] + delta
#                     data_aquifer['Adjusted_Aquifer_Head'] = data_aquifer['Temp_Aquifer_Head']
#                     data_aquifer['Delta'] = data_aquifer['Adjusted_Aquifer_Head'].diff().fillna(0)
#                     data_aquifer['Index'] = abs(data_aquifer['Delta']).apply(lambda x: 1 if x >= threshold else 0)
#                     n = data_aquifer.index[data_aquifer['Index'] == True].tolist()
                    
        
#         if 'Temp_Aquifer_Head' in data_aquifer.columns:
#             data_aquifer = data_aquifer.drop(['Temp_Aquifer_Head'], axis=1)

#         if 'Delta' in data_aquifer.columns:
#             data_aquifer = data_aquifer.drop(['Delta'], axis=1)

#         if 'Index' in data_aquifer.columns:
#             data_aquifer = data_aquifer.drop(['Index'], axis=1)

                
#         result_aquifer = result_aquifer.append(data_aquifer)

        
#     result['Aquifer_Name'] = result['Aquifer_Name'].apply(lambda x: x.rstrip())
#     result['Aquifer_Name'] = result['Aquifer_Name'].apply(lambda x: x.lstrip())
#     result['Well_Name'] = result['Well_Name'].apply(lambda x: x.rstrip())
#     result['Well_Name'] = result['Well_Name'].apply(lambda x: x.lstrip())
#     result_aquifer['Aquifer_Name'] = result_aquifer['Aquifer_Name'].apply(lambda x: x.rstrip())
#     result_aquifer['Aquifer_Name'] = result_aquifer['Aquifer_Name'].apply(lambda x: x.lstrip())
    
#     result[['year_Date_Persian', 'month_Date_Persian', 'day_Date_Persian']] = result.Date_Persian.str.split('-', expand=True)
#     result['year_Date_Persian'] = result['year_Date_Persian'].astype(int)
#     result['month_Date_Persian'] = result['month_Date_Persian'].astype(int)
#     result['day_Date_Persian'] = result['day_Date_Persian'].astype(int)
#     result['Date_Gregorian'] = pd.to_datetime(result['Date_Gregorian'])
    
#     result_aquifer[['year_Date_Persian', 'month_Date_Persian', 'day_Date_Persian']] = result_aquifer.Date_Persian.str.split('-', expand=True)
#     result_aquifer['year_Date_Persian'] = result_aquifer['year_Date_Persian'].astype(int)
#     result_aquifer['month_Date_Persian'] = result_aquifer['month_Date_Persian'].astype(int)
#     result_aquifer['day_Date_Persian'] = result_aquifer['day_Date_Persian'].astype(int)
#     result_aquifer['Date_Gregorian'] = pd.to_datetime(result_aquifer['Date_Gregorian'])
    
    
#     result.to_csv("ddd.csv")
    
#     return result, result_aquifer



# # -----------------------------------------------------------------------------
# # READ SHAPEFILES
# # -----------------------------------------------------------------------------
# # EDITPATH
# def read_shapfile(
#         file_path = AREASTUDIES,
#         mah_code = None
# ):
#     if mah_code is not None:
#         geodf = gpd.read_file(file_path, encoding='windows-1256')
#         geodf = geodf[geodf['Mah_Code'].isin(mah_code)]
#         j_file = json.loads(geodf.to_json())

#         for feature in j_file["features"]:
#             feature['id'] = feature['properties']['Mah_Code']

#         return geodf, j_file









# -----------------------------------------------------------------------------
# WATER YEAR - DIFF - CUMSUM
# -----------------------------------------------------------------------------
# Column 1: Persian Year (YYYY) - سال
# Column 2: Persian Month (MM) - ماه
# Column 3: Value -پارامتر

# def waterYear(df):
#     if df["ماه"] >= 7 and df["ماه"] <= 12:
#         WY = str(int(df["سال"])) + "-" + str(int(df["سال"]) + 1)[2:4]
#         WM = int(df["ماه"]) - 6
#     elif df["ماه"] >= 1 and df["ماه"] <= 6:
#         WY = str(int(df["سال"]) - 1) + "-" + str(int(df["سال"]))[2:4]
#         WM = int(df["ماه"]) + 6
#     else:
#         WY = None
#         WM = None
#     return [WY, WM]


# def resultTable(df):
#     df["پارامتر"] = df["پارامتر"].round(2)    
#     df["WATER_YEAR"] = df.apply(waterYear, axis=1)
#     df[['سال آبی','ماه آبی']] = pd.DataFrame(df.WATER_YEAR.tolist(), index= df.index)
#     df.drop('WATER_YEAR', inplace=True, axis=1)
#     df["اختلاف ماه"] = df["پارامتر"] - df["پارامتر"].shift(1)
#     df["اختلاف ماه"] = df["اختلاف ماه"].round(2)
#     df = df.sort_values(['ماه', 'سال'])
#     result = pd.DataFrame()
#     for m in range(1,13):
#         d = df[df["ماه"] == m]
#         d["اختلاف ماه سال"] = d["پارامتر"] - d["پارامتر"].shift(1)
#         result = pd.concat([result, d])
#     result = result.sort_values(['سال', 'ماه'])
#     result["اختلاف ماه سال"] = result["اختلاف ماه سال"].round(2)
    
#     return result

# def resultTableAquifer(df):
#     df["هد"] = df["هد"].round(2)   
#     df["مساحت"] = df["مساحت"].round(2)   
#     df["ضریب"] = df["ضریب"].round(2)
#     df["WATER_YEAR"] = df.apply(waterYear, axis=1)
#     df[['سال آبی','ماه آبی']] = pd.DataFrame(df.WATER_YEAR.tolist(), index= df.index)
#     df.drop('WATER_YEAR', inplace=True, axis=1)
#     df["اختلاف ماه"] = df["هد"] - df["هد"].shift(1)
#     df["اختلاف ماه"] = df["اختلاف ماه"].round(2)
    
#     df = df.sort_values(['ماه', 'سال'])
#     result = pd.DataFrame()
#     for m in range(1,13):
#         d = df[df["ماه"] == m]
#         d["اختلاف ماه سال"] = d["هد"] - d["هد"].shift(1)
#         result = pd.concat([result, d])
#     result = result.sort_values(['سال', 'ماه'])
#     result["اختلاف ماه سال"] = result["اختلاف ماه سال"].round(2)
    
#     return result




# -----------------------------------------------------------------------------
# DATA CLEANSING TAB
# -----------------------------------------------------------------------------

# Load GeoDatabase
# -----------------------------------------------------------------------------

## Well Points
gdf = gpd.read_file("./Assets/GeoDatabase/GeoJson/Wells.geojson")
gdf = gdf.set_crs("EPSG:4326", allow_override=True)
COLs = ['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME']
gdf[COLs] = gdf[COLs].apply(lambda x: x.str.replace('ي','ی'))
gdf[COLs] = gdf[COLs].apply(lambda x: x.str.replace('ئ','ی'))
gdf[COLs] = gdf[COLs].apply(lambda x: x.str.replace('ك', 'ک'))

## Boundary
mask = gpd.read_file("./Assets/GeoDatabase/GeoJson/Aquifers.geojson")
mask = mask.set_crs("EPSG:4326", allow_override=True)
COLs = ['MAHDOUDE_NAME', 'AQUIFER_NAME']
mask[COLs] = mask[COLs].apply(lambda x: x.str.replace('ي','ی'))
mask[COLs] = mask[COLs].apply(lambda x: x.str.replace('ئ','ی'))
mask[COLs] = mask[COLs].apply(lambda x: x.str.replace('ك', 'ک'))
