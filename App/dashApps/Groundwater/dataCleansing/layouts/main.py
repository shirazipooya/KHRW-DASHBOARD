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
                    <ul class="nav nav-tabs nav-justified mt-1" role="tablist">
                        <li class="nav-item tab-width">
                            <a class="nav-link active" data-toggle="tab" href="#DATABASE_TAB">فراخوانی داده‌ها</a>
                        </li>
                        <li class="nav-item tab-width">
                            <a class="nav-link" data-toggle="tab" href="#DATA_CLEANSING_TAB">پالایش داده‌ها</a>
                        </li>
                        <li class="nav-item tab-width">
                            <a class="nav-link" data-toggle="tab" href="#MISSING_DATA_TAB">تکمیل داده‌ها</a>
                        </li>
                        <li class="nav-item tab-width">
                            <a class="nav-link" data-toggle="tab" href="#SYNC_DATE_TAB">هماهنگ‌سازی داده‌ها</a>
                        </li>
                    </ul>
            """
        ),

        # Tab Panes -----------------------------------------------------------

        html.Div(
            children=[
                html.Div(
                    children=[
                        DATABASE_TAB
                    ],
                    className="tab-pane active",
                    id="DATABASE_TAB"
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
                    className="tab-pane fade",
                    id="MISSING_DATA_TAB"
                ),
                html.Div(
                    children=[
                        SYNC_DATE_TAB
                    ],
                    className="tab-pane fade",
                    id="SYNC_DATE_TAB"
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
