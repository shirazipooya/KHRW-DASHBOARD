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




# ---------------------------------------------------------
# CONTROLS
# ---------------------------------------------------------


# -------------------------------------
# 1- COLLAPSE SELLECT WELL
# -------------------------------------

# STUDY AREA:
STUDY_AREA_CARD___CONTROLS___DATA_CLEANSING_TAB = html.Div(
    className='form-group', 
    children=[
        html.Label(
            dir='rtl', 
            children='- محدوده مطالعاتی',
            style={
                "font-size": "1rem",
            }
        ),
        dcc.Dropdown(
            id='STUDY_AREA_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
            multi=True,
            placeholder='انتخاب ...'
        ) 
    ]
)


# AQUIFER:
AQUIFER_CARD___CONTROLS___DATA_CLEANSING_TAB = html.Div(
    className='form-group', 
    children=[
        html.Label(
            className='text-center',
            dir='rtl', 
            children='- آبخوان',
            style={
                "font-size": "1rem",
            }
        ),
        dcc.Dropdown(
            id='AQUIFER_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
            multi=True,
            placeholder='انتخاب ...'
        ) 
    ]
)


# WELL:
WELL_CARD___CONTROLS___DATA_CLEANSING_TAB = html.Div(
    className='form-group', 
    children=[
        html.Label(
            className='text-center',
            dir='rtl', 
            children='- چاه مشاهده‌ای',
            style={
                "font-size": "1rem",
            }
        ),
        dcc.Dropdown(
            id='WELL_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
            multi=True,
            placeholder='انتخاب ...'
        ) 
    ]
)


# MAP:
MAP___DATA_CLEANSING_TAB = html.Div(
    children=[
        dcc.Graph(
            id='MAP___GRAPH_MAP___DATA_CLEANSING_TAB',
            className="border border-secondary",
            style={
                "height": "300px",
            },
        )
    ],
    className="pt-3"
)


# COLLAPSE SELLECT WELL:
COLLAPSE___SELLECT_WELL___DATA_CLEANSING_TAB = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___SELECT_WELL___DATA_CLEANSING_TAB"
                        ),
                        "انتخاب چاه مشاهده‌ای",
                    ]            
                )      
            ],
            id="OPEN_CLOSE_COLLAPSE___SELECT_WELL___DATA_CLEANSING_TAB",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                STUDY_AREA_CARD___CONTROLS___DATA_CLEANSING_TAB,
                                AQUIFER_CARD___CONTROLS___DATA_CLEANSING_TAB,
                                WELL_CARD___CONTROLS___DATA_CLEANSING_TAB,
                                MAP___DATA_CLEANSING_TAB
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE___SELECT_WELL___DATA_CLEANSING_TAB",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)




# -------------------------------------
# 2- COLLAPSE SELECT OUTLIER
# -------------------------------------

DATA_CLEANSING_METHOD___MANUAL___DATA_CLEANSING_TAB = html.Div(
    children=[
        html.Div(
            className="form-group inline m-0",
            style={
                'display': 'flex',
                'justify-content': 'space-between'
            },
            children=[
                html.Label(
                    className='text-center',
                    dir='rtl', 
                    children='- روش میانگین',
                    # style={
                    #     "font-weight": "bold",
                    #     "font-size": "1rem",
                    # }
                ),
                dcc.Dropdown(
                    id='METHOD_1_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
                    placeholder='انتخاب ...',
                    value=4,
                    options=[{"label": f"{x}x", "value": x} for x in [i for i in range(1, 11)]],
                    clearable=False
                ) 
            ]
        ),
        html.Div(
            className="form-group inline m-0 mt-1",
            style={
                'display': 'flex',
                'justify-content': 'space-between'
            },
            children=[
                html.Label(
                    className='text-center',
                    dir='rtl', 
                    children='- روش مشتق',
                    # style={
                    #     "font-weight": "bold",
                    #     "font-size": "1rem",
                    # }
                ),
                dcc.Dropdown(
                    id='METHOD_2_SELECT___CONTROLS___DATA_CLEANSING_TAB', 
                    placeholder='انتخاب ...',
                    value=4,
                    options=[{"label": f"{x}%", "value": x} for x in [i for i in range(1, 11)]],
                    clearable=False
                ) 
            ]
        )
    ]
)


# COLLAPSE SELECT OUTLIER:
COLLAPSE___SELECT_OUTLIER____DATA_CLEANSING_TAB = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___SELECT_OUTLIER____DATA_CLEANSING_TAB"
                        ),
                        "شناسایی داده‌های پرت",
                    ]            
                )      
            ],
            id="OPEN_CLOSE_COLLAPSE___SELECT_OUTLIER____DATA_CLEANSING_TAB",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                DATA_CLEANSING_METHOD___MANUAL___DATA_CLEANSING_TAB
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE___SELECT_OUTLIER____DATA_CLEANSING_TAB",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)



# -------------------------------------
# 3- COLLAPSE DATA CLEANSING METHOD
# -------------------------------------


# COLLAPSE DATA CLEANSING METHOD:
COLLAPSE___DATA_CLEANSING_METHOD___DATA_CLEANSING_TAB = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___DATA_CLEANSING_METHOD___DATA_CLEANSING_TAB"
                        ),
                        "اصلاح داده‌ها",
                    ]            
                )      
            ],
            id="OPEN_CLOSE_COLLAPSE___DATA_CLEANSING_METHOD___DATA_CLEANSING_TAB",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                dcc.RadioItems(
                                    id="COLLAPSE___DATA_CLEANSING_METHOD_SELECT___DATA_CLEANSING_TAB",
                                    options=[
                                        {'label': 'دستی', 'value': 'MANUAL'},
                                        {'label': 'خودکار', 'value': 'AUTOMATIC'},
                                    ],
                                    value='MANUAL',
                                    style={
                                        'display': 'flex',
                                        'justify-content': 'space-around'
                                    },
                                    inputClassName="ml-1",
                                    labelClassName="m-0"                                    
                                ),
                                html.Div(
                                    id="COLLAPSE___DATA_CLEANSING_METHOD_SELECT_POPUP___DATA_CLEANSING_TAB",
                                    children=[]
                                )
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE___DATA_CLEANSING_METHOD___DATA_CLEANSING_TAB",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)








# -------------------------------------
# BUTTONS
# -------------------------------------

# BUTTON:
BUTTON___BUTTONS___DATA_CLEANSING_TAB = dbc.Button(
    id='BUTTON___BUTTONS___DATA_CLEANSING_TAB',
    className="me-1",
    size="md",
    children='ذخیره تغییرات', 
    color='primary',
    n_clicks=0
)

# TOAST:
TOAST___BUTTONS___DATA_CLEANSING_TAB = dbc.Toast(
    id='TOAST___BUTTONS___DATA_CLEANSING_TAB',
    is_open=False,
    dismissable=True,
    duration=5000
)




# -------------------------------------
# SIDEBAR
# -------------------------------------

SIDEBAR___DATA_CLEANSING_TAB = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        COLLAPSE___SELLECT_WELL___DATA_CLEANSING_TAB,
        COLLAPSE___SELECT_OUTLIER____DATA_CLEANSING_TAB,
        COLLAPSE___DATA_CLEANSING_METHOD___DATA_CLEANSING_TAB,
        html.Div(
            className="text-left m-0 p-0 pt-3",
            children=[
                BUTTON___BUTTONS___DATA_CLEANSING_TAB,
                TOAST___BUTTONS___DATA_CLEANSING_TAB                
            ]
        ),     
    ]
)