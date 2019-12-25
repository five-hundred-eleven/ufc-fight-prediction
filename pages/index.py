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


column1 = dbc.Col(
    [
        dcc.Markdown(
            """
                ### Which Fighter Would Win?

                In the UFC, the Vegas Odds for a given fight show who is the favorite and who is the underdog.
                Those who have insights on the fighters stand to make a lot of money on bets.

                Besides for the bets, it's inherently interesting for MMA enthusiasts to think about which fighter would
                win a given fight.

                The purpose of this project was to use data analysis to determine who would win. Note that we allow 
                for fighters from **different eras** and **different weight classes** to be compared. Long-retired fighters
                are imagined to be in their primes, and any two fighters being compared are imagined to be fighting at
                the same weight.

                Try out the app, and learn more about the technology on the [insights page](/insights).
            """
        ),
        dcc.Link(dbc.Button("Predict a Fight"), href="/predict"),
    ],
    md=4,
)

fighters_df = fighter_service.getFightersDF()
fig = go.Figure(
    go.Histogram2dContour(
        x = fighters_df["Reach_cms_ratio"],
        y = fighters_df["avg_SIG_STlanded_ratio"],
        z = fighters_df["is_winner"].replace({False: -1, True: 1}),
        ncontours=20,
        colorscale="Hot",
        showscale=False,
    ),
)
fig.update_layout({
    "title": "Reach and Number of Significant Strikes vs Winner",
})

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ],
)

layout = dbc.Row([column1, column2])
