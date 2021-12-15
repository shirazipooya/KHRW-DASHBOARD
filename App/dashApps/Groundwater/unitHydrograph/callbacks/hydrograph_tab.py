import os
import sqlite3
import json
import pandas as pd
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
            geoInfo = pd.DataFrame.from_dict(geoInfo)
            return [{"label": col, "value": col} for col in geoInfo['MAHDOUDE_NAME'].unique()]        
        else:
            return []
    
    
    
    # -----------------------------------------------------------------------------
    # AQUIFER SELECT
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'options'),
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('GEOINFO_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        Input('GEOINFO_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data')
    )
    def FUNCTION___AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        study_area, geoinfo_state, geoInfo
    ):
        if geoinfo_state == "OK" and geoInfo is not None:
            if study_area is not None and len(study_area) != 0:
                geoInfo = pd.DataFrame.from_dict(geoInfo)
                geoInfo = geoInfo[geoInfo["MAHDOUDE_NAME"] == study_area]
                return [{"label": col, "value": col} for col in geoInfo['AQUIFER_NAME'].unique()]
            else:
                return []
        else:
            return []



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
                geoInfo = pd.DataFrame.from_dict(geoInfo)
                geoInfo = geoInfo[geoInfo["MAHDOUDE_NAME"] == study_area]
                geoInfo = geoInfo[geoInfo["AQUIFER_NAME"] == aquifer]
                return [
                    [{"label": col, "value": col} for col in geoInfo['LOCATION_NAME'].unique()],
                    list(geoInfo['LOCATION_NAME'].unique())
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

            df_mahdoudes = gdf[gdf["MAHDOUDE_NAME"] == study_area]
            df_aquifers = df_mahdoudes[df_mahdoudes["AQUIFER_NAME"] == aquifer]                    
            df_locations = df_aquifers[df_aquifers["LOCATION_NAME"].isin(well)]
            df_locations = df_locations.to_crs({'init': 'epsg:4326'})
            
            mask_selected = mask[mask['MAHDOUDE_NAME'] == study_area]
            mask_selected = mask_selected[mask_selected['AQUIFER_NAME'] == aquifer]
            mask_selected = mask_selected.to_crs({'init': 'epsg:4326'})
            
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
                    lat=df_aquifers.Y,
                    lon=df_aquifers.X,
                    mode='markers',
                    marker=go.scattermapbox.Marker(size=8),
                    text=df_aquifers["LOCATION_NAME"],
                    hoverinfo='text',
                    hovertemplate='<span style="color:white;">%{text}</span><extra></extra>'
                )
            )
            
            fig.add_trace(
                go.Scattermapbox(
                    lat=df_locations.Y,
                    lon=df_locations.X,
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
                        'lat': df_locations.Y.mean(),
                        'lon': df_locations.X.mean(),
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
        Output('DISPLAY_PARAMETER_SELECT___COLLAPSE_SETTINGS___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'options'),
        Input('INTERVAL___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'n_intervals'), 
        Input('WATER_TABLE_WATER_LEVEL_SELECT___COLLAPSE_SETTINGS___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value')
    )
    def FUNCTION__DISPLAY_PARAMETER_OPTIONS___COLLAPSE_SETTINGS___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        n, waterType
    ):
        if waterType == "WATER_LEVEL":
            return [
                {'label': 'تراز سطح آب', 'value': 1},
                {'label': 'تغییرات تراز سطح آب نسبت به ماه قبل', 'value': 2},
                {'label': 'تغییرات تراز سطح آب نسبت به ماه سال قبل', 'value': 3},
            ]
        else:
            return [
                {'label': 'عمق سطح آب', 'value': 1},
                {'label': 'تغییرات عمق سطح آب نسبت به ماه قبل', 'value': 2},
                {'label': 'تغییرات عمق سطح آب نسبت به ماه سال قبل', 'value': 3},
            ]
        


    # -----------------------------------------------------------------------------
    # TABLE
    # -----------------------------------------------------------------------------
    @app.callback(       
        Output('TABLE___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'columns'),        
        Output('TABLE___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        Output('TABLE_HOLDER___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'hidden'), 
        Output('TABLE_HEADER___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'children'), 
            
        Input('INTERVAL___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'n_intervals'),        
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('WELL_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),        
        Input('WATER_TABLE_WATER_LEVEL_SELECT___COLLAPSE_SETTINGS___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        
        Input("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Input("START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Input("END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Input("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Input("START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Input("END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER", "value"),
        Input("DISPLAY_PARAMETER_SELECT___COLLAPSE_SETTINGS___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("STATISTICAL_ANALYSIS_SELECT___COLLAPSE_SETTINGS___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
                
        State('DATA_STORE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
    )
    def FUNCTION___TABLE___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        n, study_area, aquifer, well, water_type, 
        wy, wys, wye,
        shy, shys, shye,
        para, statistical,
        data,
    ):
        if well is not None and len(well) == 1:
                    
            data = pd.DataFrame.from_dict(data)
            data = data[data["MAHDOUDE_NAME"].isin(study_area)]
            data = data[data["AQUIFER_NAME"].isin(aquifer)]
            data = data[data["LOCATION_NAME"].isin(well)]          
            data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
            data = data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            data["WATER_TABLE"] = data["WATER_TABLE"].round(2)
            data["WATER_LEVEL"] = data["WATER_LEVEL"].round(2)

            day_number = data["DAY_PERSIAN"].unique()[0]
            
            wysb = wys
            wyeb = wye
            shysb=shys
            shyeb=shye

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
            
            
            
            df = data[["YEAR_PERSIAN", "MONTH_PERSIAN", water_type]]
            df["YEAR_PERSIAN"] = df["YEAR_PERSIAN"].astype(int)
            df["MONTH_PERSIAN"] = df["MONTH_PERSIAN"].astype(int)
            df.columns = ["سال", "ماه", "پارامتر"]
            df = resultTable(df)
            
            if water_type == "WATER_LEVEL":

                df.columns = [
                    "سال",
                    "ماه",
                    "تراز ماهانه سطح آب",
                    "سال آبی",
                    "ماه آبی",
                    "تغییرات تراز سطح آب نسبت به ماه قبل",
                    "تغییرات تراز سطح آب نسبت به ماه سال قبل"
                ]
                
                para_dic = {
                    1 : "تراز ماهانه سطح آب",
                    2 : "تغییرات تراز سطح آب نسبت به ماه قبل",
                    3 : "تغییرات تراز سطح آب نسبت به ماه سال قبل",
                }
                
                title_dic = {
                    1 : f"تراز ماهانه (روز {day_number} ام) سطح آب زیرزمینی (متر) - {well[0]}",
                    2 : f"تغییرات تراز سطح آب زیرزمینی نسبت به ماه قبل (متر) - {well[0]}",
                    3 : f"تغییرات تراز سطح آب زیرزمینی نسبت به ماه سال قبل (متر) - {well[0]}",
                }  

            else:
                df.columns = [
                    "سال",
                    "ماه",
                    "عمق ماهانه سطح آب",
                    "سال آبی",
                    "ماه آبی",
                    "تغییرات عمق سطح آب نسبت به ماه قبل",
                    "تغییرات عمق سطح آب نسبت به ماه سال قبل"
                ]
                
                para_dic = {
                    1 : "عمق ماهانه سطح آب",
                    2 : "تغییرات عمق سطح آب نسبت به ماه قبل",
                    3 : "تغییرات عمق سطح آب نسبت به ماه سال قبل",
                }
                
                title_dic = {
                    1 : f"عمق ماهانه (روز {day_number} ام) سطح آب زیرزمینی (متر)",
                    2 : "تغییرات عمق سطح آب زیرزمینی نسبت به ماه قبل (متر)",
                    3 : "تغییرات عمق سطح آب زیرزمینی نسبت به ماه سال قبل (متر)",
                } 
        
            if wy is not None and wy == "waterYear":
                if wysb is not None and wysb != "" and wyeb is not None and wyeb != "" and wysb == wyeb:
                    col_name =  ["سال آبی", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]
                    value = df[para_dic[para]].to_list()
                    value = [wysb] + value
                    df_result = pd.DataFrame(columns=col_name)
                    df_result = df_result.append(pd.Series(value, index=col_name), ignore_index=True)
                else:
                    df_result = df.pivot_table(
                        values=para_dic[para],
                        index="سال آبی",
                        columns="ماه آبی"
                    ).reset_index()
                    df_result.columns = ["سال آبی", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]

            else:
                if shysb is not None and shysb != "" and shyeb is not None and shyeb != "" and shysb == shyeb:
                    col_name =  ["سال شمسی", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
                    value = df[para_dic[para]].to_list()
                    value = [shysb] + value
                    df_result = pd.DataFrame(columns=col_name)
                    df_result = df_result.append(pd.Series(value, index=col_name), ignore_index=True)
                else:
                    df_result = df.pivot_table(
                        values=para_dic[para],
                        index="سال",
                        columns="ماه"
                    ).reset_index()
                    df_result.columns = ["سال شمسی", "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
            
            if statistical is not None and 'OK' in statistical:
                if para == 1:
                    df_result["حداکثر سالانه"] = df_result.iloc[:,1:13].max(axis=1).round(2)
                    df_result["حداقل سالانه"] = df_result.iloc[:,1:13].min(axis=1).round(2)
                    df_result["میانگین سالانه"] = df_result.iloc[:,1:13].mean(axis=1).round(2)
                elif para == 2:
                    df_result["حداکثر سالانه"] = df_result.iloc[:,1:13].max(axis=1).round(2)
                    df_result["حداقل سالانه"] = df_result.iloc[:,1:13].min(axis=1).round(2)
                    df_result["میانگین سالانه"] = df_result.iloc[:,1:13].mean(axis=1).round(2)
                    df_result["تجمعی میانگین سالانه"] = df_result["میانگین سالانه"].cumsum(skipna=True).round(2) 
                    df_result["مجموع سالانه"] = df_result.iloc[:,1:13].sum(axis=1).round(2)
                    df_result["تجمعی مجموع سالانه"] = df_result["مجموع سالانه"].cumsum(skipna=True).round(2)
                elif para == 3:
                    df_result["حداکثر سالانه"] = df_result.iloc[:,1:13].max(axis=1).round(2)
                    df_result["حداقل سالانه"] = df_result.iloc[:,1:13].min(axis=1).round(2)
                    df_result["میانگین سالانه"] = df_result.iloc[:,1:13].mean(axis=1).round(2)
                    df_result["تغییرات میانگین سالانه"] = df_result["میانگین سالانه"].diff().round(2)
                    df_result["تجمعی میانگین سالانه"] = df_result["میانگین سالانه"].cumsum(skipna=True).round(2)
                    if wy == "waterYear":
                        df_result["مقدار تجمعی (مهر تا مهر)"] = df_result["مهر"].cumsum(skipna=True).round(2)

            return [
                [{"name": i, "id": i} for i in df_result.columns],
                df_result.to_dict('records'),
                False,
                title_dic[para]
            ]
        else:
            return [
                [{}],
                [],
                True,
                ""
            ]
            
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
        Output('SELECT_DATE_SELECT___COLLAPSE_PLOT_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'options'),
               
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
            
            global gdf, mask
            gdf_tmp = gdf.set_crs("EPSG:4326", allow_override=True)
            mask_tmp = mask.set_crs("EPSG:4326", allow_override=True)
            
            gdf_tmp = gdf_tmp[gdf_tmp["MAHDOUDE_NAME"] == study_area]
            gdf_tmp = gdf_tmp[gdf_tmp["AQUIFER_NAME"] == aquifer]
            gdf_tmp = gdf_tmp.reset_index(drop=True)
            mask_tmp = mask_tmp[mask_tmp["MAHDOUDE_NAME"] == study_area]
            mask_tmp = mask_tmp[mask_tmp["AQUIFER_NAME"] == aquifer]
            mask_tmp = mask_tmp.reset_index(drop=True)
            
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
                
            ## Thiessen Weighted Average
            if "TWA" in hydrograph_calculation_methods:
                tmp = data.groupby(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                    ).apply(
                        lambda x: calculate_thiessen_for_each_month(
                            df=x, 
                            water_table_level=water_table_level, 
                            gdf=gdf_tmp, 
                            mask=mask_tmp
                        )
                    ).reset_index().drop(columns=["level_4"])
                                
                tmp = tmp[[
                    "MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN", "THISSEN_LOCATION", "THISSEN_AQUIFER",	"geometry"
                ]]
                
                tmp_export = tmp.copy()
                tmp_export = tmp_export[
                    ["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_PERSIAN", "THISSEN_LOCATION", "THISSEN_AQUIFER", "geometry"]
                ]
                
                tmp_export = tmp_export.to_crs({'init': 'epsg:4326'}) 
                print(tmp_export)               
                tmp_export.to_file("./Assets/GeoDatabase/GeoJson/THISSEN.geojson", driver='GeoJSON')
                
                tmp = data.merge(
                    tmp, 
                    how="left", 
                    on=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                ).sort_values(
                    ["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", 'DATE_GREGORIAN']
                ).reset_index(drop=True)
                
                tmp['TMP'] = (tmp[water_table_level] * tmp['THISSEN_LOCATION']) / tmp['THISSEN_AQUIFER']
                
                tmp = tmp.groupby(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                ).sum().reset_index()[
                    ['MAHDOUDE_NAME', 'AQUIFER_NAME', 'DATE_GREGORIAN', 'DATE_PERSIAN', 'TMP']
                ].rename(columns={'TMP': 'TWA_UNIT_HYDROGRAPH'})
                
                result = result.merge(
                    tmp, 
                    how="left", 
                    on=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
                )
            
            return [
                0,
                "OK",
                result.to_dict('records'),
                [{'label': f'{date}', 'value': f'{date}'} for date in tmp["DATE_PERSIAN"].unique()]
            ]
                
            
        else:
            return [
                0,
                "NO",
                None,
                []
            ]
            
    
    
    # -----------------------------------------------------------------------------
    # GRAPH
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('GRAPH___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'figure'),
        Input('INTERVAL___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_intervals'),
        Input('WATER_TABLE_WATER_LEVEL_SELECT___COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('UNIT_HYDROGRAPH_DATA_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
        State('UNIT_HYDROGRAPH_DATA_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'data'),
    )
    def FUNCTION___GRAPH___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        n_interval, water_t_l, data_state, data
    ):
        if data_state == "OK":
                    
            data = pd.DataFrame.from_dict(data)
       
            data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
            
            data = data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            
            fig = go.Figure()
            
            if "AM_UNIT_HYDROGRAPH" in data.columns:
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
            
            if "GM_UNIT_HYDROGRAPH" in data.columns:
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
            
            if "HM_UNIT_HYDROGRAPH" in data.columns:
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
            
            if "TWA_UNIT_HYDROGRAPH" in data.columns:
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
                title=dict(
                    text="تراز ماهانه سطح آب آبخوان (متر)" if water_t_l == "WATER_LEVEL" else "عمق ماهانه سطح آب آبخوان (متر)",
                    yanchor="top",
                    y=0.98,
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
                    yanchor="top",
                    y=0.99,
                    xanchor="left",
                    x=0.01
                )
            )
            
            fig.update_xaxes(calendar='jalali')
            
            fig.update_layout(clickmode='event+select')
                                
            return fig  
        else:
            return NO_MATCHING_GRAPH_FOUND
            

    
    # -----------------------------------------------------------------------------
    # MAP - BODY
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('MAP___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'figure'),
        Output('MAP_HOLDER___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'hidden'),
        Input('INTERVAL___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'n_intervals'),         
        Input('SELECT_DATE_SELECT___COLLAPSE_PLOT_THIESSEN___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 'value'),
    )
    def FUNCTION___MAP___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER(
        n, date, study_area, aquifer
    ):
        if date is not None and date != "" and study_area is not None and len(study_area) != 0 and aquifer is not None and len(aquifer) != 0:           
            data = gpd.read_file("./Assets/GeoDatabase/GeoJson/THISSEN.geojson")
            data = data.to_crs({'init': 'epsg:4326'})
            COLs = ['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME']
            data[COLs] = data[COLs].apply(lambda x: x.str.replace('ي','ی'))
            data[COLs] = data[COLs].apply(lambda x: x.str.replace('ئ','ی'))
            data[COLs] = data[COLs].apply(lambda x: x.str.replace('ك', 'ک'))
            
            data = data[data["DATE_PERSIAN"] == date]
            
            fig = px.choropleth_mapbox(
                data_frame=data,
                geojson=data.geometry,
                locations=data.index,
                color="THISSEN_LOCATION",
                color_continuous_scale="Viridis",
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
                        'lat': data.centroid.y.mean(),
                        'lon': data.centroid.x.mean(),
                    },
                },
                showlegend = False,
                hovermode='closest',
                margin = {'l':0, 'r':0, 'b':0, 't':0}
            )
            
            return [
                fig,
                False
            ]        
        else:
            return [
                BASE_MAP,
                True
            ]