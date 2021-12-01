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
        dcc.Store(
            id='DATABASE_STATE___DATA_CLEANSING_TAB',
            storage_type='memory'            
        ),        
        dcc.Store(
            id='DATA_STORE___DATA_CLEANSING_TAB',
            storage_type='memory'
        ),        
        dcc.Store(
            id='GEOINFO_DATA_STORE___DATA_CLEANSING_TAB',
            storage_type='memory'
        ),        
        dcc.Store(
            id='GRAPH_SELECTED_DATA_STORE___DATA_CLEANSING_TAB',
            storage_type='memory'
        ),        
        dcc.Store(
            id='DATABASE_UPDATE_STATE___DATA_CLEANSING_TAB',
            storage_type='memory',
            data="NO"
        ),        
        dcc.Interval(
            id='LOAD_DATABASE___DATA_CLEANSING_TAB',
            interval=1 * 110,
            n_intervals=0,
            max_intervals=1
        ),
        dcc.Interval(
            id='LOAD_DATABASE_UPDATE___DATA_CLEANSING_TAB',
            interval=1 * 1,
            n_intervals=0,
            max_intervals=1
        ) 
    ]
)