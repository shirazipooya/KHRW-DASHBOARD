# -----------------------------------------------------------------------------
# SYNC DATE TAB - BODY
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

GRAPH___SYNC_DATE_TAB = dcc.Graph(
    id='GRAPH___SYNC_DATE_TAB',
    style={
        "height": "100%",
        "width": "100%"
    },
)



# -------------------------------------
# BODY
# -------------------------------------

BODY___SYNC_DATE_TAB = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        html.Div(
            className="row m-0 p-2",
            children=[
                GRAPH___SYNC_DATE_TAB
            ]
        )
    ]
)