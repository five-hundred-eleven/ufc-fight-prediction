import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.graph_objects as go

from app import app

import numpy as np

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
                ### Blah

                blah blah blah

                blah blah

                blah blah blah
            """
        ),
        dcc.Link(dbc.Button("Predict"), href="/predictions"),
    ],
    md=4,
)


fig = go.Figure(
    data=go.Scatter(x=np.random.randint(0, 100, 100), y=np.random.randint(0, 100, 100))
)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ],
)

layout = dbc.Row([column1, column2])
