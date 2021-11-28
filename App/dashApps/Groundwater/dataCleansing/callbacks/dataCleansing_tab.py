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
        Output('DATABASE_STATE___DATA_CLEANSING_TAB', 'data'),
        Output('DATA_STORE___DATA_CLEANSING_TAB', 'data'),
        Output('GEOINFO_DATA_STORE___DATA_CLEANSING_TAB', 'data'),
        Output('BUTTON___BUTTONS___DATA_CLEANSING_TAB', 'n_clicks'),
        Input('LOAD_DATABASE___DATA_CLEANSING_TAB', 'n_intervals'),
        Input('BUTTON___BUTTONS___DATA_CLEANSING_TAB', 'n_clicks'),
        Input('GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB', 'selectedData'),
        State('TABLE___DATA_CLEANSING_TAB', 'data'),
        State('DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___DATABASE____DATA_CLEANSING_TAB(n_interval, n_click, graphData, tableData, data):
        if os.path.exists(PATH_DB_GROUNDWATER):
            TABLE_NAME = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", DB_GROUNDWATER)
            if TABLE_NAME['name'].str.contains('GROUNDWATER_DATA').any():
                if n_click != 0 and graphData is not None:
                    df = pd.DataFrame(tableData).reset_index(drop=True)
                    df = df.rename(
                        columns={
                            'محدوده مطالعاتی': 'MAHDOUDE_NAME',
                            'آبخوان': 'AQUIFER_NAME',
                            'چاه مشاهداتی': 'LOCATION_NAME',
                            'تاریخ': 'DATE_PERSIAN_RAW',
                            'داده خام سطح ایستابی': 'WATER_TABLE_RAW',
                            'داده اصلاح شده سطح ایستابی': 'WATER_TABLE_MODIFY',
                            'توضیحات': 'DESCRIPTION',
                        }
                    )
                    data = pd.DataFrame.from_dict(data)
                    for i in range(len(df)):                    
                        MN = df.loc[i, "MAHDOUDE_NAME"]
                        AN = df.loc[i, "AQUIFER_NAME"]
                        LN = df.loc[i, "LOCATION_NAME"]
                        DPR =  df.loc[i, "DATE_PERSIAN_RAW"]
                        data.loc[
                            (data['MAHDOUDE_NAME'] == MN) & (data['AQUIFER_NAME'] == AN) & (data['LOCATION_NAME'] == LN) & (data['DATE_PERSIAN_RAW'] == DPR),
                            'WATER_TABLE_MODIFY'
                        ] = np.nan if (df.loc[i, "WATER_TABLE_MODIFY"] == '') else float(df.loc[i, "WATER_TABLE_MODIFY"])
                        
                        data.loc[
                            (data['MAHDOUDE_NAME'] == MN) & (data['AQUIFER_NAME'] == AN) & (data['LOCATION_NAME'] == LN) & (data['DATE_PERSIAN_RAW'] == DPR),
                            'DESCRIPTION'
                        ] = np.nan if (df.loc[i, "DESCRIPTION"] == '') else str(df.loc[i, "DESCRIPTION"])
                    
                    data.to_sql(
                        name="GROUNDWATER_DATA",
                        con=DB_GROUNDWATER,
                        if_exists="replace"
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
        Input('DATABASE_STATE___DATA_CLEANSING_TAB', 'data'),
        Input('GEOINFO_DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB(database_state, geoInfo):        
        if database_state == "OK" and geoInfo is not None:
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
        Input('DATABASE_STATE___DATA_CLEANSING_TAB', 'data'),
        Input('GEOINFO_DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB(study_area, database_state, geoInfo):
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
        Output('WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'options'),
        Input('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('DATABASE_STATE___DATA_CLEANSING_TAB', 'data'),
        Input('GEOINFO_DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB(study_area, aquifer, database_state, geoInfo):
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
        Output('GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB', 'figure'),   
        Input('METHOD_1_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('METHOD_2_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('LOAD_DATABASE___DATA_CLEANSING_TAB', 'n_intervals'),
        Input('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        State('DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB(n1, n2, n_interval, study_area, aquifer, well, data):        
        if study_area is not None and len(study_area) != 0 and\
            aquifer is not None and len(aquifer) != 0 and\
                well is not None and len(well) != 0:
                    
                    data = pd.DataFrame.from_dict(data)
                    data = data[data["MAHDOUDE_NAME"].isin(study_area)]
                    data = data[data["AQUIFER_NAME"].isin(aquifer)]
                    data = data[data["LOCATION_NAME"].isin(well)]
                    data = data.sort_values(
                        by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN_RAW"]
                    ).reset_index(drop=True)
                    
                    # Method 1:
                    
                    data["DIFF"] = data["WATER_TABLE_MODIFY"].diff().abs()
                    data["DIFF_MEAN"] = data["DIFF"].rolling(6, min_periods=1).mean().shift(1)
                    data["CHECK_METHOD_1"] = data["DIFF"] > (data["DIFF_MEAN"] * n1)
                    data["SHIFT_DATE"] = data["DATE_GREGORIAN_RAW"].shift(periods=1, fill_value=0)                    
                    data[['DATE_GREGORIAN_RAW','SHIFT_DATE']] = data[['DATE_GREGORIAN_RAW','SHIFT_DATE']].apply(pd.to_datetime)                  
                    data["DIFF_DATE"] = (data["DATE_GREGORIAN_RAW"] - data["SHIFT_DATE"]).dt.days.abs()
                    data["DERIVATIV"] = (data["DIFF"] / data["DIFF_DATE"]) * 100
                    data["CHECK_METHOD_2"] = data["DERIVATIV"] > n2

                                
                    # PLOT
                    fig = go.Figure()
                                    
                    for w in well:                    
                        df_w = data[data["LOCATION_NAME"] == w]
                        
                        df_w = df_w.sort_values(
                            by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN_RAW"]
                        ).reset_index(drop=True)  
                        
                        fig.add_trace(
                            go.Scatter(
                                x=df_w['DATE_PERSIAN_RAW'],
                                y=df_w['WATER_TABLE_RAW'],
                                mode='lines+markers',
                                name=f'داده‌های خام - {w}',
                                marker=dict(
                                    color='black',
                                    size=10,
                                ),
                                line=dict(
                                    color='black',
                                    width=1
                                )  
                            )
                        )
                        
                        fig.add_trace(
                            go.Scatter(
                                x=df_w['DATE_PERSIAN_RAW'],
                                y=df_w['WATER_TABLE_MODIFY'],
                                mode='lines+markers',
                                name=f'داده‌های اصلاح شده - {w}',
                                marker=dict(
                                    color='green',
                                    size=10,
                                ),
                                line=dict(
                                    color='green',
                                    width=1
                                )  
                            )
                        )
                        
                        
                        df_w_m_1 = df_w[df_w["CHECK_METHOD_1"]]
                        
                        fig.add_trace(
                            go.Scatter(
                                x=df_w_m_1['DATE_PERSIAN_RAW'],
                                y=df_w_m_1['WATER_TABLE_MODIFY'],
                                mode='markers',
                                name=f'روش میانگین - {w}',
                                marker=dict(
                                    color='blue',
                                    size=12,
                                    symbol='x'
                                )
                            )
                        )
                        
                        df_w_m_2 = df_w[df_w["CHECK_METHOD_2"]]
                        
                        fig.add_trace(
                            go.Scatter(
                                x=df_w_m_2['DATE_PERSIAN_RAW'],
                                y=df_w_m_2['WATER_TABLE_MODIFY'],
                                mode='markers',
                                name=f'روش مشتق - {w}',
                                marker=dict(
                                    color='red',
                                    size=6,
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
    
    
    
    # -----------------------------------------------------------------------------
    # MAP - GRAPH & MAP - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('MAP___GRAPH_MAP___DATA_CLEANSING_TAB', 'figure'),
        Input('LOAD_DATABASE___DATA_CLEANSING_TAB', 'n_intervals'),   
        Input('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        State('DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___MAP___GRAPH_MAP___DATA_CLEANSING_TAB(n_interval, study_area, aquifer, well, data):        
        if study_area is not None and len(study_area) != 0 and\
            aquifer is not None and len(aquifer) != 0 and\
                well is not None and len(well) != 0:
                    
                    mask_df = mask[mask['MA_NAME'].isin(study_area)]
                    mask_df = mask_df[mask_df['AQ_NAME'].isin(aquifer)]
                    j_file = json.loads(mask_df.to_json())

                    for feature in j_file["features"]:
                        feature['id'] = feature['properties']['AQ_NAME']
                    
                    # Create Map
                    fig = px.choropleth_mapbox(
                        data_frame=mask_df,
                        geojson=j_file,
                        locations='AQ_NAME',
                        opacity=0.4
                    )
                    
                    gdf_df = gdf[gdf["MAHDOUDE_NAME"].isin(study_area)]
                    all_wells = gdf_df[gdf_df["AQUIFER_NAME"].isin(aquifer)]                    
                    selected_wells = all_wells[all_wells["LOCATION_NAME"].isin(well)]
                    
                    fig.add_trace(
                        go.Scattermapbox(
                            lat=all_wells.Y_,
                            lon=all_wells.X_,
                            mode='markers',
                            marker=go.scattermapbox.Marker(size=8),
                            text=all_wells["LOCATION_NAME"],
                            hoverinfo='text',
                            hovertemplate='<span style="color:white;">%{text}</span><extra></extra>'
                        )
                    )
                    
                    fig.add_trace(
                        go.Scattermapbox(
                            lat=selected_wells.Y_,
                            lon=selected_wells.X_,
                            mode='markers',
                            marker=go.scattermapbox.Marker(
                                size=10,
                                color='green'
                            ),
                            text=selected_wells["LOCATION_NAME"],
                            hoverinfo='text',
                            hovertemplate='<b>%{text}</b><extra></extra>'
                        ), 
                    )
                        
                    fig.update_layout(
                        mapbox = {
                            'style': "stamen-terrain",
                            'zoom': 7,
                            'center': {
                                'lon': selected_wells.X_.mean(),
                                'lat': selected_wells.Y_.mean()
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
        Input('LOAD_DATABASE___DATA_CLEANSING_TAB', 'n_intervals'),
        Input('STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 'value'),
        Input('GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB', 'selectedData'),
        State('DATA_STORE___DATA_CLEANSING_TAB', 'data')
    )
    def FUNCTION___TABLE___DATA_CLEANSING_TAB(n_interval, study_area, aquifer, well, graphData, data):     
        if study_area is not None and len(study_area) != 0 and\
            aquifer is not None and len(aquifer) != 0 and\
                well is not None and len(well) != 0 and\
                    graphData is not None:
                        
                        data = pd.DataFrame.from_dict(data)
                        data = data[data["MAHDOUDE_NAME"].isin(study_area)]
                        data = data[data["AQUIFER_NAME"].isin(aquifer)]
                        data = data[data["LOCATION_NAME"].isin(well)]
                        data = data.sort_values(
                            by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN_RAW"]
                        ).reset_index(drop=True)
                        
                        x = []
                        curveNumber = []
                        
                        for i in graphData["points"]:
                            x.append(i['x'])
                            curveNumber.append(i['curveNumber'])

                        df = data[data["DATE_PERSIAN_RAW"].isin(x)][["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_PERSIAN_RAW", "WATER_TABLE_RAW", "WATER_TABLE_MODIFY", "DESCRIPTION"]]
                        
                        df.columns = ["محدوده مطالعاتی", "آبخوان", "چاه مشاهداتی", "تاریخ", "داده خام سطح ایستابی", "داده اصلاح شده سطح ایستابی", "توضیحات"]
                                                
                        return [
                            [{"name": i, "id": i} for i in df.columns],
                            df.to_dict('records'),
                            False
                        ]
        else:
            return [
                [{}],
                [],
                True,
            ]