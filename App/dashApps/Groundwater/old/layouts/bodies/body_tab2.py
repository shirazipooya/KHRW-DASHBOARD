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
# TAB 2 - BODY
# -----------------------------------------------------------------------------


TAB_2_BODY = [
    # html.Div(
    #     children=[
    #         # Graph
    #         TAB2_BODY_CARDINFO
    #     ],
    #     className="row justify-content-center",
    # ),
    html.Div(
        children=[
            # Graph
            TAB2_BODY_CONTENT1
        ],
        className="row justify-content-center",
        style={
            "height": "655px",
            # "margin-bottom": "10px"
        }
    ),
    html.Div(
        children=[
            html.H6(
                id="TABLE_HEADER-TAB2_BODY_CONTENT2",
                className="text-center text-secondary my-2",
            ),
            html.Div(
                children=[
                    # Table
                    TAB2_BODY_CONTENT2
                ],
                className="w-100 h-100 px-4"
            ),
            dcc.Store(id='DATA_TABLE_WELL_STORE-TAB2_BODY_CONTENT2'),
            html.Div(
                children=[
                    html.Button(
                        children=[
                            "دانلود",
                            html.I(className="fa fa-download ml-2"),
                        ],
                        n_clicks=0,
                        className="btn btn-outline-dark mt-3 float-right",
                        id="DOWNLOAD_TABLE_BUTTON-TAB2_BODY_CONTENT2"
                    ),
                    dcc.Download(id="DOWNLOAD_TABLE_COMPONENT-TAB2_BODY_CONTENT2"),
                ],
                className="row justify-content-center"
            ),

        ],
        className="row justify-content-center"
    )
]
