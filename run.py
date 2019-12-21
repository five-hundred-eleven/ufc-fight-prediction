import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


from app import app, server
from pages import index, predict, insights


navbar = dbc.NavbarSimple(
    brand="UFC Predictions",
    brand_href="/",
    children=[
        dbc.NavItem(dcc.Link("Predict a Fight", href="/predict", className="nav-link")),
        dbc.NavItem(dcc.Link("Insights", href="/insights", className="nav-link")),
    ],
    sticky="top",
    color="#511",
    light=False,
    dark=True,
)


footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span("Erik Cowley", className="mr-2"),
                ],
                className="lead"
            )
        )
    )
)


app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    navbar,
    html.Div([
        html.Div([
            html.Hr(),
            dbc.Container(id="page-content", className="mt-4"),
            html.Hr(),
        ], id="background-shader"),
    ], id="background-img-ufc"),
    footer,
])



@app.callback(Output("page-content", "children"),
            [Input("url", "pathname"),],)
def displayPage(path_name):
    if path_name == "/":
        return index.layout
    elif path_name == "/predict":
        return predict.layout
    elif path_name == "/insights":
        return predict.layout
