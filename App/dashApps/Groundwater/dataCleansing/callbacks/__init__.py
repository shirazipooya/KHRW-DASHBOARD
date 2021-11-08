from App.dashApps.Groundwater.dataCleansing.callbacks.settings_tab import groundwater_callback_settings_tab
from App.dashApps.Groundwater.dataCleansing.callbacks.dataCleansing_tab import groundwater_callback_dataCleansing_tab

def groundwater_callback(app):
    groundwater_callback_settings_tab(app=app)
    groundwater_callback_dataCleansing_tab(app=app)
