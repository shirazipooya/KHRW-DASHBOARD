from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.dataVisualization.layouts.bodies import *
from App.dashApps.Groundwater.dataVisualization.layouts.sidebars import *


# -----------------------------------------------------------------------------
# DATA CLEANSING TAB
# -----------------------------------------------------------------------------

AQUIFERS_TAB = html.Div(
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
                        SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER
                    ]
                ),
                html.Div(
                    className='col-9 m-0 p-0',
                    children=[
                        # BODY___DATA_CLEANSING_TAB
                    ]
                )
            ]
        ),
        
        # DATA STATE ------------------------------ 
        dcc.Store(
            id='DATA_STATE___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
            storage_type='memory'            
        ),

        # DATA STORE ------------------------------
        dcc.Store(
            id='DATA_STORE___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
            storage_type='memory'
        ),        
       
        # DATA INTERVAL ---------------------------         
        dcc.Interval(
            id='INTERVAL___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
            interval=1 * 90,
            n_intervals=0,
            max_intervals=1
        ),

    ]
)