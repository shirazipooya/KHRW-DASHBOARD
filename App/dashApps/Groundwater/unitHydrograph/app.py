import dash
from flask_login.utils import login_required

from App.dashApps.Groundwater.unitHydrograph.layouts.main import MAIN_LAYOUT
from App.dashApps.Groundwater.unitHydrograph.callbacks import callback___unitHydrograph___groundwater


# EXTERNAL STYLESHEETS
external_stylesheets=[
    "/static/vendor/fontawesome/v5.15.3/css/all.css",
    "/static/vendor/bootstrap/v4.6.0/css/bootstrap.min.css",
    "/static/vendor/animate/v4.1.1/animate.min.css",
    "/static/css/groundwater_unitHydrograph.css",
]


# EXTERNAL SCRIPTS
external_scripts=[
    "/static/vendor/jquery/v3.6.0/jquery.min.js",
    "/static/vendor/popper/v2.9.2/popper.min.js",
    "/static/vendor/bootstrap/v4.6.0/js/bootstrap.min.js",
]


def create_groundwater_unitHydrograph_app(server):
    groundwater_unitHydrograph_app = dash.Dash(
        name="groundwater_unitHydrograph",
        server=server,
        url_base_pathname="/groundwater/unitHydrograph/",
        external_stylesheets=external_stylesheets,
        external_scripts=external_scripts,
        title='هیدروگراف واحد آبخوان',
        prevent_initial_callbacks=True,
        suppress_callback_exceptions=True
    )
    
    groundwater_unitHydrograph_app.layout = MAIN_LAYOUT()
    
    callback___unitHydrograph___groundwater(app=groundwater_unitHydrograph_app)

    for view_function in groundwater_unitHydrograph_app.server.view_functions:
        if view_function.startswith(groundwater_unitHydrograph_app.config.url_base_pathname):
            groundwater_unitHydrograph_app.server.view_functions[view_function] = login_required(
                groundwater_unitHydrograph_app.server.view_functions[view_function]
            )

    return groundwater_unitHydrograph_app
