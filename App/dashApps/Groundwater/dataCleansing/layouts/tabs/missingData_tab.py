from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.dataCleansing.layouts.bodies import *
from App.dashApps.Groundwater.dataCleansing.layouts.sidebars import *


# -----------------------------------------------------------------------------
# MISSING DATA TAB
# -----------------------------------------------------------------------------

MISSING_DATA_TAB = html.Div(
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
                        SIDEBAR___MISSING_DATA_TAB
                    ]
                ),
                html.Div(
                    className='col-9 m-0 p-0',
                    children=[
                        BODY___MISSING_DATA_TAB
                    ]
                )
            ]
        ),
        
        dcc.Store(
            id='GROUNDWATER_INTERPOLATED_DATA_STATE___MISSING_DATA_TAB',
            storage_type='memory'            
        ), 
        
        
        dcc.Store(
            id='GROUNDWATER_INTERPOLATED_DATA_STORE___MISSING_DATA_TAB',
            storage_type='memory'            
        ),
        
        dcc.Store(
            id='GROUNDWATER_INTERPOLATED_DATA_UPDATE_STATE___DATA_CLEANSING_TAB',
            storage_type='memory',
            data="NO"
        ),
        
        dcc.Interval(
            id='GROUNDWATER_INTERPOLATED_DATA_UPDATE_INTERVAL___DATA_CLEANSING_TAB',
            interval=1 * 70,
            n_intervals=0,
            max_intervals=1
        ),
            
        dcc.Interval(
            id='INTERVAL___MISSING_DATA_TAB',
            interval=1 * 80,
            n_intervals=0,
            max_intervals=1
        ),
        
    ]
)