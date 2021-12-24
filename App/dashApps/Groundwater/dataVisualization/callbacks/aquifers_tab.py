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



def callback___aquifers_tab___dataVisualization___groundwater(app):

    # -----------------------------------------------------------------------------
    # CHECK DATABASE EXIST AND STORE DATA
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('GEOINFO_STATE___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        Output('DATA_STATE___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        Output('GEOINFO_STORE___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        Input('INTERVAL___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'n_intervals'),
    )
    def FUNCTION___READ_DATABASE___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        n
    ):
        try:
            data = pd.read_sql_query(
                sql="SELECT * FROM hydrograph",
                con=engine_db_hydrograph
            )
            
            geoInfo = data.drop_duplicates(
                subset=["MAHDOUDE_NAME", "AQUIFER_NAME"]
            )[["MAHDOUDE_NAME", "AQUIFER_NAME"]]
            
            return [
                "OK",
                "OK",
                geoInfo.to_dict('records')
            ]
        except:
            return [
                "NO",
                "NO",
                None
            ]

    

    # -----------------------------------------------------------------------------
    # OPEN CLOSE COLLAPSE
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "is_open"),
        Output("ARROW___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "className"),
        Output("COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "is_open"),
        Output("ARROW___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "className"),
        Output("COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "is_open"),
        Output("ARROW___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "className"),

        
        Input("OPEN_CLOSE_COLLAPSE___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "n_clicks"),
        Input("OPEN_CLOSE___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "n_clicks"),
        Input("OPEN_CLOSE___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "n_clicks"),
        
        State("COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "is_open"),
        State("COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "is_open"),
        State("COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "is_open"),
    )
    def FUNCTION__COLLAPSE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        n_select_aquifer, n_select_date, n_settings,
        state_select_aquifer, state_select_date, state_settings,
    ):
        ctx = dash.callback_context

        if not ctx.triggered:
            return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

        else:
            button_id = ctx.triggered[0]["prop_id"].split(".")[0]
            
            if button_id == "OPEN_CLOSE_COLLAPSE___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER" and n_select_aquifer:
                if not state_select_aquifer:
                    return True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER" and n_select_date:
                if not state_select_date:
                    return False, "fas fa-caret-left ml-2", True, "fas fa-caret-down ml-2", False, "fas fa-caret-left ml-2"
                else:
                    return False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2", False, "fas fa-caret-left ml-2"

            elif button_id == "OPEN_CLOSE___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER" and n_settings:
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
        Output("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Output("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        
        Output("START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "disabled"),
        Output("END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "disabled"),
        
        Output("START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "disabled"),
        Output("END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "disabled"),
        
        Output("START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Output("END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        
        Output("START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Output("END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        
        Output("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "labelClassName"),
        Output("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "labelClassName"),
        
        Input("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
    )
    def FUNCTION__WATERYEAR_SHAMSIYEAR___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        waterYear_selected, shamsiYear_selected
    ):
        ctx = dash.callback_context
        selected_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
        if selected_id == "WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER":
            waterYear_selected = "waterYear"
            shamsiYear_selected = ""
            return waterYear_selected, shamsiYear_selected, False, False, True, True, None, None, None, None, "d-flex align-items-center text-dark font-weight-bold", "d-flex align-items-center text-secondary"
        
        elif selected_id == "SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER":
            waterYear_selected = ""
            shamsiYear_selected = "shamsiYear"
            return waterYear_selected, shamsiYear_selected, True, True, False, False, None, None, None, None, "d-flex align-items-center text-secondary", "d-flex align-items-center text-dark font-weight-bold"
       
        else:
            waterYear_selected = ""
            shamsiYear_selected = ""
            return waterYear_selected, shamsiYear_selected, True, True, True, True, None, None, None, None, "d-flex align-items-center text-secondary", "d-flex align-items-center text-secondary",



    @app.callback(
        Output('END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'options'),
        Input('START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value')
    )
    def FUNCTION__SELECT_END_YEAR______WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER(
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
        Output('END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'options'),
        Input('START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value')
    )
    def FUNCTION__SELECT_END_YEAR___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER(
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
        Output('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'options'),
        Input('GEOINFO_STATE___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        Input('GEOINFO_STORE___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data')
    )
    def FUNCTION___STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER(
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
        Output('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'options'),
        Output('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('GEOINFO_STATE___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        Input('GEOINFO_STORE___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data')
    )
    def FUNCTION___AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        study_area, geoinfo_state, geoInfo
    ):
        if geoinfo_state == "OK" and geoInfo is not None:
            if study_area is not None and len(study_area) != 0:
                geoInfo = pd.DataFrame.from_dict(geoInfo)
                geoInfo = geoInfo[geoInfo["MAHDOUDE_NAME"].isin(study_area)]
                return [
                    [{"label": col, "value": col} for col in geoInfo['AQUIFER_NAME'].unique()],
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
    # MAP
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('MAP___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'figure'),
        Input('INTERVAL___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'n_intervals'), 
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
    )
    def FUNCTION___MAP___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        n, study_area, aquifer
    ):
        if study_area is not None and len(study_area) != 0 and aquifer is not None and len(aquifer) != 0:
            
            aquifers = read_data_from_postgis(
                table='aquifers', 
                engine=engine_db_layers, 
                geom_col='geometry', 
                modify_cols=['MAHDOUDE_NAME', 'AQUIFER_NAME']
            )
            
            mask_selected = aquifers[aquifers['MAHDOUDE_NAME'].isin(study_area)]
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
                
            fig.update_layout(
                mapbox = {
                    'style': "stamen-terrain",
                    'zoom': 7,
                    'center': {
                        'lat': mask_selected.geometry.centroid.y.mean(),
                        'lon': mask_selected.geometry.centroid.x.mean(),
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
    # SELECT METHOD UNIT HYDROGRAPH
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('METHOD_UNIT_HYDROGRAPH_SELECT___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'options'),
        Output('METHOD_UNIT_HYDROGRAPH_SELECT___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('INTERVAL___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'n_intervals'), 
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
    )
    def FUNCTION___SELECT_METHODS___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        n, study_area, aquifer
    ):
        if study_area is not None and len(study_area) != 0 and aquifer is not None and len(aquifer) != 0:
            
            data = pd.read_sql_query(
                sql="SELECT * FROM hydrograph",
                con=engine_db_hydrograph
            )
            data = data[data['MAHDOUDE_NAME'].isin(study_area)]
            data = data[data['AQUIFER_NAME'].isin(aquifer)]        
            data.dropna(axis=1, how='all', inplace=True)
                        
            op = pd.DataFrame(
                {
                    "label": [
                        "Arithmetic Mean", "Geometric Mean", "Harmonic Mean", "Median",
                        "Thiessen Weighted Average", "Adjusted Thiessen Weighted Average",
                        "Inverse Distance Weighting", "Triangular Interpolation Network",
                        "Spline with Barriers", "Simple kriging", "Ordinary kriging",
                        "Regression kriging", "Co-kriging"
                    ],
                    "value": [
                        "AM", "GM", "HM", "ME", "TWA", "TWA_ADJ", "IDW", "TIN", "SB", "SK", "OK", "RK", "CK"
                    ],
                    "disabled": True
                }
            )
            
            methods = [s.replace('_UNIT_HYDROGRAPH','') for s in data.columns if "_UNIT_HYDROGRAPH" in s]
            
            op['disabled'] = op['value'].map(lambda x : False  if x in methods else True)
                        
            return [
                [{"label": x, "value": y, "disabled": z} for x, y, z in zip(op['label'], op['value'], op['disabled'])],
                "TWA"
            ]
        else:
            return [
                [
                    {"label": "Arithmetic Mean", "value": "AM", "disabled": True},
                    {"label": "Geometric Mean", "value": "GM", "disabled": True},
                    {"label": "Harmonic Mean", "value": "HM", "disabled": True},
                    {"label": "Median", "value": "ME", "disabled": True},
                    {"label": "Thiessen Weighted Average", "value": "TWA", "disabled": True},
                    {"label": "Adjusted Thiessen Weighted Average", "value": "TWA_ADJ", "disabled": True},
                    {"label": "Inverse Distance Weighting", "value": "IDW", "disabled": True},
                    {"label": "Triangular Interpolation Network", "value": "TIN", "disabled": True},
                    {"label": "Spline with Barriers", "value": "SB", "disabled": True},
                    {"label": "Simple kriging", "value": "SK", "disabled": True},
                    {"label": "Ordinary kriging", "value": "OK", "disabled": True},
                    {"label": "Regression kriging", "value": "RK", "disabled": True},
                    {"label": "Co-kriging", "value": "CK", "disabled": True},
                ],
                "TWA"
            ]
            
    
    
    
    
    # -----------------------------------------------------------------------------
    # GRAPH
    # -----------------------------------------------------------------------------
    @app.callback(
        Output('GRAPH___BODY___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'figure'),
                
        Input('INTERVAL___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'n_intervals'),
        Input('METHOD_UNIT_HYDROGRAPH_SELECT___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
                
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'), 
                     
        Input("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
                
        Input('GEOINFO_STATE___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data')
    )
    def FUNCTION___GRAPH___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        n, method,
        study_area, aquifer,
        wy, wys, wye,
        shy, shys, shye,
        geoinfo_state,
    ):
        if geoinfo_state == "OK" and geoinfo_state is not None and study_area is not None and len(study_area) != 0 and aquifer is not None and len(aquifer) != 0:
            
            data = pd.read_sql_query(
                sql="SELECT * FROM hydrograph",
                con=engine_db_hydrograph
            )
            
            data = data[data['MAHDOUDE_NAME'].isin(study_area)]
            
            data = data[data['AQUIFER_NAME'].isin(aquifer)]            
                     
            data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
            
            data = data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN"]
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
            
                            
            for aq in aquifer:
                                    
                df = data[data["AQUIFER_NAME"] == aq]
                
                df = df.sort_values(
                    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN"]
                ).reset_index(drop=True)

               
                fig.add_trace(
                    go.Scatter(
                        x=df['DATE_GREGORIAN'],
                        y=df[f"{method}_UNIT_HYDROGRAPH"],
                        mode='lines+markers',
                        name=f'{aq}',
                        marker=dict(
                            size=14,
                        ),
                        line=dict(
                            width=1.5
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
                    text="تراز ماهانه سطح آب آبخوان بر حسب متر" if len(aquifer) > 1 else f"تراز ماهانه سطح آب آبخوان {aquifer[0]} بر حسب متر",
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
        Output('TABLE___BODY___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'columns'),        
        Output('TABLE___BODY___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
        Output('TABLE_HOLDER___BODY___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'hidden'), 
        Output('TABLE_HEADER___BODY___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'children'), 
            
        Input('INTERVAL___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'n_intervals'),
                
        Input('STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'),
        Input('AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'value'), 
        
        Input("WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        
        Input("METHOD_UNIT_HYDROGRAPH_SELECT___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("DISPLAY_PARAMETER_SELECT___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
        Input("STATISTICAL_ANALYSIS_SELECT___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER", "value"),
                
        State('GEOINFO_STATE___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 'data'),
    )
    def FUNCTION___TABLE___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER(
        n,
        study_area, aquifer,
        wy, wys, wye,
        shy, shys, shye,
        method, para, statistical,
        geoinfo_state,
    ):
        if geoinfo_state == "OK" and geoinfo_state is not None and study_area is not None and len(study_area) != 0 and aquifer is not None and len(aquifer) == 1:
            
            
            data = pd.read_sql_query(
                sql="SELECT * FROM hydrograph",
                con=engine_db_hydrograph
            )
            
            data = data[data['MAHDOUDE_NAME'].isin(study_area)]
            
            data = data[data['AQUIFER_NAME'].isin(aquifer)]            
                     
            data["DATE_GREGORIAN"] = data["DATE_GREGORIAN"].apply(pd.to_datetime)
            
            data = data.sort_values(
                by=["MAHDOUDE_NAME", "AQUIFER_NAME", "DATE_GREGORIAN"]
            ).reset_index(drop=True)
            
            data = data.round(2)
            
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
                        
            data[['YEAR_PERSIAN', 'MONTH_PERSIAN', 'DAY_PERSIAN']] = data['DATE_PERSIAN'].str.split('-', 2, expand=True)
            data["YEAR_PERSIAN"] = data["YEAR_PERSIAN"].str.zfill(4)
            data["MONTH_PERSIAN"] = data["MONTH_PERSIAN"].str.zfill(2)
            data["DAY_PERSIAN"] = data["DAY_PERSIAN"].str.zfill(2)
            
            day_number = data["DAY_PERSIAN"].unique()[0]
            
            df = data[["YEAR_PERSIAN", "MONTH_PERSIAN", f"{method}_UNIT_HYDROGRAPH", "THISSEN_AQUIFER", "STORAGE_COEFFICIENT_AQUIFER"]]
            df["YEAR_PERSIAN"] = df["YEAR_PERSIAN"].astype(int)
            df["MONTH_PERSIAN"] = df["MONTH_PERSIAN"].astype(int)
            df.columns = ["سال", "ماه", "هد", "مساحت", "ضریب"]
            df = resultTableAquifer(df)
            
            df.columns = [
                "سال", 
                "ماه", 
                "تراز ماهانه سطح آب", 
                "مساحت شبکه تیسن", 
                "ضریب ذخیره", 
                "سال آبی", 
                "ماه آبی", 
                "تغییرات تراز سطح آب نسبت به ماه قبل", 
                "تغییرات تراز سطح آب نسبت به ماه سال قبل"
            ]
            
            df["تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل"] = df["تغییرات تراز سطح آب نسبت به ماه قبل"] * df["مساحت شبکه تیسن"] * df["ضریب ذخیره"]
            df["تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل"] = df["تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل"].round(2)
            df["تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل"] = df["تغییرات تراز سطح آب نسبت به ماه سال قبل"] * df["مساحت شبکه تیسن"] * df["ضریب ذخیره"]
            df["تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل"] = df["تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل"] .round(2)
            
            
            para_dic = {
                1 : "تراز ماهانه سطح آب",
                2 : "تغییرات تراز سطح آب نسبت به ماه قبل",
                3 : "تغییرات تراز سطح آب نسبت به ماه سال قبل",
                4 : "تغییرات ذخیره آبخوان هر ماه نسبت به ماه قبل",
                5 : "تغییرات ذخیره آبخوان هر ماه نسبت به ماه سال قبل",
            }
            
            title_dic = {
                1 : f"تراز ماهانه (روز {day_number} ام) سطح آب آبخوان {aquifer[0]} بر حسب متر",
                2 : f"تغییرات تراز سطح آب آبخوان {aquifer[0]} نسبت به ماه قبل بر حسب متر",
                3 : f"تغییرات تراز سطح آب آبخوان {aquifer[0]} نسبت به ماه سال قبل بر حسب متر",
                4 : f"تغییرات ذخیره آبخوان {aquifer[0]} نسبت به ماه قبل بر حسب متر",
                5 : f"تغییرات ذخیره آبخوان {aquifer[0]} نسبت به ماه سال قبل بر حسب متر"
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
                elif para == 2 or para == 4:
                    df_result["حداکثر سالانه"] = df_result.iloc[:,1:13].max(axis=1).round(2)
                    df_result["حداقل سالانه"] = df_result.iloc[:,1:13].min(axis=1).round(2)
                    df_result["میانگین سالانه"] = df_result.iloc[:,1:13].mean(axis=1).round(2)
                    df_result["تجمعی میانگین سالانه"] = df_result["میانگین سالانه"].cumsum(skipna=True).round(2) 
                    df_result["مجموع سالانه"] = df_result.iloc[:,1:13].sum(axis=1).round(2)
                    df_result["تجمعی مجموع سالانه"] = df_result["مجموع سالانه"].cumsum(skipna=True).round(2)
                elif para == 3 or para == 5:
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