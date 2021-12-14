
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
# 1- COLLAPSE SELLECT AQUIFER
# -------------------------------------

# STUDY AREA:
STUDY_AREA_CARD___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
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
            id='STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 
            multi=False,
            placeholder='انتخاب ...'
        ) 
    ]
)

# AQUIFER:
AQUIFER_CARD___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
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
            id='AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 
            multi=False,
            placeholder='انتخاب ...'
        ) 
    ]
)

# COLLAPSE SELLECT AQUIFER:
COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER"
                        ),
                        "انتخاب آبخوان",
                    ]            
                )      
            ],
            id="OPEN_CLOSE___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                STUDY_AREA_CARD___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER,
                                AQUIFER_CARD___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER,
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)

# -------------------------------------
# 2- COLLAPSE SELLECT WELLS
# -------------------------------------

# WELL:
WELL_CARD___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
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
            id='WELL_SELECT___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER', 
            multi=True,
            placeholder='انتخاب ...'
        ) 
    ]
)

# MAP:
MAP_CARD___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    children=[
        dcc.Graph(
            id='MAP___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
            className="border border-secondary",
            style={
                "height": "300px",
            },
        )
    ],
    className="pt-3"
)

# COLLAPSE SELLECT WELL:
COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER"
                        ),
                        "انتخاب چاه‌های مشاهده‌ای",
                    ]            
                )      
            ],
            id="OPEN_CLOSE___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                WELL_CARD___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER,
                                MAP_CARD___COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)



# -------------------------------------
# 3- COLLAPSE SELLECT DATE
# -------------------------------------

# WATER YEAR:
WATER_YEAR_DATE_CARD___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    className='form-group', 
    children=[
        dcc.Checklist(
            id="WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            options=[
                {"label": "سال آبی", "value": "waterYear"}
            ],
            value="waterYear",
            labelStyle={"display": "inline-block"},
            labelClassName="d-flex align-items-center text-dark font-weight-bold",
            inputClassName="ml-2",
            inputStyle={
                "transform": "scale(1.5)"
            }
        ),
        
        html.Div(
            className="form-group inline m-0 mt-2",
            style={
                'display': 'flex',
                'justify-content': 'space-between'
            },
            children=[
                html.Div(
                    dir='ltr',
                    className="w-50 p-2 m-0 text-center",
                    children=[
                        html.Label(
                            "شروع",
                            id='LABEL_START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
                            className="text-secondary"
                        ),
                        dcc.Dropdown(
                            id='START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
                            placeholder='انتخاب',
                            options=[
                                {'label': f'{year} - {str(year + 1)[2:4]}', 'value': f'{year}-{year + 1}'} for year in range(1371, 1420)
                            ],
                            clearable=False,
                            disabled=False
                        ) 

                    ]
                ),
                html.Div(
                    dir='ltr',
                    className="w-50 p-2 m-0 text-center",
                    children=[
                        html.Label(
                            "پایان",
                            id='LABEL_END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
                            className="text-secondary"
                        ),
                        dcc.Dropdown(
                            id='END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
                            placeholder='انتخاب',
                            options=[
                                {'label': f'{year} - {str(year + 1)[2:4]}', 'value': f'{year}-{year + 1}'} for year in range(1371, 1420)
                            ],
                            clearable=False,
                            disabled=False
                        ) 

                    ]
                ),
            ]
        )
        
    ]
)

# SHAMSI YEAR:
SHAMSI_YEAR_DATE_CARD___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    className='form-group', 
    children=[
        dcc.Checklist(
            id="SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            options=[
                {"label": "سال شمسی", "value": "shamsiYear"}
            ],
            value="",
            labelStyle={"display": "inline-block"},
            labelClassName="d-flex align-items-center text-secondary",
            inputClassName="ml-2",
            inputStyle={
                "transform": "scale(1.5)"
            }
        ),
        html.Div(
            className="form-group inline m-0 mt-2",
            style={
                'display': 'flex',
                'justify-content': 'space-between'
            },
            children=[
                html.Div(
                    dir='ltr',
                    className="w-50 p-2 m-0 text-center",
                    children=[
                        html.Label(
                            "شروع",
                            id='LABEL_START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
                            className="text-secondary"
                        ),
                        dcc.Dropdown(
                            id='START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
                            placeholder='انتخاب',
                            options=[
                                {'label': year, 'value': year} for year in range(1371, 1421)
                            ],
                            clearable=False,
                            disabled=True
                        ) 

                    ]
                ),
                html.Div(
                    dir='ltr',
                    className="w-50 p-2 m-0 text-center",
                    children=[
                        html.Label(
                            "پایان",
                            id='LABEL_END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
                            className="text-secondary"
                        ),
                        dcc.Dropdown(
                            id='END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
                            placeholder='انتخاب',
                            options=[
                                {'label': f'{year}', 'value': f'{year}'} for year in range(1371, 1421)
                            ],
                            clearable=False,
                            disabled=True
                        ) 

                    ]
                ),
            ]
        )
    ]
)



# COLLAPSE SELLECT DATE:
COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER"
                        ),
                        "انتخاب بازه زمانی",
                    ]            
                )      
            ],
            id="OPEN_CLOSE___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                WATER_YEAR_DATE_CARD___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER,
                                SHAMSI_YEAR_DATE_CARD___COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER

                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)



# -------------------------------------
# 3- COLLAPSE SETTINGS
# -------------------------------------

# WATER_TABLE OR WATER_TABLE_LEVEL:

WATER_TABLE_WATER_LEVEL_CARD___COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    className='form-group', 
    children=[
        html.Label(
            dir='rtl', 
            children='- انتخاب تراز یا عمق سطح آب',
            style={
                "font-size": "1rem",
            }
        ),
        html.Div(
            className="p-0 pt-2 m-0 text-center",
            children=[
                dcc.RadioItems(
                    id='WATER_TABLE_WATER_LEVEL_SELECT___COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
                    options=[
                        {"label": "تراز سطح آب", "value": "WATER_LEVEL"},
                        {"label": "عمق سطح آب", "value": "WATER_TABLE"},
                    ],
                    inputClassName="ml-2",
                    labelClassName="mr-2 d-flex align-items-center",
                    value='WATER_LEVEL',
                    inputStyle={
                        "transform": "scale(1.5)"
                    }
                ) 
            ]
        )
    ]
)





# COLLAPSE SETTINGS:
COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER"
                        ),
                        "تنظیمات",
                    ]            
                )      
            ],
            id="OPEN_CLOSE___COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                WATER_TABLE_WATER_LEVEL_CARD___COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER,
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)





# -------------------------------------
# 4- CALCULATE UNIT HYDROGRAPH METHOD
# -------------------------------------

# WATER_TABLE OR WATER_TABLE_LEVEL:

HYDROGRAPH_METHOD_CARD___COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    className='form-group m-0', 
    children=[
        html.Div(
            className="p-0 pt-2 m-0 text-center",
            dir='ltr',
            children=[
                dcc.Checklist(
                    id="HYDROGRAPH_METHOD_SELLECT___COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
                    options=[
                        {"label": "Arithmetic Mean", "value": "AM"},
                        {"label": "Geometric Mean", "value": "GM"},
                        {"label": "Harmonic Mean", "value": "HM"},
                        {"label": "Thiessen Weighted Average", "value": "TWA"},
                        {"label": "Inverse Distance Weighting", "value": "IDW", "disabled": True},
                        {"label": "Triangular Interpolation Network", "value": "TIN", "disabled": True},
                        {"label": "Spline with Barriers", "value": "SB", "disabled": True},
                        {"label": "Simple kriging", "value": "SK", "disabled": True},
                        {"label": "Ordinary kriging", "value": "OK", "disabled": True},
                        {"label": "Regression kriging", "value": "RK", "disabled": True},
                        {"label": "Co-kriging", "value": "CK", "disabled": True},
                    ],
                    value=["AM", "GM", "HM", "TWA"],
                    labelStyle={"display": "inline-block"},
                    labelClassName="d-flex align-items-center",
                    inputClassName="mr-2",
                    inputStyle={
                        "transform": "scale(1.5)"
                    }
                ),
            ]
        )
    ]
)



# COLLAPSE SETTINGS:
COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER"
                        ),
                        "انتخاب روش محاسبه هیدروگراف واحد آبخوان",
                    ]            
                )      
            ],
            id="OPEN_CLOSE___COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                HYDROGRAPH_METHOD_CARD___COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER,
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)









# -------------------------------------
# 5- STORAGE COEFFICIENT
# -------------------------------------

# WATER_TABLE OR WATER_TABLE_LEVEL:

STORAGE_COEFFICIENT_CARD___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    className='form-group m-0', 
    children=[
        html.Div(
            className="p-0 pt-2 m-0 text-center",
            children=[
                dcc.RadioItems(
                    id='STORAGE_COEFFICIENT_SELECT___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER',
                    options=[
                        {"label": "ضریب ذخیره آبخوان", "value": "AQUIFER"},
                        {"label": "ضریب ذخیره چاه‌ها", "value": "WELLS"},
                    ],
                    inputClassName="ml-2",
                    labelClassName="mr-2 d-flex align-items-center",
                    value='AQUIFER',
                    inputStyle={
                        "transform": "scale(1.5)"
                    }
                )
            ]
        )
    ]
)

STORAGE_COEFFICIENT_HOLDER_CARD___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    className='form-group m-0', 
    children=[
        html.Div(
            id="STORAGE_COEFFICIENT_AQUIFER_HOLDER___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            className="p-0 pt-3 m-0 text-center",
            children=[
                html.Div(
                    className="form-group m-0 my-1",
                    children=[
                        html.Div(
                            className="form-group m-0 my-1 align-items-center",
                            style={
                                'display': 'flex',
                                'justify-content': 'space-around'
                            },
                            children=[
                                html.Label(
                                    id="STORAGE_COEFFICIENT_AQUIFER_LABEL___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
                                    className='text-right m-0',
                                    dir='rtl', 
                                    style={
                                        "font-size": "1rem",
                                    }
                                ),
                                dcc.Input(
                                    id="STORAGE_COEFFICIENT_AQUIFER_SELECT___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
                                    type="number",
                                    step=0.01,
                                    min=0,
                                    className="p-0 m-0 w-25 text-center"                          
                                )
                            ]
                        )
                    ]
                )
            ]
        ),
        html.Div(
            id="STORAGE_COEFFICIENT_WELLS_HOLDER___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            className="p-0 pt-3 m-0 text-center text-danger",
            children=[
                html.I(
                        className="fa fa-exclamation-triangle ml-2",
                    ),
                    "در حال تکمیل",
                    html.I(
                        className="fa fa-exclamation-triangle mr-2",
                    )
                ]
        )
    ]
)



# COLLAPSE STORAGE COEFFICIENT:
COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER"
                        ),
                        "انتخاب ضریب ذخیره آبخوان",
                    ]            
                )      
            ],
            id="OPEN_CLOSE___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                STORAGE_COEFFICIENT_CARD___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER,
                                STORAGE_COEFFICIENT_HOLDER_CARD___COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)



# -------------------------------------
# SIDEBAR
# -------------------------------------

SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        COLLAPSE_SELLECT_AQUIFER___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER,
        COLLAPSE_SELLECT_WELL___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER,
        COLLAPSE_SELLECT_DATE___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER,
        COLLAPSE_STORAGE_COEFFICIENT___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER,
        COLLAPSE_HYDROGRAPH_METHOD___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER,
        COLLAPSE_SETTINGS___SIDEBAR___HYDROGRAPH_TAB___UNIT_HYDROGRAPH___GROUNDWATER   
    ]
)