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
            ##### fighting out of the
            ### RED CORNER
        """), 
        dcc.Dropdown(
            id="red-corner",
            options=[{"label": s, "value": s} for s in fighter_service.getAllFighters()]
        ),
        html.Div([], id="red-corner-nick"),
    ],
    md=4,
    className="red-corner"
)


select_blue_column = dbc.Col(
    [
        dcc.Markdown("""
            ##### fighting out of the
            ### BLUE CORNER
        """), 
        dcc.Dropdown(
            id="blue-corner",
            options=[{"label": s, "value": s} for s in fighter_service.getAllFighters()]
        ),
        html.Div([], id="blue-corner-nick"),
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
        dbc.Col([], id="results", md=4, className="mx-auto")
    ])
])


def getFighterStats(fighter):
    """
        Gets the nickname, reach, wins, and losses of a fighter and formats it
        into markdown.

        @type fighter: str
        @rtype: dcc.Markdown
    """

    nick = fighter_service.getNickname(fighter)

    if nick:
        s = f"##### \"{nick}\""
    else:
        s = ""

    reach = fighter_service.getReach(fighter)
    height = fighter_service.getHeight(fighter)
    wins = fighter_service.getWins(fighter)
    losses = fighter_service.getLosses(fighter)

    s += f"\n\nreach: {reach}\n\nheight: {height}"

    return dcc.Markdown(s)
        

@app.callback(
    dash.dependencies.Output("red-corner-nick", "children"),
    [dash.dependencies.Input("red-corner", "value")],
)
def setRedNick(fighter):
    return getFighterStats(fighter)


@app.callback(
    dash.dependencies.Output("blue-corner-nick", "children"),
    [dash.dependencies.Input("blue-corner", "value")],
)
def setBlueNick(fighter):
    return getFighterStats(fighter)


@app.callback(
    dash.dependencies.Output("results", "children"),
    [
        dash.dependencies.Input("red-corner", "value"),
        dash.dependencies.Input("blue-corner", "value"),
    ]
)
def makePrediction(r_fighter, b_fighter):

    prob, winner, pos_shaps, neg_shaps = fighter_service.doPrediction(r_fighter, b_fighter)

    loser = b_fighter if r_fighter == winner else r_fighter

    if winner == "-":
        return dcc.Markdown("")

    s = f"""
            ### Winner: {winner}

            ##### confidence: {prob:.2f}%
    """

    if pos_shaps and neg_shaps:

        pos1, pos2, pos3 = pos_shaps
        neg3, neg2, neg1 = neg_shaps

        s += f"""
            #### Arguments in Favor of {winner}
            * {pos1}
        """

        if pos2 and pos2 != pos1:
            s += f"""
            * {pos2}
            """

        if pos3 and pos3 not in [pos1, pos2]:
            s += f"""
            * {pos3}
            """

        s += f"""
            #### Counter Arguments
            * {neg1}
        """

        if neg2 and neg2 != neg1:
            s += f"""
            * {neg2}
            """

        if neg3 and neg3 not in [neg1, neg2]:
            s += f"""
            * {neg3}
            """

    return [
        dcc.Markdown(s)
    ]

