  
from dash import html
from dash import dcc
import dash_dangerously_set_inner_html
from App.dashApps.Groundwater.unitHydrograph.layouts.tabs import *


# -----------------------------------------------------------------------------
# Tab Pan
# -----------------------------------------------------------------------------

TAB_PAN = html.Div(
    children=[

        # Nav Tabs ------------------------------------------------------------

        dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
            """
                    <ul class="nav nav-tabs mt-1" role="tablist">
                        <li class="nav-item tab-width">
                            <a class="nav-link active" data-toggle="tab" href="#HYDROGRAPH_TAB">محاسبات هیدروگراف واحد</a>
                        </li>
                    </ul>
            """
        ),

        # Tab Panes -----------------------------------------------------------

        html.Div(
            children=[
                html.Div(
                    children=[
                        HYDROGRAPH_TAB
                    ],
                    className="tab-pane active",
                    id="HYDROGRAPH_TAB"
                ),
            ],
            className="tab-content"
        )
    ],
    className="tabbable"
)


# -----------------------------------------------------------------------------
# Main Layout
# -----------------------------------------------------------------------------

def MAIN_LAYOUT():
    return html.Div(
        children=[
            TAB_PAN
        ],
        className="m-0 p-0",
    )

