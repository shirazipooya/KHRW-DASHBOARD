
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
# 1- COLLAPSE SELLECT WELL
# -------------------------------------

# STUDY AREA:
STUDY_AREA_CARD___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
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
            id='STUDY_AREA_SELECT___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 
            multi=True,
            placeholder='انتخاب ...'
        ) 
    ]
)

# AQUIFER:
AQUIFER_CARD___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
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
            id='AQUIFER_SELECT___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 
            multi=True,
            placeholder='انتخاب ...'
        ) 
    ]
)

# # WELL:
# WELL_CARD___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
#     className='form-group', 
#     children=[
#         html.Label(
#             className='text-center',
#             dir='rtl', 
#             children='- چاه مشاهده‌ای',
#             style={
#                 "font-size": "1rem",
#             }
#         ),
#         dcc.Dropdown(
#             id='WELL_SELECT___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 
#             multi=True,
#             placeholder='انتخاب ...'
#         ) 
#     ]
# )

# MAP:
MAP_CARD___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
    children=[
        dcc.Graph(
            id='MAP___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
            className="border border-secondary",
            style={
                "height": "300px",
            },
        )
    ],
    className="pt-3"
)

# COLLAPSE SELLECT WELL:
COLLAPSE___SELLECT_WELL___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___SELECT_WELL___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER"
                        ),
                        "انتخاب آبخوان",
                    ]            
                )      
            ],
            id="OPEN_CLOSE_COLLAPSE___SELECT_WELL___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                STUDY_AREA_CARD___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER,
                                AQUIFER_CARD___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER,
                                # WELL_CARD___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER,
                                MAP_CARD___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE___SELECT_WELL___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)



# -------------------------------------
# SIDEBAR
# -------------------------------------

SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        COLLAPSE___SELLECT_WELL___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER,    
    ]
)