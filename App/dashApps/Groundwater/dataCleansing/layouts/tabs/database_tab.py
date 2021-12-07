from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.dataCleansing.layouts.bodies import *
from App.dashApps.Groundwater.dataCleansing.layouts.sidebars import *


# -----------------------------------------------------------------------------
# SETTINGS TAB
# -----------------------------------------------------------------------------

DATABASE_TAB = html.Div(
    className="m-0 p-0",
    children=[
        html.Div(
            className='row m-0 p-0',
            style={
                "height": "100vh"
            },
            children=[
                html.Div(
                    className='col-3 m-0 p-3 bg-light',
                    children=[
                        SIDEBAR___DATABASE_TAB
                    ]
                ),
                html.Div(
                    className='col-9 m-0 p-0',
                    children=[

                    ]
                )
            ]
        ),
        dcc.Store(
            id='SPREADSHEET_DATA_STATE___DATABASE_TAB',
            storage_type='memory'            
        ),
        dcc.Store(
            id='DATA_STORE___DATABASE_TAB',
            storage_type='memory'
        ),        
        dcc.Store(
            id='GEOINFO_DATA_STORE___DATABASE_TAB',
            storage_type='memory'
        ),        
        dcc.Interval(
            id='INTERVAL___SPREADSHEET_DATABASE___DATABASE_TAB',
            interval=1 * 20,
            n_intervals=0,
            max_intervals=1
        ) 
    ]
)
