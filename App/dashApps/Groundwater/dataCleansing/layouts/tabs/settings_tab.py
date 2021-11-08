from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.dataCleansing.layouts.bodies import *


# -----------------------------------------------------------------------------
# Tab 1
# -----------------------------------------------------------------------------


SETTINGS_TAB = html.Div(
    className="container-fluid p-0 m-0",
    style={
        "height": "95vh",
        "width": "100%",
        "height": "100%"
    },
    children=[
        BODY_TAB_SETTINGS,
    ],
)
