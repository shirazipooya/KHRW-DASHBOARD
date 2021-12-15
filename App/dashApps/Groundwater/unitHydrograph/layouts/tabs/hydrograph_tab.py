from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.unitHydrograph.layouts.bodies import *
from App.dashApps.Groundwater.unitHydrograph.layouts.sidebars import *


# -----------------------------------------------------------------------------
# DATA CLEANSING TAB
# -----------------------------------------------------------------------------

HYDROGRAPH_TAB = html.Div(
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
                        SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER
                    ]
                ),
                html.Div(
                    className='col-9 m-0 p-0',
                    children=[
                        BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER
                    ]
                )
            ]
        ),
        
        # DATA STATE ------------------------------ 
        dcc.Store(
            id='DATA_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
            storage_type='memory',
            data="NO"
        ),
        
        dcc.Store(
            id='GEOINFO_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
            storage_type='memory',
            data="NO"
        ),  
        
        dcc.Store(
            id='UNIT_HYDROGRAPH_DATA_STATE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
            storage_type='memory',
            data="NO"
        ),  

        # DATA STORE ------------------------------
        dcc.Store(
            id='DATA_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
            storage_type='memory'
        ),        
       
        dcc.Store(
            id='GEOINFO_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
            storage_type='memory'
        ),        
       
        dcc.Store(
            id='UNIT_HYDROGRAPH_DATA_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
            storage_type='memory'
        ),        
       
        dcc.Store(
            id='THIESSEN_STORE___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
            storage_type='memory'
        ),        
       
        # DATA INTERVAL ---------------------------         
        dcc.Interval(
            id='INTERVAL___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
            interval=1 * 800,
            n_intervals=0,
            max_intervals=1
        ),

    ]
)