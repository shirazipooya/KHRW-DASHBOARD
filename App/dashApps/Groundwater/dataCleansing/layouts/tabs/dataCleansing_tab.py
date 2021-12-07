from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.dataCleansing.layouts.bodies import *
from App.dashApps.Groundwater.dataCleansing.layouts.sidebars import *


# -----------------------------------------------------------------------------
# DATA CLEANSING TAB
# -----------------------------------------------------------------------------

DATA_CLEANSING_TAB = html.Div(
    className="m-0 p-0",
    children=[
        html.Div(
            className='row m-0 p-0',
            style={
                "height": "95vh"
            },
            children=[
                html.Div(
                    className='col-3 m-0 p-2 bg-light',
                    children=[
                        SIDEBAR___DATA_CLEANSING_TAB
                    ]
                ),
                html.Div(
                    className='col-9 m-0 p-0',
                    children=[
                        BODY___DATA_CLEANSING_TAB
                    ]
                )
            ]
        ),
        # DATA STATE ------------------------------ 
        dcc.Store(
            id='GROUNDWATER_RAW_DATA_STATE___DATA_CLEANSING_TAB',
            storage_type='memory'            
        ),
        dcc.Store(
            id='GROUNDWATER_CLEANSING_DATA_STATE___DATA_CLEANSING_TAB',
            storage_type='memory'            
        ),
        dcc.Store(
            id='GEOINFO_DATA_STATE___DATA_CLEANSING_TAB',
            storage_type='memory'
        ),
        # DATA STORE ------------------------------        
        dcc.Store(
            id='GROUNDWATER_RAW_DATA_STORE___DATA_CLEANSING_TAB',
            storage_type='memory'
        ),        
        dcc.Store(
            id='GROUNDWATER_CLEANSING_DATA_STORE___DATA_CLEANSING_TAB',
            storage_type='memory'
        ),        
        dcc.Store(
            id='GEOINFO_DATA_STORE___DATA_CLEANSING_TAB',
            storage_type='memory'
        ),
        # ------------------------------    
        dcc.Store(
            id='GRAPH_SELECTED_DATA_STORE___DATA_CLEANSING_TAB',
            storage_type='memory'
        ),        
        dcc.Store(
            id='GROUNDWATER_CLEANSING_DATA_UPDATE_STATE___DATA_CLEANSING_TAB',
            storage_type='memory',
            data="NO"
        ),        
        dcc.Interval(
            id='INTERVAL___DATA_CLEANSING_TAB',
            interval=1 * 90,
            n_intervals=0,
            max_intervals=1
        ),
        dcc.Interval(
            id='GROUNDWATER_CLEANSING_DATA_UPDATE_INTERVAL___DATA_CLEANSING_TAB',
            interval=1 * 100,
            n_intervals=0,
            max_intervals=1
        ) 
    ]
)