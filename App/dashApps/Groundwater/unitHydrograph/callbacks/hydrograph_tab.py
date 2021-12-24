import os
import sqlite3
import json
import pandas as pd
import geopandas as gpd
import dash
from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash.exceptions import PreventUpdate
import statistics
import string

import psycopg2

from geoalchemy2 import Geometry, WKTElement
from sqlalchemy import *

from App.dashApps.Groundwater.unitHydrograph.callbacks.config import *



def callback___hydrograph_tab___unitHydrograph___groundwater(app):

    # -----------------------------------------------------------------------------
    # CHECK DATABASE EXIST AND STORE DATA
    # -----------------------------------------------------------------------------
    @app.callback(

        Output('DATA_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Output('DATA_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Output('GEOINFO_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Output('GEOINFO_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        
        Input('INTERVAL___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_intervals'),
        State('DATA_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data')

    )
    def FUNCTION___READ_DATABASE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        n, data_state
    ):
        if os.path.exists(PATH_DB_GROUNDWATER):
            TABLE_NAME = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", DB_GROUNDWATER)
            if TABLE_NAME['name'].str.contains('GEOINFO_DATA').any() and\
                TABLE_NAME['name'].str.contains('GROUNDWATER_DATA').any():
 
                    DATA = pd.read_sql_query(
                        sql="SELECT * FROM GROUNDWATER_DATA",
                        con=DB_GROUNDWATER
                    ).drop(['index'], axis=1)
                    
                    GEOINFO = pd.read_sql_query(
                        sql="SELECT * FROM GEOINFO_DATA",
                        con=DB_GROUNDWATER
                    ).drop(['index'], axis=1)
                    
                    return [
                        "OK",
                        DATA.to_dict('records'),
                        "OK",
                        GEOINFO.to_dict('records'),
                    ]

            else:
                return [
                    "NO",
                    None,
                    "NO",
                    None,
                ]
                                        
        else:
            return [
                "NO",
                None,
                "NO",
                None,
            ]
    
    

    # -----------------------------------------------------------------------------
    # OPEN CLOSE COLLAPSE
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        Output("ARROW___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "className"),
        
        Output("COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        Output("ARROW___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "className"),
        
        Output("COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        Output("ARROW___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "className"),
        
        Output("COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        Output("ARROW___COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "className"),
        
        Output("COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        Output("ARROW___COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "className"),
        
        Output("COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        Output("ARROW___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "className"),
        
        Output("COLLAPSE_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        Output("ARROW___COLLAPSE_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "className"),
        
        Output("COLLAPSE_PLOT_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        Output("ARROW___COLLAPSE_PLOT_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "className"),

        
        Input("OPEN_CLOSE___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "n_clicks"),
        Input("OPEN_CLOSE___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "n_clicks"),
        Input("OPEN_CLOSE___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "n_clicks"),
        Input("OPEN_CLOSE___COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "n_clicks"),
        Input("OPEN_CLOSE___COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "n_clicks"),
        Input("OPEN_CLOSE___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "n_clicks"),
        Input("OPEN_CLOSE___COLLAPSE_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "n_clicks"),
        Input("OPEN_CLOSE___COLLAPSE_PLOT_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "n_clicks"),
        
        State("COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        State("COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        State("COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        State("COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        State("COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        State("COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        State("COLLAPSE_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
        State("COLLAPSE_PLOT_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "is_open"),
    )
    def FUNCTION__COLLAPSE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        n_select_aquifer, n_select_well, n_select_date, n_select_hydrograph_method, n_settings, n_coeff_storage, n_thiessen, n_plot_thiessen,
        state_select_aquifer, state_select_well, state_select_date, state_select_hydrograph_method, state_settings, state_coeff_storage, state_thiessen, state_plot_thiessen,
    ):
        ctx = dash.callback_context

        if not ctx.triggered:
            return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

        else:
            button_id = ctx.triggered[0]["prop_id"].split(".")[0]
            
            if button_id == "OPEN_CLOSE___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER" and n_select_aquifer:
                if not state_select_aquifer:
                    return True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"
            
            elif button_id == "OPEN_CLOSE___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER" and n_select_well:
                if not state_select_well:
                    return False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER" and n_select_date:
                if not state_select_date:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE___COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER" and n_select_hydrograph_method:
                if not state_select_hydrograph_method:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE___COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER" and n_settings:
                if not state_settings:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER" and n_coeff_storage:
                if not state_coeff_storage:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE___COLLAPSE_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER" and n_thiessen:
                if not state_thiessen:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE___COLLAPSE_PLOT_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER" and n_plot_thiessen:
                if not state_plot_thiessen:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            else:
                return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"



    # -----------------------------------------------------------------------------
    # SELECT DATE COLLAPSE
    # -----------------------------------------------------------------------------

    @app.callback(
        Output("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Output("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Output("START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "disabled"),
        Output("END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "disabled"),
        Output("START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "disabled"),
        Output("END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "disabled"),
        Output("START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Output("END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Output("START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Output("END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Output("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "labelClassName"),
        Output("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "labelClassName"),
        Input("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Input("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
    )
    def FUNCTION__WATERYEAR_SHAMSIYEAR___COLLAPSE_DATE_SELECT___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        waterYear_selected, shamsiYear_selected
    ):
        ctx = dash.callback_context
        selected_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
        if selected_id == "WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER":
            waterYear_selected = "waterYear"
            shamsiYear_selected = ""
            return waterYear_selected, shamsiYear_selected, False, False, True, True, None, None, None, None, "d-flex align-items-center text-dark font-weight-bold", "d-flex align-items-center text-secondary"
        
        elif selected_id == "SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER":
            waterYear_selected = ""
            shamsiYear_selected = "shamsiYear"
            return waterYear_selected, shamsiYear_selected, True, True, False, False, None, None, None, None, "d-flex align-items-center text-secondary", "d-flex align-items-center text-dark font-weight-bold"
       
        else:
            waterYear_selected = ""
            shamsiYear_selected = ""
            return waterYear_selected, shamsiYear_selected, True, True, True, True, None, None, None, None, "d-flex align-items-center text-secondary", "d-flex align-items-center text-secondary",



    @app.callback(
        Output('END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'options'),
        Input('START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value')
    )
    def FUNCTION__SELECT_END_YEAR___WATER_YEAR_DATE_SELECT___COLLAPSE_DATE_SELECT___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        start
    ):
        if start is not None:
            start = int(start[0:4])
            return [
                {
                    'label': f'{year} - {str(year + 1)[2:4]}',
                    'value': f'{year}-{year + 1}',
                    'disabled': False if year >= start else True
                } for year in range(1371, 1420)
            ]
        else:
            return []
        
        

    @app.callback(
        Output('END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'options'),
        Input('START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value')
    )
    def FUNCTION__SELECT_END_YEAR___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_DATE_SELECT___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        start
    ):
        if start is not None:
            start = int(start)
            return [
                {
                    'label': year,
                    'value': year,
                    'disabled': False if year >= start else True
                } for year in range(1371, 1420)
            ]
        else:
            return []



    # -----------------------------------------------------------------------------
    # STUDY AREA SELECT
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'options'),
        Input('GEOINFO_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Input('GEOINFO_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data')
    )
    def FUNCTION___STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        geoinfo_state, geoInfo
    ):   
        if geoinfo_state == "OK" and geoInfo is not None:
            wells = read_data_from_postgis(
                table='wells', 
                engine=engine_db_layers, 
                geom_col='geometry', 
                modify_cols=['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME']
            )
            wells.sort_values(by=['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME'], inplace=True)
            return [{"label": col, "value": col} for col in wells['MAHDOUDE_NAME'].unique()]     
        else:
            return []
    
    
    
    # -----------------------------------------------------------------------------
    # AQUIFER SELECT
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'options'),
        Output('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('GEOINFO_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Input('GEOINFO_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data')
    )
    def FUNCTION___AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        study_area, geoinfo_state, geoInfo
    ):
        if geoinfo_state == "OK" and geoInfo is not None:
            if study_area is not None and len(study_area) != 0:
                wells = read_data_from_postgis(
                    table='wells', 
                    engine=engine_db_layers, 
                    geom_col='geometry', 
                    modify_cols=['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME']
                )
                wells.sort_values(by=['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME'], inplace=True)
                wells = wells[wells["MAHDOUDE_NAME"] == study_area]
                return [
                    [{"label": col, "value": col} for col in wells['AQUIFER_NAME'].unique()],
                    None
                ]
            else:
                return [
                    [],
                    None
                ]
        else:
            return [
                [],
                None
            ]



    # -----------------------------------------------------------------------------
    # WELL SELECT
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('WELL_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'options'),
        Output('WELL_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('GEOINFO_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Input('GEOINFO_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data')
    )
    def FUNCTION___WELL_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        study_area, aquifer, geoinfo_state, geoInfo
    ):
        if geoinfo_state == "OK" and geoInfo is not None:
            if study_area is not None and len(study_area) != 0 and aquifer is not None and len(aquifer) != 0:
                
                wells = read_data_from_postgis(
                    table='wells', 
                    engine=engine_db_layers, 
                    geom_col='geometry', 
                    modify_cols=['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME']
                )
                wells.sort_values(by=['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME'], inplace=True)
                wells = wells[wells["MAHDOUDE_NAME"] == study_area]                
                wells = wells[wells["AQUIFER_NAME"] == aquifer]
                
                return [
                    [{"label": col, "value": col} for col in wells['LOCATION_NAME'].unique()],
                    list(wells['LOCATION_NAME'].unique())
                ]
            else:
                return [
                    [],
                    []
                ]
        else:
            return [
                    [],
                    []
                ]
    
    
    
    # -----------------------------------------------------------------------------
    # MAP - GRAPH & MAP - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('MAP___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'figure'),
        Input('INTERVAL___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_intervals'), 
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('WELL_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
    )
    def FUNCTION___MAP___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        n, study_area, aquifer, well
    ):
        if well is not None and len(well) != 0:
            
            wells = read_data_from_postgis(
                table='wells', 
                engine=engine_db_layers, 
                geom_col='geometry', 
                modify_cols=['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME']
            )
            
            df_mahdoudes = wells[wells["MAHDOUDE_NAME"] == study_area]
            df_aquifers = df_mahdoudes[df_mahdoudes["AQUIFER_NAME"] == aquifer]                
            df_locations = df_aquifers[df_aquifers["LOCATION_NAME"].isin(well)]
            
            
            aquifers = read_data_from_postgis(
                table='aquifers', 
                engine=engine_db_layers, 
                geom_col='geometry', 
                modify_cols=['MAHDOUDE_NAME', 'AQUIFER_NAME']
            )
            
            mask_selected = aquifers[aquifers['MAHDOUDE_NAME'] == study_area]
            mask_selected = mask_selected[mask_selected['AQUIFER_NAME'] == aquifer]

            
            j_file = json.loads(mask_selected.to_json())

            for feature in j_file["features"]:
                feature['id'] = feature['properties']['AQUIFER_NAME']
                
            fig = px.choropleth_mapbox(
                data_frame=mask_selected,
                geojson=j_file,
                locations="AQUIFER_NAME",
                hover_name="AQUIFER_NAME",
                hover_data={"AQUIFER_NAME": False},
                opacity=0.4,
            )
            
            # fig = go.Figure(
            fig.add_trace(
                go.Scattermapbox(
                    lat=df_aquifers.geometry.y,
                    lon=df_aquifers.geometry.x,
                    mode='markers',
                    marker=go.scattermapbox.Marker(size=8),
                    text=df_aquifers["LOCATION_NAME"],
                    hoverinfo='text',
                    hovertemplate='<span style="color:white;">%{text}</span><extra></extra>'
                )
            )
            
            fig.add_trace(
                go.Scattermapbox(
                    lat=df_locations.geometry.y,
                    lon=df_locations.geometry.x,
                    mode='markers',
                    marker=go.scattermapbox.Marker(
                        size=10,
                        color='green'
                    ),
                    text=df_locations["LOCATION_NAME"],
                    hoverinfo='text',
                    hovertemplate='<b>%{text}</b><extra></extra>'
                ), 
            )           
                
            fig.update_layout(
                mapbox = {
                    'style': "stamen-terrain",
                    'zoom': 7,
                    'center': {
                        'lat': df_locations.geometry.y.mean(),
                        'lon': df_locations.geometry.x.mean(),
                    },
                },
                showlegend = False,
                hovermode='closest',
                margin = {'l':0, 'r':0, 'b':0, 't':0}
            )
            
            return fig        
        else:
            return BASE_MAP

        
            
    @app.callback(
        Output('STORAGE_COEFFICIENT_AQUIFER_HOLDER___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'hidden'),
        Output('STORAGE_COEFFICIENT_WELLS_HOLDER___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'hidden'),
        Input('INTERVAL___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_intervals'),
        Input('STORAGE_COEFFICIENT_SELECT___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'), 
    )
    def FUNCTION__STORAGE_COEFFICIENT_HOLDER_CARD___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        n, type
    ):
        if type == "AQUIFER":
            return [
                False,
                True
            ]
        else:
            return [
                True,
                False
            ]



    @app.callback(
        Output('STORAGE_COEFFICIENT_AQUIFER___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'hidden'),
        Output('NOT_SElECT_AQUIFER___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'hidden'),
        Output('STORAGE_COEFFICIENT_AQUIFER_LABEL___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'children'),
        Input('INTERVAL___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_intervals'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'), 
    )
    def FUNCTION__STORAGE_COEFFICIENT_AQUIFER_LABEL___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        n, aquifer
    ):
        if aquifer is not None and len(aquifer) != 0:
            return [
                False,
                True,
                f"ضریب ذخیره آبخوان {aquifer}"
            ]
        else:
            return [
                True,
                False,
                ""
            ]
  
    

    @app.callback(
        Output('STORAGE_COEFFICIENT_AQUIFER_SELECT___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'placeholder'),
        Output('STORAGE_COEFFICIENT_AQUIFER_SELECT___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('INTERVAL___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_intervals'),
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value')
    )
    def FUNCTION__STORAGE_COEFFICIENT_AQUIFER_SELECT___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        n, study_area, aquifer
    ):
        if study_area is not None and len(study_area) != 0 and aquifer is not None and len(aquifer) != 0:
            try:
                sc = STORAGE_COEFFICIENTS[STORAGE_COEFFICIENTS["MAHDOUDE_NAME"] == study_area]
                sc = sc[sc["AQUIFER_NAME"] == aquifer]
                return [
                    sc["STORAGE_COEFFICIENT"].values[0],
                    sc["STORAGE_COEFFICIENT"].values[0],
                ]
            except:
                return [
                    None,
                    None,
                ]
        else:
            return [
                None,              
                None,              
            ]
            
            
            
    @app.callback(
        Output('THIESSEN_SELECT_METHOD_ITEMS___COLLAPSE_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'options'),
        Input('INTERVAL___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_intervals'),
        Input('HYDROGRAPH_METHOD_SELLECT___COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
    )
    def FUNCTION___ENABLE_DISABLE_THIESSEN_SELECT_METHOD___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        n, methods
    ):
        if "TWA" in methods:
            return [
                {"label": "محاسبه مساحت پلیگون‌های تیسن", "value": 1},
                {"label": "فراخوانی پلیگون‌های تیسن از بانک داده", "value": 2, "disabled": True},
                {"label": "فراخوانی پلیگون‌های تیسن از فایل ورودی", "value": 3, "disabled": True}
            ]
        else:
            return [
                {"label": "محاسبه مساحت پلیگون‌های تیسن", "value": 1, "disabled": True},
                {"label": "فراخوانی پلیگون‌های تیسن از بانک داده", "value": 2, "disabled": True},
                {"label": "فراخوانی پلیگون‌های تیسن از فایل ورودی", "value": 3, "disabled": True}
            ]
    


    @app.callback(
        Output('BUTTON_CALCULATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'disabled'),
        
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('WELL_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        
        Input('HYDROGRAPH_METHOD_SELLECT___COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('STORAGE_COEFFICIENT_AQUIFER_SELECT___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        State('DATA_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
    )
    def FUNCTION___ENABLE_DISABLE_BUTTON_CALCULATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        study_area, aquifer, well, 
        method, sc,
        data_state
    ):
        if data_state == "OK" and\
            study_area is not None and len(study_area) != 0 and\
                aquifer is not None and len(aquifer) != 0 and\
                    well is not None and len(aquifer) != 0 and\
                        sc is not None and\
                            len(method) != 0:
                            
                                return False
        else:
            return True
        

    
    @app.callback(
        Output('BUTTON_CALCULATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_clicks'),
        Output('UNIT_HYDROGRAPH_DATA_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Output('UNIT_HYDROGRAPH_DATA_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Output('CHECK_CHANGE_THIESSEN_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Output('CHECK_CHANGE_THIESSEN_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
               
        Input('BUTTON_CALCULATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_clicks'),
        Input('INTERVAL___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_intervals'),
        
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('WELL_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        
        Input("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Input("START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Input("END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Input("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Input("START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Input("END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        
        Input("STORAGE_COEFFICIENT_SELECT___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Input('STORAGE_COEFFICIENT_AQUIFER_SELECT___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        
        Input('HYDROGRAPH_METHOD_SELLECT___COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        
        Input('WATER_TABLE_WATER_LEVEL_SELECT___COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),


        
        Input('DATA_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Input('DATA_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
    )
    def FUNCTION___CALCULATE_UNIT_HYDROGRAPH___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        n_click, n_intervals, 
        study_area, aquifer, well,
        wy, wys, wye, shy, shys, shye,
        sc_method, sc_aquifer,
        hydrograph_calculation_methods,
        water_table_level,
        data_state, data
    ):
        if n_click != 0:
            
            
            wells_df = read_data_from_postgis(
                table='wells', 
                engine=engine_db_layers, 
                geom_col='geometry', 
                modify_cols=['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME']
            )     
            
            aquifers_df = read_data_from_postgis(
                table='aquifers', 
                engine=engine_db_layers, 
                geom_col='geometry', 
                modify_cols=['MAHDOUDE_NAME', 'AQUIFER_NAME']
            )
           
            wells_df = wells_df[wells_df["MAHDOUDE_NAME"] == study_area]
            wells_df = wells_df[wells_df["AQUIFER_NAME"] == aquifer]
            wells_df = wells_df.reset_index(drop=True)
            aquifers_df = aquifers_df[aquifers_df["MAHDOUDE_NAME"] == study_area]
            aquifers_df = aquifers_df[aquifers_df["AQUIFER_NAME"] == aquifer]
            aquifers_df = aquifers_df.reset_index(drop=True)
            
            # LOAD DATA
            data = pd.DataFrame.from_dict(data)
            data = data[[
                'MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME',
                'DATE_GREGORIAN', 'YEAR_GREGORIAN', 'MONTH_GREGORIAN', 'DAY_GREGORIAN',
                'DATE_PERSIAN', 'YEAR_PERSIAN', 'MONTH_PERSIAN', 'DAY_PERSIAN',
                'WATER_TABLE', 'WATER_LEVEL', 
                'WATER_TABLE_RAW', 'WATER_TABLE_CLEANSING', 'WATER_TABLE_INTERPOLATED', 'WATER_TABLE_SYNCDATE',
                'DATE_GREGORIAN_RAW', 'DATE_PERSIAN_RAW',                
                'COLOR', 'DESCRIPTION'    
            ]]
            
            
            # FILTER DATA BASE STUDY AREA, AQUIFER AND WELL
            data = data[data["MAHDOUDE_NAME"] == study_area]
            data = data[data["AQUIFER_NAME"] == aquifer]
            data = data[data["LOCATION_NAME"].isin(well)]
            data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
            data = data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            
            
            # FILTER DATA BASE DATE
            if wy is not None and wy == "waterYear" and\
                wys is not None and wys != "" and\
                    wye is not None and wye != "":
                        wys = wys.split("-")[0] + "-07-01"
                        wye = wye.split("-")[1] + "-06-31"
                        data = data[data["DATE_PERSIAN"] >= wys]
                        data = data[data["DATE_PERSIAN"] <= wye]
            
            if shy is not None and shy == "shamsiYear" and shy != "" and\
                shys is not None and shys != "" and\
                    shye is not None and shye != "":
                        shys = str(shys) + "-01-01"
                        shye = str(shye) + "-12-30"
                        data = data[data["DATE_PERSIAN"] >= shys]
                        data = data[data["DATE_PERSIAN"] <= shye]
            
            data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
            data = data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            
            
            # ADD STORAGE COEFFICIENTS
            if sc_method == "AQUIFER":
                data["STORAGE_COEFFICIENT"] = sc_aquifer
            else:
                pass
            
            # CREATE RESULT DATAFRAME
            result = data.groupby(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
            ).agg({
                water_table_level: 'mean'
            }).reset_index()
            
            result["DATE_GREGORIAN"] = result["DATE_GREGORIAN"].apply(pd.to_datetime)
            result = result.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
            ).reset_index(drop=True).drop(columns=[water_table_level])
            
            
            # CALCULATE UNIT HYDROGRAPH
            
            ## Arithmetic Mean
            if "AM" in hydrograph_calculation_methods:
                
                tmp = data.groupby(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                ).agg({
                    water_table_level: statistics.mean
                }).reset_index()
                
                tmp["DATE_GREGORIAN"] = tmp["DATE_GREGORIAN"].apply(pd.to_datetime)
                tmp = tmp.sort_values(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                ).reset_index(drop=True).rename(columns={water_table_level: "AM_UNIT_HYDROGRAPH"})
                
                result = result.merge(
                    tmp, 
                    how="left", 
                    on=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                )
                
            ## Geometric Mean
            if "GM" in hydrograph_calculation_methods:
                
                tmp = data.groupby(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                ).agg({
                    water_table_level: statistics.geometric_mean
                }).reset_index()
                
                tmp["DATE_GREGORIAN"] = tmp["DATE_GREGORIAN"].apply(pd.to_datetime)
                tmp = tmp.sort_values(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                ).reset_index(drop=True).rename(columns={water_table_level: "GM_UNIT_HYDROGRAPH"})
                
                result = result.merge(
                    tmp, 
                    how="left", 
                    on=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                )
                
            ## Harmonic Mean
            if "HM" in hydrograph_calculation_methods:
                
                tmp = data.groupby(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                ).agg({
                    water_table_level: statistics.harmonic_mean
                }).reset_index()
                
                tmp["DATE_GREGORIAN"] = tmp["DATE_GREGORIAN"].apply(pd.to_datetime)
                tmp = tmp.sort_values(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                ).reset_index(drop=True).rename(columns={water_table_level: "HM_UNIT_HYDROGRAPH"})
                
                result = result.merge(
                    tmp, 
                    how="left", 
                    on=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                )
                
            ## Median
            if "ME" in hydrograph_calculation_methods:
                
                tmp = data.groupby(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                ).agg({
                    water_table_level: statistics.median
                }).reset_index()
                
                tmp["DATE_GREGORIAN"] = tmp["DATE_GREGORIAN"].apply(pd.to_datetime)
                tmp = tmp.sort_values(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                ).reset_index(drop=True).rename(columns={water_table_level: "ME_UNIT_HYDROGRAPH"})
                
                result = result.merge(
                    tmp, 
                    how="left", 
                    on=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                )

            ## Thiessen Weighted Average
            if "TWA" in hydrograph_calculation_methods:
                tmp = data.groupby(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                    ).apply(
                        lambda x: calculate_thiessen_for_each_month(
                            df=x, 
                            water_table_level=water_table_level, 
                            gdf=wells_df, 
                            mask=aquifers_df
                        )
                    ).reset_index().drop(columns=["level_4"])
                                
                tmp = tmp[[
                    "MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN", "THISSEN_LOCATION", "THISSEN_AQUIFER",	"geometry"
                ]]
                
                tmp_export = tmp.copy()
                tmp_export = tmp_export[
                    ["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_PERSIAN", "THISSEN_LOCATION", "THISSEN_AQUIFER", "geometry"]
                ]
                
                              
                try:
                    df_calculated_thiessen = read_data_from_postgis(
                        table='calculated_thiessen', 
                        engine=engine_db_thiessen, 
                        geom_col='geometry', 
                        modify_cols=None
                    )
                    
                    indexes = df_calculated_thiessen[ (df_calculated_thiessen['MAHDOUDE_NAME'] == study_area) & (df_calculated_thiessen['AQUIFER_NAME'] == aquifer) ].index
                    
                    df_calculated_thiessen.drop(indexes, inplace=True)
                    
                    frames = [tmp_export, df_calculated_thiessen]
                    
                    tmp_export = pd.concat(frames)

                except:
                    pass

                tmp_export.to_postgis(
                    'calculated_thiessen',
                    engine_db_thiessen,
                    if_exists='replace',
                    index=False,
                    dtype={'geometry': Geometry(srid= 4326)}
                )

                
                tmp = data.merge(
                    tmp, 
                    how="left", 
                    on=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                ).sort_values(
                    ["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", 'DATE_GREGORIAN']
                ).reset_index(drop=True)
                
                
                tmp['TMP1'] = (tmp[water_table_level] * tmp['THISSEN_LOCATION']) / tmp['THISSEN_AQUIFER']
                tmp['TMP2'] = (tmp["STORAGE_COEFFICIENT"] * tmp['THISSEN_LOCATION']) / tmp['THISSEN_AQUIFER']
                
                tmp = tmp.groupby(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                ).agg({
                    "TMP1": 'sum',
                    "TMP2": 'sum',
                    "THISSEN_AQUIFER": 'mean', 
                }).reset_index()[
                    ['MAHDOUDE_NAME', 'AQUIFER_NAME', 'DATE_GREGORIAN', 'DATE_PERSIAN', 'TMP1', 'TMP2', 'THISSEN_AQUIFER']
                ].rename(columns={
                    'TMP1': 'TWA_UNIT_HYDROGRAPH',
                    'TMP2': 'STORAGE_COEFFICIENT_AQUIFER',
                })
                

                
                result = result.merge(
                    tmp, 
                    how="left", 
                    on=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                )
                
                # ADJUST TWA ---------------------------------------------------------------------------------
                
                median_diff = data.groupby(by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME"])[water_table_level].diff().reset_index(drop=True).abs().median()

                
                df_thiessen_change = data.groupby(by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"])["LOCATION_NAME"]\
                    .apply(list)\
                        .reset_index(name='LOCATION_LIST').sort_values(['DATE_GREGORIAN'])
                                        
                df_thiessen_change_aquifer = df_thiessen_change.groupby(by=["MAHDOUDE_NAME", "AQUIFER_NAME"])\
                    .apply(check_thiessen_change).reset_index(drop=True)
                
                result = result.merge(
                    right=df_thiessen_change_aquifer[["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN", "THISSEN_CHANGE"]],
                    how='left',
                    on=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"])\
                        .sort_values(["MAHDOUDE_NAME", "AQUIFER_NAME", 'DATE_GREGORIAN'])
                                
                tmp = result.copy()                
                tmp['DELTA'] = tmp['TWA_UNIT_HYDROGRAPH'].diff().fillna(0)
                tmp['TWA_ADJ_UNIT_HYDROGRAPH'] = tmp['TWA_UNIT_HYDROGRAPH']
                
                n = tmp[tmp["THISSEN_CHANGE"]]["DATE_PERSIAN"].tolist()
                

                if len(n) > 0:                    
                    for dt in n:                
                        delta = tmp.loc[tmp["DATE_PERSIAN"] == dt, "DELTA"].reset_index()["DELTA"][0]
                        if delta >= 0:
                            delta = delta - median_diff
                        else:
                            delta = delta + median_diff
                        ix = tmp.loc[tmp["DATE_PERSIAN"] == dt, "DELTA"].reset_index()["index"][0]
                        tmp['TMP'] = tmp['TWA_ADJ_UNIT_HYDROGRAPH']
                        for i in range(ix):                    
                            tmp['TMP'][i] = tmp['TWA_ADJ_UNIT_HYDROGRAPH'][i] + delta                    
                        tmp['TWA_ADJ_UNIT_HYDROGRAPH'] = tmp['TMP']
                
                result = result.merge(
                    right=tmp[["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN", "TWA_ADJ_UNIT_HYDROGRAPH"]],
                    how='left',
                    on=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                )                

            
            return [
                0,
                "OK",
                result.to_dict('records'),
                "OK",
                df_thiessen_change.to_dict('df_thiessen_change')
            ]
                
            
        else:
            return [
                0,
                "NO",
                None,
                "NO",
                None
            ]

            
    
    
    # -----------------------------------------------------------------------------
    # GRAPH
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('GRAPH___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'figure'),
        Output('TABLE___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'columns'),        
        Output('TABLE___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Output('TABLE_HOLDER___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'hidden'), 
        Output('TABLE_TITLE___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'children'),
        Input('INTERVAL___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_intervals'),
        Input('WATER_TABLE_WATER_LEVEL_SELECT___COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('UNIT_HYDROGRAPH_DATA_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Input('UNIT_HYDROGRAPH_DATA_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Input('HYDROGRAPH_METHOD_SELLECT___COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value')

    )
    def FUNCTION___GRAPH___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        n_interval, water_t_l, study_area, aquifer, data_state, data, hydrograph_calculation_methods
    ):
        if data_state == "OK" and study_area is not None and len(study_area) != 0 and aquifer is not None and len(aquifer) != 0:
            
            data = pd.DataFrame.from_dict(data)
                               
            # data = pd.read_sql_query(
            #     sql="SELECT * FROM hydrograph",
            #     con=engine_db_hydrograph
            # )
            
            data = data[data["MAHDOUDE_NAME"] == study_area]
            data = data[data["AQUIFER_NAME"] == aquifer]
       
            data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
            
            data = data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
                        
            fig = go.Figure()
            
            if "AM_UNIT_HYDROGRAPH" in data.columns and "AM" in hydrograph_calculation_methods:
                fig.add_trace(
                    go.Scatter(
                        x=data["DATE_GREGORIAN"],
                        y=data["AM_UNIT_HYDROGRAPH"],
                        name="Arithmetic Mean",
                        mode="lines+markers",
                        marker=dict(
                            color="blue",
                            size=10,
                        ),
                        line=dict(
                            color="blue",
                            width=1
                        )
                    )
                )
            
            if "GM_UNIT_HYDROGRAPH" in data.columns and "GM" in hydrograph_calculation_methods:
                fig.add_trace(
                    go.Scatter(
                        x=data["DATE_GREGORIAN"],
                        y=data["GM_UNIT_HYDROGRAPH"],
                        name="Geometric Mean",
                        mode="lines+markers",
                        marker=dict(
                            color="red",
                            size=10,
                        ),
                        line=dict(
                            color="red",
                            width=1
                        )
                    )
                )
            
            if "HM_UNIT_HYDROGRAPH" in data.columns and "HM" in hydrograph_calculation_methods:
                fig.add_trace(
                    go.Scatter(
                        x=data["DATE_GREGORIAN"],
                        y=data["HM_UNIT_HYDROGRAPH"],
                        name="Harmonic Mean",
                        mode="lines+markers",
                        marker=dict(
                            color="green",
                            size=10,
                        ),
                        line=dict(
                            color="green",
                            width=1
                        )
                    )
                )
            
            if "ME_UNIT_HYDROGRAPH" in data.columns and "ME" in hydrograph_calculation_methods:
                fig.add_trace(
                    go.Scatter(
                        x=data["DATE_GREGORIAN"],
                        y=data["ME_UNIT_HYDROGRAPH"],
                        name="Median",
                        mode="lines+markers",
                        marker=dict(
                            color="brown",
                            size=10,
                        ),
                        line=dict(
                            color="brown",
                            width=1
                        )
                    )
                )
            
            if "TWA_UNIT_HYDROGRAPH" in data.columns and "TWA" in hydrograph_calculation_methods:
                fig.add_trace(
                    go.Scatter(
                        x=data["DATE_GREGORIAN"],
                        y=data["TWA_UNIT_HYDROGRAPH"],
                        name="Thiessen Weighted Average",
                        mode="lines+markers",
                        marker=dict(
                            color="black",
                            size=10,
                        ),
                        line=dict(
                            color="black",
                            width=1
                        )
                    )
                )
                
                fig.add_trace(
                    go.Scatter(
                        x=data["DATE_GREGORIAN"],
                        y=data["TWA_ADJ_UNIT_HYDROGRAPH"],
                        name="Adjusted Thiessen Weighted Average",
                        mode="lines+markers",
                        marker=dict(
                            color="gray",
                            size=10,
                        ),
                        line=dict(
                            color="gray",
                            width=1
                        )
                    )
                )
                
                fig.add_trace(
                    go.Scatter(
                        x=data[data["THISSEN_CHANGE"]]["DATE_GREGORIAN"],
                        y=data[data["THISSEN_CHANGE"]]["TWA_UNIT_HYDROGRAPH"],
                        name="Thiessen Changed",
                        mode="markers",
                        marker=dict(
                            color="orange",
                            size=16,
                            symbol='x'
                        ),
                    )
                )

            fig.update_layout(
                hoverlabel=dict(
                    namelength = -1
                ),
                autosize=False,
                font=dict(
                    family="Vazir-FD",
                    size=14,
                    color="RebeccaPurple"
                ),
                xaxis=dict(
                    tickformat="%Y-%m-%d",
                ),
                yaxis=dict(
                    tickformat=".1f",
                ),
                title=dict(
                    text=f"تراز ماهانه سطح آب آبخوان {aquifer} بر حسب متر" if water_t_l == "WATER_LEVEL" else f"عمق ماهانه سطح آب آبخوان {aquifer} بر حسب متر",
                    yanchor="top",
                    y=1,
                    xanchor="center",
                    x=0.500
                ),
                margin=dict(
                    l=50,
                    r=0,
                    b=30,
                    t=50,
                    pad=0
                ),
                legend=dict(
                    # yanchor="top",
                    # y=0.99,
                    # xanchor="left",
                    # x=0.01
                    orientation="h",
                    yanchor="bottom",
                    y=0.92,
                    xanchor="center",
                    x=0.5
                )
            )
            
            fig.update_xaxes(calendar='jalali')
            
            fig.update_layout(clickmode='event+select')
            
            data[['YEAR_PERSIAN', 'MONTH_PERSIAN', 'DAY_PERSIAN']] = data['DATE_PERSIAN'].str.split('-', 2, expand=True)          
            data["YEAR_PERSIAN"] = data["YEAR_PERSIAN"].astype(int)
            data["MONTH_PERSIAN"] = data["MONTH_PERSIAN"].astype(int)
            
            data = data[["YEAR_PERSIAN", "MONTH_PERSIAN", "TWA_UNIT_HYDROGRAPH", "THISSEN_AQUIFER", "STORAGE_COEFFICIENT_AQUIFER"]]
            data.columns = ["سال", "ماه", "هد", "مساحت", "ضریب"]
            data = resultTableAquifer(data)
            
            data.columns = ["سال", "ماه", "تراز ماهانه سطح آب زیرزمینی", "مساحت شبکه تیسن", "ضریب ذخیره", "سال آبی", "ماه آبی", "تغییرات هر ماه نسبت به ماه قبل", "تغییرات هر ماه نسبت به ماه سال قبل"]
            data["تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل"] = data["تغییرات هر ماه نسبت به ماه قبل"] * data["مساحت شبکه تیسن"] * data["ضریب ذخیره"]
            data["تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل"] = data["تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل"].round(2)
            data["تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل"] = data["تغییرات هر ماه نسبت به ماه سال قبل"] * data["مساحت شبکه تیسن"] * data["ضریب ذخیره"]
            data["تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل"] = data["تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل"] .round(2)
            
            
            result = data.pivot_table(
                values="تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل",
                index="سال آبی",
                columns="ماه آبی"
            ).reset_index()
            
            result.columns = ["سال آبی", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]
            
            result["حداکثر سالانه"] = result.iloc[:,1:13].max(axis=1).round(2)
            result["حداقل سالانه"] = result.iloc[:,1:13].min(axis=1).round(2)
            result["میانگین سالانه"] = result.iloc[:,1:13].mean(axis=1).round(2)
            result["تجمعی میانگین سالانه"] = result["میانگین سالانه"].cumsum(skipna=True).round(2) 
            result["مجموع سالانه"] = result.iloc[:,1:13].sum(axis=1).round(2)
            result["تجمعی مجموع سالانه"] = result["مجموع سالانه"].cumsum(skipna=True).round(2)
            result["مقدار تجمعی (مهر تا مهر)"] = result["مهر"].cumsum(skipna=True).round(2)
                                
            return [
                fig,
                [{"name": i, "id": i} for i in result.columns],
                result.to_dict('records'),
                False,
                "تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل"
            ]
        else:
            return [
                NO_MATCHING_GRAPH_FOUND,
                [{}],
                [],
                True,
                ""
            ]
    
    
    # -----------------------------------------------------------------------------
    # SELECT DATE TO SHOW THIESSEN
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('SELECT_DATE_SELECT___COLLAPSE_PLOT_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'options'),
        Output('SELECT_DATE_SELECT___COLLAPSE_PLOT_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('INTERVAL___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_intervals'),         
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('UNIT_HYDROGRAPH_DATA_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
    )
    def FUNCTION___MAP___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        n, study_area, aquifer, data_state
    ):
        if data_state == "OK" and study_area is not None and len(study_area) != 0 and aquifer is not None and len(aquifer) != 0:
                       
            df_calculated_thiessen = read_data_from_postgis(
                table='calculated_thiessen', 
                engine=engine_db_thiessen, 
                geom_col='geometry', 
                modify_cols=None
            )
            
            df_calculated_thiessen = df_calculated_thiessen[df_calculated_thiessen["MAHDOUDE_NAME"] == study_area]
            
            df_calculated_thiessen = df_calculated_thiessen[df_calculated_thiessen["AQUIFER_NAME"] == aquifer]
            
            if len(df_calculated_thiessen) != 0:
                return [
                    [{'label': f'{date}', 'value': f'{date}'} for date in df_calculated_thiessen["DATE_PERSIAN"].unique()],
                    df_calculated_thiessen["DATE_PERSIAN"].unique()[-1]
                ]
            else:
                return [
                    [],
                    None
                ]
        else:
            return [
                [],
                None
            ]
                
            

    
    # -----------------------------------------------------------------------------
    # MAP - TABLE - BODY
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('MAP___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'figure'),
        Output('MAP_HOLDER___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'hidden'),
        Output('TABLE_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'columns'),
        Output('TABLE_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Output('TABLE_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'style_data_conditional'),
        Output('TABLE_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'style_header_conditional'),
        Output('TABLE_INFO_HOLDER___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'hidden'),
        Input('INTERVAL___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_intervals'),         
        Input('SELECT_DATE_SELECT___COLLAPSE_PLOT_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('DATA_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
    )
    def FUNCTION___MAP___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        n, date, study_area, aquifer, data
    ):
        if date is not None and date != "" and study_area is not None and len(study_area) != 0 and aquifer is not None and len(aquifer) != 0:
            
            df_calculated_thiessen = read_data_from_postgis(
                table='calculated_thiessen', 
                engine=engine_db_thiessen, 
                geom_col='geometry',
                modify_cols=None
            )
            df_calculated_thiessen = df_calculated_thiessen[df_calculated_thiessen["MAHDOUDE_NAME"] == study_area]
            df_calculated_thiessen = df_calculated_thiessen[df_calculated_thiessen["AQUIFER_NAME"] == aquifer]
            
            # LOAD DATA
            data = pd.DataFrame.from_dict(data)
            data = data[[
                'MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME',
                'DATE_GREGORIAN', 'YEAR_GREGORIAN', 'MONTH_GREGORIAN', 'DAY_GREGORIAN',
                'DATE_PERSIAN', 'YEAR_PERSIAN', 'MONTH_PERSIAN', 'DAY_PERSIAN',
                'WATER_TABLE', 'WATER_LEVEL', 
                'WATER_TABLE_RAW', 'WATER_TABLE_CLEANSING', 'WATER_TABLE_INTERPOLATED', 'WATER_TABLE_SYNCDATE',
                'DATE_GREGORIAN_RAW', 'DATE_PERSIAN_RAW',                
                'COLOR', 'DESCRIPTION'    
            ]]
            
            # FILTER DATA BASE STUDY AREA, AQUIFER AND WELL
            data = data[data["MAHDOUDE_NAME"] == study_area]
            data = data[data["AQUIFER_NAME"] == aquifer]
            
            median_diff = data.groupby(by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME"])['WATER_LEVEL'].diff().reset_index(drop=True).abs().median()
            
            date_unique = sorted(list(df_calculated_thiessen["DATE_PERSIAN"].unique()))
            date_index = [i for i, value in enumerate(date_unique) if value == date]
            
            if date_index[0] == 0:
                dt = [date_unique[0], date_unique[1]]   
                df_calculated_thiessen = df_calculated_thiessen[df_calculated_thiessen["DATE_PERSIAN"].isin(dt)]                
                df_calculated_thiessen.reset_index(inplace=True, drop=True)

                data = data[data["DATE_PERSIAN"].isin(dt)]
                data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
                data = data.sort_values(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
                ).reset_index(drop=True)
            elif date_index[0] == (len(date_unique) - 1):
                dt = [date_unique[-2], date_unique[-1]]
                df_calculated_thiessen = df_calculated_thiessen[df_calculated_thiessen["DATE_PERSIAN"].isin(dt)]                
                df_calculated_thiessen.reset_index(inplace=True, drop=True)

                data = data[data["DATE_PERSIAN"].isin(dt)]
                data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
                data = data.sort_values(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
                ).reset_index(drop=True)
            else:
                dt = [date_unique[date_index[0] - 1], date_unique[date_index[0]], date_unique[date_index[0] + 1]]
                df_calculated_thiessen = df_calculated_thiessen[df_calculated_thiessen["DATE_PERSIAN"].isin(dt)]                
                df_calculated_thiessen.reset_index(inplace=True, drop=True)

                data = data[data["DATE_PERSIAN"].isin(dt)]
                data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
                data = data.sort_values(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
                ).reset_index(drop=True)

            df_plot = pd.merge(
                left=df_calculated_thiessen,
                right=data[[
                    'MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME',
                    'DATE_GREGORIAN', 'DATE_PERSIAN',
                    'WATER_TABLE', 'WATER_LEVEL',              
                    'COLOR'
                ]],
                on=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_PERSIAN"],
                how="left"
            )
            
            df_plot.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"], 
                inplace=True
            )
            
            df_plot["UNIT_HYDROGRAPH_LOCATION"] = df_plot["WATER_LEVEL"] * df_plot["THISSEN_LOCATION"] / df_plot["THISSEN_AQUIFER"]
            df_plot["UNIT_HYDROGRAPH_LOCATION_PERCENT"] = df_plot["UNIT_HYDROGRAPH_LOCATION"] * 100 / df_plot["UNIT_HYDROGRAPH_LOCATION"].sum()
            df_plot["UNIT_HYDROGRAPH_LOCATION_PERCENT"] = df_plot["UNIT_HYDROGRAPH_LOCATION_PERCENT"].round(2)
            
            df_table = df_plot.pivot_table(
                values="UNIT_HYDROGRAPH_LOCATION",
                index="LOCATION_NAME",
                columns="DATE_PERSIAN"
            ).reset_index()
            
            df_table.columns = ["چاه مشاهده‌ای"] + dt

            df_plot = df_plot[df_plot["DATE_PERSIAN"] == date] 
                                    
            def basemap():          
                fig = px.choropleth_mapbox(
                    data_frame=df_plot,
                    geojson=df_plot.geometry,
                    locations=df_plot.index,
                    color="UNIT_HYDROGRAPH_LOCATION_PERCENT",
                    color_continuous_scale="RdYlGn_r",
                    hover_name="LOCATION_NAME",
                    hover_data={"LOCATION_NAME": False},
                    opacity=0.4,
                )
                
                fig.update_coloraxes(showscale=False)
        
                    
                fig.update_layout(
                    mapbox = {
                        'style': "stamen-terrain",
                        'zoom': 9,
                        'center': {
                            'lat': df_plot.centroid.y.mean(),
                            'lon': df_plot.centroid.x.mean(),
                        },
                    },
                    showlegend = False,
                    hovermode='closest',
                    margin = {'l':0, 'r':0, 'b':0, 't':0}
                )
                
                fig.update_layout(mapbox_accesstoken=MAPBOX_TOKEN)
                # fig.update_layout(mapbox_style="light", mapbox_accesstoken=MAPBOX_TOKEN)
                
                return fig
            
            # texttrace = go.Scattermapbox(
            #     lat=df_plot.geometry.centroid.y,
            #     lon=df_plot.geometry.centroid.x,
            #     # text=df_plot["UNIT_HYDROGRAPH_PERCENTAGE"].round(1).astype(str) + "%",
            #     text=df_plot["LOCATION_NAME"],
            #     textfont=dict(size=12, color='black'),
            #     mode='text'
            # )
            
            if date_index[0] == 0:
                
                df_table["c1"] = df_table[df_table.columns[1]] - df_table[df_table.columns[2]]
            
                return [
                    basemap(),
                    # basemap().add_trace(texttrace),
                    False,
                    [{"name": i, "id": i} for i in df_table.columns],
                    df_table.round(2).to_dict('records'),
                    
                    [
                        {
                            'if': {
                                'filter_query': f'{{{df_table.columns[3]}}} > {median_diff}',
                                'column_id': f'{df_table.columns[2]}'
                            },
                            'backgroundColor': 'lightblue'
                        }
                    ] + 
                    [
                        {
                            'if': {
                                'filter_query': f'{{{df_table.columns[1]}}} < {-1 * median_diff}',
                                'column_id': f'{df_table.columns[2]}'
                            },
                            'backgroundColor': 'lightgreen'
                        }
                    ] +
                    [
                        {
                            'if': {'column_id': 'c1'},
                            'display': 'None'
                        }    
                    ] +
                    [
                        {
                            'if': {
                                'filter_query': '{{{}}} is blank'.format(col),
                                'column_id': col
                            },
                            'backgroundColor': 'red',
                            'color': 'white'
                        } for col in df_table.columns
                    ],
                    
                    [
                        {
                            'if': {'column_id': 'c1'},
                            'display': 'None'
                        }
                    ],
                    
                    False,
                ]
            
            elif date_index[0] == (len(date_unique) - 1):
                
                df_table["c1"] = df_table[df_table.columns[2]] - df_table[df_table.columns[1]]
            
                return [
                    basemap(),
                    # basemap().add_trace(texttrace),
                    False,
                    [{"name": i, "id": i} for i in df_table.columns],
                    df_table.round(2).to_dict('records'),
                    
                    [
                        {
                            'if': {
                                'filter_query': f'{{{df_table.columns[3]}}} > {median_diff}',
                                'column_id': f'{df_table.columns[1]}'
                            },
                            'backgroundColor': 'lightblue'
                        }
                    ] + 
                    [
                        {
                            'if': {
                                'filter_query': f'{{{df_table.columns[3]}}} < {-1 * median_diff}',
                                'column_id': f'{df_table.columns[1]}'
                            },
                            'backgroundColor': 'lightgreen'
                        }
                    ] +
                    [
                        {
                            'if': {'column_id': 'c1'},
                            'display': 'None'
                        }    
                    ] +
                    [
                        {
                            'if': {
                                'filter_query': '{{{}}} is blank'.format(col),
                                'column_id': col
                            },
                            'backgroundColor': 'red',
                            'color': 'white'
                        } for col in df_table.columns
                    ],
                    
                    [
                        {
                            'if': {'column_id': 'c1'},
                            'display': 'None'
                        }
                    ],
                    
                    False,
                ]
                
            else:
                
                df_table["c1"] = df_table[df_table.columns[2]] - df_table[df_table.columns[1]]
                df_table["c2"] = df_table[df_table.columns[2]] - df_table[df_table.columns[3]]
            
                return [
                    basemap(),
                    # basemap().add_trace(texttrace),
                    False,
                    [{"name": i, "id": i} for i in df_table.columns],
                    df_table.round(2).to_dict('records'),
                    
                    [
                        {
                            'if': {
                                'filter_query': f'{{{df_table.columns[4]}}} > {median_diff}',
                                'column_id': f'{df_table.columns[1]}'
                            },
                            'backgroundColor': 'lightblue'
                        }
                    ] + 
                    [
                        {
                            'if': {
                                'filter_query': f'{{{df_table.columns[4]}}} < {-1 * median_diff}',
                                'column_id': f'{df_table.columns[1]}'
                            },
                            'backgroundColor': 'lightgreen'
                        }
                    ] +
                                        [
                        {
                            'if': {
                                'filter_query': f'{{{df_table.columns[5]}}} > {median_diff}',
                                'column_id': f'{df_table.columns[3]}'
                            },
                            'backgroundColor': 'lightblue'
                        }
                    ] + 
                    [
                        {
                            'if': {
                                'filter_query': f'{{{df_table.columns[5]}}} < {-1 * median_diff}',
                                'column_id': f'{df_table.columns[3]}'
                            },
                            'backgroundColor': 'lightgreen'
                        }
                    ] +
                    [
                        {
                            'if': {'column_id': 'c1'},
                            'display': 'None'
                        },
                        {
                            'if': {'column_id': 'c2'},
                            'display': 'None'
                        }     
                    ] +
                    [
                        {
                            'if': {
                                'filter_query': '{{{}}} is blank'.format(col),
                                'column_id': col
                            },
                            'backgroundColor': 'red',
                            'color': 'white'
                        } for col in df_table.columns
                    ],
                    
                    [
                        {
                            'if': {'column_id': 'c1'},
                            'display': 'None'
                        },
                        {
                            'if': {'column_id': 'c2'},
                            'display': 'None'
                        }
                    ],
                    
                    False,
                ]
                
                        
        else:
            return [
                BASE_MAP,
                True,
                [{}],
                [],
                [{}],
                [{}],
                True,
            ]
            

    # -----------------------------------------------------------------------------
    # INFO CARD - BODY
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('BP_CARD_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'children'),
        Output('BM_CARD_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'children'),
        Output('AP_CARD_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'children'),
        Output('AM_CARD_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'children'),
        Output('HOLDER_CARD_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'hidden'),
        Output('GRAPH_THIESSEN___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'figure'),
        Input('INTERVAL___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_intervals'), 
        Input('SELECT_DATE_SELECT___COLLAPSE_PLOT_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('CHECK_CHANGE_THIESSEN_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Input('CHECK_CHANGE_THIESSEN_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
    )
    def FUNCTION___INFO_CARD___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        n, date, data_state, data
    ):
        if  data_state == "OK" and date is not None:
            data = pd.DataFrame.from_dict(data)
            data = data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
            ).reset_index(drop=True)
            
            # location_list_unique = sorted(data.LOCATION_LIST.apply(sorted).transform(tuple).unique(), key=len)
            location_list_unique = data.LOCATION_LIST.apply(sorted).transform(tuple).unique()
            
            
            
            location_list_unique = pd.DataFrame(
                {
                    "CLASS": list(string.ascii_uppercase)[0:len(location_list_unique)],
                    "LOCATION_LIST": location_list_unique
                }    
            )
            
            data["LOCATION_LIST"] = data.LOCATION_LIST.apply(sorted).transform(tuple)
            data["LOCATION_LIST_NUMBER"] = data.LOCATION_LIST.apply(len)
            
            # data.sort_values(by=["LOCATION_LIST"], inplace=True)
            
            data = data.merge(
                right=location_list_unique,
                how="left",
                on="LOCATION_LIST"
            )
                        
            fig = go.Figure()
            
            fig.add_trace(
                go.Scatter(
                    x=data["DATE_GREGORIAN"],
                    y=data["LOCATION_LIST_NUMBER"],
                    mode="lines+markers",
                    marker=dict(
                        color="blue",
                        size=10,
                    ),
                    line=dict(
                        color="blue",
                        width=1
                    )
                )
            )

            fig.update_layout(
                clickmode='event+select',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                height=200,
                hoverlabel=dict(
                    namelength = -1
                ),
                autosize=False,
                font=dict(
                    family="Vazir-FD",
                    size=14,
                    color="RebeccaPurple"
                ),
                xaxis=dict(
                    tickformat="%Y-%m-%d",
                ),
                margin=dict(
                    l=20,
                    r=0,
                    b=0,
                    t=0,
                    pad=0
                )
            )
            
            fig.update_xaxes(
                calendar='jalali',
            )
            
            i = data.index[data['DATE_PERSIAN'] == date].tolist()[0]
            
            if i == 0:
                BP = None
                BM = None
                AP = ' |-----| '.join(list(set(data.loc[i, "LOCATION_LIST"]) - set(data.loc[i+1, "LOCATION_LIST"])))
                AM = ' |-----| '.join(list(set(data.loc[i+1, "LOCATION_LIST"]) - set(data.loc[i, "LOCATION_LIST"]))) 
            
            elif i == (len(data) - 1):
                BP = ' |-----| '.join(list(set(data.loc[i, "LOCATION_LIST"]) - set(data.loc[i-1, "LOCATION_LIST"])))
                BM = ' |-----| '.join(list(set(data.loc[i-1, "LOCATION_LIST"]) - set(data.loc[i, "LOCATION_LIST"]))) 
                AP = None
                AM = None
            
            else:
                BP = ' |-----| '.join(list(set(data.loc[i, "LOCATION_LIST"]) - set(data.loc[i-1, "LOCATION_LIST"])))
                BM = ' |-----| '.join(list(set(data.loc[i-1, "LOCATION_LIST"]) - set(data.loc[i, "LOCATION_LIST"]))) 
                AP = ' |-----| '.join(list(set(data.loc[i, "LOCATION_LIST"]) - set(data.loc[i+1, "LOCATION_LIST"])))
                AM = ' |-----| '.join(list(set(data.loc[i+1, "LOCATION_LIST"]) - set(data.loc[i, "LOCATION_LIST"])))
            
            return [
                BP if BP is not None and BP != "" else "-",
                BM if BM is not None and BM != "" else "-",
                AP if AP is not None and AP != "" else "-",
                AM if AM is not None and AM != "" else "-",
                False,
                fig
            ]
            
        else:
            return [
                "-",
                "-",
                "-",
                "-",
                True,
                NO_MATCHING_GRAPH_FOUND
            ]
            

    # -----------------------------------------------------------------------------
    # SAVE RESULTS
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('BUTTON_UPDATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_clicks'),
        Input('BUTTON_UPDATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_clicks'),
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('UNIT_HYDROGRAPH_DATA_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Input('UNIT_HYDROGRAPH_DATA_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data')
    )
    def FUNCTION___INFO_CARD___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        n, study_area, aquifer, data_state, data
    ):
        if n != 0 and data_state == "OK":
            
            result = pd.DataFrame.from_dict(data)
            
            try:
                
                df_hydrograph = pd.read_sql_query(
                    sql="SELECT * FROM hydrograph",
                    con=engine_db_hydrograph
                )
                
                indexes = df_hydrograph[ (df_hydrograph['MAHDOUDE_NAME'] == study_area) & (df_hydrograph['AQUIFER_NAME'] == aquifer) ].index
                
                df_hydrograph.drop(indexes, inplace=True)
                
                frames = [result, df_hydrograph]
                
                result_all = pd.concat(frames)

            except:
                
                result_all = result.copy()

            result_all.reset_index(drop=True).to_sql(
                'hydrograph',
                engine_db_hydrograph,
                if_exists='replace',
                index=False
            )            
            
            return 0
        else:
            return 0