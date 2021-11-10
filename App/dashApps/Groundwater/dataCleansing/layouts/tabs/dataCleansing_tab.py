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
                "height": "100%"
            },
            children=[
                html.Div(
                    className='col-3 m-0 p-3 bg-light',
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
        dcc.Interval(
            id='LOAD_DATABASE___DATA_CLEANSING_TAB',
            interval=1 * 5000,
            n_intervals=0,
            max_intervals=1
        ) 
    ]
)