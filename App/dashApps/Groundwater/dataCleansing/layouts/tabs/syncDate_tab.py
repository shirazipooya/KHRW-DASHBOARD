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
                "height": "95vh"
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
            id='GROUNDWATER_SYNC_DATE_DATA_STATE___SYNC_DATE_TAB',
            storage_type='memory'            
        ), 
        
        
        dcc.Store(
            id='GROUNDWATER_SYNC_DATE_DATA_STORE___SYNC_DATE_TAB',
            storage_type='memory'            
        ),
        
        dcc.Store(
            id='GROUNDWATER_SYNC_DATE_DATA_UPDATE_STATE___SYNC_DATE_TAB',
            storage_type='memory',
            data="NO"
        ),
        
        dcc.Interval(
            id='GROUNDWATER_SYNC_DATE_DATA_UPDATE_INTERVAL___SYNC_DATE_TAB',
            interval=1 * 1,
            n_intervals=0,
            max_intervals=1
        ),
            
        dcc.Interval(
            id='INTERVAL___SYNC_DATE_TAB',
            interval=1 * 2,
            n_intervals=0,
            max_intervals=1
        ),
        
    ]
)