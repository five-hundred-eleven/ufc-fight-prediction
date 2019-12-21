import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


from app import app, server


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


footer = (
    html.Div([
        dbc.Container(
            dbc.Row(
                dbc.Col(
                    html.P(
                        [
                            html.A(html.Span("Erik Cowley", className="mr-2"), href="https://datascience.stromsy.com"),
                            html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:ecowley@protonmail.com'),
                            html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/ekoly/ufc-fight-prediction'),
                            html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/erik-cowley-89090120/'),
                        ],
                        className="lead"
                    )
                )
            ),
        ),
    ], id="footer")
)


app.layout = (
    html.Div([
        html.Div([html.Div([], id="background-shader")], id="background-img-ufc"),
        html.Div([
            dcc.Location(id="url", refresh=False),
            navbar,
            html.Hr(),
            dbc.Container(id="page-content", className="mt-4"),
            html.Hr(),
            footer,
        ]),
    ])
)


# this line needs to be after setting app.layout
from pages import index, predict, insights

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname"),],
)
def displayPage(path_name):
    if path_name == "/":
        return index.layout
    elif path_name == "/predict":
        return predict.layout
    elif path_name == "/insights":
        return predict.layout
