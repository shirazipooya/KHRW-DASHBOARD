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

GRAPH___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER = dcc.Graph(
    id='GRAPH___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER',
    style={
        "height": "50%",
        "width": "100%"
    },
)


# -------------------------------------
# TABLE
# -------------------------------------

TABLE___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER = dash_table.DataTable(
    id="TABLE___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER",
    editable=False,
    # sort_action='native',
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
        'backgroundColor': 'rgb(120, 180, 220)',
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

BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        
        html.Div(
            className="row m-0 p-2",
            style={
                "height": "50%",
                "width": "100%"
            },
            children=[
                GRAPH___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER
            ]
        ),
        
        html.Div(
            id="TABLE_HOLDER___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER",
            className="row m-0 p-2 pt-4 justify-content-center",
            dir="ltr",
            hidden=True,
            style={
                "height": "50%",
            },
            children=[
                html.Div(
                    children=[
                        TABLE___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER
                    ],
                    className="row p-0 m-0"
                ),
                
            ]
        ),
    ]
)