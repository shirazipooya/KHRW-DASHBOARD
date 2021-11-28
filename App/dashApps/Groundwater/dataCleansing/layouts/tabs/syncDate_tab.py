from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.dataCleansing.layouts.bodies import *
from App.dashApps.Groundwater.dataCleansing.layouts.sidebars import *


# -----------------------------------------------------------------------------
# SYNC DATE TAB
# -----------------------------------------------------------------------------

SYNC_DATE_TAB = html.Div(
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
                        SIDEBAR___SYNC_DATE_TAB
                    ]
                ),
                html.Div(
                    className='col-9 m-0 p-0',
                    children=[
                        BODY___SYNC_DATE_TAB
                    ]
                )
            ]
        ),
        dcc.Store(
            id='DATABASE_STATE___SYNC_DATE_TAB',
            storage_type='memory'            
        ),        
        dcc.Store(
            id='DATA_STORE___SYNC_DATE_TAB',
            storage_type='memory'
        ),
        dcc.Store(
            id='GEOINFO_DATA_STORE___SYNC_DATE_TAB',
            storage_type='memory'
        ),       
        dcc.Interval(
            id='LOAD_DATABASE___SYNC_DATE_TAB',
            interval=1 * 10000,
            n_intervals=0,
            max_intervals=1
        ),
        
    ]
)