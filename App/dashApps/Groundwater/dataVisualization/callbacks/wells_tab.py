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


from App.dashApps.Groundwater.dataVisualization.callbacks.config import *



def callback___wells_tab___dataVisualization___groundwater(app):

    # -----------------------------------------------------------------------------
    # CHECK DATABASE EXIST AND STORE DATA
    # -----------------------------------------------------------------------------
    @app.callback(

        Output('DATA_STATE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        Output('DATA_STORE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        Output('GEOINFO_STATE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        Output('GEOINFO_STORE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        
        Input('INTERVAL___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'n_intervals'),
        State('DATA_STATE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data')

    )
    def FUNCTION___READ_DATABASE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
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
        Output("COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "is_open"),
        Output("ARROW___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "className"),
        Output("COLLAPSE_SELECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "is_open"),
        Output("ARROW___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "className"),
        Output("COLLAPSE_SETTINGS___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "is_open"),
        Output("ARROW___COLLAPSE_SETTINGS___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "className"),

        
        Input("OPEN_CLOSE___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "n_clicks"),
        Input("OPEN_CLOSE___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "n_clicks"),
        Input("OPEN_CLOSE___COLLAPSE_SETTINGS___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "n_clicks"),
        State("COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "is_open"),
        State("COLLAPSE_SELECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "is_open"),
        State("COLLAPSE_SETTINGS___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "is_open"),
    )
    def FUNCTION__COLLAPSE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        n_select_well, n_select_date, n_settings,
        state_select_well, state_select_date, state_settings,
    ):
        ctx = dash.callback_context

        if not ctx.triggered:
            return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

        else:
            button_id = ctx.triggered[0]["prop_id"].split(".")[0]
            
            if button_id == "OPEN_CLOSE___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER" and n_select_well:
                if not state_select_well:
                    return True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER" and n_select_date:
                if not state_select_date:
                    return False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE___COLLAPSE_SETTINGS___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER" and n_settings:
                if not state_settings:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            else:
                return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"


    # -----------------------------------------------------------------------------
    # SELECT DATE COLLAPSE
    # -----------------------------------------------------------------------------

    @app.callback(
        Output("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Output("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Output("START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "disabled"),
        Output("END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "disabled"),
        Output("START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "disabled"),
        Output("END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "disabled"),
        Output("START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Output("END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Output("START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Output("END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Output("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "labelClassName"),
        Output("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "labelClassName"),
        Input("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
    )
    def FUNCTION__WATERYEAR_SHAMSIYEAR___COLLAPSE_DATE_SELECT___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        waterYear_selected, shamsiYear_selected
    ):
        ctx = dash.callback_context
        selected_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
        if selected_id == "WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER":
            waterYear_selected = "waterYear"
            shamsiYear_selected = ""
            return waterYear_selected, shamsiYear_selected, False, False, True, True, None, None, None, None, "d-flex align-items-center text-dark font-weight-bold", "d-flex align-items-center text-secondary"
        
        elif selected_id == "SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER":
            waterYear_selected = ""
            shamsiYear_selected = "shamsiYear"
            return waterYear_selected, shamsiYear_selected, True, True, False, False, None, None, None, None, "d-flex align-items-center text-secondary", "d-flex align-items-center text-dark font-weight-bold"
       
        else:
            waterYear_selected = ""
            shamsiYear_selected = ""
            return waterYear_selected, shamsiYear_selected, True, True, True, True, None, None, None, None, "d-flex align-items-center text-secondary", "d-flex align-items-center text-secondary",



    @app.callback(
        Output('END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'options'),
        Input('START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value')
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
        Output('END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'options'),
        Input('START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value')
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
        Output('STUDY_AREA_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'options'),
        Input('GEOINFO_STATE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        Input('GEOINFO_STORE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data')
    )
    def FUNCTION___STUDY_AREA_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
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
        Output('AQUIFER_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'options'),
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('GEOINFO_STATE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        Input('GEOINFO_STORE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data')
    )
    def FUNCTION___AQUIFER_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        study_area, geoinfo_state, geoInfo
    ):
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
    # WELL SELECT
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('WELL_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'options'),
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('GEOINFO_STATE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        Input('GEOINFO_STORE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data')
    )
    def FUNCTION___WELL_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        study_area, aquifer, geoinfo_state, geoInfo
    ):
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
    # MAP - GRAPH & MAP - DATA CLEANSING TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('MAP___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'figure'),
        Input('INTERVAL___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'n_intervals'), 
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('WELL_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
    )
    def FUNCTION___MAP___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        n, study_area, aquifer, well
    ):
        if well is not None and len(well) != 0:

            df_mahdoudes = gdf[gdf["MAHDOUDE_NAME"].isin(study_area)]
            df_aquifers = df_mahdoudes[df_mahdoudes["AQUIFER_NAME"].isin(aquifer)]                    
            df_locations = df_aquifers[df_aquifers["LOCATION_NAME"].isin(well)]
            
            mask_selected = mask[mask['MAHDOUDE_NAME'].isin(study_area)]
            mask_selected = mask_selected[mask_selected['AQUIFER_NAME'].isin(aquifer)]
            
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

    
    
    
    # -----------------------------------------------------------------------------
    # GRAPH
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('GRAPH___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'figure'),        
        Input('INTERVAL___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'n_intervals'),        
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('WELL_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),        
        Input('WATER_TABLE_WATER_LEVEL_SELECT___COLLAPSE_SETTINGS___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        
        Input("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
                
        State('DATA_STORE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
    )
    def FUNCTION___GRAPH___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        n, study_area, aquifer, well, water_type, 
        wy, wys, wye,
        shy, shys, shye,
        data,
    ):
        if well is not None and len(well) != 0:
                    
            data = pd.DataFrame.from_dict(data)
            data = data[data["MAHDOUDE_NAME"].isin(study_area)]
            data = data[data["AQUIFER_NAME"].isin(aquifer)]
            data = data[data["LOCATION_NAME"].isin(well)]          
            data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
            data = data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            
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
            
            fig = go.Figure()
            
                            
            for w in well:
                                    
                data_w = data[data["LOCATION_NAME"] == w]
                
                data_w = data_w.sort_values(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN"]
                ).reset_index(drop=True)

               
                fig.add_trace(
                    go.Scatter(
                        x=data_w['DATE_GREGORIAN'],
                        y=data_w[water_type],
                        mode='lines+markers',
                        name=f'{w}',
                        marker=dict(
                            color=data_w["COLOR"],
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
                    text="تراز ماهانه سطح آب چاه (متر)" if water_type == "WATER_LEVEL" else "عمق ماهانه سطح آب چاه (متر)",
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
    # TABLE
    # -----------------------------------------------------------------------------
    @app.callback(       
        Output('TABLE___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'columns'),        
        Output('TABLE___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        Output('TABLE_HOLDER___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'hidden'), 
            
        Input('INTERVAL___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'n_intervals'),        
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('WELL_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),        
        Input('WATER_TABLE_WATER_LEVEL_SELECT___COLLAPSE_SETTINGS___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        
        Input("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
                
        State('DATA_STORE___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
    )
    def FUNCTION___TABLE___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        n, study_area, aquifer, well, water_type, 
        wy, wys, wye,
        shy, shys, shye,
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
            df.columns = ["سال", "ماه", "پارامتر"]
            df = resultTable(df)
            
            if water_type == "WATER_LEVEL":
                df.columns = ["سال", "ماه", "تراز ماهانه سطح آب", "سال آبی", "ماه آبی", "تغییرات تراز سطح آب هر ماه نسبت به ماه قبل", "تغییرات تراز سطح آب هر ماه نسبت به ماه سال قبل"]
                
                para_dic = {
                    "WATER_TABLE_MONTLY" : "تراز ماهانه سطح آب",
                    "WATER_TABLE_DIFF_MONTLY" : "تغییرات هر ماه نسبت به ماه قبل",
                    "WATER_TABLE_DIFF_MONTLY_YEARLY" : "تغییرات هر ماه نسبت به ماه سال قبل",
                }
                
                title_dic = {
                    "WATER_TABLE_MONTLY" : "تراز ماهانه (روز پانزدهم) سطح آب زیرزمینی (متر)",
                    "WATER_TABLE_DIFF_MONTLY" : "تغییرات ماهانه (هر ماه نسبت به ماه قبل) تراز سطح آب زیرزمینی (متر)",
                    "WATER_TABLE_DIFF_MONTLY_YEARLY" : "تغییرات ماهانه (هر ماه در سال جاری نسبت به ماه متناظر در سال قبل) تراز سطح آب زیرزمینی (متر)",
                }  
            else:
                df.columns = ["سال", "ماه", "عمق ماهانه سطح آب", "سال آبی", "ماه آبی", "تغییرات عمق سطح آب هر ماه نسبت به ماه قبل", "تغییرات عمق سطح آب هر ماه نسبت به ماه سال قبل"]

                
        
        
        
        
        
      
        
            
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