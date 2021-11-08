from dash import html
from dash import dcc
from dash import dash_table
import dash_bootstrap_components as dbc


# -----------------------------------------------------------------------------
# Tab 3 - Body
# -----------------------------------------------------------------------------


# Tab 3 - Body - Content 1 --------------------------------
# Graph
TAB3_BODY_CONTENT1 = dcc.Graph(
    id='GRAPH-TAB3_BODY_CONTENT1',
    className="w-100 h-100 mx-4 mb-4"
)


# Tab 3 - Body - Content 2 --------------------------------
# Table
TAB3_BODY_CONTENT2 = dash_table.DataTable(
    id='TABLE-TAB3_BODY_CONTENT2',
    filter_action="native",
    # sort_action="native",
    # sort_mode="multi",
    style_table={
        'overflowX': 'auto',
        'overflowY': 'auto',
    },
    style_cell={
        'border': '1px solid grey',
        'font-size': '14px',
        'font_family': 'Tanha-FD',
        'text_align': 'center',
        'minWidth': 65,
        'maxWidth': 200,
        'width': 65
    },
    style_header={
        'backgroundColor': 'rgb(220, 220, 220)',
        'fontWeight': 'bold',
        'whiteSpace': 'normal',
        'text_align': 'center',
        'height': 'auto',
    },
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        },
        {
            'if': {'column_id': ['نام چاه', 'نام آبخوان', 'نام محدوده']},
            'textAlign': 'right'
        },
        # {
        #     'if': {'column_id': ['طول جغرافیایی', 'عرض جغرافیایی', 'ارتفاع']},
        #     'textAlign': 'left'
        # }
    ],
    css=[{
        'selector': '.dash-table-tooltip',
        'rule': 'background-color: yellow;'
    }],
    page_size=30
)


# -----------------------------------------------------------------------------
# Tab 3 - Sidebar Left
# -----------------------------------------------------------------------------
MAP_TAB3_SIDEBAR_LEFT_CARD1 = dcc.Graph(
    id='MAP-TAB3_SIDEBAR_LEFT_CARD1',
    style={
        "width": "250px",
        "height": "250px",
        "margin": "auto"
    }
)