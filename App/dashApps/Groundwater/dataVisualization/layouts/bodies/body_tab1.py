import base64
import numpy as np
from datetime import date
from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc
import dash_daq as daq

from App.dashApps.Groundwater.dataVisualization.layouts.visualizations.visualization import *


# -----------------------------------------------------------------------------
# TAB 1 - BODY
# -----------------------------------------------------------------------------


TAB_1_BODY = [
    html.Div(
        children=[
            # Map: Study Area & Stations.
            TAB1_BODY_CONTENT1
        ],
        className="row justify-content-center",
        style={
            "height": "390px",
            "margin-bottom": "10px"
        }
    ),
    html.Div(
        children=[
            html.Div(
                children=[
                    # Table: Geographic Information of Stations.
                    TAB1_BODY_CONTENT2
                ],
                className="w-100 h-100 px-4"
            )

        ],
        className="row justify-content-center"
    )
]
