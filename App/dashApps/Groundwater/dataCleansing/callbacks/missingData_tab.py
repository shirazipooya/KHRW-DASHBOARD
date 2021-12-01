import os
import sqlite3
import json
import pandas as pd
from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash.exceptions import PreventUpdate
import dash


from App.dashApps.Groundwater.dataCleansing.callbacks.config import *
from App.dashApps.Groundwater.dataCleansing.layouts.sidebars.missingData_tab import *



def groundwater___dataCleansing___callback___missingData_tab(app):
    
    
    # -----------------------------------------------------------------------------
    # CHECK DATABASE EXIST AND STORE DATA
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('DATABASE_STATE___MISSING_DATA_TAB', 'data'),
        Output('DATA_STORE___MISSING_DATA_TAB', 'data'),
        Output('GEOINFO_DATA_STORE___MISSING_DATA_TAB', 'data'),
        Output('BUTTON___BUTTONS___MISSING_DATA_TAB', 'n_clicks'),
        Input('LOAD_DATABASE___MISSING_DATA_TAB', 'n_intervals'),
        Input('BUTTON___BUTTONS___MISSING_DATA_TAB', 'n_clicks'),
        State('DATA_STORE___MISSING_DATA_TAB', 'data'),
        State('INTERPOLATE_METHOD_SELECT___CONTROLS___MISSING_DATA_TAB', 'value'),
        State('ORDER_INTERPOLATE_METHOD_SELECT___CONTROLS___MISSING_DATA_TAB', 'value'),
        State('DURATION_SELECT___CONTROLS___MISSING_DATA_TAB', 'value'),
    )
    def FUNCTION___DATABASE____MISSING_DATA_TAB(n_interval, n_click, data, method, order, limit):
        if os.path.exists(PATH_DB_GROUNDWATER):
            TABLE_NAME = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", DB_GROUNDWATER)
            if TABLE_NAME['name'].str.contains('GROUNDWATER_DATA').any():
                if n_click != 0:
                    data = pd.read_sql_query(
                        sql="SELECT * FROM GROUNDWATER_DATA",
                        con=DB_GROUNDWATER
                    ).drop(['index'], axis=1)
                    
                    if "DATE_GREGORIAN" in data.columns:
                        data.drop(["DATE_GREGORIAN", "DATE_PERSIAN", "WATER_TABLE"], axis=1, inplace=True)
                    
                    data = date_fix___interpolate___missingData(
                        data=data,
                        con=DB_GROUNDWATER,
                        name="GROUNDWATER_DATA",
                        if_exists="replace",
                        method=method,
                        order=order,
                        limit=limit
                    )

                    geoInfo = pd.read_sql_query(
                        sql="SELECT * FROM GEOINFO_DATA",
                        con=DB_GROUNDWATER
                    ).drop(['index'], axis=1)
                    
                    return [
                        "OK",
                        data.to_dict('records'),
                        geoInfo.to_dict('records'),
                        0,
                    ]
                else:
                    data = pd.read_sql_query(
                        sql="SELECT * FROM GROUNDWATER_DATA",
                        con=DB_GROUNDWATER
                    ).drop(['index'], axis=1)
                    
                    geoInfo = pd.read_sql_query(
                        sql="SELECT * FROM GEOINFO_DATA",
                        con=DB_GROUNDWATER
                    ).drop(['index'], axis=1)
                    
                    return [
                        "OK",
                        data.to_dict('records'),
                        geoInfo.to_dict('records'),
                        0,
                    ]
            else:
                return [
                    "NO",
                    None,
                    None,
                    0,
                ]                        
        else:
            return [
                "NO",
                None,
                None,
                0,
            ]

    # -----------------------------------------------------------------------------
    # OPEN CLOSE COLLAPSE
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("COLLAPSE___SELECT_WELL___MISSING_DATA_TAB", "is_open"),
        Output("ARROW___SELECT_WELL___MISSING_DATA_TAB", "className"),
        Output("COLLAPSE___INTERPOLATE_METHOD___MISSING_DATA_TAB", "is_open"),
        Output("ARROW___INTERPOLATE_METHOD___MISSING_DATA_TAB", "className"),
        Output("COLLAPSE___HOW_MODIFY___MISSING_DATA_TAB", "is_open"),
        Output("ARROW___HOW_MODIFY___MISSING_DATA_TAB", "className"),
        Input("OPEN_CLOSE_COLLAPSE___SELECT_WELL___MISSING_DATA_TAB", "n_clicks"),
        Input("OPEN_CLOSE_COLLAPSE___INTERPOLATE_METHOD___MISSING_DATA_TAB", "n_clicks"),
        Input("OPEN_CLOSE_COLLAPSE___HOW_MODIFY___MISSING_DATA_TAB", "n_clicks"),
        State("COLLAPSE___SELECT_WELL___MISSING_DATA_TAB", "is_open"),
        State("COLLAPSE___INTERPOLATE_METHOD___MISSING_DATA_TAB", "is_open"),
        State("COLLAPSE___HOW_MODIFY___MISSING_DATA_TAB", "is_open"),
    )
    def FUNCTION__COLLAPSE___MISSING_DATA_TAB(
        n_select_well, n_select_method, n_select_outlier,
        state_select_well, state_select_method, state_select_outlier,
    ):
        ctx = dash.callback_context

        if not ctx.triggered:
            return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2",  False, "fas fa-caret-left ml-2",

        else:
            button_id = ctx.triggered[0]["prop_id"].split(".")[0]
            
            if button_id == "OPEN_CLOSE_COLLAPSE___SELECT_WELL___MISSING_DATA_TAB" and n_select_well:
                if not state_select_well:
                    return True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE_COLLAPSE___INTERPOLATE_METHOD___MISSING_DATA_TAB" and n_select_method:
                if not state_select_method:
                    return False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE_COLLAPSE___HOW_MODIFY___MISSING_DATA_TAB" and n_select_outlier:
                if not state_select_outlier:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            else:
                return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2",



    # -----------------------------------------------------------------------------
    # STUDY AREA SELECT - CONTROLS - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('STUDY_AREA_SELECT___CONTROLS___MISSING_DATA_TAB', 'options'),
        Input('DATABASE_STATE___MISSING_DATA_TAB', 'data'),
        Input('GEOINFO_DATA_STORE___MISSING_DATA_TAB', 'data')
    )
    def FUNCTION___STUDY_AREA_SELECT___CONTROLS___MISSING_DATA_TAB(database_state, geoInfo):        
        if database_state == "OK" and geoInfo is not None:
            geoInfo = pd.DataFrame.from_dict(geoInfo)
            return [{"label": col, "value": col} for col in geoInfo['MAHDOUDE_NAME'].unique()]        
        else:
            return []
    
    
    
    # -----------------------------------------------------------------------------
    # AQUIFER SELECT - CONTROLS - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('AQUIFER_SELECT___CONTROLS___MISSING_DATA_TAB', 'options'),
        Input('STUDY_AREA_SELECT___CONTROLS___MISSING_DATA_TAB', 'value'),
        Input('DATABASE_STATE___MISSING_DATA_TAB', 'data'),
        Input('GEOINFO_DATA_STORE___MISSING_DATA_TAB', 'data')
    )
    def FUNCTION___AQUIFER_SELECT___CONTROLS___MISSING_DATA_TAB(study_area, database_state, geoInfo):
        if database_state == "OK" and geoInfo is not None:
            if study_area is not None and len(study_area) != 0:
                geoInfo = pd.DataFrame.from_dict(geoInfo)
                geoInfo = geoInfo[geoInfo["MAHDOUDE_NAME"].isin(study_area)]
                return [{"label": col, "value": col} for col in geoInfo['AQUIFER_NAME'].unique()]
            else:
                return []
        else:
            return []



    # -----------------------------------------------------------------------------
    # WELL SELECT - CONTROLS - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('WELL_SELECT___CONTROLS___MISSING_DATA_TAB', 'options'),
        Input('STUDY_AREA_SELECT___CONTROLS___MISSING_DATA_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___MISSING_DATA_TAB', 'value'),
        Input('DATABASE_STATE___MISSING_DATA_TAB', 'data'),
        Input('GEOINFO_DATA_STORE___MISSING_DATA_TAB', 'data')
    )
    def FUNCTION___WELL_SELECT___CONTROLS___MISSING_DATA_TAB(study_area, aquifer, database_state, geoInfo):
        if database_state == "OK" and geoInfo is not None:
            if study_area is not None and len(study_area) != 0 and aquifer is not None and len(aquifer) != 0:
                geoInfo = pd.DataFrame.from_dict(geoInfo)
                geoInfo = geoInfo[geoInfo["MAHDOUDE_NAME"].isin(study_area)]
                geoInfo = geoInfo[geoInfo["AQUIFER_NAME"].isin(aquifer)]
                return [{"label": col, "value": col} for col in geoInfo['LOCATION_NAME'].unique()]
            else:
                return []
        else:
            return []
    
    
    
    # -----------------------------------------------------------------------------
    # GRAPH - GRAPH & MAP - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('GRAPH___MISSING_DATA_TAB', 'figure'),
         
        Input('LOAD_DATABASE___MISSING_DATA_TAB', 'n_intervals'),
        Input('STUDY_AREA_SELECT___CONTROLS___MISSING_DATA_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___MISSING_DATA_TAB', 'value'),
        Input('WELL_SELECT___CONTROLS___MISSING_DATA_TAB', 'value'),
        Input('INTERPOLATE_METHOD_SELECT___CONTROLS___MISSING_DATA_TAB', 'value'),
        Input('ORDER_INTERPOLATE_METHOD_SELECT___CONTROLS___MISSING_DATA_TAB', 'value'),
        Input('DURATION_SELECT___CONTROLS___MISSING_DATA_TAB', 'value'),
        State('DATA_STORE___MISSING_DATA_TAB', 'data')
    )
    def FUNCTION___GRAPH___MISSING_DATA_TAB(n_interval, study_area, aquifer, well, method, order, duration, data):        
        if study_area is not None and len(study_area) != 0 and\
            aquifer is not None and len(aquifer) != 0 and\
                well is not None and len(well) != 0 and method is not None:
                    
                    data = pd.DataFrame.from_dict(data)
                    data = data[data["MAHDOUDE_NAME"].isin(study_area)]
                    data = data[data["AQUIFER_NAME"].isin(aquifer)]
                    data = data[data["LOCATION_NAME"].isin(well)]
                    data = data.sort_values(
                        by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN_RAW"]
                    ).reset_index(drop=True)
                    
                    # PLOT
                    fig = go.Figure()
                                    
                    for w in well:                    
                        df_w = data[data["LOCATION_NAME"] == w]
                        
                        df_w = df_w.sort_values(
                            by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN_RAW"]
                        ).reset_index(drop=True)
                        
                        fig.add_trace(
                            go.Scatter(
                                x=df_w['DATE_PERSIAN'],
                                y=df_w['WATER_TABLE'],
                                mode='lines+markers',
                                name=f'داده‌های اصلاح شده - {w}',
                                marker=dict(
                                    color='red',
                                    size=8,
                                ),
                                line=dict(
                                    color='red',
                                    width=1
                                )  
                            )
                        )
                    
                                            
                        if "WATER_TABLE_INTERPOLATE" in data.columns: 
                            fig.add_trace(
                                go.Scatter(
                                    x=df_w['DATE_PERSIAN'],
                                    y=df_w['WATER_TABLE_INTERPOLATE'],
                                    mode='lines+markers',
                                    name=f'داده‌های بازسازی شده - {w}',
                                    marker=dict(
                                        color='green',
                                        size=8,
                                    ),
                                    line=dict(
                                        color='green',
                                        width=1
                                    )  
                                )
                            ),
                            
                        
                    
                # fig.update_traces(hovertemplate=None)

                    fig.update_layout(
                        hoverlabel=dict(
                            namelength = -1
                        ),
                        # hovermode="x unified",
                        yaxis_title="ارتفاع سطح ایستابی - متر",
                        autosize=False,
                        font=dict(
                            family="Vazir-FD",
                            size=14,
                            color="RebeccaPurple"
                        ),
                        xaxis=dict(
                            tickformat="%Y-%m-%d"
                        ),
                        title=dict(
                            text='ارتفاع ماهانه سطح ایستابی',
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
                    
                    fig.update_layout(clickmode='event+select')
                                    
                    return fig

        else:
            return NO_MATCHING_GRAPH_FOUND
        
        
    @app.callback(
        Output('ORDER_INTERPOLATE_METHOD_SELECT___CONTROLS___MISSING_DATA_TAB', 'disabled'),
        Input('INTERPOLATE_METHOD_SELECT___CONTROLS___MISSING_DATA_TAB', 'value'),
    )
    def FUNCTION___SELECT_ORDER_INTERPOLATE_METHOD___MISSING_DATA_TAB(
        method
    ):
        if method in ["polynomial", "spline"]:
            return False
        else:
            return True