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


from App.dashApps.Groundwater.dataCleansing.callbacks.config import *
from App.dashApps.Groundwater.dataCleansing.layouts.sidebars.dataCleansing_tab import *



def groundwater___dataCleansing___callback___dataCleansing_tab(app):

    # -----------------------------------------------------------------------------
    # CHECK DATABASE EXIST AND STORE DATA
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('GEOINFO_DATA_STORE___DATA_CLEANSING_TAB', 'data'),
        Output('GEOINFO_DATA_STATE___DATA_CLEANSING_TAB', 'data'),
        Output('GROUNDWATER_RAW_DATA_STORE___DATA_CLEANSING_TAB', 'data'),
        Output('GROUNDWATER_RAW_DATA_STATE___DATA_CLEANSING_TAB', 'data'),
        Output('GROUNDWATER_CLEANSING_DATA_STORE___DATA_CLEANSING_TAB', 'data'),
        Output('GROUNDWATER_CLEANSING_DATA_STATE___DATA_CLEANSING_TAB', 'data'),
        Input('GROUNDWATER_CLEANSING_DATA_UPDATE_INTERVAL___DATA_CLEANSING_TAB', 'n_intervals'),
        State('GROUNDWATER_CLEANSING_DATA_UPDATE_STATE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___DATABASE____DATA_CLEANSING_TAB(n, groundwater_cleansing_data_update_state):
        print("FUNCTION___DATABASE____DATA_CLEANSING_TAB")
        if os.path.exists(PATH_DB_GROUNDWATER):
            TABLE_NAME = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", DB_GROUNDWATER)
            if TABLE_NAME['name'].str.contains('GEOINFO_DATA').any() and\
                TABLE_NAME['name'].str.contains('GROUNDWATER_RAW_DATA').any() and\
                    TABLE_NAME['name'].str.contains('GROUNDWATER_CLEANSING_DATA').any():
                        if groundwater_cleansing_data_update_state == "YES":
                            
                            geoInfo = pd.read_sql_query(
                                sql="SELECT * FROM GEOINFO_DATA",
                                con=DB_GROUNDWATER
                            ).drop(['index'], axis=1)
                            
                            groundwater_raw = pd.read_sql_query(
                                sql="SELECT * FROM GROUNDWATER_RAW_DATA",
                                con=DB_GROUNDWATER
                            ).drop(['index'], axis=1)
                            
                            groundwater_cleansing = pd.read_sql_query(
                                sql="SELECT * FROM GROUNDWATER_CLEANSING_DATA",
                                con=DB_GROUNDWATER
                            ).drop(['index'], axis=1)
                            
                            return [
                                geoInfo.to_dict('records'),
                                "OK",
                                groundwater_raw.to_dict('records'),
                                "OK",
                                groundwater_cleansing.to_dict('records'),
                                "OK",
                            ]
                        else:
                            geoInfo = pd.read_sql_query(
                                sql="SELECT * FROM GEOINFO_DATA",
                                con=DB_GROUNDWATER
                            ).drop(['index'], axis=1)
                            
                            groundwater_raw = pd.read_sql_query(
                                sql="SELECT * FROM GROUNDWATER_RAW_DATA",
                                con=DB_GROUNDWATER
                            ).drop(['index'], axis=1)
                            
                            groundwater_cleansing = pd.read_sql_query(
                                sql="SELECT * FROM GROUNDWATER_CLEANSING_DATA",
                                con=DB_GROUNDWATER
                            ).drop(['index'], axis=1)
                            
                            return [
                                geoInfo.to_dict('records'),
                                "OK",
                                groundwater_raw.to_dict('records'),
                                "OK",
                                groundwater_cleansing.to_dict('records'),
                                "OK",
                            ]   
            else:
                return [
                    None,
                    "NO",
                    None,
                    "NO",
                    None,
                    "NO",
                ]                        
        else:
            return [
                None,
                "NO",
                None,
                "NO",
                None,
                "NO",
            ]
    
    
    # -----------------------------------------------------------------------------
    # UPDATE DATABASE
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('BUTTON___BUTTONS___DATA_CLEANSING_TAB', 'n_clicks'),
        Output('GROUNDWATER_CLEANSING_DATA_UPDATE_STATE___DATA_CLEANSING_TAB', 'data'),
        Output('GROUNDWATER_CLEANSING_DATA_UPDATE_INTERVAL___DATA_CLEANSING_TAB', 'n_intervals'),
        
        Input('INTERVAL___DATA_CLEANSING_TAB', 'n_intervals'),
        
        Input('BUTTON___BUTTONS___DATA_CLEANSING_TAB', 'n_clicks'),
        
        State('GRAPH_SELECTED_DATA_STORE___DATA_CLEANSING_TAB', 'data'),
        
        State('TABLE_SELECTED___DATA_CLEANSING_TAB', 'data'),
        
        State('GROUNDWATER_CLEANSING_DATA_STORE___DATA_CLEANSING_TAB', 'data')
        
        # State('GROUNDWATER_CLEANSING_DATA_UPDATE_STATE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___MODIFY_DATABASE____DATA_CLEANSING_TAB(
        n_interval, n_click, graphData_selected, tableData, data#, database_update_state
    ):
        print("FUNCTION___MODIFY_DATABASE____DATA_CLEANSING_TAB")
        if (n_click != 0) and (graphData_selected is not None):
            
            data = pd.DataFrame.from_dict(data)
            
            graphData_selected = pd.DataFrame.from_dict(graphData_selected)

            df = pd.DataFrame(tableData).reset_index(drop=True)
            
            df = df.rename(
                columns={
                    'محدوده مطالعاتی': 'MAHDOUDE_NAME',
                    'آبخوان': 'AQUIFER_NAME',
                    'چاه مشاهداتی': 'LOCATION_NAME',
                    'تاریخ': 'DATE_PERSIAN',
                    'داده خام سطح آب': 'WATER_TABLE_RAW',
                    'داده اصلاح شده سطح آب': 'WATER_TABLE_CLEANSING',
                    'توضیحات': 'DESCRIPTION',
                }
            )

                    
            if len(graphData_selected) != len(df):
                if len(df) != 0:
                    df['WATER_TABLE_RAW'] = df['WATER_TABLE_RAW'].astype('float64')
                    df['WATER_TABLE_CLEANSING'] = df['WATER_TABLE_CLEANSING'].astype('float64')
                    graphData_selected['WATER_TABLE_RAW'] = graphData_selected['WATER_TABLE_RAW'].astype('float64')
                    graphData_selected['WATER_TABLE_CLEANSING'] = graphData_selected['WATER_TABLE_CLEANSING'].astype('float64')
                    
                    deleted_row = graphData_selected.merge(df, on=['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME', 'DATE_PERSIAN'], how = 'outer' , indicator=True)
                    deleted_row = deleted_row[(deleted_row['_merge'] == "left_only")]
                    deleted_row = deleted_row.reset_index(drop=True)
                
                    for i in range(len(deleted_row)):
                        MN_D = deleted_row.loc[i, "MAHDOUDE_NAME"]
                        AN_D = deleted_row.loc[i, "AQUIFER_NAME"]
                        LN_D = deleted_row.loc[i, "LOCATION_NAME"]
                        DPR_D =  deleted_row.loc[i, "DATE_PERSIAN"]

                        index_names = data[
                            (data['MAHDOUDE_NAME'] == MN_D) & \
                                (data['AQUIFER_NAME'] == AN_D) & \
                                    (data['LOCATION_NAME'] == LN_D) & \
                                        (data['DATE_PERSIAN'] == DPR_D)
                        ].index

                        data.drop(index_names, inplace=True)

                        data = data.reset_index(drop=True)
                else:
                    graphData_selected['WATER_TABLE_RAW'] = graphData_selected['WATER_TABLE_RAW'].astype('float64')
                    graphData_selected['WATER_TABLE_CLEANSING'] = graphData_selected['WATER_TABLE_CLEANSING'].astype('float64')
                    deleted_row = graphData_selected.reset_index(drop=True)
                
                    for i in range(len(deleted_row)):
                        MN_D = deleted_row.loc[i, "MAHDOUDE_NAME"]
                        AN_D = deleted_row.loc[i, "AQUIFER_NAME"]
                        LN_D = deleted_row.loc[i, "LOCATION_NAME"]
                        DPR_D =  deleted_row.loc[i, "DATE_PERSIAN"]

                        index_names = data[
                            (data['MAHDOUDE_NAME'] == MN_D) & \
                                (data['AQUIFER_NAME'] == AN_D) & \
                                    (data['LOCATION_NAME'] == LN_D) & \
                                        (data['DATE_PERSIAN'] == DPR_D)
                        ].index

                        data.drop(index_names, inplace=True)

                        data = data.reset_index(drop=True)

            if len(df) != 0:
                df['WATER_TABLE_RAW'] = df['WATER_TABLE_RAW'].astype('float64')
                df['WATER_TABLE_CLEANSING'] = df['WATER_TABLE_CLEANSING'].astype('float64')
                df = df.reset_index(drop=True)
                for i in range(len(df)):
                    MN = df.loc[i, "MAHDOUDE_NAME"]
                    AN = df.loc[i, "AQUIFER_NAME"]
                    LN = df.loc[i, "LOCATION_NAME"]
                    DPR =  df.loc[i, "DATE_PERSIAN"]
                    data.loc[
                        (data['MAHDOUDE_NAME'] == MN) & (data['AQUIFER_NAME'] == AN) & (data['LOCATION_NAME'] == LN) & (data['DATE_PERSIAN'] == DPR),
                        'WATER_TABLE'
                    ] = np.nan if (df.loc[i, "WATER_TABLE_CLEANSING"] == '') else float(df.loc[i, "WATER_TABLE_CLEANSING"])
                    
                    data.loc[
                        (data['MAHDOUDE_NAME'] == MN) & (data['AQUIFER_NAME'] == AN) & (data['LOCATION_NAME'] == LN) & (data['DATE_PERSIAN'] == DPR),
                        'DESCRIPTION'
                    ] = np.nan if (df.loc[i, "DESCRIPTION"] == '') else str(df.loc[i, "DESCRIPTION"])
                        
                    
            data.to_sql(
                name="GROUNDWATER_CLEANSING_DATA",
                con=DB_GROUNDWATER,
                if_exists="replace"
            )
            
            return [
                0,
                "YES",
                0
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
        Output("COLLAPSE___SELECT_WELL___DATA_CLEANSING_TAB", "is_open"),
        Output("ARROW___SELECT_WELL___DATA_CLEANSING_TAB", "className"),
        Output("COLLAPSE___DATA_CLEANSING_METHOD___DATA_CLEANSING_TAB", "is_open"),
        Output("ARROW___DATA_CLEANSING_METHOD___DATA_CLEANSING_TAB", "className"),
        Output("COLLAPSE___SELECT_OUTLIER____DATA_CLEANSING_TAB", "is_open"),
        Output("ARROW___SELECT_OUTLIER____DATA_CLEANSING_TAB", "className"),
        Input("OPEN_CLOSE_COLLAPSE___SELECT_WELL___DATA_CLEANSING_TAB", "n_clicks"),
        Input("OPEN_CLOSE_COLLAPSE___DATA_CLEANSING_METHOD___DATA_CLEANSING_TAB", "n_clicks"),
        Input("OPEN_CLOSE_COLLAPSE___SELECT_OUTLIER____DATA_CLEANSING_TAB", "n_clicks"),
        State("COLLAPSE___SELECT_WELL___DATA_CLEANSING_TAB", "is_open"),
        State("COLLAPSE___DATA_CLEANSING_METHOD___DATA_CLEANSING_TAB", "is_open"),
        State("COLLAPSE___SELECT_OUTLIER____DATA_CLEANSING_TAB", "is_open"),
    )
    def FUNCTION__COLLAPSE___SELECT_WELL___DATA_CLEANSING_TAB(
        n_select_well, n_select_method, n_select_outlier,
        state_select_well, state_select_method, state_select_outlier,
    ):
        print("FUNCTION__COLLAPSE___SELECT_WELL___DATA_CLEANSING_TAB")
        ctx = dash.callback_context

        if not ctx.triggered:
            return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2",  False, "fas fa-caret-left ml-2",

        else:
            button_id = ctx.triggered[0]["prop_id"].split(".")[0]
            
            if button_id == "OPEN_CLOSE_COLLAPSE___SELECT_WELL___DATA_CLEANSING_TAB" and n_select_well:
                if not state_select_well:
                    return True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE_COLLAPSE___DATA_CLEANSING_METHOD___DATA_CLEANSING_TAB" and n_select_method:
                if not state_select_method:
                    return False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE_COLLAPSE___SELECT_OUTLIER____DATA_CLEANSING_TAB" and n_select_outlier:
                if not state_select_outlier:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            else:
                return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2",



    # -----------------------------------------------------------------------------
    # SELECT MANUAL & AUTOMATIC DATA CLEANSING METHOD
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("COLLAPSE___DATA_CLEANSING_METHOD_SELECT_POPUP___DATA_CLEANSING_TAB", "children"),
        Output("COLLAPSE___DATA_CLEANSING_METHOD_SELECT_POPUP___DATA_CLEANSING_TAB", "className"),
        Input("COLLAPSE___DATA_CLEANSING_METHOD_SELECT___DATA_CLEANSING_TAB", "value")
    )
    def FUNCTION___COLLAPSE___DATA_CLEANSING_METHOD_SELECT_POPUP___DATA_CLEANSING_TAB(
        method
    ):
        print("FUNCTION___COLLAPSE___DATA_CLEANSING_METHOD_SELECT_POPUP___DATA_CLEANSING_TAB")
        if method == "MANUAL":
            return [], "text-center text-danger"
        else:
            children = [
                html.I(
                    className="fa fa-exclamation-triangle ml-2",
                ),
                "در حال تکمیل",
                html.I(
                    className="fa fa-exclamation-triangle mr-2",
                )
            ]
            return children, "text-center text-danger pt-3"



    # -----------------------------------------------------------------------------
    # STUDY AREA SELECT - CONTROLS - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'options'),
        Input('GEOINFO_DATA_STATE___DATA_CLEANSING_TAB', 'data'),
        Input('GEOINFO_DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB(geoinfo_state, geoInfo):   
        print("FUNCTION___STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB")     
        if geoinfo_state == "OK" and geoInfo is not None:
            geoInfo = pd.DataFrame.from_dict(geoInfo)
            return [{"label": col, "value": col} for col in geoInfo['MAHDOUDE_NAME'].unique()]        
        else:
            return []
    
    
    
    # -----------------------------------------------------------------------------
    # AQUIFER SELECT - CONTROLS - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'options'),
        Input('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('GEOINFO_DATA_STATE___DATA_CLEANSING_TAB', 'data'),
        Input('GEOINFO_DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB(study_area, geoinfo_state, geoInfo):
        print("FUNCTION___AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB")
        if geoinfo_state == "OK" and geoInfo is not None:
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
        Output('WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'options'),
        Input('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('GEOINFO_DATA_STATE___DATA_CLEANSING_TAB', 'data'),
        Input('GEOINFO_DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB(study_area, aquifer, geoinfo_state, geoInfo):
        print("FUNCTION___WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB")
        if geoinfo_state == "OK" and geoInfo is not None:
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
        Output('GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB', 'figure'),
        
        Input('INTERVAL___DATA_CLEANSING_TAB', 'n_intervals'),
          
        Input('METHOD_1_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('METHOD_2_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        
        Input('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        
        State('GROUNDWATER_RAW_DATA_STORE___DATA_CLEANSING_TAB', 'data'),
        State('GROUNDWATER_CLEANSING_DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB(n0, n1, n2, study_area, aquifer, well, groundwater_raw_data, groundwater_cleansing_data):
        print("FUNCTION___GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB")      
        if well is not None and len(well) != 0:
                    
            # groundwater raw data
            groundwater_raw_data = pd.DataFrame.from_dict(groundwater_raw_data)
            groundwater_raw_data = groundwater_raw_data[groundwater_raw_data["MAHDOUDE_NAME"].isin(study_area)]
            groundwater_raw_data = groundwater_raw_data[groundwater_raw_data["AQUIFER_NAME"].isin(aquifer)]
            groundwater_raw_data = groundwater_raw_data[groundwater_raw_data["LOCATION_NAME"].isin(well)]
            groundwater_raw_data["DATE_GREGORIAN"] = groundwater_raw_data["DATE_GREGORIAN"].apply(pd.to_datetime)
            groundwater_raw_data = groundwater_raw_data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            groundwater_raw_data = groundwater_raw_data[["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN", "WATER_TABLE"]]
            
            # groundwater cleansing data
            groundwater_cleansing_data = pd.DataFrame.from_dict(groundwater_cleansing_data)
            groundwater_cleansing_data = groundwater_cleansing_data[groundwater_cleansing_data["MAHDOUDE_NAME"].isin(study_area)]
            groundwater_cleansing_data = groundwater_cleansing_data[groundwater_cleansing_data["AQUIFER_NAME"].isin(aquifer)]
            groundwater_cleansing_data = groundwater_cleansing_data[groundwater_cleansing_data["LOCATION_NAME"].isin(well)]
            groundwater_cleansing_data["DATE_GREGORIAN"] = groundwater_cleansing_data["DATE_GREGORIAN"].apply(pd.to_datetime)
            groundwater_cleansing_data = groundwater_cleansing_data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            
            # Method 1:                
            groundwater_cleansing_data["WATER_TABLE_PAD"] = groundwater_cleansing_data["WATER_TABLE"].interpolate(method="pad")    
            groundwater_cleansing_data["DIFF"] = groundwater_cleansing_data["WATER_TABLE_PAD"].diff().abs()
            groundwater_cleansing_data["DIFF_MEAN"] = groundwater_cleansing_data["DIFF"].rolling(6, min_periods=1).mean().shift(1)
            groundwater_cleansing_data["CHECK_METHOD_1"] = groundwater_cleansing_data["DIFF"] > (groundwater_cleansing_data["DIFF_MEAN"] * n1)
            
            
            # Method 2:
            groundwater_cleansing_data["SHIFT_DATE"] = groundwater_cleansing_data["DATE_GREGORIAN"].shift(periods=1, fill_value=0)                    
            groundwater_cleansing_data[['DATE_GREGORIAN','SHIFT_DATE']] = groundwater_cleansing_data[['DATE_GREGORIAN','SHIFT_DATE']].apply(pd.to_datetime)       
            groundwater_cleansing_data["DIFF_DATE"] = (groundwater_cleansing_data["DATE_GREGORIAN"] - groundwater_cleansing_data["SHIFT_DATE"]).dt.days.abs()
            groundwater_cleansing_data["DERIVATIV"] = (groundwater_cleansing_data["DIFF"] / groundwater_cleansing_data["DIFF_DATE"]) * 100
            groundwater_cleansing_data["CHECK_METHOD_2"] = groundwater_cleansing_data["DERIVATIV"] > n2
            
           
            groundwater_cleansing_data = groundwater_cleansing_data[
                ["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN", "WATER_TABLE", "CHECK_METHOD_1", "CHECK_METHOD_2", "DESCRIPTION"]
            ]

                        
            # PLOT
            fig = go.Figure()
                            
            for w in well:
                                    
                groundwater_raw_data_w = groundwater_raw_data[groundwater_raw_data["LOCATION_NAME"] == w]
                groundwater_raw_data_w = groundwater_raw_data_w.sort_values(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
                ).reset_index(drop=True)
                groundwater_raw_data_w.rename(columns={"WATER_TABLE": "WATER_TABLE_RAW"}, inplace=True)
                                   
                groundwater_cleansing_data_w = groundwater_cleansing_data[groundwater_cleansing_data["LOCATION_NAME"] == w]
                groundwater_cleansing_data_w = groundwater_cleansing_data_w.sort_values(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
                ).reset_index(drop=True)
                groundwater_cleansing_data_w.rename(columns={"WATER_TABLE": "WATER_TABLE_CLEANSING"}, inplace=True)

                df_w = pd.merge(
                    left=groundwater_cleansing_data_w,
                    right=groundwater_raw_data_w,
                    on=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"],
                    how="left"
                )

                df_w = df_w[
                    ["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN", "WATER_TABLE_RAW", "WATER_TABLE_CLEANSING", "CHECK_METHOD_1", "CHECK_METHOD_2", "DESCRIPTION"]
                ]
                
                df_w["CHANGE_WATER_TABLE"] = np.where(df_w["WATER_TABLE_CLEANSING"] == df_w["WATER_TABLE_RAW"], "blue", "red")

                fig.add_trace(
                    go.Scatter(
                        x=groundwater_raw_data_w['DATE_GREGORIAN'],
                        y=groundwater_raw_data_w['WATER_TABLE_RAW'],
                        mode='lines+markers',
                        name=f'داده‌های خام - {w}',
                        marker=dict(
                            color='black',
                            size=5,
                        ),
                        line=dict(
                            color='black',
                            width=0.8
                        )  
                    )
                )
                
                fig.add_trace(
                    go.Scatter(
                        x=df_w['DATE_GREGORIAN'],
                        y=df_w['WATER_TABLE_CLEANSING'],
                        mode='lines+markers',
                        name=f'داده‌های اصلاح شده - {w}',
                        marker=dict(
                            color=df_w["CHANGE_WATER_TABLE"],
                            size=8,
                        ),
                        line=dict(
                            color='blue',
                            width=1
                        )  
                    )
                )
                
                                
                df_w_m_1 = df_w[df_w["CHECK_METHOD_1"]]
                
                fig.add_trace(
                    go.Scatter(
                        x=df_w_m_1['DATE_GREGORIAN'],
                        y=df_w_m_1['WATER_TABLE_CLEANSING'],
                        mode='markers',
                        name=f'روش میانگین',
                        marker=dict(
                            color='green',
                            size=10,
                            symbol='x'
                        )
                    )
                )
                
                df_w_m_2 = df_w[df_w["CHECK_METHOD_2"]]
                
                fig.add_trace(
                    go.Scatter(
                        x=df_w_m_2['DATE_GREGORIAN'],
                        y=df_w_m_2['WATER_TABLE_CLEANSING'],
                        mode='markers',
                        name=f'روش مشتق',
                        marker=dict(
                            color='orange',
                            size=10,
                            symbol='x'
                        )
                    )
                )
            # fig.update_traces(hovertemplate=None)

            fig.update_layout(
                hoverlabel=dict(
                    namelength = -1
                ),
                # hovermode="x unified",
                yaxis_title="عمق سطح آب - متر",
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
                    text='عمق ماهانه سطح آب',
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
    # MAP - GRAPH & MAP - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('MAP___GRAPH_MAP___DATA_CLEANSING_TAB', 'figure'),
        Input('INTERVAL___DATA_CLEANSING_TAB', 'n_intervals'), 
        Input('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
    )
    def FUNCTION___MAP___GRAPH_MAP___DATA_CLEANSING_TAB(n0, study_area, aquifer, well):
        print('FUNCTION___MAP___GRAPH_MAP___DATA_CLEANSING_TAB')     
        if well is not None and len(well) != 0:

            df_mahdoudes = gdf[gdf["MAHDOUDE_NAME"].isin(study_area)]
            df_aquifers = df_mahdoudes[df_mahdoudes["AQUIFER_NAME"].isin(aquifer)]                    
            df_locations = df_aquifers[df_aquifers["LOCATION_NAME"].isin(well)]
            
            fig = go.Figure(
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



    # -----------------------------------------------------------------------------
    # TABLE - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('TABLE___DATA_CLEANSING_TAB', 'columns'),
        Output('TABLE___DATA_CLEANSING_TAB', 'data'),
        Output('TABLE_HOLDER___BODY___DATA_CLEANSING_TAB', 'hidden'),        
        Output('INFO_CARD___MAX___BODY___DATA_CLEANSING_TAB', 'children'),        
        Output('INFO_CARD___MIN___BODY___DATA_CLEANSING_TAB', 'children'),        
        Output('INFO_CARD___MEAN___BODY___DATA_CLEANSING_TAB', 'children'),        
        Output('INFO_CARD___MEDIAN___BODY___DATA_CLEANSING_TAB', 'children'),        
        Output('INFO_CARD___ZERO_VALUE___BODY___DATA_CLEANSING_TAB', 'children'),        
        Output('INFO_CARD___DATE___BODY___DATA_CLEANSING_TAB', 'children'),        
        Output('INFO_CARD_HOLDER___BODY___DATA_CLEANSING_TAB', 'hidden'),
        
        Output('TABLE_SELECTED___DATA_CLEANSING_TAB', 'columns'),
        Output('TABLE_SELECTED___DATA_CLEANSING_TAB', 'data'),
        Output('TABLE_SELECTED_HOLDER___BODY___DATA_CLEANSING_TAB', 'hidden'),        
        Output('GRAPH_SELECTED_DATA_STORE___DATA_CLEANSING_TAB', 'data'), 
              
        Input('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        
        Input('GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB', 'selectedData'),
        
        State('GROUNDWATER_RAW_DATA_STORE___DATA_CLEANSING_TAB', 'data'),
        State('GROUNDWATER_CLEANSING_DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___TABLE___DATA_CLEANSING_TAB(
        study_area, aquifer, well, graphData, groundwater_raw_data, groundwater_cleansing_data
    ):
        print("FUNCTION___TABLE___DATA_CLEANSING_TAB")
        if well is not None and len(well) == 1:
                    
            # groundwater raw data
            groundwater_raw_data = pd.DataFrame.from_dict(groundwater_raw_data)
            groundwater_raw_data = groundwater_raw_data[groundwater_raw_data["MAHDOUDE_NAME"].isin(study_area)]
            groundwater_raw_data = groundwater_raw_data[groundwater_raw_data["AQUIFER_NAME"].isin(aquifer)]
            groundwater_raw_data = groundwater_raw_data[groundwater_raw_data["LOCATION_NAME"].isin(well)]
            groundwater_raw_data["DATE_GREGORIAN"] = groundwater_raw_data["DATE_GREGORIAN"].apply(pd.to_datetime)
            groundwater_raw_data = groundwater_raw_data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            groundwater_raw_data = groundwater_raw_data[["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN", "WATER_TABLE"]]
            groundwater_raw_data.rename(columns={"WATER_TABLE": "WATER_TABLE_RAW"}, inplace=True)
            
            
            # groundwater cleansing data
            groundwater_cleansing_data = pd.DataFrame.from_dict(groundwater_cleansing_data)
            groundwater_cleansing_data = groundwater_cleansing_data[groundwater_cleansing_data["MAHDOUDE_NAME"].isin(study_area)]
            groundwater_cleansing_data = groundwater_cleansing_data[groundwater_cleansing_data["AQUIFER_NAME"].isin(aquifer)]
            groundwater_cleansing_data = groundwater_cleansing_data[groundwater_cleansing_data["LOCATION_NAME"].isin(well)]
            groundwater_cleansing_data["DATE_GREGORIAN"] = groundwater_cleansing_data["DATE_GREGORIAN"].apply(pd.to_datetime)
            groundwater_cleansing_data = groundwater_cleansing_data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            groundwater_cleansing_data = groundwater_cleansing_data[["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN", "WATER_TABLE", "DESCRIPTION"]]
            groundwater_cleansing_data.rename(columns={"WATER_TABLE": "WATER_TABLE_CLEANSING"}, inplace=True)
            
            
            df = pd.merge(
                left=groundwater_raw_data,
                right=groundwater_cleansing_data,
                on=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"],
                how="outer"
            ).sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN", "DATE_PERSIAN"]
            ).reset_index(drop=True)
            
            df = df[["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_PERSIAN", "WATER_TABLE_RAW", "WATER_TABLE_CLEANSING", "DESCRIPTION"]]
            
            df_show_all = df.copy()
            df_show_all.columns = ["محدوده مطالعاتی", "آبخوان", "چاه مشاهداتی", "تاریخ", "داده خام سطح آب", "داده اصلاح شده سطح آب", "توضیحات"]
        
            
            if graphData is None:
            
                return [
                    [{"name": i, "id": i} for i in df_show_all.columns],
                    df_show_all.to_dict('records'),
                    False,
                    round(df["WATER_TABLE_CLEANSING"].max(), 1),
                    round(df["WATER_TABLE_CLEANSING"].min(), 1),
                    round(df["WATER_TABLE_CLEANSING"].mean(), 1),
                    round(df["WATER_TABLE_CLEANSING"].median(), 1),
                    len(df[df["WATER_TABLE_CLEANSING"] == 0]),
                    0,
                    False,
                    [{}],
                    [],
                    True,
                    None
                ]
                
            else:
                
                point_selected = pd.DataFrame(graphData["points"])
                point_selected = point_selected[point_selected["curveNumber"] == 1]

                df_selected = df[df["DATE_PERSIAN"].isin(point_selected["x"].tolist())]

                df_show_selected = df_selected.copy()
                df_show_selected.columns = ["محدوده مطالعاتی", "آبخوان", "چاه مشاهداتی", "تاریخ", "داده خام سطح آب", "داده اصلاح شده سطح آب", "توضیحات"]
                                                                                        
                return [
                    [{"name": i, "id": i} for i in df_show_all.columns],
                    df_show_all.to_dict('records'),
                    False,
                    round(df["WATER_TABLE_CLEANSING"].max(), 1),
                    round(df["WATER_TABLE_CLEANSING"].min(), 1),
                    round(df["WATER_TABLE_CLEANSING"].mean(), 1),
                    round(df["WATER_TABLE_CLEANSING"].median(), 1),
                    len(df[df["WATER_TABLE_CLEANSING"] == 0]),
                    0,
                    False,
                    [{"name": i, "id": i} for i in df_show_selected.columns],
                    df_show_selected.to_dict('records'),
                    False,
                    df_selected.to_dict('records')
                ]
        else:
            
            return [
                [{}],
                [],
                True,
                "",
                "",
                "",
                "",
                "",
                "",
                True,
                [{}],
                [],
                True,
                None
            ]