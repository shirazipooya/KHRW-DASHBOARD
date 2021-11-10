# -----------------------------------------------------------------------------
# MISSING DATA TAB - BODY
# -----------------------------------------------------------------------------



# -------------------------------------
# MODULES
# -------------------------------------

import base64
import numpy as np
from datetime import date
from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc
import dash_daq as daq



# -------------------------------------
# GRAPH
# -------------------------------------

GRAPH___MISSING_DATA_TAB = dcc.Graph(
    id='GRAPH___MISSING_DATA_TAB',
    style={
        "height": "50%",
        "width": "100%"
    },
)



# -------------------------------------
# BODY
# -------------------------------------

BODY___MISSING_DATA_TAB = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        html.Div(
            className="row m-0 p-2",
            style={
                "height": "50%",
                "width": "100%"
            },
            children=[
                GRAPH___MISSING_DATA_TAB
            ]
        )
    ]
)