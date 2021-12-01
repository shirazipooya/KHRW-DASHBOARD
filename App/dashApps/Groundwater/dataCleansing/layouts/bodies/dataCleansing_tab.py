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
# TABLE SELECTED
# -------------------------------------

TABLE_SELECTED___DATA_CLEANSING_TAB = dash_table.DataTable(
    id="TABLE_SELECTED___DATA_CLEANSING_TAB",
    editable=True,
    row_deletable=True,
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
# TABLE
# -------------------------------------

TABLE___DATA_CLEANSING_TAB = dash_table.DataTable(
    id="TABLE___DATA_CLEANSING_TAB",
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

BODY___DATA_CLEANSING_TAB = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        html.Div(
            id="INFO_CARD_HOLDER___BODY___DATA_CLEANSING_TAB",
            className="row m-0 p-2 justify-content-center",
            dir="ltr",
            hidden=True,
            # style={
            #     "height": "50%",
            # },
            children=[
                html.Div(
                    className="card-group justify-content-around w-100",
                    children=[
                        # CARD 1
                        html.Div(
                            className="card border mb-1",
                            style={"min-width": "12rem"},
                            children=[
                                html.Div(
                                    className="card-header text-center fw-bold",
                                    children="بیشینه - کمینه"
                                ),
                                html.Div(
                                    className="card-body  py-1 px-3",
                                    children=[
                                        html.Div(
                                            className="card-text text-center",
                                            children=[
                                                html.Div(
                                                    dir="rtl",
                                                    style={
                                                        'display': 'flex',
                                                        'justify-content': 'space-around'
                                                    },
                                                    children=[
                                                        html.Label(
                                                            children="بیشینه"
                                                        ),
                                                        html.P(
                                                            id="INFO_CARD___MAX___BODY___DATA_CLEANSING_TAB",
                                                            children="225.5"
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    dir="rtl",
                                                    style={
                                                        'display': 'flex',
                                                        'justify-content': 'space-around'
                                                    },
                                                    children=[
                                                        html.Label(
                                                            className="m-0",
                                                            children="کمینه"
                                                        ),
                                                        html.P(
                                                            id="INFO_CARD___MIN___BODY___DATA_CLEANSING_TAB",
                                                            className="m-0",
                                                            children="225.5"
                                                        )
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ]
                                )
                            ]
                        ),
                        # CARD 2
                        html.Div(
                            className="card border mb-1",
                            style={"min-width": "12rem"},
                            children=[
                                html.Div(
                                    className="card-header text-center fw-bold",
                                    children="میانگین - میانه"
                                ),
                                html.Div(
                                    className="card-body   py-1 px-3",
                                    children=[
                                        html.Div(
                                            className="card-text text-center",
                                            children=[
                                                html.Div(
                                                    dir="rtl",
                                                    style={
                                                        'display': 'flex',
                                                        'justify-content': 'space-around'
                                                    },
                                                    children=[
                                                        html.Label(
                                                            children="میانگین"
                                                        ),
                                                        html.P(
                                                            id="INFO_CARD___MEAN___BODY___DATA_CLEANSING_TAB",
                                                            children="225.5"
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    dir="rtl",
                                                    style={
                                                        'display': 'flex',
                                                        'justify-content': 'space-around'
                                                    },
                                                    children=[
                                                        html.Label(
                                                            className="m-0",
                                                            children="میانه"
                                                        ),
                                                        html.P(
                                                            id="INFO_CARD___MEDIAN___BODY___DATA_CLEANSING_TAB",
                                                            className="m-0",
                                                            children="225.5"
                                                        )
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ]
                                )
                            ]
                        ),
                        # CARD 3
                        html.Div(
                            className="card border mb-1",
                            style={"min-width": "12rem"},
                            children=[
                                html.Div(
                                    className="card-header text-center fw-bold",
                                    children="سطح ایستابی صفر"
                                ),
                                html.Div(
                                    className="card-body  py-1 px-3 align-items-center",
                                    children=[
                                        html.P(
                                            className="card-text",
                                            children=[
                                                html.Div(
                                                    dir="rtl",
                                                    style={
                                                        'display': 'flex',
                                                        'justify-content': 'center'
                                                    },
                                                    children=[
                                                        html.P(
                                                            id="INFO_CARD___ZERO_VALUE___BODY___DATA_CLEANSING_TAB",
                                                            className="m-0  pl-2",
                                                            children="5"
                                                        ),
                                                        html.Label(
                                                            children="عدد"
                                                        ),
                                                    ]
                                                ),
                                            ]
                                        ),

                                    ]
                                )
                            ]
                        ),
                        # CARD 4
                        html.Div(
                            className="card border mb-1",
                            style={"min-width": "12rem"},
                            children=[
                                html.Div(
                                    className="card-header text-center fw-bold",
                                    children="تاریخ اشتباه"
                                ),
                                html.Div(
                                    className="card-body  py-1 px-3",
                                    children=[
                                        html.P(
                                            className="card-text align-items-center",
                                            children=[
                                                html.Div(
                                                    dir="rtl",
                                                    style={
                                                        'display': 'flex',
                                                        'justify-content': 'center'
                                                    },
                                                    children=[
                                                        html.P(
                                                            id="INFO_CARD___DATE___BODY___DATA_CLEANSING_TAB",
                                                            className="m-0 pl-2",
                                                            children="0"
                                                        ),
                                                        html.Label(
                                                            children="عدد"
                                                        ),
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ]
                                )
                            ]
                        ),
                    ],

                )

            ]
        ),
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
            id="TABLE_SELECTED_HOLDER___BODY___DATA_CLEANSING_TAB",
            className="row m-0 p-2 justify-content-center",
            dir="ltr",
            hidden=True,
            style={
                "height": "50%",
            },
            children=[
                html.H4(
                    children=[
                        "داده‌های انتخاب شده"
                    ],
                    className="row p-0 pb-1 m-0 text-secondary"
                ),
                html.Div(
                    children=[
                        TABLE_SELECTED___DATA_CLEANSING_TAB
                    ],
                    className="row p-0 m-0"
                ),
            ]
        ),
        html.Div(
            id="TABLE_HOLDER___BODY___DATA_CLEANSING_TAB",
            className="row m-0 p-2 pt-4 justify-content-center",
            dir="ltr",
            hidden=True,
            style={
                "height": "50%",
            },
            children=[
                html.H4(
                    children=[
                        "همه داده‌ها"
                    ],
                    className="row p-0 pb-1 m-0 text-primary"
                ),
                html.Div(
                    children=[
                        TABLE___DATA_CLEANSING_TAB
                    ],
                    className="row p-0 m-0"
                ),
                
            ]
        ),
    ]
)