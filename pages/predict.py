import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.graph_objects as go

from app import app

import numpy as np


select_red_column = dbc.Col(
    [
        dcc.Markdown("""
            ### Red Corner
        """), 
        dcc.Dropdown(
            id="red-corner",
            options=[{"label": s, "value": s} for s in ["Khabib Nurmagomedov", "Conor McGregor", "Dusitin Pourier", "Tony Ferguson", "Justin Gaethje",]]
        )
    ],
    md=4,
    className="red-corner"
)


select_blue_column = dbc.Col(
    [
        dcc.Markdown("""
            ### Blue Corner
        """), 
        dcc.Dropdown(
            id="blue-corner",
            options=[{"label": s, "value": s} for s in ["Khabib Nurmagomedov", "Conor McGregor", "Dusitin Pourier", "Tony Ferguson", "Justin Gaethje",]]
        )
    ],
    md=4,
    className="blue-corner"
)


layout = html.Div([
    dbc.Row([select_red_column, select_blue_column]),
    dbc.Row([
        dbc.Col([], id="results")
    ])
])



@app.callback(
    dash.dependencies.Output("results", "children"),
    [
        dash.dependencies.Input("red-corner", "value"),
        dash.dependencies.Input("blue-corner", "value"),
    ]
)
def makePrediction(r_fighter, b_fighter):

    winner = np.random.choice([r_fighter, b_fighter])

    return [
        dcc.Markdown(f"""
            ### Winner: {winner}
        """)
    ]

