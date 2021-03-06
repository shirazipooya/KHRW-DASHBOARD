  
from dash import html
from dash import dcc
import dash_dangerously_set_inner_html
from App.dashApps.Groundwater.dataVisualization.layouts.tabs import *


# -----------------------------------------------------------------------------
# Tab Pan
# -----------------------------------------------------------------------------

TAB_PAN = html.Div(
    children=[

        # Nav Tabs ------------------------------------------------------------

        dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
            """
                    <ul class="nav nav-tabs nav-justified mt-1" role="tablist">
                        <li class="nav-item tab-width">
                            <a class="nav-link active" data-toggle="tab" href="#HOME_TAB">خانه</a>
                        </li>
                        <li class="nav-item tab-width">
                            <a class="nav-link" data-toggle="tab" href="#WELLS_TAB">چاه‌های مشاهده‌ای</a>
                        </li>
                        <li class="nav-item tab-width">
                            <a class="nav-link" data-toggle="tab" href="#AQUIFERS_TAB">آبخوان‌ها</a>
                        </li>
                    </ul>
            """
        ),

        # Tab Panes -----------------------------------------------------------

        html.Div(
            children=[
                html.Div(
                    children=[
                        HOME_TAB
                    ],
                    className="tab-pane active",
                    id="HOME_TAB"
                ),
                html.Div(
                    children=[
                        WELLS_TAB
                    ],
                    className="tab-pane fade",
                    id="WELLS_TAB"
                ),
                html.Div(
                    children=[
                        AQUIFERS_TAB
                    ],
                    className="tab-pane fade",
                    id="AQUIFERS_TAB"
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

