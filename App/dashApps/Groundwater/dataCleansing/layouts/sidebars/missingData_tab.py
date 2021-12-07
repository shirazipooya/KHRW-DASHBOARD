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
STUDY_AREA_CARD___CONTROLS___MISSING_DATA_TAB = html.Div(
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
            id='STUDY_AREA_SELECT___CONTROLS___MISSING_DATA_TAB', 
            multi=False,
            placeholder='انتخاب ...'
        ) 
    ]
)

# AQUIFER:
AQUIFER_CARD___CONTROLS___MISSING_DATA_TAB = html.Div(
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
            id='AQUIFER_SELECT___CONTROLS___MISSING_DATA_TAB', 
            multi=False,
            placeholder='انتخاب ...'
        ) 
    ]
)

# WELL:
WELL_CARD___CONTROLS___MISSING_DATA_TAB = html.Div(
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
            id='WELL_SELECT___CONTROLS___MISSING_DATA_TAB', 
            multi=False,
            placeholder='انتخاب ...'
        ) 
    ]
)


# COLLAPSE SELLECT WELL:
COLLAPSE___SELLECT_WELL___MISSING_DATA_TAB = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___SELECT_WELL___MISSING_DATA_TAB"
                        ),
                        "انتخاب چاه مشاهده‌ای",
                    ]            
                )      
            ],
            id="OPEN_CLOSE_COLLAPSE___SELECT_WELL___MISSING_DATA_TAB",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                STUDY_AREA_CARD___CONTROLS___MISSING_DATA_TAB,
                                AQUIFER_CARD___CONTROLS___MISSING_DATA_TAB,
                                WELL_CARD___CONTROLS___MISSING_DATA_TAB,
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE___SELECT_WELL___MISSING_DATA_TAB",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)







# -------------------------------------
# 2- COLLAPSE SELECT OUTLIER
# -------------------------------------

# INTERPOLATE METHOD:
INTERPOLATE_METHOD_CARD___CONTROLS___MISSING_DATA_TAB = html.Div(
    className="form-group inline m-0 my-1",
    style={
        'display': 'flex',
        'justify-content': 'space-between'
    },
    children=[
        html.Label(
            className='text-center',
            dir='rtl', 
            children='- روش',
            style={
                "font-size": "1rem",
            }
        ),
        html.Div(
            className="w-75 p-0 m-0 text-center",
            children=[
                dcc.Dropdown(
                    id='INTERPOLATE_METHOD_SELECT___CONTROLS___MISSING_DATA_TAB',
                    value='akima',
                    options=[
                        {'label': 'Back Fill', 'value': 'bfill'},
                        {'label': 'Forward Fill', 'value': 'ffill'},
                        {'label': 'Pad', 'value': 'pad'},
                        {'label': 'Zero', 'value': 'zero'},
                        {'label': 'Linear', 'value': 'linear'},
                        {'label': 'Slinear', 'value': 'slinear'},
                        {'label': 'Akima', 'value': 'akima'},
                        {'label': 'Nearest', 'value': 'nearest'},
                        {'label': 'Spline', 'value': 'spline'},
                        {'label': 'Polynomial', 'value': 'polynomial'},
                        {'label': 'Cubic', 'value': 'cubic'},
                        {'label': 'Quadratic', 'value': 'quadratic'},
                        {'label': 'Barycentric', 'value': 'barycentric'},
                        {'label': 'Krogh', 'value': 'krogh'},
                        {'label': 'Piecewise Polynomial', 'value': 'piecewise_polynomial'},
                        {'label': 'Pchip', 'value': 'pchip'},
                        {'label': 'Cubicspline', 'value': 'cubicspline'},
                    ],
                    clearable=False
                ) 

            ]
        )
    ]
)

# ORDER INTERPOLATE METHOD:
ORDER_INTERPOLATE_METHOD_CARD___CONTROLS___MISSING_DATA_TAB = html.Div(
    className="form-group inline m-0 my-1",
    style={
        'display': 'flex',
        'justify-content': 'space-between'
    },
    children=[
        html.Label(
            className='text-center',
            dir='rtl', 
        children='- مرتبه',
        style={
            "font-size": "1rem",
        }
        ),
        html.Div(
            className="w-75 p-0 m-0 text-center",
            children=[
                dcc.Dropdown(
                    id='ORDER_INTERPOLATE_METHOD_SELECT___CONTROLS___MISSING_DATA_TAB', 
                    value=1,
                    disabled=True,
                    options=[
                        {'label': '0', 'value': 0},
                        {'label': '1', 'value': 1},
                        {'label': '2', 'value': 2},
                        {'label': '3', 'value': 3},
                        {'label': '4', 'value': 4},
                        {'label': '5', 'value': 5},
                    ],
                    clearable=False
                )
            ]
        )
    ]
)

# DURATION:
DURATION_CARD___CONTROLS___MISSING_DATA_TAB = html.Div(
    className="form-group inline m-0 my-1",
    style={
        'display': 'flex',
        'justify-content': 'space-between'
    },
    children=[
        html.Label(
            className='text-center',
            dir='rtl', 
            children='- تعداد ماه',
            style={
                "font-size": "1rem",
            }
        ),
        html.Div(
            className="w-75 p-0 m-0 text-center",
            children=[
                dcc.Dropdown(
                    id='DURATION_SELECT___CONTROLS___MISSING_DATA_TAB', 
                    value=0,
                    options=[
                        {'label': 'بدون محدودیت', 'value': 0},
                        {'label': '1', 'value': 1},
                        {'label': '2', 'value': 2},
                        {'label': '3', 'value': 3},
                        {'label': '4', 'value': 4},
                        {'label': '6', 'value': 6},
                        {'label': '9', 'value': 9},
                        {'label': '12', 'value': 12},
                        {'label': '15', 'value': 15},
                        {'label': '18', 'value': 18},
                        {'label': '21', 'value': 21},
                        {'label': '24', 'value': 24},
                    ],
                    clearable=False
                ) 
            ]
        )
    ]
)

# COLLAPSE SELECT OUTLIER:
COLLAPSE___INTERPOLATE_METHOD___MISSING_DATA_TAB = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___INTERPOLATE_METHOD___MISSING_DATA_TAB"
                        ),
                        "تنظیمات روش تکمیل داده‌ها",
                    ]            
                )      
            ],
            id="OPEN_CLOSE_COLLAPSE___INTERPOLATE_METHOD___MISSING_DATA_TAB",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                INTERPOLATE_METHOD_CARD___CONTROLS___MISSING_DATA_TAB,
                                ORDER_INTERPOLATE_METHOD_CARD___CONTROLS___MISSING_DATA_TAB,
                                DURATION_CARD___CONTROLS___MISSING_DATA_TAB

                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE___INTERPOLATE_METHOD___MISSING_DATA_TAB",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)







# -------------------------------------
# 3- COLLAPSE HOW MODIFY
# -------------------------------------

HOW_MODIFY_CARD___CONTROLS___MISSING_DATA_TAB = html.Div(
    className='form-group pt-2', 
    children=[
        dcc.RadioItems(
            id='HOW_MODIFY_CARD___CONTROLS___MISSING_DATA_TAB', 
            value=0,
            inputClassName="ml-1",
            labelStyle={'display': 'block'},
            labelClassName="mr-2"
        ) 
    ]
)

# COLLAPSE HOW MODIFY:
COLLAPSE___HOW_MODIFY___MISSING_DATA_TAB = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___HOW_MODIFY___MISSING_DATA_TAB"
                        ),
                        "نحوه اعمال تغییرات",
                    ]            
                )      
            ],
            id="OPEN_CLOSE_COLLAPSE___HOW_MODIFY___MISSING_DATA_TAB",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                html.Label("بازسازی داده‌های مفقودی:"),
                                HOW_MODIFY_CARD___CONTROLS___MISSING_DATA_TAB
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE___HOW_MODIFY___MISSING_DATA_TAB",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)





# -------------------------------------
# BUTTONS
# -------------------------------------

# BUTTON:
BUTTON___BUTTONS___MISSING_DATA_TAB = dbc.Button(
    id='BUTTON___BUTTONS___MISSING_DATA_TAB',
    className="me-1 w-50",
    size="md",
    children='درون‌یابی', 
    color='primary',
    n_clicks=0
)

# TOAST:
TOAST___BUTTONS___MISSING_DATA_TAB = dbc.Toast(
    id='TOAST___BUTTONS___MISSING_DATA_TAB',
    is_open=False,
    dismissable=True,
    duration=5000
)




# -------------------------------------
# SIDEBAR
# -------------------------------------

SIDEBAR___MISSING_DATA_TAB = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        COLLAPSE___SELLECT_WELL___MISSING_DATA_TAB,
        COLLAPSE___INTERPOLATE_METHOD___MISSING_DATA_TAB,
        COLLAPSE___HOW_MODIFY___MISSING_DATA_TAB,
        html.Div(
            className="text-left m-0 p-0 pt-3",
            children=[
                BUTTON___BUTTONS___MISSING_DATA_TAB,
                TOAST___BUTTONS___MISSING_DATA_TAB                
            ]
        )

    ]
)