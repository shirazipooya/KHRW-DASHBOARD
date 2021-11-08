# -----------------------------------------------------------------------------
# DATA CLEANSING TAB - BODY
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

GRAPH___DATA_CLEANSING_TAB = dcc.Graph(
    id='GRAPH___GRAPH_MAP___DATA_CLEANSING_TAB',
    style={
        "height": "50%",
        "width": "100%"
    },
)


# -------------------------------------
# TABLE
# -------------------------------------

TABLE___DATA_CLEANSING_TAB = dash_table.DataTable(
    id="TABLE___DATA_CLEANSING_TAB",
    editable=True,
    page_size=12,
    style_as_list_view=True,
    style_table={
        'overflowX': 'auto',
        'overflowY': 'auto',
        'direction': 'rtl',
    },
    style_cell={
        'border': '1px solid grey',
        'font-size': '14px',
        'text_align': 'center',
        'minWidth': 150,
        'maxWidth': 200,
    },
    style_header={
        'backgroundColor': 'rgb(210, 210, 210)',
        'border':'1px solid grey',
        'fontWeight': 'bold',
        'text_align': 'center',
        'height': 'auto',
    },
    style_data={
        'color': 'black',
        'backgroundColor': 'white'
    },
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(245, 245, 245)',
        }
    ]
)




# -------------------------------------
# BODY
# -------------------------------------

BODY___DATA_CLEANSING_TAB = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        html.Div(
            className="row m-0 p-2",
            style={
                "height": "50%",
                "width": "100%"
            },
            children=[
                GRAPH___DATA_CLEANSING_TAB
            ]
        ),
        html.Div(
            id="TABLE_HOLDER___BODY___DATA_CLEANSING_TAB",
            className="row m-0 p-2 justify-content-center",
            dir="ltr",
            hidden=True,
            style={
                "height": "50%",
            },
            children=[
                TABLE___DATA_CLEANSING_TAB
            ]
        )
    ]
)