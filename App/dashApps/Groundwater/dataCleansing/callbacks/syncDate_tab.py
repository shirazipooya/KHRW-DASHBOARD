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
from App.dashApps.Groundwater.dataCleansing.layouts.sidebars.syncDate_tab import *



def groundwater___dataCleansing___callback___syncDate_tab(app):
    
    # -----------------------------------------------------------------------------
    # CHECK DATABASE EXIST AND STORE DATA
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('GROUNDWATER_SYNC_DATE_DATA_STATE___SYNC_DATE_TAB', 'data'),
        Output('GROUNDWATER_SYNC_DATE_DATA_STORE___SYNC_DATE_TAB', 'data'),

        Input('GROUNDWATER_SYNC_DATE_DATA_UPDATE_INTERVAL___SYNC_DATE_TAB', 'n_intervals'),
        State('GROUNDWATER_SYNC_DATE_DATA_UPDATE_STATE___SYNC_DATE_TAB', 'data')
    )
    def FUNCTION___DATABASE____SYNC_DATE_TAB(
        n, groundwater_sync_date_data_update_state
    ):
        print("FUNCTION___DATABASE____SYNC_DATE_TAB")
        if os.path.exists(PATH_DB_GROUNDWATER):
            TABLE_NAME = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", DB_GROUNDWATER)
            if TABLE_NAME['name'].str.contains('GEOINFO_DATA').any() and\
                TABLE_NAME['name'].str.contains('GROUNDWATER_RAW_DATA').any() and\
                    TABLE_NAME['name'].str.contains('GROUNDWATER_CLEANSING_DATA').any() and\
                        TABLE_NAME['name'].str.contains('GROUNDWATER_INTERPOLATED_DATA').any() and\
                            TABLE_NAME['name'].str.contains('GROUNDWATER_SYNCDATE_DATA').any():
                                if groundwater_sync_date_data_update_state == "YES":

                                    groundwater_sync_date = pd.read_sql_query(
                                        sql="SELECT * FROM GROUNDWATER_SYNCDATE_DATA",
                                        con=DB_GROUNDWATER
                                    ).drop(['index'], axis=1)
                                    
                                    return [
                                        "OK",
                                        groundwater_sync_date.to_dict('records'),
                                    ]
                                    
                                else:

                                    groundwater_sync_date = pd.read_sql_query(
                                        sql="SELECT * FROM GROUNDWATER_SYNCDATE_DATA",
                                        con=DB_GROUNDWATER
                                    ).drop(['index'], axis=1)
                                    
                                    return [
                                        "OK",
                                        groundwater_sync_date.to_dict('records'),
                                    ]  
            else:
                return [
                    "NO",
                    None,
                ]                        
        else:
            return [
                "NO",
                None,
            ]
    
    # -----------------------------------------------------------------------------
    # CHECK DATABASE EXIST AND STORE DATA
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('BUTTON___BUTTONS___SYNC_DATE_TAB', 'n_clicks'),
        Output('GROUNDWATER_SYNC_DATE_DATA_UPDATE_STATE___SYNC_DATE_TAB', 'data'),
        Output('GROUNDWATER_SYNC_DATE_DATA_UPDATE_INTERVAL___SYNC_DATE_TAB', 'n_intervals'),
        
        Input('INTERVAL___SYNC_DATE_TAB', 'n_intervals'),
        Input('BUTTON___BUTTONS___SYNC_DATE_TAB', 'n_clicks'),

        State('SYNC_METHOD_SELECT___CONTROLS___SYNC_DATE_TAB', 'value'),
        State('HOW_MODIFY_CARD___CONTROLS___SYNC_DATE_TAB', 'value'),
    )
    def FUNCTION___SYNCDATE____SYNC_DATE_TAB(
        n_interval, n_click, method, how_modify
    ):
        print("FUNCTION___SYNCDATE____SYNC_DATE_TAB")
        if n_click != 0:
            
            data_interpolated = pd.read_sql_query(
                sql="SELECT * FROM GROUNDWATER_INTERPOLATED_DATA",
                con=DB_GROUNDWATER
            ).drop(['index'], axis=1)
                                

            synchronize_date(
                data_interpolated=data_interpolated,
                method=method,
                how_modify=how_modify
            )
            
            return [
                0,
                "YES",
                0,
            ]
                            
        else:
            
            return [
                0,
                "NO",
                1
            ]

    # -----------------------------------------------------------------------------
    # OPEN CLOSE COLLAPSE
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("COLLAPSE___SELECT_WELL___SYNC_DATE_TAB", "is_open"),
        Output("ARROW___SELECT_WELL___SYNC_DATE_TAB", "className"),
        Output("COLLAPSE___SYNC_METHOD___SYNC_DATE_TAB", "is_open"),
        Output("ARROW___SYNC_METHOD___SYNC_DATE_TAB", "className"),
        Output("COLLAPSE___HOW_MODIFY___SYNC_DATE_TAB", "is_open"),
        Output("ARROW___HOW_MODIFY___SYNC_DATE_TAB", "className"),
        Input("OPEN_CLOSE_COLLAPSE___SELECT_WELL___SYNC_DATE_TAB", "n_clicks"),
        Input("OPEN_CLOSE_COLLAPSE___SYNC_METHOD___SYNC_DATE_TAB", "n_clicks"),
        Input("OPEN_CLOSE_COLLAPSE___HOW_MODIFY___SYNC_DATE_TAB", "n_clicks"),
        State("COLLAPSE___SELECT_WELL___SYNC_DATE_TAB", "is_open"),
        State("COLLAPSE___SYNC_METHOD___SYNC_DATE_TAB", "is_open"),
        State("COLLAPSE___HOW_MODIFY___SYNC_DATE_TAB", "is_open"),
    )
    def FUNCTION__COLLAPSE___SYNC_DATE_TAB(
        n_select_well, n_select_method, n_select_outlier,
        state_select_well, state_select_method, state_select_outlier,
    ):
        print("FUNCTION__COLLAPSE___SYNC_DATE_TAB")
        ctx = dash.callback_context

        if not ctx.triggered:
            return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2",  False, "fas fa-caret-left ml-2",

        else:
            button_id = ctx.triggered[0]["prop_id"].split(".")[0]
            
            if button_id == "OPEN_CLOSE_COLLAPSE___SELECT_WELL___SYNC_DATE_TAB" and n_select_well:
                if not state_select_well:
                    return True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE_COLLAPSE___SYNC_METHOD___SYNC_DATE_TAB" and n_select_method:
                if not state_select_method:
                    return False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE_COLLAPSE___HOW_MODIFY___SYNC_DATE_TAB" and n_select_outlier:
                if not state_select_outlier:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            else:
                return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2",



    # -----------------------------------------------------------------------------
    # STUDY AREA SELECT - CONTROLS - SYNC DATE TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('STUDY_AREA_SELECT___CONTROLS___SYNC_DATE_TAB', 'options'),
        Input('GEOINFO_DATA_STATE___DATA_CLEANSING_TAB', 'data'),
        Input('GEOINFO_DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___STUDY_AREA_SELECT___CONTROLS___SYNC_DATE_TAB(geoinfo_state, geoInfo): 
        print("FUNCTION___STUDY_AREA_SELECT___CONTROLS___SYNC_DATE_TAB")     
        if geoinfo_state == "OK" and geoInfo is not None:
            geoInfo = pd.DataFrame.from_dict(geoInfo)
            return [{"label": col, "value": col} for col in geoInfo['MAHDOUDE_NAME'].unique()]        
        else:
            return []
    
    
    
    # -----------------------------------------------------------------------------
    # AQUIFER SELECT - CONTROLS - SYNC DATE TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('AQUIFER_SELECT___CONTROLS___SYNC_DATE_TAB', 'options'),
        Input('STUDY_AREA_SELECT___CONTROLS___SYNC_DATE_TAB', 'value'),
        Input('GEOINFO_DATA_STATE___DATA_CLEANSING_TAB', 'data'),
        Input('GEOINFO_DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___AQUIFER_SELECT___CONTROLS___SYNC_DATE_TAB(study_area, geoinfo_state, geoInfo):
        print("FUNCTION___AQUIFER_SELECT___CONTROLS___SYNC_DATE_TAB")
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
    # WELL SELECT - CONTROLS - SYNC DATE TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('WELL_SELECT___CONTROLS___SYNC_DATE_TAB', 'options'),
        Input('STUDY_AREA_SELECT___CONTROLS___SYNC_DATE_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___SYNC_DATE_TAB', 'value'),
        Input('GEOINFO_DATA_STATE___DATA_CLEANSING_TAB', 'data'),
        Input('GEOINFO_DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___WELL_SELECT___CONTROLS___SYNC_DATE_TAB(study_area, aquifer, geoinfo_state, geoInfo):
        print("FUNCTION___WELL_SELECT___CONTROLS___SYNC_DATE_TAB")
        if geoinfo_state == "OK" and geoInfo is not None:
            if study_area is not None and len(study_area) != 0 and aquifer is not None and len(aquifer) != 0:
                geoInfo = pd.DataFrame.from_dict(geoInfo)
                geoInfo = geoInfo[geoInfo["MAHDOUDE_NAME"] == study_area]
                geoInfo = geoInfo[geoInfo["AQUIFER_NAME"] == aquifer]
                return [{"label": col, "value": col} for col in geoInfo['LOCATION_NAME'].unique()]
            else:
                return []
        else:
            return []
    

    # -----------------------------------------------------------------------------
    # GRAPH - GRAPH & MAP - SYNC DATE TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('GRAPH___SYNC_DATE_TAB', 'figure'),
         
        Input('INTERVAL___SYNC_DATE_TAB', 'n_intervals'),
        
        Input('STUDY_AREA_SELECT___CONTROLS___SYNC_DATE_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___SYNC_DATE_TAB', 'value'),
        Input('WELL_SELECT___CONTROLS___SYNC_DATE_TAB', 'value'),


        State('GROUNDWATER_RAW_DATA_STORE___DATA_CLEANSING_TAB', 'data'),
        State('GROUNDWATER_CLEANSING_DATA_STORE___DATA_CLEANSING_TAB', 'data'),
        State('GROUNDWATER_INTERPOLATED_DATA_STORE___MISSING_DATA_TAB', 'data'),
        State('GROUNDWATER_SYNC_DATE_DATA_STORE___SYNC_DATE_TAB', 'data'),
    )
    def FUNCTION___GRAPH___SYNC_DATE_TAB(
        n_interval, study_area, aquifer, well, groundwater_raw_data, groundwater_cleansing_data, groundwater_interpolated_data, groundwater_syncdate_data
    ): 
        print("FUNCTION___GRAPH___SYNC_DATE_TAB")
        if well is not None and len(well) != 0:

            # groundwater raw data
            groundwater_raw_data = pd.DataFrame.from_dict(groundwater_raw_data)
            groundwater_raw_data = groundwater_raw_data[groundwater_raw_data["MAHDOUDE_NAME"] == study_area]
            groundwater_raw_data = groundwater_raw_data[groundwater_raw_data["AQUIFER_NAME"] == aquifer]
            groundwater_raw_data = groundwater_raw_data[groundwater_raw_data["LOCATION_NAME"] == well]
            groundwater_raw_data["DATE_GREGORIAN"] = groundwater_raw_data["DATE_GREGORIAN"].apply(pd.to_datetime)
            groundwater_raw_data = groundwater_raw_data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            groundwater_raw_data = groundwater_raw_data[["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN", "WATER_TABLE"]]
            
            # groundwater cleansing data
            groundwater_cleansing_data = pd.DataFrame.from_dict(groundwater_cleansing_data)
            groundwater_cleansing_data = groundwater_cleansing_data[groundwater_cleansing_data["MAHDOUDE_NAME"] == study_area]
            groundwater_cleansing_data = groundwater_cleansing_data[groundwater_cleansing_data["AQUIFER_NAME"] == aquifer]
            groundwater_cleansing_data = groundwater_cleansing_data[groundwater_cleansing_data["LOCATION_NAME"] == well]
            groundwater_cleansing_data["DATE_GREGORIAN"] = groundwater_cleansing_data["DATE_GREGORIAN"].apply(pd.to_datetime)
            groundwater_cleansing_data = groundwater_cleansing_data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            groundwater_cleansing_data = groundwater_cleansing_data[["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN", "WATER_TABLE"]]

            
            # groundwater interpolated data
            groundwater_interpolated_data = pd.DataFrame.from_dict(groundwater_interpolated_data)
            groundwater_interpolated_data = groundwater_interpolated_data[groundwater_interpolated_data["MAHDOUDE_NAME"] == study_area]
            groundwater_interpolated_data = groundwater_interpolated_data[groundwater_interpolated_data["AQUIFER_NAME"] == aquifer]
            groundwater_interpolated_data = groundwater_interpolated_data[groundwater_interpolated_data["LOCATION_NAME"] == well]
            groundwater_interpolated_data["DATE_GREGORIAN"] = groundwater_interpolated_data["DATE_GREGORIAN"].apply(pd.to_datetime)
            groundwater_interpolated_data = groundwater_interpolated_data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            groundwater_interpolated_data = groundwater_interpolated_data[["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN", "WATER_TABLE"]]
            

            # groundwater raw data
            groundwater_syncdate_data = pd.DataFrame.from_dict(groundwater_syncdate_data)
            groundwater_syncdate_data = groundwater_syncdate_data[groundwater_syncdate_data["MAHDOUDE_NAME"] == study_area]
            groundwater_syncdate_data = groundwater_syncdate_data[groundwater_syncdate_data["AQUIFER_NAME"] == aquifer]
            groundwater_syncdate_data = groundwater_syncdate_data[groundwater_syncdate_data["LOCATION_NAME"] == well]
            groundwater_syncdate_data["DATE_GREGORIAN"] = groundwater_syncdate_data["DATE_GREGORIAN"].apply(pd.to_datetime)
            groundwater_syncdate_data = groundwater_syncdate_data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            groundwater_syncdate_data = groundwater_syncdate_data[["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN", "WATER_TABLE", "DATE_GREGORIAN_RAW"]]

            groundwater_syncdate_data.rename(
                columns={
                    'DATE_GREGORIAN': 'DATE_GREGORIAN_NEW',
                    'DATE_GREGORIAN_RAW': 'DATE_GREGORIAN'
                    },
                inplace=True
            )


            # PLOT
            fig = go.Figure()

            groundwater_raw_data_w = groundwater_raw_data[groundwater_raw_data["LOCATION_NAME"] == well]
            groundwater_raw_data_w = groundwater_raw_data_w.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            groundwater_raw_data_w.rename(columns={"WATER_TABLE": "WATER_TABLE_RAW"}, inplace=True)

                                            
            groundwater_cleansing_data_w = groundwater_cleansing_data[groundwater_cleansing_data["LOCATION_NAME"] == well]
            groundwater_cleansing_data_w = groundwater_cleansing_data_w.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            groundwater_cleansing_data_w.rename(columns={"WATER_TABLE": "WATER_TABLE_CLEANSING"}, inplace=True)

            
            groundwater_interpolated_data_w = groundwater_interpolated_data[groundwater_interpolated_data["LOCATION_NAME"] == well]
            groundwater_interpolated_data_w = groundwater_interpolated_data_w.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            groundwater_interpolated_data_w.rename(columns={"WATER_TABLE": "WATER_TABLE_INTERPOLATED"}, inplace=True)
            

            groundwater_syncdate_data = groundwater_syncdate_data[groundwater_syncdate_data["LOCATION_NAME"] == well]
            groundwater_syncdate_data = groundwater_syncdate_data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            groundwater_syncdate_data.rename(columns={"WATER_TABLE": "WATER_TABLE_SYNCDATE"}, inplace=True)
            groundwater_syncdate_data["DATE_GREGORIAN"] = groundwater_syncdate_data["DATE_GREGORIAN"].apply(pd.to_datetime)
            groundwater_syncdate_data["DATE_GREGORIAN_NEW"] = groundwater_syncdate_data["DATE_GREGORIAN_NEW"].apply(pd.to_datetime)

            
            df_w = pd.merge(
                left=groundwater_interpolated_data_w,
                right=groundwater_cleansing_data_w,
                on=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"],
                how="left"
            )
            
            
            df_w = pd.merge(
                left=df_w,
                right=groundwater_raw_data_w,
                on=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"],
                how="left"
            )

            df_w["DATE_GREGORIAN"] = df_w["DATE_GREGORIAN"].apply(pd.to_datetime)

            df_w = pd.merge(
                left=groundwater_syncdate_data,
                right=df_w,
                on=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"],
                how="left"
            )
            
            
            df_w = df_w[
                ["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN_NEW", "DATE_GREGORIAN", "WATER_TABLE_RAW", "WATER_TABLE_CLEANSING", "WATER_TABLE_INTERPOLATED", "WATER_TABLE_SYNCDATE"]
            ]

            
            df_w["CHANGE_WATER_TABLE"] = np.where(
                df_w["WATER_TABLE_INTERPOLATED"] == df_w["WATER_TABLE_RAW"],
                "blue",
                np.where(
                    df_w["WATER_TABLE_INTERPOLATED"] == df_w["WATER_TABLE_CLEANSING"],
                    "red",
                    "green"
                )
            )

            df_w["DATE_GREGORIAN_NEW"] = df_w["DATE_GREGORIAN_NEW"].apply(pd.to_datetime)

            
            fig.add_trace(
                go.Scatter(
                    x=df_w['DATE_GREGORIAN_NEW'],
                    y=df_w['WATER_TABLE_SYNCDATE'],
                    mode='lines+markers',
                    name=f'داده‌های هماهنگ‌سازی شده تاریخ - {well}',
                    marker=dict(
                        color=df_w["CHANGE_WATER_TABLE"],
                        size=10,
                    ),
                    line=dict(
                        color='blue',
                        width=1
                    )  
                )
            )


            fig.update_layout(
                hoverlabel=dict(
                    namelength = -1
                ),
                # yaxis_title="عمق سطح آب - متر",
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
                    text='عمق ماهانه سطح آب (متر)',
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
            
            fig.update_xaxes(calendar='jalali')
                            
            return fig

        else:
            return NO_MATCHING_GRAPH_FOUND
        
