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
    style_as_list_view=False,
    style_table={
        'overflowX': 'auto',
        'direction': 'rtl',
    },
    style_cell={
        'height': 'auto',
        'border': '1px solid grey',
        'font-size': '14px',
        'text_align': 'center',
        'minWidth': 50,
        'width': 'auto',
        'maxWidth': 70,
        'direction': 'ltr',
        'padding': '5px',
    },
    style_header={
        'backgroundColor': 'rgb(90, 170, 255)',
        'border':'1px solid grey',
        'fontWeight': 'bold',
        'text_align': 'center',
        'whiteSpace': 'normal',
        'height': 'auto',
    },
    # style_data={
    #     'color': 'black',
    #     'backgroundColor': 'white',
    #     'whiteSpace': 'normal',
    #     'height': 'auto',
    #     'lineHeight': '15px'
    # },
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
            className="text-center p-0 m-0 pt-5",
            children=[
                html.Label(
                    id="TABLE_HEADER___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER",
                    className="text-primary",
                    style={
                        "font-size": "larger"
                    }
                ),
            ]
        ),
    

        html.Div(
            id="TABLE_HOLDER___BODY___WELLS_TAB___DATA_VISUALIZATION___GROUNDWATER",
            className="row m-0 p-2 justify-content-center",
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