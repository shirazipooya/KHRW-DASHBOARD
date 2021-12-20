# -----------------------------------------------------------------------------
# MISSING DATA TAB - SIDEBAR
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
# CONTROLS
# -------------------------------------

# -------------------------------------
# 1- COLLAPSE SELLECT WELL
# -------------------------------------


# STUDY AREA:
STUDY_AREA_CARD___CONTROLS___SYNC_DATE_TAB = html.Div(
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
            id='STUDY_AREA_SELECT___CONTROLS___SYNC_DATE_TAB', 
            multi=False,
            placeholder='انتخاب ...'
        ) 
    ]
)

# AQUIFER:
AQUIFER_CARD___CONTROLS___SYNC_DATE_TAB = html.Div(
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
            id='AQUIFER_SELECT___CONTROLS___SYNC_DATE_TAB', 
            multi=False,
            placeholder='انتخاب ...'
        ) 
    ]
)

# WELL:
WELL_CARD___CONTROLS___SYNC_DATE_TAB = html.Div(
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
            id='WELL_SELECT___CONTROLS___SYNC_DATE_TAB', 
            multi=False,
            placeholder='انتخاب ...'
        ) 
    ]
)


# COLLAPSE SELLECT WELL:
COLLAPSE___SELLECT_WELL___SYNC_DATE_TAB = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___SELECT_WELL___SYNC_DATE_TAB"
                        ),
                        "انتخاب چاه مشاهده‌ای",
                    ]            
                )      
            ],
            id="OPEN_CLOSE_COLLAPSE___SELECT_WELL___SYNC_DATE_TAB",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                STUDY_AREA_CARD___CONTROLS___SYNC_DATE_TAB,
                                AQUIFER_CARD___CONTROLS___SYNC_DATE_TAB,
                                WELL_CARD___CONTROLS___SYNC_DATE_TAB,
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE___SELECT_WELL___SYNC_DATE_TAB",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)







# -------------------------------------
# 2- COLLAPSE SYNC DATE
# -------------------------------------

# SYNC DATE:
SYNC_METHOD_CARD___CONTROLS___SYNC_DATE_TAB = html.Div(
    className="form-group m-0 my-1",
    children=[
        html.Div(
            className="form-group inline m-0 my-1 d-flex align-items-center",
            style={
                'display': 'flex',
                # 'justify-content': 'space-between'
            },
            children=[
                html.Label(
                    className='text-right m-0',
                    dir='rtl', 
                    children='تبدیل به روز',
                    style={
                        "font-size": "1rem",
                    }
                ),
                dcc.Dropdown(
                    id='SYNC_METHOD_SELECT___CONTROLS___SYNC_DATE_TAB',
                    value=15,
                    options=[
                        {"label": day, "value": day} for day in range(1,31)
                    ],
                    multi=False,
                    clearable=False,
                    className="mx-3"
                ),
                html.Label(
                    className='text-center m-0',
                    dir='rtl', 
                    children='هر ماه',
                    style={
                        "font-size": "1rem",
                    }
                ),

            ]
        )
    ]
)


# COLLAPSE SELECT DATE:
COLLAPSE___SYNC_METHOD___SYNC_DATE_TAB = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___SYNC_METHOD___SYNC_DATE_TAB"
                        ),
                        "تنظیمات هماهنگ‌سازی تاریخ",
                    ]            
                )      
            ],
            id="OPEN_CLOSE_COLLAPSE___SYNC_METHOD___SYNC_DATE_TAB",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                SYNC_METHOD_CARD___CONTROLS___SYNC_DATE_TAB,
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE___SYNC_METHOD___SYNC_DATE_TAB",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)







# -------------------------------------
# 3- COLLAPSE HOW MODIFY
# -------------------------------------

HOW_MODIFY_CARD___CONTROLS___SYNC_DATE_TAB = html.Div(
    className='form-group pt-2', 
    children=[
        dcc.RadioItems(
            id='HOW_MODIFY_CARD___CONTROLS___SYNC_DATE_TAB', 
            value=0,
            options=[
                {'label': 'همه چاه‌های مشاهده‌ای بانک داده', 'value': 0},
            ],
            inputClassName="ml-1",
            labelClassName="mr-2"
        ) 
    ]
)

# COLLAPSE HOW MODIFY:
COLLAPSE___HOW_MODIFY___SYNC_DATE_TAB = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___HOW_MODIFY___SYNC_DATE_TAB"
                        ),
                        "نحوه اعمال تغییرات",
                    ]            
                )      
            ],
            id="OPEN_CLOSE_COLLAPSE___HOW_MODIFY___SYNC_DATE_TAB",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                html.Label("هماهنگ‌‌سازی تاریخ:"),
                                HOW_MODIFY_CARD___CONTROLS___SYNC_DATE_TAB
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE___HOW_MODIFY___SYNC_DATE_TAB",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)





# -------------------------------------
# BUTTONS
# -------------------------------------

# BUTTON:
BUTTON___BUTTONS___SYNC_DATE_TAB = dbc.Button(
    id='BUTTON___BUTTONS___SYNC_DATE_TAB',
    className="me-1 w-50",
    size="md",
    children='هماهنگ‌سازی تاریخ', 
    color='primary',
    n_clicks=0
)

# TOAST:
TOAST___BUTTONS___SYNC_DATE_TAB = dbc.Toast(
    id='TOAST___BUTTONS___SYNC_DATE_TAB',
    is_open=False,
    dismissable=True,
    duration=5000
)




# -------------------------------------
# SIDEBAR
# -------------------------------------

SIDEBAR___SYNC_DATE_TAB = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        COLLAPSE___SELLECT_WELL___SYNC_DATE_TAB,
        COLLAPSE___SYNC_METHOD___SYNC_DATE_TAB,
        COLLAPSE___HOW_MODIFY___SYNC_DATE_TAB,
        html.Div(
            className="text-left m-0 p-0 pt-3",
            children=[
                BUTTON___BUTTONS___SYNC_DATE_TAB,
                TOAST___BUTTONS___SYNC_DATE_TAB                
            ]
        )

    ]
)