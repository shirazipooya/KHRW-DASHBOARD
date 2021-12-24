import dash
from flask_login.utils import login_required
import dash_bootstrap_components as dbc

from App.dashApps.Groundwater.dataCleansing.layouts.main import MAIN_LAYOUT
from App.dashApps.Groundwater.dataCleansing.callbacks import groundwater___dataCleansing___callback


# EXTERNAL STYLESHEETS
external_stylesheets=[
    "/static/vendor/fontawesome/v5.15.3/css/all.css",
    "/static/vendor/bootstrap/v4.6.0/css/bootstrap.min.css",
    "/static/vendor/animate/v4.1.1/animate.min.css",
    "/static/css/groundwater_dataCleansing.css",
    # dbc.themes.BOOTSTRAP
]


# EXTERNAL SCRIPTS
external_scripts=[
    "/static/vendor/jquery/v3.6.0/jquery.min.js",
    "/static/vendor/popper/v2.9.2/popper.min.js",
    "/static/vendor/bootstrap/v4.6.0/js/bootstrap.min.js",
]


def create_groundwater_dataCleansing_app(server):
    groundwater_dataCleansing_app = dash.Dash(
        name="groundwater_dataCleansing",
        server=server,
        url_base_pathname="/groundwater/dataCleansing/",
        external_stylesheets=external_stylesheets,
        external_scripts=external_scripts,
        title='پالایش و اصلاح داده‌های آب زیرزمینی',
        prevent_initial_callbacks=True,
        suppress_callback_exceptions=True
    )
    
    groundwater_dataCleansing_app.layout = MAIN_LAYOUT()
    
    groundwater___dataCleansing___callback(app=groundwater_dataCleansing_app)

    for view_function in groundwater_dataCleansing_app.server.view_functions:
        if view_function.startswith(groundwater_dataCleansing_app.config.url_base_pathname):
            groundwater_dataCleansing_app.server.view_functions[view_function] = login_required(
                groundwater_dataCleansing_app.server.view_functions[view_function]
            )

    return groundwater_dataCleansing_app
