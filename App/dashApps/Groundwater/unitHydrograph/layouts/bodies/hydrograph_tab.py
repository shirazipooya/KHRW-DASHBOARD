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

GRAPH___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = dcc.Graph(
    id='GRAPH___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
    style={
        "height": "50%",
        "width": "100%"
    },
)


# -------------------------------------
# MAP
# -------------------------------------

MAP___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = dcc.Graph(
    id='MAP___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
    style={
        "height": "50%",
        "width": "100%"
    },
)


# -------------------------------------
# TABLE
# -------------------------------------

TABLE___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = dash_table.DataTable(
    id="TABLE___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
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


TABLE_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = dash_table.DataTable(
    id="TABLE_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
    editable=False,
    # sort_action='native',
    page_size=100,
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
        'minWidth': 120,
        'width': 'auto',
        'maxWidth': 180,
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

BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    className='container-fluid m-0 p-0 block',
    children=[
        
        html.Div(
            className="row m-0 p-2",
            style={
                "height": "50%",
                "width": "100%"
            },
            children=[
                GRAPH___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER
            ]
        ),
        
        html.Div(
            className="text-center p-0 m-0 pt-5",
            children=[
                html.Label(
                    id="TABLE_TITLE___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
                    className="text-primary",
                    style={
                        "font-size": "larger"
                    }
                ),
            ]
        ),

        html.Div(
            id="TABLE_HOLDER___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            className="row m-0 p-2 justify-content-center",
            dir="ltr",
            hidden=True,
            style={
                "height": "50%",
            },
            children=[
                html.Div(
                    children=[
                        TABLE___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER
                    ],
                    className="row p-0 m-0"
                ),
            ]
        ),
        
        html.Div(
            id="MAP_HOLDER___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            className="row m-0 p-2",
            style={
                "height": "50%",
                "width": "100%"
            },
            children=[
                MAP___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER
            ]
        ),
                      
        html.Div(
            id="HOLDER_CARD_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            className="row p-0 m-0 pt-2",
            style={
                'display': 'flex',
                'justify-content': 'space-around'
            },
            children=[
                html.Div(
                    className="m-0 p-0 col-4 card",
                    children=[
                        html.Div(
                            className="card-header text-center font-weight-bold display-5",
                            children="تغییرات شبکه تیسن نسبت به ماه قبل"
                        ),
                        html.Div(
                            className="card-body",
                            children=[
                                html.Div(
                                    className="card-title text-primary",
                                    children=[
                                        html.I(
                                            className="fas fa-plus-circle ml-2",
                                        ),
                                        "چاه‌های بیشتر"
                                    ]
                                ),
                                html.Div(
                                    id="BP_CARD_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
                                    className="card-text text-center",
                                ),
                                html.Hr(),
                                html.Div(
                                    className="card-title text-danger pt-2",
                                    children=[
                                        html.I(
                                            className="fas fa-minus-circle ml-2",
                                        ),
                                        "چاه‌های کمتر"
                                    ]
                                ),
                                html.Div(
                                    id="BM_CARD_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
                                    className="card-text text-center",
                                )                                                
                            ]
                        ),                                        
                    ]
                ),
                html.Div(
                    className="m-0 p-0 col-4 card",
                    children=[
                        html.Div(
                            className="card-header text-center font-weight-bold display-5",
                            children="تغییرات شبکه تیسن نسبت به ماه بعد"
                        ),
                        html.Div(
                            className="card-body",
                            children=[
                                html.Div(
                                    className="card-title text-primary",
                                    children=[
                                        html.I(
                                            className="fas fa-plus-circle ml-2",
                                        ),
                                        "چاه‌های بیشتر"
                                    ]
                                ),
                                html.Div(
                                    className="card-text text-center",
                                    id="AP_CARD_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
                                ),
                                html.Hr(),
                                html.Div(
                                    className="card-title text-danger pt-2",
                                    children=[
                                        html.I(
                                            className="fas fa-minus-circle ml-2",
                                        ),
                                        "چاه‌های کمتر"
                                    ]
                                ),
                                html.Div(
                                    className="card-text text-center",
                                    id="AM_CARD_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
                                )                                                
                            ]
                        ),                                        
                    ]
                ),
            ]
        ),
        html.Div(
            id="TABLE_INFO_HOLDER___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            className="row m-0 p-2 justify-content-center",
            dir="ltr",
            hidden=True,
            style={
                "height": "50%",
            },
            children=[
                html.Div(
                    children=[
                        TABLE_INFO___BODY___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER
                    ],
                    className="row p-0 m-0"
                ),
            ]
        )         
    ]
)