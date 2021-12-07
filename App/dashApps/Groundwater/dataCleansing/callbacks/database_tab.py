from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, MATCH, ALL, ALLSMALLER
from dash.exceptions import PreventUpdate

from App.dashApps.Groundwater.dataCleansing.callbacks.config import *


def groundwater___dataCleansing___callback___database_tab(app):
    
    # -----------------------------------------------------------------------------
    # CONNECT TO SPREADSHEET FILE AND CREATE DATABASE - DATABASE TAB
    # -----------------------------------------------------------------------------
    @app.callback(
        Output("BUTTON___SPREADSHEET_DATABASE___DATABASE_TAB", "n_clicks"),
        Output("SELECT_FILE_NAME___SPREADSHEET_DATABASE___DATABASE_TAB", "children"),
        Output("SELECT_FILE_NAME___SPREADSHEET_DATABASE___DATABASE_TAB", "style"),
        Output("TOAST___SPREADSHEET_DATABASE___DATABASE_TAB", "is_open"),
        Output("TOAST___SPREADSHEET_DATABASE___DATABASE_TAB", "icon"),
        Output("TOAST___SPREADSHEET_DATABASE___DATABASE_TAB", "header"),
        Output("TOAST___SPREADSHEET_DATABASE___DATABASE_TAB", "children"),
        Output("TOAST___SPREADSHEET_DATABASE___DATABASE_TAB", "headerClassName"),
        Output('SELECT_FILE___SPREADSHEET_DATABASE___DATABASE_TAB', 'contents'),
        Output('SELECT_GEOINFO_WORKSHEET___SPREADSHEET_DATABASE___DATABASE_TAB', 'options'),
        Output('SELECT_DATA_WORKSHEET___SPREADSHEET_DATABASE___DATABASE_TAB', 'options'),
        Output('SPREADSHEET_DATA_STATE___DATABASE_TAB', 'data'),

        Input("TYPE_DATE___SPREADSHEET_DATABASE___DATABASE_TAB", "value"),
        Input("BUTTON___SPREADSHEET_DATABASE___DATABASE_TAB", "n_clicks"),
        Input('SELECT_FILE___SPREADSHEET_DATABASE___DATABASE_TAB', 'contents'),        
        State('SELECT_FILE___SPREADSHEET_DATABASE___DATABASE_TAB', 'contents'),
        State('SELECT_FILE___SPREADSHEET_DATABASE___DATABASE_TAB', 'filename'),
        State('SELECT_GEOINFO_WORKSHEET___SPREADSHEET_DATABASE___DATABASE_TAB', 'value'),
        State('SELECT_DATA_WORKSHEET___SPREADSHEET_DATABASE___DATABASE_TAB', 'value'),      
        State('SELECT_GEOINFO_WORKSHEET___SPREADSHEET_DATABASE___DATABASE_TAB', 'options'),
        State('SELECT_DATA_WORKSHEET___SPREADSHEET_DATABASE___DATABASE_TAB', 'options'),
        State('SPREADSHEET_DATA_STATE___DATABASE_TAB', 'data'),
        State('UPDATE_REPLACE___SPREADSHEET_DATABASE___DATABASE_TAB', 'value'),
    )
    def FUNCTION___SPREADSHEET_DATABASE___DATABASE_TAB(
        date_type, n,
        content, state_content, state_filename,
        geoInfo_worksheet_name, data_worksheet_name,
        geoInfo_worksheet_options, data_worksheet_options,
        spreadsheet_data, if_exists
    ):
        
        print("FUNCTION___SPREADSHEET_DATABASE___DATABASE_TAB")
        
        if (n != 0 and content is None):
            result = [
                0,
                "فایلی انتخاب نشده است!",
                {'direction': 'rtl', 'color': 'red', 'text-align': 'center'},
                True,
                None,
                "هشدار",
                "فایل صفحه گسترده‌ای انتخاب نشده است.",
                "popup-notification-header-warning",
                None,
                [],
                [],
                None      
            ]
            return result
        
        elif n == 0 and content is not None:
            
            data, worksheet_name = read_spreadsheet(contents=content, filename=state_filename)
            
            if worksheet_name is None:
                result = [
                    0,
                    "فایلی انتخاب نشده است!",
                    {'direction': 'rtl', 'color': 'red', 'text-align': 'right'},
                    True,
                    None,
                    "اخطار",
                    "تعداد کاربرگ‏‌های فایل ورودی باید حداقل دو عدد باشند.",
                    "popup-notification-header-danger",
                    None,      
                    [],
                    [],
                    None  
                ]
                return result

            result = [
                0,
                f"{state_filename[0:12]}...{state_filename[-8:]}" if len(state_filename) > 20 else state_filename,
                {'direction': 'ltr', 'color': 'green', 'text-align': 'left'},
                False,
                None,
                None,
                None,
                None,
                state_content,
                [{'label': wn, 'value': wn} for wn in worksheet_name],
                [{'label': wn, 'value': wn} for wn in worksheet_name],
                data                
            ]
            return result
        
        elif n != 0 and content is not None:
            
            if (geoInfo_worksheet_name is None) | (data_worksheet_name is None):
                result = [
                    1,
                    f"{state_filename[0:12]}...{state_filename[-8:]}" if len(state_filename) > 20 else state_filename,
                    {'direction': 'ltr', 'color': 'green', 'text-align': 'left'},
                    True,
                    None,
                    "هشدار",
                    "کاربرگ مشخصات یا کاربرگ داده‌ها انتخاب نشده است!",
                    "popup-notification-header-warning",
                    state_content,
                    geoInfo_worksheet_options,
                    data_worksheet_options,
                    spreadsheet_data
                ]
                return result 
            
            elif geoInfo_worksheet_name == data_worksheet_name:
                result = [
                    1,
                    f"{state_filename[0:12]}...{state_filename[-8:]}" if len(state_filename) > 20 else state_filename,
                    {'direction': 'ltr', 'color': 'green', 'text-align': 'left'},
                    True,
                    None,
                    "هشدار",
                    "کاربرگ مشخصات و کاربرگ داده‌ها نمی‌توانند یکسان باشند!",
                    "popup-notification-header-warning",
                    state_content,
                    geoInfo_worksheet_options,
                    data_worksheet_options,
                    spreadsheet_data
                ]
                return result
            
            elif set(spreadsheet_data[geoInfo_worksheet_name].keys()) != set(HydrographDataSample_GeoInfoColumns):
                result = [
                    0,
                    "فایلی انتخاب نشده است!",
                    {'direction': 'rtl', 'color': 'red', 'text-align': 'right'},
                    True,
                    None,
                    "اخطار",
                    "سر ستون‌های «کاربرگ مشخصات» با فایل نمونه همخوانی ندارند!",
                    "popup-notification-header-danger",
                    None,
                    [],
                    [],
                    None
                ]
                return result
            
            elif set(spreadsheet_data[data_worksheet_name].keys()) != set(HydrographDataSample_DataColumns):
                result = [
                    0,
                    "فایلی انتخاب نشده است!",
                    {'direction': 'rtl', 'color': 'red', 'text-align': 'right'},
                    True,
                    None,
                    "اخطار",
                    "سر ستون‌های «کاربرگ داده‌ها» با فایل نمونه همخوانی ندارند!",
                    "popup-notification-header-danger",
                    None,
                    [],
                    [],
                    None
                ]
                return result
            
            
            create___geoinfo_table___spreadsheet_database(
                data=pd.DataFrame.from_dict(spreadsheet_data[geoInfo_worksheet_name]),
                con=DB_GROUNDWATER,
                name="GEOINFO_DATA",
                column=HydrographDataSample_GeoInfoColumns,
                if_exists=if_exists
            )
            
            create___groundwater_raw_data_table___spreadsheet_database(
                data=pd.DataFrame.from_dict(spreadsheet_data[data_worksheet_name]),
                con=DB_GROUNDWATER,
                raw_table_name="GROUNDWATER_RAW_DATA",
                cleansing_table_name="GROUNDWATER_CLEANSING_DATA",
                interpolated_table_name="GROUNDWATER_INTERPOLATED_DATA",
                syncdate_table_name="GROUNDWATER_SYNCDATE_DATA",
                column=HydrographDataSample_DataColumns,
                date_type=date_type,
                if_exists=if_exists
            )
            
            result = [
                0,
                "فایلی انتخاب نشده است!",
                {'direction': 'rtl', 'color': 'red', 'text-align': 'right'},
                True,
                None,
                "موفقیت آمیز",
                "پایگاه داده با موفقیت ایجاد شد.",
                "popup-notification-header-success",
                None,
                [],
                [],
                None
            ]
            return result
             
        else:
            result = [
                0,
                "فایلی انتخاب نشده است!",
                {'direction': 'rtl', 'color': 'red', 'text-align': 'right'},
                False,
                None,
                None,
                None,
                None,
                None,        
                [],
                [],
                None
            ]
            return result