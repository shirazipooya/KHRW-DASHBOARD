from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.dataVisualization.layouts.sidebars import *
from App.dashApps.Groundwater.dataVisualization.layouts.bodies import *


# -----------------------------------------------------------------------------
# Tab 2
# -----------------------------------------------------------------------------


TAB_2 = html.Div(
    children=[
        # Sidebars & Body ------------------------------------------------------
        html.Div(
            children=[
                # Sidebar Left ----------------------------
                html.Div(
                    children=[
                        TAB_2_SIDEBAR_LEFT
                    ],
                    className='left-sidebar'
                ),
                # Body ------------------------------------
                html.Div(
                    id="TAB_2_BODY",
                    children=[
                        html.Div(
                            children=TAB_2_BODY,
                            className="container-fluid"
                        )
                    ],
                    className='tab2-right-sidebar-hidden-my-body pt-2'
                ),
                # Sidebar right ---------------------------
                html.Div(
                    id="TAB_2_SIDEBAR_RIGHT",
                    hidden=True,
                    children=[
                        TAB_2_SIDEBAR_RIGHT
                    ],
                    className='tab2-right-sidebar-hidden'
                ),
            ],
            className="row p-0 m-0 w-100"
        ),
    ],
    className="container-fluid p-0",
    style={"position": "relativ"}
)

