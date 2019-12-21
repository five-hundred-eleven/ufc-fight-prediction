import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.graph_objects as go

from app import app

import numpy as np

from service.fighter_service import fighter_service


select_red_column = dbc.Col(
    [
        dcc.Markdown("""
            fighting out of the
            ### RED CORNER
        """), 
        dcc.Dropdown(
            id="red-corner",
            options=[{"label": s, "value": s} for s in fighter_service.getAllFighters()]
        ),
        dcc.Markdown("""
        """, id="red-corner-nick"),
    ],
    md=4,
    className="red-corner"
)


select_blue_column = dbc.Col(
    [
        dcc.Markdown("""
            fighting out of the
            ### BLUE CORNER
        """), 
        dcc.Dropdown(
            id="blue-corner",
            options=[{"label": s, "value": s} for s in fighter_service.getAllFighters()]
        ),
        dcc.Markdown("""
        """, id="blue-corner-nick"),
    ],
    md=4,
    className="blue-corner"
)

buffer_column = dbc.Col(
    [],
    md=4,
    className="bruce-buffer",
)


layout = html.Div([
    dbc.Row([select_red_column, buffer_column, select_blue_column]),
    dbc.Row([
        dbc.Col([], id="results")
    ])
])



@app.callback(
    dash.dependencies.Output("red-corner-nick", "children"),
    [dash.dependencies.Input("red-corner", "value")],
)
def setRedNick(fighter):
    nick = fighter_service.getNickname(fighter)
    return """
        "{nick}"
    """


@app.callback(
    dash.dependencies.Output("blue-corner-nick", "children"),
    [dash.dependencies.Input("blue-corner", "value")],
)
def setBlueNick(fighter):
    nick = fighter_service.getNickname(fighter)
    return """
        "{nick}"
    """


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

