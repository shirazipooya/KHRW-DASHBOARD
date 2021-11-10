from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.dataCleansing.callbacks.config import *

# -----------------------------------------------------------------------------
# DATABASE TAB - SIDEBAR
# -----------------------------------------------------------------------------

# -------------------------------------
# SPREADSHEET DATABASE
# -------------------------------------

# SELECT FILE
SELECT_FILE___SPREADSHEET_DATABASE___DATABASE_TAB = html.Div(
    className='form-group', 
    children=[
        html.Label(
            dir='rtl', 
            children='- انتخاب فایل صفحه گسترده',
            style={
                "font-weight": "bold",
                "font-size": "1rem",
            },
            className="pb-1"
        ),
        dcc.Upload(
            id="SELECT_FILE___SPREADSHEET_DATABASE___DATABASE_TAB",
            accept=".xlsx, .xls",
            children=[
                html.A('انتخاب فایل')
            ], 
            className="SELECT_FILE_BUTTON"
        ),
        html.Div(
            id='SELECT_FILE_NAME___SPREADSHEET_DATABASE___DATABASE_TAB',
            children=[
                "فایلی انتخاب نشده است!"
            ],
            className='text-center pt-2',
        )
    ]
)



# SELECT WORKSHEET
SELECT_WORKSHEET___SPREADSHEET_DATABASE___DATABASE_TAB = html.Div(
    className='form-group', 
    children=[
        html.Label(
            dir='rtl', 
            children='- انتخاب کاربرگ',
            style={
                "font-weight": "bold",
                "font-size": "1rem",
            },
            className="py-1"
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Span(
                            children=[
                                "کاربرگ مشخصات"
                            ]
                        ),
                        dcc.Dropdown(
                            id="SELECT_GEOINFO_WORKSHEET___SPREADSHEET_DATABASE___DATABASE_TAB",
                            placeholder="انتخاب...",
                            clearable=False
                        )
                    ],
                    className='col-5 p-0 m-0 text-center',
                ),
                html.Div(
                    children=[
                        html.Span(
                            children=[
                                "کاربرگ داده‏‌ها"
                            ]
                        ),
                        dcc.Dropdown(
                            id="SELECT_DATA_WORKSHEET___SPREADSHEET_DATABASE___DATABASE_TAB",
                            placeholder="انتخاب...",
                            clearable=False,
                        )
                    ],
                    className='col-5 p-0 m-0 text-center ',
                ),
            ],
            className='row p-0 m-0 align-items-center justify-content-center',
        ),
    ]
)



# SELECT FILE
UPDATE_REPLACE___SPREADSHEET_DATABASE___DATABASE_TAB = html.Div(
    className='form-group', 
    children=[
        html.Label(
            dir='rtl', 
            children='- تغییرات پایگاه داده',
            style={
                "font-weight": "bold",
                "font-size": "1rem",
            },
            className="pb-1"
        ),
        dcc.RadioItems(
            id='UPDATE_REPLACE___SPREADSHEET_DATABASE___DATABASE_TAB', 
            value='replace',
            options=[
                {'label': 'جایگزینی پایگاه داده موجود', 'value': 'replace'},
                {'label': 'به‌روزرسانی پایگاه داده موجود', 'value': 'append'},
            ],
            inputClassName="ml-1"
        ) 
    ]
)




# BUTTON
BUTTON___SPREADSHEET_DATABASE___DATABASE_TAB = dbc.Button(
    id='BUTTON___SPREADSHEET_DATABASE___DATABASE_TAB',
    className="me-1 w-50",
    size="lg",
    children='ایجاد', 
    color='primary',
    n_clicks=0
)


# TOAST
TOAST___SPREADSHEET_DATABASE___DATABASE_TAB = dbc.Toast(
    id='TOAST___SPREADSHEET_DATABASE___DATABASE_TAB',
    className="popup-notification",
    is_open=False,
    dismissable=True,
    duration=5000
)


# -------------------------------------
# SIDEBAR
# -------------------------------------

SIDEBAR___DATABASE_TAB = html.Div(
    className='container-fluid m-0 p-0',
    children=[
        html.H5(
            className="text-center pb-3",
            children="ایجاد پایگاه داده",
            style={
                "color": "#2c8cff",
                "font-size": "1.3rem",
                "font-weight": "bold",
                "font-weight": 300,
            }
        ),
        SELECT_FILE___SPREADSHEET_DATABASE___DATABASE_TAB,
        SELECT_WORKSHEET___SPREADSHEET_DATABASE___DATABASE_TAB,
        TOAST___SPREADSHEET_DATABASE___DATABASE_TAB,
        UPDATE_REPLACE___SPREADSHEET_DATABASE___DATABASE_TAB,
        html.Div(
            className="text-center pt-3",
            children=[
                BUTTON___SPREADSHEET_DATABASE___DATABASE_TAB,
            ]
        )
    ]
)