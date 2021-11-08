from dash import html
from dash import dcc
import dash_dangerously_set_inner_html
from App.dashApps.Groundwater.dataCleansing.layouts.tabs import *


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
                            <a class="nav-link" data-toggle="tab" href="#SETTINGS_TAB">تنظیمات</a>
                        </li>
                        <li class="nav-item tab-width">
                            <a class="nav-link" data-toggle="tab" href="#DATA_CLEANSING_TAB">پاک‌سازی داده‌ها</a>
                        </li>
                        <li class="nav-item tab-width">
                            <a class="nav-link active" data-toggle="tab" href="#MISSING_DATA_TAB">بازسازی داده‌ها</a>
                        </li>
                    </ul>
            """
        ),

        # Tab Panes -----------------------------------------------------------

        html.Div(
            children=[
                html.Div(
                    children=[
                        SETTINGS_TAB
                    ],
                    className="tab-pane fade",
                    id="SETTINGS_TAB"
                ),
                html.Div(
                    children=[
                        DATA_CLEANSING_TAB
                    ],
                    className="tab-pane fade",
                    id="DATA_CLEANSING_TAB"
                ),
                html.Div(
                    children=[
                        MISSING_DATA_TAB
                    ],
                    className="tab-pane active",
                    id="MISSING_DATA_TAB"
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
            html.Div(
                children=[
                    html.Div(
                        children=[
                            TAB_PAN
                        ],
                        className="col m-0 p-0"
                    )
                ],
                className="row m-0 p-0"
            )
        ],
        className="container-fluid m-0 p-0",
    )
