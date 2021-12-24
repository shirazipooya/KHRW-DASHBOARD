
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



# -----------------------------------------------------------------------------
# 1- COLLAPSE SELLECT AQUIFER
# -----------------------------------------------------------------------------

# STUDY AREA:
STUDY_AREA_CARD___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
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
            id='STUDY_AREA_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 
            multi=True,
            placeholder='انتخاب ...'
        ) 
    ]
)

# AQUIFER:
AQUIFER_CARD___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
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
            id='AQUIFER_SELECT___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER', 
            multi=True,
            placeholder='انتخاب ...'
        ) 
    ]
)


# MAP:
MAP_CARD___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
    children=[
        dcc.Graph(
            id='MAP___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
            className="border border-secondary",
            style={
                "height": "300px",
            },
        )
    ],
    className="pt-3"
)

# COLLAPSE SELLECT AQUIFER:
COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER"
                        ),
                        html.I(
                            className="fas fa-map  ml-2",
                        ),
                        "انتخاب آبخوان",
                    ]            
                )      
            ],
            id="OPEN_CLOSE_COLLAPSE___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                STUDY_AREA_CARD___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER,
                                AQUIFER_CARD___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER,
                                MAP_CARD___COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)




# -----------------------------------------------------------------------------
# 2- COLLAPSE SELLECT DATE
# -----------------------------------------------------------------------------

# WATER YEAR:
WATER_YEAR_DATE_CARD___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
    className='form-group', 
    children=[
        dcc.Checklist(
            id="WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER",
            options=[
                {"label": "سال آبی", "value": "waterYear"}
            ],
            value="waterYear",
            labelStyle={"display": "inline-block"},
            labelClassName="d-flex align-items-center text-dark font-weight-bold",
            inputClassName="ml-1",
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
                            id='LABEL_START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
                            className="text-secondary"
                        ),
                        dcc.Dropdown(
                            id='START___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
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
                            id='LABEL_END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
                            className="text-secondary"
                        ),
                        dcc.Dropdown(
                            id='END___WATER_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
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
SHAMSI_YEAR_DATE_CARD___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
    className='form-group', 
    children=[
        dcc.Checklist(
            id="SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER",
            options=[
                {"label": "سال شمسی", "value": "shamsiYear"}
            ],
            value="",
            labelStyle={"display": "inline-block"},
            labelClassName="d-flex align-items-center text-secondary",
            inputClassName="ml-1",
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
                            id='LABEL_START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
                            className="text-secondary"
                        ),
                        dcc.Dropdown(
                            id='START___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
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
                            id='LABEL_END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
                            className="text-secondary"
                        ),
                        dcc.Dropdown(
                            id='END___SHAMSI_YEAR_DATE_SELECT___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
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
COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER"
                        ),
                        html.I(
                            className="fas fa-calendar-day ml-2",
                        ),
                        "انتخاب بازه زمانی",
                    ]            
                )      
            ],
            id="OPEN_CLOSE___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                WATER_YEAR_DATE_CARD___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER,
                                SHAMSI_YEAR_DATE_CARD___COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)




# -----------------------------------------------------------------------------
# 3- COLLAPSE SETTINGS
# -----------------------------------------------------------------------------

METHOD_UNIT_HYDROGRAPH_CARD___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
    className='form-group pt-3',
    children=[
        html.Label(
            dir='rtl', 
            children='- انتخاب روش محاسبه هیدروگراف',
            style={
                "font-size": "1rem",
            }
        ),
        html.Div(
            dir='ltr', 
            className="p-0 pt-2 m-0 text-left",
            children=[
                dcc.RadioItems(
                    id='METHOD_UNIT_HYDROGRAPH_SELECT___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
                    value=1,
                    inputClassName="mr-1",
                    labelStyle={'display': 'block'},
                    className="pr-3",
                ) 
            ]
        )
    ]
)



DISPLAY_PARAMETER_CARD___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
    className='form-group pt-3', 
    children=[
        html.Label(
            dir='rtl', 
            children='- انتخاب پارامتر جدول',
            style={
                "font-size": "1rem",
            }
        ),
        html.Div(
            className="p-0 pt-2 m-0 text-right",
            children=[
                dcc.RadioItems(
                    id='DISPLAY_PARAMETER_SELECT___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER',
                    options=[
                        {'label': 'تراز سطح آب', 'value': 1},
                        {'label': 'تغییرات تراز سطح آب نسبت به ماه قبل', 'value': 2},
                        {'label': 'تغییرات تراز سطح آب نسبت به ماه سال قبل', 'value': 3},
                        {'label': 'تغییرات ذخیره آبخوان نسبت به ماه قبل', 'value': 4},
                        {'label': 'تغییرات ذخیره آبخوان نسبت به ماه سال قبل', 'value': 5},
                    ],
                    value=1,
                    inputClassName="ml-1",
                    labelStyle={'display': 'block'},
                    className="pr-3",
                ) 
            ]
        )
    ]
)



STATISTICAL_ANALYSIS_CARD___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
    className='form-group pt-3', 
    children=[
        html.Div(
            className="p-0 m-0 text-right",
            children=[
                dcc.Checklist(
                    id="STATISTICAL_ANALYSIS_SELECT___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER",
                    options=[
                        {"label": "نمایش تحلیل‌های آماری", "value": "OK"}
                    ],
                    labelStyle={"display": "inline-block"},
                    labelClassName="d-flex align-items-center",
                    inputClassName="ml-1",
                ),
            ]
        )
    ]
)





# COLLAPSE SETTINGS:
COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
    children=[
        html.H6(
            children=[
                html.Div(
                    children = [
                        html.I(
                            className="fas fa-caret-left ml-2",
                            id="ARROW___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER"
                        ),
                        html.I(
                            className="fas fa-cogs ml-2",
                        ),
                        "تنظیمات",
                    ]            
                )      
            ],
            id="OPEN_CLOSE___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER",
            n_clicks=0,
            className="collapse-card-header"
        ),
        dbc.Collapse(
            children=[
                html.Div(
                    children=[
                        html.Ul(
                            children=[
                                METHOD_UNIT_HYDROGRAPH_CARD___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER,
                                DISPLAY_PARAMETER_CARD___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER,
                                STATISTICAL_ANALYSIS_CARD___COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER
                            ],
                            className="list-group list-group-flush"
                        )
                    ],
                    className="card p-3 mx-2 rounded-0 border-top-0"
                )
            ],
            id="COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER",
            is_open=False
        )
    ],
    className="pb-1 collapse-card"
)



# -----------------------------------------------------------------------------
# SIDEBAR
# -----------------------------------------------------------------------------

SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        COLLAPSE_SELLECT_AQUIFER___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER,
        COLLAPSE_SELLECT_DATE___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER,
        COLLAPSE_SETTINGS___SIDEBAR___AQUIFERS_TAB___DATA_VISUALIZATION___GROUNDWATER
    ]
)