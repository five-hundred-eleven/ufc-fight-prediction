import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.graph_objects as go

from app import app

import numpy as np

column00 = dbc.Col(
    [
        dcc.Markdown(
            """
                ### Positive Features

                This graphic shows features that were highly predictive of the winner.
                The green bars are the best estimate of predictiveness and the thin bars
                are the margin of error.
                
                Here are some notes to help you interpret it:
                * Features **not** ending in "\_opponent" are features of the red fighter. 
                * Features that **do** end in "\_opponent" are features of the blue fighter.
                * Features ending in "\_ratio" are the feature of the red fighter over the feature of the blue fighter.
                * Features containing "\_opp\_" represent the average of that action that the fighter **receives** during fights.
                * "att" usually means attempts
                * "td" usually means takedowns
            """
        ),
    ],
    md=4,
)
column01 = html.Img(id="pos-features", src="/img/positive-features.png")

column10 = dbc.Col(
    [
        dcc.Markdown(
            """
                ### Negative Features

                This graphic shows features that caused predictions to become worse when included in the analysis.
            """
        ),
    ],
    md=4,
)
column11 = html.Img(id="neg-features", src="/img/negative-features.png")

layout = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Markdown("""
                # Insights

                For full methodology, consult [this notebook](https://github.com/ekoly/ufc-fight-prediction/blob/master/ipynb/ufc-predictions.ipynb).
            """)
        ])
    ]),
    dbc.Row([column00, column01]),
    dbc.Row([column10, column11]),
])
